import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest

import markdown
from mkdocs.config import load_config
from mkdocs.exceptions import PluginError
from mkdocs.structure.files import File, Files, get_files


ROOT = Path(__file__).resolve().parents[2]


def load_hook(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "hooks" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


nav = load_hook("nav_tree")
render = load_hook("md_in_html_fix")


def nav_paths(items):
    for item in items:
        for value in item.values():
            if isinstance(value, list):
                yield from nav_paths(value)
            else:
                yield value


class NavigationTests(unittest.TestCase):
    def test_real_repository_pages_are_published_once(self):
        with TemporaryDirectory() as output:
            config = load_config(str(ROOT / "mkdocs.yml"), site_dir=output)
            config = config.plugins.on_config(config)
            files = config.plugins.on_files(get_files(config), config=config)
            pages = {file.src_uri for file in files.documentation_pages()}
            paths = list(nav_paths(config.nav))
            self.assertEqual(len(paths), len(set(paths)))
            self.assertEqual(set(paths), pages)
            self.assertIn("msmodeling/README.md", pages)
            self.assertIn("msmodeling/README_EN.md", pages)
            self.assertEqual(config.nav[1]["工具资料"][0].keys(), {"mstt"})
            published = {file.src_uri for file in files}
            self.assertIn("msmodeling/docs/perf_database/forward_pass_traces/dsv3_dc_1tok.csv", published)
            self.assertFalse(any(p.startswith((".sync/", "hooks/", "tests/", "docs/superpowers/")) for p in published))
            self.assertNotIn("requirements-docs.txt", published)
            manifest = json.loads((ROOT / ".sync/manifest.json").read_text(encoding="utf-8"))
            imported_pages = {
                repo["name"] + "/" + file["path"]
                for repo in manifest["repositories"] for file in repo["files"]
                if file["path"].endswith(".md")
            }
            self.assertEqual(pages, imported_pages | set(nav.ROOT_PAGES))

    def test_inventory_and_missing_entry_points_fail_explicitly(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaisesRegex(PluginError, "inventory"):
                nav.tool_order(root)
            (root / ".sync").mkdir()
            inventory = root / ".sync/manifest.json"
            inventory.write_text(json.dumps({"repositories": [{"name": "msmissing"}]}))
            with self.assertRaisesRegex(PluginError, "missing README"):
                nav.tool_order(root)
            inventory.write_text(json.dumps({"repositories": [{"name": "msx"}, {"name": "msx"}]}))
            with self.assertRaisesRegex(PluginError, "unique"):
                nav.tool_order(root)

    def test_utf16_import_is_decoded_only_in_memory(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            original = '# 分位数\n\n说明。'.encode('utf-16')
            source = root / 'quantile.md'
            source.write_bytes(original)
            file = File('quantile.md', directory, str(root / 'site'), True)
            nav.normalize_encoding(file)
            self.assertEqual(nav.page_title(file), '分位数')
            self.assertEqual(file.content_string, '# 分位数\n\n说明。')
            self.assertEqual(source.read_bytes(), original)


class RenderingTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "msprobe/docs").mkdir(parents=True)
        self.source = self.root / "msprobe/README.md"
        self.config = SimpleNamespace(docs_dir=str(self.root), repo_url="https://github.com/mindstudio-docs/26.2.0")
        self.page = SimpleNamespace(file=SimpleNamespace(abs_src_path=str(self.source), src_uri="msprobe/README.md"))

    def transform(self, text):
        return render.on_page_markdown(text, self.page, self.config)

    def test_html_markdown_is_rendered_without_editing_source(self):
        source = '<div align="center">\n\n[快速入门](docs/start.md)\n\n</div>\n'
        self.source.write_text(source, encoding="utf-8")
        result = self.transform(source)
        html = markdown.markdown(result, extensions=["md_in_html"])
        self.assertIn('<a href="docs/start.md">快速入门</a>', html)
        self.assertEqual(self.source.read_text(encoding="utf-8"), source)
        self.assertEqual(self.transform(result), result)

    def test_existing_markdown_attributes_and_fenced_examples_are_preserved(self):
        source = '<div markdown="0">plain</div>\n````html\n<div>\n```\n<div>\n````\n<div>\n'
        result = self.transform(source)
        self.assertTrue(result.startswith('<div markdown="0">plain</div>\n````html\n<div>\n```\n<div>\n````\n'))
        self.assertTrue(result.endswith('<div markdown="1">\n'))

    def test_inline_code_examples_are_preserved(self):
        source = 'Use `<div>` or ``<div markdown="1">`` here.\n'
        self.assertEqual(self.transform(source), source)

    def test_local_image_paths_are_relative_and_url_encoded(self):
        target = self.root / "msprobe/docs/图 示例.png"
        target.write_bytes(b"example")
        url = 'https://raw.gitcode.com/Ascend/msprobe/raw/26.2.0/docs/%E5%9B%BE%20%E7%A4%BA%E4%BE%8B.png'
        result = self.transform(f'<img src="{url}">')
        self.assertIn('src="docs/%E5%9B%BE%20%E7%A4%BA%E4%BE%8B.png"', result)
        self.assertEqual(self.transform(f'![missing]({url}x)'), f'![missing]({url}x)')

    def test_cross_tool_images_and_metadata_links(self):
        (self.root / "msit/docs").mkdir(parents=True)
        (self.root / "msit/docs/image.png").write_bytes(b"example")
        source = '![image](https://raw.gitcode.com/Ascend/msit/files/master/docs/image.png)'
        self.assertEqual(self.transform(source), '![image](../msit/docs/image.png)')
        self.page.file.src_uri = "README.md"
        result = self.transform('[来源](.sync/manifest.json)')
        self.assertIn('https://github.com/mindstudio-docs/26.2.0/blob/main/.sync/manifest.json', result)

    def test_raw_html_links_follow_generated_directory_urls(self):
        page_file = File('msprobe/docs/guide.md', str(self.root), str(self.root / 'site'), True)
        image = File('msprobe/docs/figures/image.png', str(self.root), str(self.root / 'site'), True)
        other = File('msprobe/docs/other.md', str(self.root), str(self.root / 'site'), True)
        page = SimpleNamespace(file=page_file)
        source = '<img src="./figures/image.png"><a href="other.md#usage">用法</a>\n'
        result = render.on_page_markdown(source, page, self.config, files=Files([page_file, image, other]))
        self.assertIn('src="../figures/image.png"', result)
        self.assertIn('href="../other/#usage"', result)


if __name__ == "__main__":
    unittest.main()
