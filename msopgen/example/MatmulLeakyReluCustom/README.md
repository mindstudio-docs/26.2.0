# MatmulLeakyReluCustom 算子案例

## 概述

本样例演示如何使用 msOpGen 工具生成 **矩阵乘法 + LeakyReLU 激活** 的复合算子工程（MatmulLeakyReluCustom），并使用 msOpST 工具进行功能测试。

该算子先对输入矩阵 a、b 进行矩阵乘法，加上 bias 偏置后，再通过 LeakyReLU（alpha=0.001）激活函数得到输出。

## 支持的产品范围

- Ascend 950PR&950DT系列产品
- Atlas A3系列产品
- Atlas A2系列产品

## 目录结构

```text
MatmulLeakyReluCustom/
├── README.md                                  # 本文件
├── MatmulLeakyReluCustom.json                 # 算子原型定义文件
├── st_example/
│   └── MatmulLeakyreluCustom_case.json         # ST 测试用例示例（预配好 shape）
├── op_host/
│   ├── matmul_leakyrelu_custom.cpp            # Host 侧算子实现（Tiling + 算子注册）
│   └── matmul_leakyrelu_custom_tiling.h       # Tiling 数据结构定义
└── op_kernel/
    └── matmul_leakyrelu_custom.cpp            # Kernel 侧算子实现（Matmul + LeakyReLU）
```

## 算子定义

**算子名**：`MatmulLeakyreluCustom` | **功能**：c = LeakyReLU(matmul(a, b) + bias, alpha=0.001)

| 张量 | 名称 | 类型 | 格式 | 说明 |
|------|------|------|------|------|
| 输入 1 | `a` | float16 | ND | 矩阵 A |
| 输入 2 | `b` | float16 | ND | 矩阵 B |
| 输入 3 | `bias` | float | ND | 偏置向量 |
| 输出 | `c` | float | ND | 输出矩阵 |

## 前置条件

- CANN 工具包已安装
- `msopgen`、`msopst` 命令可用
- 参考《[msOpGen 用户指南](../../docs/zh/user_guide/msopgen_user_guide.md)》完成使用准备

## 操作步骤

以下步骤以 `Ascend910B2` 为例，请根据实际环境替换为对应的芯片型号。

### 步骤 1：确认算子原型文件

算子原型文件 `MatmulLeakyReluCustom.json` 已准备在案例目录下：

```bash
cd msopgen/example/MatmulLeakyReluCustom
cat MatmulLeakyReluCustom.json
```

### 步骤 2：使用 msOpGen 创建算子工程

```bash
msopgen gen \
    -i MatmulLeakyReluCustom.json \
    -f tf \
    -c ai_core-Ascend910B2 \
    -lan cpp \
    -out ./MatmulLeakyReluCustom
```

**参数说明**：

| 参数 | 值 | 说明 |
|------|-----|------|
| `-i` | `MatmulLeakyReluCustom.json` | 算子原型定义文件 |
| `-f` | `tf` | 框架类型（tensorflow） |
| `-c` | `ai_core-Ascend910B2` | 计算单元和芯片型号 |
| `-lan` | `cpp` | 算子开发语言（Ascend C） |
| `-out` | `./MatmulLeakyReluCustom` | 输出路径 |

命令执行完毕后，会在当前目录生成算子工程：

```text
MatmulLeakyReluCustom/
├── build.sh
├── CMakeLists.txt
├── CMakePresets.json
├── framework/
├── op_host/
│   ├── matmul_leakyrelu_custom.cpp         // Host 侧实现（模板）
│   ├── matmul_leakyrelu_custom_tiling.h    // Tiling 定义（模板）
│   └── CMakeLists.txt
└── op_kernel/
    ├── CMakeLists.txt
    └── matmul_leakyrelu_custom.cpp         // Kernel 侧实现（模板）
```

> **注意**：`msopgen gen` 生成的是空模板文件。案例目录下已提供完整的算子实现代码，直接覆盖即可：

```bash
# 将案例中的算子实现文件覆盖到生成的工程
cp op_host/matmul_leakyrelu_custom.cpp         MatmulLeakyReluCustom/op_host/
cp op_host/matmul_leakyrelu_custom_tiling.h    MatmulLeakyReluCustom/op_host/
cp op_kernel/matmul_leakyrelu_custom.cpp        MatmulLeakyReluCustom/op_kernel/
```

### 步骤 3：编译算子工程

```bash
cd MatmulLeakyReluCustom
chmod +x build.sh
./build.sh
```

编译成功后，`build_out/` 目录下会生成自定义算子安装包（`.run` 文件）。

### 步骤 4：部署自定义算子包

```bash
# 部署到 CANN 默认路径
./build_out/custom_opp_<target_os>_<target_architecture>.run

# 或部署到自定义路径
./build_out/custom_opp_<target_os>_<target_architecture>.run --install-path="/your/custom/path"
```

> `<target_os>` 和 `<target_architecture>` 根据实际编译环境确定，例如 `linux_x86_64`。

### 步骤 5：使用 msOpST 生成 ST 测试用例

```bash
# 回到案例根目录
cd ..

# 基于 Host 侧实现文件生成测试用例
msopst create -i MatmulLeakyReluCustom/op_host/matmul_leakyrelu_custom.cpp -out ./st
```

生成完毕后，`st/` 目录下会包含测试用例模板 JSON 文件。

> **注意**：`msopst create` 生成的 shape 默认为空（`[]`），需要根据算子特点手动编辑。对于矩阵乘法算子，需要设置至少 2D 的 shape。
>
> 案例目录下已提供 `st_example/MatmulLeakyreluCustom_case.json`，预配了合法的矩阵 shape（a:[1024,256] × b:[256,512] = c:[1024,512]），可直接用于测试。

### 步骤 6：配置环境变量并运行 ST 测试

```bash
# 配置环境变量
export DDK_PATH=${ASCEND_HOME_PATH}
export NPU_HOST_LIB=${ASCEND_HOME_PATH}/$(uname -m)-linux/devlib

# 方式一：使用预配好的示例测试用例（推荐）
msopst run -i ./st_example/MatmulLeakyreluCustom_case.json -soc Ascend910B2 -out ./st/out

# 方式二：使用 msopst create 生成的文件（需先自行编辑 shape）
msopst run -i ./st/xxx.json -soc Ascend910B2 -out ./st/out
```

测试结果输出到 `./st/out` 目录。

---

## 各步骤速查

| 步骤 | 操作 | 命令 |
|------|------|------|
| 1 | 确认算子原型文件 | `cat MatmulLeakyReluCustom.json` |
| 2 | 创建算子工程 + 覆盖实现 | `msopgen gen` + `cp` |
| 3 | 编译算子工程 | `./build.sh` |
| 4 | 部署算子包 | `.run` 安装包 |
| 5 | 生成 ST 测试用例 | `msopst create` |
| 6 | 运行 ST 测试 | `msopst run` |

---

## 实现说明

本算子是一个复合算子，包含两个计算步骤：

1. **矩阵乘法（Matmul）**：使用 Ascend C 的 `matmul` 库接口完成矩阵乘法，通过 Tiling 策略实现多核并行
2. **LeakyReLU 激活**：对矩阵乘法的结果逐元素施加 LeakyReLU 激活（alpha=0.001）

关键实现文件：

| 文件 | 说明 |
|------|------|
| `op_host/matmul_leakyrelu_custom_tiling.h` | 定义 TilingData 结构体，包含 alpha 参数和 `TCubeTiling` 矩阵分块数据 |
| `op_host/matmul_leakyrelu_custom.cpp` | Host 侧：TilingFunc 计算策略 + OpDef 算子注册（支持 310P/910B） |
| `op_kernel/matmul_leakyrelu_custom.cpp` | Kernel 侧：`MatmulLeakyKernel` 类，实现 MatmulCompute → LeakyReluCompute → CopyOut 流水线 |

## 常见问题

### Q: 执行 `msopgen gen` 时报 "Invalid compute unit format"？

A: 检查 `-c` 参数格式，必须为 `ai_core-Ascendxxx`（如 `ai_core-Ascend910B2`）。

### Q: 编译时找不到 CANN 头文件？

A: 确保 `ASCEND_HOME_PATH` 已正确设置，指向 CANN 工具包安装目录。

### Q: 如何确认芯片型号？

A: 运行 `npu-smi info` 查看 NPU 芯片信息，或查看 CANN 版本适配列表。
