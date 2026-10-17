# 文档网站维护

本站使用 MkDocs + Material，将仓库根目录的聚合资料构建为 Read the Docs 文档网站。工具正文和附件保持上游原文，展示适配只在构建时进行。

## 本地构建

在仓库根目录使用 Python 3.12：

```bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows PowerShell 使用：.venv\Scripts\Activate.ps1
python -m pip install -r requirements-docs.txt
python -m unittest discover -s tests/docs -v
python -m mkdocs build --strict
```

默认输出目录为仓库同级的 `26.2.0-site/`。也可用 `--site-dir <目录>` 指定独立输出目录。

本地预览：

```bash
python -m mkdocs serve
```

打开命令输出的本地地址即可浏览；本地全文搜索同时支持中文与英文。

## 在 Read the Docs 导入

1. 登录 Read the Docs，连接拥有该仓库访问权限的 GitHub 账号。
2. 导入 `https://github.com/mindstudio-docs/26.2.0`，或手动填写仓库地址。
3. 将默认构建分支设置为 **`main`**，确认配置文件为根目录的 `.readthedocs.yaml`。
4. 触发首次构建，检查构建日志和生成的首页。
5. 检查 GitHub webhook/集成状态，确认后续推送能够触发构建；按需启用拉取请求预览。

`26.2.0` 是仓库名称和上游资料版本，当前仓库的构建分支是 `main`。项目 slug 和公开站点地址以 Read the Docs 导入结果为准。

构建环境通过 `READTHEDOCS_CANONICAL_URL` 设置 canonical URL，本地构建不需要填写此变量。页面编辑入口始终指向 GitHub 的 `main` 分支。

## 配置与导航

| 文件 | 职责 |
| --- | --- |
| `.readthedocs.yaml` | Ubuntu、Python 3.12、依赖安装和严格构建 |
| `mkdocs.yml` | 主题、搜索、Markdown 扩展和验证级别 |
| `requirements-docs.in` / `requirements-docs.txt` | 直接依赖及包含传递依赖的版本锁定清单 |
| `hooks/nav_tree.py` | 发布范围、工具导航和 BOM 标记的 UTF-16/UTF-32 文档解码 |
| `hooks/md_in_html_fix.py` | HTML 中的 Markdown、目录式页面 URL 下的 HTML 链接、本地图片与元数据链接适配 |
| `assets/stylesheets/extra.css` | 内容宽度、表格和徽章样式 |

工具范围读取 `.sync/manifest.json`，顺序参考首页工具表；导航覆盖已发布的全部 Markdown 文档，保留中英文及子组件目录结构。新增工具资料时，应同时更新同步清单及首页入口。

少数上游文档使用带 BOM 的 UTF-16 编码，Hook 在内存中解码后交给 MkDocs，仓库文件的原始编码及哈希保持不变。

网站发布首页、工具目录及站点资源。资料来源和建站维护说明仅保留在代码仓库中，不加入站点导航或发布页面；同步元数据、测试、Hook 和设计记录也不作为站点文件发布。

## 验证与排查

- **导航不完整或工具缺失**：检查同步清单中的仓库名称、工具目录及 `README.md` 是否存在。
- **构建失败**：先运行上面的单元测试和 `mkdocs build --strict`，查看首条错误或 WARNING。
- **上游缺失链接或锚点**：使用 INFO 级别记录，避免既有问题阻断整站发布。来源审计见根目录 `SOURCES.md` 与 `.sync/link-audit.json`。
- **图片**：原文中的 GitCode raw 图片若在聚合目录中有对应文件，会在构建时使用本地附件；未收录的远程图片保持原始地址。

更新文档构建依赖时，修改 `requirements-docs.in`，使用 uv 重新锁定，并重新运行测试及完整构建：

```bash
uv pip compile requirements-docs.in --python-version 3.12 --universal --output-file requirements-docs.txt
```

`mkdocs-same-dir` 固定在兼容 MkDocs 的版本；升级前需核实其项目依赖，避免引入面向其他构建器的版本。
