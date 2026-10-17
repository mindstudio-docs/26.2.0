# 文档来源与同步范围

## 本次同步

- 来源：GitCode `Ascend` 组织下的 **24 个 MindStudio 上游仓库**。
- 来源分支：每个仓库自身的 `26.2.0` 分支；导入时锁定到下表的具体提交。
- 结果：**6,557 个上游文件，其中 2,497 个 Markdown 文件**，共 922,776,757 字节；不含本仓库首页和同步元数据。
- 目录映射：上游 `<仓库>/<相对路径>` → 本仓库 `<仓库名>/<相同相对路径>`。
- 追溯清单：[`.sync/manifest.json`](.sync/manifest.json)，记录同步时间、仓库 URL、分支、提交、范围、每个文件的路径和哈希。

上游范围以既有 `mindstudio-docs/26.1.0`、`mindstudio-docs/master` 的工具清单为起点，并核对 `mstt`、`msit`、`msot` 的 `26.2.0` 分支工具入口及各仓库实际分支。所有已导入仓库均通过 Git 验证存在 `refs/heads/26.2.0`；子模块中记录的历史提交不作为本次工具资料的来源。

## 每个仓库的资料路径

上游仓库 URL 统一为 `https://gitcode.com/Ascend/<仓库名>.git`。

下表“主要资料树”按收录规则保留其文件；“补充资料所在目录”只收录其中的文档及文档直接引用的文件，**不代表复制整个组件源码目录**。此外，各仓根目录的 README、中英文 README 和已有的贡献、许可等文档也纳入范围；具体文件以同步清单为准。

| 工具目录 | 主要资料树（上游相对路径） | 补充资料所在目录 | 文件数 / Markdown 数 | 来源提交 |
| --- | --- | --- | ---: | --- |
| [msagent](msagent/README.md) | `docs/`, `skills/profiler/mindstudio-cpu-binding/docs/` | `resources/`, `skills/` | 501 / 365 | [`9821bf264ddf`](https://gitcode.com/Ascend/msagent/commit/9821bf264ddf50504dbb305f84e22b8c6d550a98) |
| [msboost](msboost/README.md) | `docs/` | `KAOT/`, `oec-ascend/` | 7 / 6 | [`924fe4048ee6`](https://gitcode.com/Ascend/msboost/commit/924fe4048ee62306b0f32ea8de494da2c153c610) |
| [msdebug](msdebug/README.md) | `docs/` | `example/` | 61 / 31 | [`31a5680b803a`](https://gitcode.com/Ascend/msdebug/commit/31a5680b803a22eeebab64a50b233be75f340bb6) |
| [msinsight](msinsight/README.md) | `docs/`, `scripts/ftrace_tools/docs/` | `docker/`, `modules/`, `scripts/`, `server/`, `streamer/` | 1617 / 108 | [`dc1fe484dd54`](https://gitcode.com/Ascend/msinsight/commit/dc1fe484dd544bb059b11603364e71d9889cc11c) |
| [msit](msit/README.md) | `docs/`, `msit/docs/` | `msit/`, `msprechecker/` | 84 / 60 | [`86d9a0535849`](https://gitcode.com/Ascend/msit/commit/86d9a05358494f4d68299b906feab1a0eb848676) |
| [mskl](mskl/README.md) | `docs/` | — | 32 / 26 | [`a30e4426e63f`](https://gitcode.com/Ascend/mskl/commit/a30e4426e63f77a03e4a0c46e47d2bba02379551) |
| [mskpp](mskpp/README.md) | `docs/` | — | 60 / 26 | [`e5af7ba64e3f`](https://gitcode.com/Ascend/mskpp/commit/e5af7ba64e3fc37c0114de2dc5833fe2e0cd00c9) |
| [msmemscope](msmemscope/README.md) | `docs/` | `example/` | 112 / 44 | [`d4dfaca20d73`](https://gitcode.com/Ascend/msmemscope/commit/d4dfaca20d736783f5ac94535617bc71554cdfef) |
| [msmodeling](msmodeling/README.md) | `docs/`, `web_ui/frontend/public/docs/` | `contrib/`, `optix/`, `scripts/`, `serving_cast/`, `spec/`, `tensor_cast/`, `tools/` | 211 / 178 | [`5480509cca67`](https://gitcode.com/Ascend/msmodeling/commit/5480509cca67edb4bda1b4bf87d6fd5a92d8d922) |
| [msmodelslim](msmodelslim/README.md) | `docs/` | `example/`, `lab_calib/`, `skills/` | 880 / 639 | [`e4ee01a38e68`](https://gitcode.com/Ascend/msmodelslim/commit/e4ee01a38e682af3688b552a63316f9a7faf66aa) |
| [msmonitor](msmonitor/README.md) | `docs/` | — | 102 / 43 | [`59d7446bbaab`](https://gitcode.com/Ascend/msmonitor/commit/59d7446bbaab289950ed84772b88cfc6cf36efe6) |
| [msopcom](msopcom/README.md) | `docs/` | — | 20 / 16 | [`892c3ca76b71`](https://gitcode.com/Ascend/msopcom/commit/892c3ca76b71c3167804977c12db9000abf0b9df) |
| [msopgen](msopgen/README.md) | `docs/` | `example/`, `tools/` | 59 / 33 | [`60a89813ad0c`](https://gitcode.com/Ascend/msopgen/commit/60a89813ad0c8378734495620729bc9b3f81486d) |
| [msopprof](msopprof/README.md) | `docs/` | `example/` | 243 / 44 | [`631264d626d1`](https://gitcode.com/Ascend/msopprof/commit/631264d626d10041ad71297797b484f39608d729) |
| [msoptuner](msoptuner/README.md) | `docs/` | `tuner/` | 17 / 13 | [`e181b11a6ace`](https://gitcode.com/Ascend/msoptuner/commit/e181b11a6ace906eeeba79233ed375660ea6e40e) |
| [msot](msot/README.md) | `docs/` | — | 73 / 37 | [`23310db4deca`](https://gitcode.com/Ascend/msot/commit/23310db4deca8b3f85abcd1d2dbc31d3a714f8fa) |
| [msprobe](msprobe/README.md) | `docs/` | `plugins/` | 631 / 157 | [`a47651c8b62b`](https://gitcode.com/Ascend/msprobe/commit/a47651c8b62bec9de9d921808a2a6ba785bcc8ed) |
| [msprof-analyze](msprof-analyze/README.md) | `docs/` | `misc/` | 192 / 58 | [`d59443361ad9`](https://gitcode.com/Ascend/msprof-analyze/commit/d59443361ad9f6a0636fea8d8cc1e2649dcf9e12) |
| [msprof](msprof/README.md) | `docs/` | `misc/`, `samples/` | 425 / 85 | [`6ad7c6ae2353`](https://gitcode.com/Ascend/msprof/commit/6ad7c6ae2353b643e67197a81ffcecf461b714a2) |
| [mspti](mspti/README.md) | `docs/` | `samples/` | 213 / 203 | [`5f69dfe1d62a`](https://gitcode.com/Ascend/mspti/commit/5f69dfe1d62a210c56328d763969bbaef6d79588) |
| [mssanitizer](mssanitizer/README.md) | `docs/` | `example/` | 47 / 38 | [`5a2589ce3303`](https://gitcode.com/Ascend/mssanitizer/commit/5a2589ce33039fbeaefae50b75c7227d6a31d37f) |
| [msserviceprofiler](msserviceprofiler/README.md) | `docs/` | `ms_service_metric/`, `ms_service_profiler/`, `ms_serviceparam_optimizer/` | 260 / 183 | [`374bc0ff8c20`](https://gitcode.com/Ascend/msserviceprofiler/commit/374bc0ff8c20a86c8b1a5bd81aedfb8031b415f4) |
| [mstt](mstt/README.md) | `docs/`, `msfmktransplt/docs/` | `msfmktransplt/`, `plugins/`, `profiler/` | 660 / 58 | [`3ae37ee3bdf9`](https://gitcode.com/Ascend/mstt/commit/3ae37ee3bdf97b0cdfd5741b1ae6e9974475bec4) |
| [mstx](mstx/README.md) | `docs/` | — | 50 / 46 | [`a5b57a17ca8b`](https://gitcode.com/Ascend/mstx/commit/a5b57a17ca8bcc9da6652319e15aae1d99cb571d) |

## 收录规则

1. **根目录资料**：已有的 Markdown、reStructuredText、README 各语言版本，以及 LICENSE、NOTICE、版权和第三方许可说明。
2. **资料目录**：`doc/`、`docs/`、`documentation/` 中的正文、图片、动图、表格、示例配置、HTML 等资源；覆盖子组件的同类目录。
3. **分散资料**：资料目录外的 Markdown/reStructuredText，包括组件说明、示例说明、Skills 参考资料、设计与开发指南。
4. **引用附件**：补充静态相对链接直接引用、且在同一上游提交中存在的普通文件，如图片、配置、脚本和代码示例。此类文件在清单中标记为 `linked_resource`。
5. **范围排除**：隐藏文件/目录、测试目录、第三方依赖和代理控制文件（`AGENTS.md`、`CLAUDE.md`、`GEMINI.md`、`agent_router.md`）；不递归导入 Git 子模块。`msdebug` 的资料范围限定为根目录资料、`docs/` 和 `example/` 的文档，避免将其 LLVM 源码树的资料混入。

普通文件保持上游原始字节，包括换行符；没有改写版本链接、翻译正文或重新生成工具说明。`.gitattributes` 防止 Git 在提交工具资料时自动转换换行符。

`msmodeling/docs/perf_database/forward_pass_traces/` 中的 **5 个 Git LFS CSV** 已下载为实际数据文件，按上游 LFS 指针中的 SHA-256 和长度校验。清单同时记录上游指针的 Git 对象哈希、实际文件哈希和 LFS SHA-256，避免将指针文本当作数据内容。

## 特殊范围处理

- **`msopmodeling`**：`https://gitcode.com/Ascend/msopmodeling.git` 及原始文件接口拒绝访问，无法核实 `26.2.0` 分支。用户已明确要求跳过；未创建该工具目录，也未用其他分支资料代替。
- **`msmonitor-dyno` / `msmonitor-whl`**：旧聚合仓中的两个目录均指向 `Ascend/msmonitor`，同名独立上游未能访问。本次按实际可访问的 `Ascend/msmonitor` 的 `26.2.0` 分支统一导入 `msmonitor/`。

## 校验与链接扫描

- 导出文件逐一校验 Git blob SHA-1；5 个 LFS 数据文件额外校验 SHA-256 和长度。
- 静态扫描 Markdown 内联/引用式链接及 HTML `href`/`src`，补齐可解析且符合范围的文件目标。
- 扫描记录见 [`.sync/link-audit.json`](.sync/link-audit.json)：42 条目标在来源提交中不存在、35 条指向范围排除文件、42 条指向未收录的源码/资源目录、1 条越出上游仓库边界。
- 上述数字按链接出现次数计，并非完整 Markdown/HTML 解析器确认的错误数；扫描跳过代码围栏、外部 URL 与锚点验证。原文中的这些引用保留，以便与上游逐字追溯。

后续更新应重新读取各上游 `26.2.0` 分支、按相同路径规则提取资料，并更新来源提交、文件清单及校验结果。
