"""Publish aggregated documentation with navigation derived from actual files."""

import json
from pathlib import Path, PurePosixPath
import re

from mkdocs.exceptions import PluginError
from mkdocs.structure.files import Files


ROOT_PAGES = ("README.md",)
TOOL_ROW = re.compile(r"^\|\s*(ms[\w-]+)\s*\|", re.MULTILINE)
HEADING = re.compile(r"^#\s+(.+?)\s*#*\s*$", re.MULTILINE)
LINK_LABEL = re.compile(r"!?\[([^\]]*)\]\([^)]+\)")


def tool_order(docs_dir):
    root = Path(docs_dir)
    try:
        manifest = json.loads((root / ".sync/manifest.json").read_text(encoding="utf-8"))
        names = [repo["name"] for repo in manifest["repositories"]]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise PluginError(f"Cannot read tool inventory from .sync/manifest.json: {exc}") from exc
    if not names or len(names) != len(set(names)):
        raise PluginError("Tool inventory must contain unique repository names")
    for name in names:
        if not re.fullmatch(r"ms[\w-]+", name) or not (root / name / "README.md").is_file():
            raise PluginError(f"Invalid tool directory or missing README.md: {name}")
    overview = (root / "README.md").read_text(encoding="utf-8")
    ordered = list(dict.fromkeys(name for name in TOOL_ROW.findall(overview) if name in names))
    return ordered + sorted(set(names) - set(ordered))


def normalize_encoding(file):
    """Decode BOM-marked upstream pages in memory, preserving their Git bytes."""
    if file.abs_src_path is None:
        return
    path = Path(file.abs_src_path)
    with path.open("rb") as source:
        prefix = source.read(4)
    if prefix.startswith((b"\xff\xfe\x00\x00", b"\x00\x00\xfe\xff")):
        file.content_string = path.read_bytes().decode("utf-32")
    elif prefix.startswith((b"\xff\xfe", b"\xfe\xff")):
        file.content_string = path.read_bytes().decode("utf-16")


def page_title(file):
    text = file.content_string
    match = HEADING.search("\n".join(text.splitlines()[:80]))
    if not match:
        return PurePosixPath(file.src_uri).stem
    title = LINK_LABEL.sub(r"\1", match[1])
    return re.sub(r"[`*_]", "", title).strip() or PurePosixPath(file.src_uri).stem


def directory_nav(directory, paths, docs_dir):
    """Keep upstream hierarchy; every published Markdown page appears once."""
    prefix = directory + "/"
    direct = sorted(p for p in paths if p.startswith(prefix) and "/" not in p[len(prefix):])
    children = sorted({p[len(prefix):].split("/")[0] for p in paths if p.startswith(prefix) and "/" in p[len(prefix):]}, key=str.casefold)
    entries = []
    for filename in ("README.md", "index.md"):
        path = prefix + filename
        if path in direct:
            entries.append({"概览": path})
            direct.remove(path)
    for child in children:
        entries.append({child: directory_nav(prefix + child, paths, docs_dir)})
    for path in direct:
        entries.append({page_title(paths[path]): path})
    return entries


def on_files(files, config, **kwargs):
    tools = tool_order(config.docs_dir)
    allowed_roots = set(tools) | {"assets"}
    published = Files([
        file for file in files
        if file.src_uri in ROOT_PAGES or PurePosixPath(file.src_uri).parts[0] in allowed_roots
    ])
    pages = {file.src_uri: file for file in published.documentation_pages()}
    for file in pages.values():
        normalize_encoding(file)
    missing = set(ROOT_PAGES) - pages.keys()
    if missing:
        raise PluginError(f"Missing site pages: {', '.join(sorted(missing))}")
    config.nav = [
        {"首页": "README.md"},
        {"工具资料": [{tool: directory_nav(tool, pages, config.docs_dir)} for tool in tools]},
    ]
    return published
