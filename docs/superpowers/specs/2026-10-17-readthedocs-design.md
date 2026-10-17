# Read the Docs 接入设计

## 目标与已确认方案

将当前 MindStudio 26.2.0 聚合仓接入 Read the Docs。用户已确认采用前一轮提出的 MkDocs + Material、根目录配置、自动导航和渲染兼容 Hook 方案，并要求创建分支、合入并提交。

## 方案选择

- **采用：MkDocs + Material，直接读取聚合目录。** 延续 26.1.0 聚合仓做法，保持上游路径和哈希；使用兼容 MkDocs 1.x 的固定版本 same-dir 插件。
- Sphinx + MyST：需要另加 Markdown 转换和导航适配，当前没有收益。
- 构建前复制到独立 docs 树：可避免 same-dir 插件，但增加近 1 GB 资料的重复复制和路径维护。

## 组件与数据流

1. `.readthedocs.yaml`：使用受支持的 Ubuntu 构建环境和 Python 3.12，安装 `requirements-docs.txt`，通过 `mkdocs.yml` 构建。
2. `mkdocs.yml`：Material 中文界面，中英文搜索，代码复制、表格、HTML 内 Markdown 支持。站点 canonical URL 从 Read the Docs 环境变量获取；编辑链接固定当前仓库的 `main` 分支。
3. `hooks/nav_tree.py`：从 `.sync/manifest.json` 识别工具，以根 README 工具顺序生成导航；只发布首页、来源说明、建站说明、工具资料和站点 assets。原始同步元数据、Hook、测试、设计记录不进入站点。
4. `hooks/md_in_html_fix.py`：仅在构建内存中兼容 HTML 中的 Markdown；可用的 GitCode 图片转为本地资源；站点中对同步清单的引用转到 GitHub。
5. `docs/site-maintenance.md`：记录本地构建命令和 Read the Docs 导入、分支选择、构建操作。

流程：Read the Docs 拉取当前仓库 main → 安装固定文档依赖 → 发现资料与生成导航 → 仅在构建时处理展示兼容 → 输出静态站点。仓库名 26.2.0 表示上游资料版本，不用作本仓构建分支。

## 内容边界与错误处理

- 上游 `ms*/` 文件保持原始字节，不在工具目录添加或改写建站配置。
- 保留中英文文档以及附件；README 文件继续作为工具和子目录入口。
- 不预设 Read the Docs 项目 slug；使用平台 canonical URL，避免写入尚未创建的站点地址。
- 上游已存在的缺失链接与锚点以 info 记录，不阻断构建；新增站点文件及导航必须通过独立检查。
- 同步清单缺失、重复导航或未知工具范围等配置错误应明确失败。
- 在 Read the Docs 平台导入仓库和开启自动构建属于后续平台操作，本次交付为仓库配置。

## 验收与执行计划

1. 创建 `docs/readthedocs-setup` 分支，保留用户要求的 README 删除修改。
2. 添加配置、固定依赖、自动导航和渲染 Hook，以及维护说明。
3. 对导航覆盖、发布范围、HTML Markdown 渲染和本地图片映射运行针对性测试。
4. 在 Python 3.12 环境执行完整严格构建，核实首页、msmodeling、中英文页面、附件及搜索索引。
5. 对所有导入工具文件重算哈希，确认与同步清单一致。
6. 提交实现，在 main 上快进合入，并推送分支和 main；确认远端提交一致。
