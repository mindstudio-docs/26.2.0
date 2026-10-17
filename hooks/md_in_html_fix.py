"""Render imported documents without changing their upstream source bytes."""

from html import escape, unescape
import posixpath
import re
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit, urlunsplit


DIV = re.compile(r'<div\b(?![^>]*\bmarkdown\s*=)([^>]*)>', re.IGNORECASE)
CODE_FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
INLINE_CODE = re.compile(r"(`+)(?!`)(.*?)\1(?!`)")
RAW_IMAGE = re.compile(
    r'https?://raw\.gitcode\.com/Ascend/([^/]+)/(?:raw|files)/[^/]+/([^\s<>"\')]+)'
)
METADATA_LINK = re.compile(r"(\]\()(?P<path>(?:\./)?\.sync/[^)\s]+)(\))")
HTML_LINK = re.compile(
    r'(<(?:img|a|source|video)\b[^>]*?\s(?:src|href|poster)\s*=\s*)(["\'])([^"\']+)\2',
    re.IGNORECASE,
)


def local_image(match, page_dir, docs_dir):
    tool, file_path = match.groups()
    relative_path = unquote(unescape(file_path.split("?", 1)[0].split("#", 1)[0]))
    candidate = (docs_dir / tool / relative_path).resolve()
    # Only rewrite resources inside the published tool tree.
    tool_dir = (docs_dir / tool).resolve()
    if tool_dir.parent != docs_dir or not candidate.is_relative_to(tool_dir) or not candidate.is_file():
        return match[0]
    return quote(posixpath.relpath(candidate.as_posix(), page_dir.as_posix()), safe="/.-_~")


def on_page_markdown(markdown, page, config, **kwargs):
    docs_dir = Path(config.docs_dir).resolve()
    page_dir = (docs_dir / page.file.src_uri).parent
    files = kwargs.get("files")

    def html_link(match):
        url = urlsplit(unescape(match[3]))
        if files is None or url.scheme or url.netloc or not url.path or url.path.startswith("/"):
            return match[0]
        source = posixpath.normpath(posixpath.join(posixpath.dirname(page.file.src_uri), unquote(url.path)))
        target = files.get_file_from_path(source)
        if target is None:
            return match[0]
        relative_url = urlunsplit(("", "", target.url_relative_to(page.file), url.query, url.fragment))
        return match[1] + match[2] + escape(relative_url, quote=True) + match[2]

    def rewrite(text):
        text = DIV.sub(r'<div\1 markdown="1">', text)
        text = RAW_IMAGE.sub(lambda m: local_image(m, page_dir, docs_dir), text)
        # Raw HTML attributes bypass MkDocs' Markdown link rewriting. Rebase
        # them to the generated page URL (foo.md becomes foo/index.html).
        text = HTML_LINK.sub(html_link, text)
        if page.file.src_uri in {"README.md", "SOURCES.md"}:
            base = config.repo_url.rstrip("/") + "/blob/main/"
            text = METADATA_LINK.sub(lambda m: m[1] + base + m['path'].removeprefix('./') + m[3], text)
        return text

    lines = []
    fence = None
    for line in markdown.splitlines(keepends=True):
        match = CODE_FENCE.match(line)
        if match:
            marker = match[1]
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            lines.append(line)
            continue
        if fence is None:
            parts = []
            end = 0
            for code in INLINE_CODE.finditer(line):
                parts.extend((rewrite(line[end:code.start()]), code[0]))
                end = code.end()
            parts.append(rewrite(line[end:]))
            line = "".join(parts)
        lines.append(line)
    return "".join(lines)
