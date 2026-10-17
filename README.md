# MindStudio 26.2.0 工具链文档

本仓库汇总 MindStudio 各上游仓库 **`26.2.0` 分支**的资料，为 DeepWiki、ZRead 等工具提供统一的跨工具文档索引与引用来源。

每个工具使用独立的顶层目录，目录内部保留上游相对路径、文档原文和附件。

## 工具资料入口

| 工具 | 内容 | 资料入口 |
| --- | --- | --- |
| mstt | 训练开发工具链、框架迁移与训练性能调优 | [README](mstt/README.md) |
| msit | 推理开发工具链、模型分析与推理验证 | [README](msit/README.md) |
| msot | 算子开发工具链 | [README](msot/README.md) |
| msagent | 面向昇腾 NPU 的 AI 辅助调试调优及 Skills 参考资料 | [README](msagent/README.md) |
| msboost | HostBound 场景的线程绑核与亲和性调度优化 | [README](msboost/README.md) |
| msprobe | 精度数据采集、比对与异常定位 | [README](msprobe/README.md) |
| msprof | 模型性能数据采集与解析 | [README](msprof/README.md) |
| msprof-analyze | 性能分析、集群分析与性能比对 | [README](msprof-analyze/README.md) |
| msmemscope | 内存采集、泄漏分析与显存调优 | [README](msmemscope/README.md) |
| msinsight | 性能数据可视化分析 | [README](msinsight/README.md) |
| mspti | 昇腾 Profiling 接口 | [README](mspti/README.md) |
| msmonitor | 在线监控与动态性能采集 | [README](msmonitor/README.md) |
| msmodelslim | 模型量化与压缩 | [README](msmodelslim/README.md) |
| msserviceprofiler | 服务化性能采集、分析与参数寻优 | [README](msserviceprofiler/README.md) |
| msmodeling | 模型与服务化场景的性能建模 | [README](msmodeling/README.md) |
| mskpp | 算子性能预测 | [README](mskpp/README.md) |
| msopgen | 算子工程生成 | [README](msopgen/README.md) |
| mskl | Kernel 快捷调用与验证 | [README](mskl/README.md) |
| mssanitizer | 算子内存、竞争、初始化与同步异常检测 | [README](mssanitizer/README.md) |
| msdebug | 昇腾原生调试 | [README](msdebug/README.md) |
| msopprof | 算子性能采集与分析 | [README](msopprof/README.md) |
| msopcom | 算子工具公共组件 | [README](msopcom/README.md) |
| msoptuner | 算子 Tiling 参数寻优 | [README](msoptuner/README.md) |
| mstx | 扩展打点接口 | [README](mstx/README.md) |

## 阅读与引用

- 先查对应工具的 README，再进入其 `docs/`、子组件资料或示例说明；同时收录上游已有的中英文版本。
- 文档中的版本历史及外部链接保留上游原文；链接指向 `master` 或旧版本，不改变本次文件取自 `26.2.0` 分支的来源事实。
- `msmonitor` 统一使用上游仓库同名目录。
