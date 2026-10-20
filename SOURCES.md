# 文档来源与同步范围

## 当前范围

- 来源：GitCode `Ascend` 组织下的 **22 个 MindStudio 上游仓库**。
- 内容版本：各仓库的 `26.2.0` 分支，保持下表已锁定的来源提交。
- 范围基准：[mindstudio-docs/26.1.0，提交 15c1db0](https://github.com/mindstudio-docs/26.1.0/tree/15c1db011a2f1c7040f4aa7a624fe9536cbd3659)。
- 收录规则：每个工具仅收录 **`README.md` 与根目录 `docs/` 下的全部普通文件**，包括图片、动图、配置和数据附件。
- 结果：**3,857 个上游文件，其中 1,754 个 Markdown 文件**，共 **458,384,935 字节**；不含本仓库首页、建站配置和同步元数据。
- 追溯清单：[`.sync/manifest.json`](.sync/manifest.json)，记录来源分支、提交、逐文件哈希与范围基准。

本次对齐的是工具范围与资料路径规则，文件内容仍取自 26.2.0，不替换为 26.1.0 文件，也不按旧版本的逐文件名单删除新版 `docs/` 内容。

26.1.0 有 23 个实际工具目录，其中 `msmonitor-dyno`、`msmonitor-whl` 均对应同一上游 `Ascend/msmonitor`。本仓统一保留 `msmonitor/`，因此为 22 个唯一上游仓库。其余工具名称与基准一致。

## 来源提交

每个工具的上游地址为 `https://gitcode.com/Ascend/<工具名>.git`，资料路径均为 `README.md` 和 `docs/`。

| 工具 | 文件数 / Markdown 数 | 26.2.0 来源提交 |
| --- | ---: | --- |
| [msboost](msboost/README.md) | 4 / 4 | [`924fe4048ee6`](https://gitcode.com/Ascend/msboost/commit/924fe4048ee62306b0f32ea8de494da2c153c610) |
| [msdebug](msdebug/README.md) | 53 / 25 | [`31a5680b803a`](https://gitcode.com/Ascend/msdebug/commit/31a5680b803a22eeebab64a50b233be75f340bb6) |
| [msit](msit/README.md) | 39 / 23 | [`86d9a0535849`](https://gitcode.com/Ascend/msit/commit/86d9a05358494f4d68299b906feab1a0eb848676) |
| [mskl](mskl/README.md) | 30 / 25 | [`a30e4426e63f`](https://gitcode.com/Ascend/mskl/commit/a30e4426e63f77a03e4a0c46e47d2bba02379551) |
| [mskpp](mskpp/README.md) | 58 / 25 | [`e5af7ba64e3f`](https://gitcode.com/Ascend/mskpp/commit/e5af7ba64e3fc37c0114de2dc5833fe2e0cd00c9) |
| [msmemscope](msmemscope/README.md) | 99 / 37 | [`d4dfaca20d73`](https://gitcode.com/Ascend/msmemscope/commit/d4dfaca20d736783f5ac94535617bc71554cdfef) |
| [msmodeling](msmodeling/README.md) | 156 / 147 | [`5480509cca67`](https://gitcode.com/Ascend/msmodeling/commit/5480509cca67edb4bda1b4bf87d6fd5a92d8d922) |
| [msmodelslim](msmodelslim/README.md) | 569 / 517 | [`e4ee01a38e68`](https://gitcode.com/Ascend/msmodelslim/commit/e4ee01a38e682af3688b552a63316f9a7faf66aa) |
| [msmonitor](msmonitor/README.md) | 99 / 42 | [`59d7446bbaab`](https://gitcode.com/Ascend/msmonitor/commit/59d7446bbaab289950ed84772b88cfc6cf36efe6) |
| [msopcom](msopcom/README.md) | 18 / 15 | [`892c3ca76b71`](https://gitcode.com/Ascend/msopcom/commit/892c3ca76b71c3167804977c12db9000abf0b9df) |
| [msopgen](msopgen/README.md) | 54 / 29 | [`60a89813ad0c`](https://gitcode.com/Ascend/msopgen/commit/60a89813ad0c8378734495620729bc9b3f81486d) |
| [msopprof](msopprof/README.md) | 213 / 35 | [`631264d626d1`](https://gitcode.com/Ascend/msopprof/commit/631264d626d10041ad71297797b484f39608d729) |
| [msoptuner](msoptuner/README.md) | 14 / 11 | [`e181b11a6ace`](https://gitcode.com/Ascend/msoptuner/commit/e181b11a6ace906eeeba79233ed375660ea6e40e) |
| [msot](msot/README.md) | 72 / 36 | [`23310db4deca`](https://gitcode.com/Ascend/msot/commit/23310db4deca8b3f85abcd1d2dbc31d3a714f8fa) |
| [msprobe](msprobe/README.md) | 614 / 154 | [`a47651c8b62b`](https://gitcode.com/Ascend/msprobe/commit/a47651c8b62bec9de9d921808a2a6ba785bcc8ed) |
| [msprof](msprof/README.md) | 403 / 77 | [`6ad7c6ae2353`](https://gitcode.com/Ascend/msprof/commit/6ad7c6ae2353b643e67197a81ffcecf461b714a2) |
| [msprof-analyze](msprof-analyze/README.md) | 182 / 53 | [`d59443361ad9`](https://gitcode.com/Ascend/msprof-analyze/commit/d59443361ad9f6a0636fea8d8cc1e2649dcf9e12) |
| [mspti](mspti/README.md) | 209 / 201 | [`5f69dfe1d62a`](https://gitcode.com/Ascend/mspti/commit/5f69dfe1d62a210c56328d763969bbaef6d79588) |
| [mssanitizer](mssanitizer/README.md) | 37 / 29 | [`5a2589ce3303`](https://gitcode.com/Ascend/mssanitizer/commit/5a2589ce33039fbeaefae50b75c7227d6a31d37f) |
| [msserviceprofiler](msserviceprofiler/README.md) | 252 / 177 | [`374bc0ff8c20`](https://gitcode.com/Ascend/msserviceprofiler/commit/374bc0ff8c20a86c8b1a5bd81aedfb8031b415f4) |
| [mstt](mstt/README.md) | 634 / 47 | [`3ae37ee3bdf9`](https://gitcode.com/Ascend/mstt/commit/3ae37ee3bdf97b0cdfd5741b1ae6e9974475bec4) |
| [mstx](mstx/README.md) | 48 / 45 | [`a5b57a17ca8b`](https://gitcode.com/Ascend/mstx/commit/a5b57a17ca8bcc9da6652319e15aae1d99cb571d) |

## 范围调整

- 移除未出现在 26.1.0 实际资料树中的 `msagent/`、`msinsight/`。
- 移除各工具根目录除 `README.md` 外的资料，以及 `docs/` 外的子组件文档、示例、Skills 和引用附件。
- 保留每个上游根 `docs/` 下的普通文件，包括该目录内已有的许可证、隐藏构建文件和占位文件。
- 没有追随链接扩展到范围以外；原文中的相应引用保留，缺失目标由链接记录说明。

普通文件保持来源提交的原始字节，包括换行与编码；`.gitattributes` 防止 Git 自动转换上游资料的换行符。`msmodeling/docs/perf_database/forward_pass_traces/` 的 5 个 LFS CSV 继续保留真实数据，并按 SHA-256 和长度验证。

## 校验与链接记录

逐文件校验结果见 [`.sync/verification.json`](.sync/verification.json)。静态链接记录见 [`.sync/link-audit.json`](.sync/link-audit.json)：17 条目标在来源提交中不存在，582 条指向本次范围外的文件或目录。数字按链接出现次数统计，不包含外部 URL 和锚点验证。

资料来源和建站维护说明仅供仓库维护使用，不发布到 Read the Docs。

本次减少的是当前文件快照体积。Git 历史仍包含此前提交的大文件，不能将当前快照缩小等同于完整 Git 克隆体积已经下降。
