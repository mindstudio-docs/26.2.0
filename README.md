# MindStudio 26.2.0 工具链文档

MindStudio 是华为面向昇腾 AI 开发者提供的全流程工具链，致力于提供端到端的昇腾 AI 应用开发解决方案，使能开发者高效完成训练开发、推理开发和算子开发。

本文档对应 **MindStudio 26.2.0**，各工具资料入口如下。

## 工具简介及资料入口

| 工具目录 | 功能简介 | README |
| --- | --- | --- |
| mstt | **【训练开发工具链】** 提供分析迁移、精度调试与性能调优能力，助力实现精度与性能双优。 | [mstt/README.md](mstt/README.md) |
| msit | **【推理开发工具链】** 提供模型分析、压缩、调试与调优等能力，助力用户提升推理性能。 | [msit/README.md](msit/README.md) |
| msot | **【算子开发工具链】** 提供算子设计、开发框架生成、功能调试、异常检测与多维性能调优等能力。 | [msot/README.md](msot/README.md) |
| msboost | **【亲和调优】** 面向训练与推理的 HostBound 场景，提供线程绑核、任务分组与亲和性调度能力，减少资源干扰。 | [msboost/README.md](msboost/README.md) |
| msprobe | **【精度调试】** 昇腾全场景精度工具，提供数据采集、精度比对与异常检测，辅助定位训练和推理中的精度问题。 | [msprobe/README.md](msprobe/README.md) |
| msprof | **【模型调优】** 采集与解析 CANN 层和昇腾 AI 处理器的软硬件性能数据，为训练和推理性能调优提供基础能力。 | [msprof/README.md](msprof/README.md) |
| msprof-analyze | **【性能分析】** 基于采集数据进行性能分析、集群分析与性能比对，帮助识别性能瓶颈。 | [msprof-analyze/README.md](msprof-analyze/README.md) |
| msmemscope | **【内存调优】** 提供内存采集、泄漏分析、内存对比、监测与拆解等能力，辅助定位和优化内存问题。 | [msmemscope/README.md](msmemscope/README.md) |
| mspti | **【性能剖析】** 提供面向昇腾的 Profiling 接口，支持开发 NPU 应用性能分析工具。 | [mspti/README.md](mspti/README.md) |
| msmonitor | **【在线监控】** 提供集群在线监控与动态性能采集能力，辅助运行状态监测和性能问题定位。 | [msmonitor/README.md](msmonitor/README.md) |
| msmodelslim | **【模型压缩】** 提供量化和压缩等推理优化技术，支持大语言稠密模型、MoE 模型及多模态模型等场景。 | [msmodelslim/README.md](msmodelslim/README.md) |
| msserviceprofiler | **【服务调优】** 提供服务化性能采集、请求与模型执行分析及参数寻优能力，提升服务化性能分析效率。 | [msserviceprofiler/README.md](msserviceprofiler/README.md) |
| msmodeling | **【建模寻优】** 评估模型及服务化场景下的理论性能，并探索性能较优的部署策略与参数。 | [msmodeling/README.md](msmodeling/README.md) |
| mskpp | **【性能预测】** 支持输入算子描述，预测算子在特定算法实现下的性能上限。 | [mskpp/README.md](mskpp/README.md) |
| msopgen | **【工程生成】** 提供算子模板工程生成能力，简化工程搭建，提升算子开发效率。 | [msopgen/README.md](msopgen/README.md) |
| mskl | **【快捷调用】** 提供 Python 接口，快速实现 Kernel 的下发运行，便于完成功能验证。 | [mskl/README.md](mskl/README.md) |
| mssanitizer | **【异常检测】** 提供内存、竞争、未初始化及同步检测，辅助定位多核程序中的异常问题。 | [mssanitizer/README.md](mssanitizer/README.md) |
| msdebug | **【原生调试】** 基于昇腾处理器的原生环境调试，支持变量查看、单步执行及上板调试。 | [msdebug/README.md](msdebug/README.md) |
| msopprof | **【性能分析】** 支持算子上板与仿真性能数据采集，结合可视化分析定位算子性能瓶颈。 | [msopprof/README.md](msopprof/README.md) |
| msopcom | **【基础组件】** 为算子工具提供统一劫持能力，支持桩函数注入、接口劫持与注入函数管理。 | [msopcom/README.md](msopcom/README.md) |
| msoptuner | **【Tiling 寻优】** 面向 CATLASS 模板库算子，支持自定义搜索空间并批量完成在板性能测试。 | [msoptuner/README.md](msoptuner/README.md) |
| mstx | **【扩展打点】** 提供打点接口，用于标记关键函数或时间段，辅助性能和算子问题定界。 | [mstx/README.md](mstx/README.md) |
