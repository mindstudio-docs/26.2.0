# Tinker

## Overview

The large model parallel strategy automatic optimization system, Tinker, performs approximately 15 minutes of single-node NPU performance measurement based on the provided training script, and recommends a high-performance parallel strategy training script.

1. Data measurement: Specify the `.sh` training script to be optimized. `Tinker` uses the `profiler` to obtain the cost performance data of each model subgraph under different parallel strategies on the current hardware for the specified model;
2. Strategy optimization: Specify the `.sh` training script to be optimized and the measurement data from step 1. `Tinker` uses the `optimizer` to recommend the parallel strategy with the optimal time cost.
3. Obtain the recommended result script: Strategy optimization generates the script in a subfolder under `./results/` by default.
4. You are advised to use the one-click run feature to automatically perform data measurement & strategy optimization.

## Pre-Use Checklist

1. Configure the training framework environment: Ensure that the current environment has installed/configured dependencies such as `CANN suite`, `training framework dependency libraries`, `Megatron`, and `MindSpeed acceleration library` (Tinker requires training framework capabilities to run);

   | Software and Version     | Corresponding Branch              |
   |--------------------------|-----------------------------------|
   | ModelLink 1.0.RC3 (1.2)  | git checkout 4ea42a23             |
   | ModelLink 1.0.RC2 (1.1)  | git checkout 2b0edd               |
   | ModelLink 1.0.RC1 (1.0)  | git checkout 224ae35              |
   | MindSpeed-LLM 1.0.0      | git checkout 969686ff             |
   | MindSpeed-LLM 2.0.0      | git checkout 2.0.0_core_r0.8.0    |
   | MindSpeed-LLM 2.3.0      | git checkout 2.3.0                |

    For installation steps of Python, driver, firmware, CANN, Torch, TorchNPU, and other dependencies, please refer to the [README](https://gitcode.com/Ascend/MindSpeed-LLM/blob/master/docs/en) of the training framework (MindSpeed LLM).

    Note: ModelLink was officially renamed to MindSpeed LLM starting from version 1.0.0. Tinker supports the above versions of ModelLink/MindSpeed LLM. You are advised to use the latest version for better performance and feature support.

2. Prepare the `training script to be optimized`: Configure the `.sh` training script to be optimized, especially the paths for the vocabulary file (`TOKENIZER_PATH` or `TOKENIZER_MODEL`) and data file (`DATA_PATH`) (Tinker needs to align with the model (training configuration) used during the user's actual training when performing strategy optimization);

3. Import the MindSpeed LLM framework path `export ML_PATH=/XX/XX/XX/MindSpeed-LLM`

4. Clone the mstt repository `git clone https://gitcode.com/Ascend/mstt.git`

## Specific Usage

Please use the Tinker optimization functionality through the tinker_auto_parallel entry script, and run commands and related parameters in the working directory. You are advised to use the One-Click Run mode.

### One-Click Run

[Entry]

`python /xxx/tinker/tinker_auto_parallel.py --mode all --config_path XXX.json ...`

[Command Example] Modify the input parameters before running

```shell
python /xxx/tinker/tinker_auto_parallel.py --mode all --config_path /xxx/tinker/parameter_config.json
python /xxx/tinker/tinker_auto_parallel.py --mode all --pretrain_script_path /xxx/xxx.sh  --output_dir /xxx/results ...
```

- `--mode`: Positional parameter. The one-click run (all) function is recommended. Additionally, three modes are supported: performance measurement (profile), strategy optimization (search), and simulation (simulate).
- The default full set of parameters is located at `/xxx/tinker/utils/constant.py`
- `--config_path`: (Optional) Positional parameter used to specify the configuration file path. The default configuration file is located at `/xxx/tinker/parameter_config.json`. Using this parameter will override the original path `/xxx/tinker/utils/constant.py`. Users can adjust parameters in config_path.
- `--is_full_tune`: Boolean value, marking whether it is a full-parameter fine-tuning task. The default is False. The program will detect and automatically assign the value through the keywords `tune` and `full` in the script path, requiring no user awareness.

The following three mode parameters can be modified in config_path or added directly to the command line

[Profile Mode Parameters]

- `--model_name`: Positional parameter, used to identify the model name
- `--model_size`: Positional parameter, used to identify the model size
- `--pretrain_script_path`: Specifies the `script to be optimized`.
- `--version`: Specifies the MindSpeed LLM framework version to use. Options include `1.2`, `1.1`, `1.0`, `1.0.0`, and `2.0.0`, corresponding to `1.0.RC3`, `1.0.RC2`, `1.0.RC1`, `1.0.0`, and `2.0.0` respectively (optional, default value: 1.1).
- `--max_npu`: Specifies the maximum number of NPUs (optional, default value: 8).

After execution, Tinker will generate a measurement data folder named like `profiled_data_xxx` under `./profiled_data`, containing several `.csv` files and execution logs.

[Search Mode Parameters]

- `--profiled_data_path`: Specifies the path where the performance data is located. You can also pass only the folder name, and Tinker will look for that folder under the `./profiled_data` path (this parameter is not required in One-Click Run mode).
- `--global_batch_size` `--num_nodes` `--num_npus_per_node`: Specifies the data batch size, number of nodes, and number of compute devices per node, respectively.
- `--memory_limit`: Specifies the memory limit (in MB, operator memory usage only; for 64GB memory, 57000 is recommended, and 60000 can be set for performance ceiling testing; for 32GB memory, 25000 is recommended, and 27000 can be set for performance ceiling testing).
- `--cpus`: Specifies the number of processes used for multi-process accelerated computation (optional, default value: 5).
- `--output_dir`: Specifies the output result path (optional, default: `./results`).

After the run is complete, Tinker will generate a folder in the results directory with a name like `qwen15-7b-gbs32-56000-1nodes8npus-2024-11-18-01-50-38`, where `.log` is the run log and the `config` folder stores the CLI parameter results.

[Simulate Mode Parameters]

- `--profiled_data_path`: Specifies the path where the performance data is located. You can also pass only the folder name, and Tinker will look for the file under the `./profiled_data` path.
- `--global_batch_size` `--num_nodes` `--num_npus_per_node`: Specifies the data batch size, number of nodes, and number of compute devices per node, respectively.
- `--simu_tp`: Specifies the tp value (optional, default value 1).
- `--simu_pp`: Specifies the pp value (optional, default value 1).
- `--simu_ep`: Specifies the ep value (optional, default value 1).
- `--simu_sp`: Specifies the sp value (optional, default value 0).
- `--zero`: Specifies the ZeRO mode (0 for off or 1 for on).
- `--micro_batch_size`: Specifies the micro batch size.
- `--num_layer_list`: Model layer list, for example, 4,4,4,4
- `--recompute`: Whether to enable recomputation (0 for off or 1 for on)
- `--detail`: Whether to display detailed cost information

[Note]

1. All parameters other than mode and config are related running parameters for enabling the tinker tool. Manually specifying them will override the default parameters in `parameter_config.json`.

2. When enabling the tinker tool, you can choose to specify related parameters in the command, or you can directly write the parameters into `parameter_config.json` and specify it as the configuration file corresponding to the config parameter.

3. The one-click run mode requires profile mode parameters and search mode parameters, while other modes only require their corresponding parameters.

4. When using a full-parameter fine-tuning training script, ensure that the script name contains the `tune` and `full` keywords (if not, enable the `--is_full_tune` parameter). Use the converted fine-tuning dataset, and the rest of the usage process remains unchanged.

[Configuration File Example]

```json
{
    "profile": {
      "model_name": null,
      "model_size": null,
      "pretrain_script_path": null,
      "version": "1.1",
      "max_npu": 8
    },
    "search": {
      "profiled_data_path": null,
      "global_batch_size": null,
      "num_nodes": null,
      "num_npus_per_node": 8,
      "cpus": 5,
      "memory_limit": 57000,
      "output_dir": "./results",
      "pretrain_script_path_search": null
    },
    "simulate": {
      "profiled_data_path": null,
      "num_layers": null,
      "global_batch_size": null,
      "num_nodes": null,
      "num_npus_per_node": 8,
      "simu_tp": 1,
      "simu_pp": 1,
      "simu_ep": 1,
      "simu_sp": 0,
      "zero": 0,
      "micro_batch_size": 1,
      "num_layer_list": null,
      "recompute": 0
    }
  }
```

## FAQs

1. Notes on the dependency of Tinker on the training script during performance measurement

    When measuring data, Tinker processes, stores, and partially runs the specified training script. Ensure that `TOKENIZER_PATH` and `DATA_PATH` are correctly filled in (refer to the MindSpeed LLM [README](https://gitcode.com/Ascend/MindSpeed-LLM/blob/master/docs/en) for guidance). When processing the script, Tinker removes torchrun logic, parallel strategy, and CLI parameters related to pretrained weight access, then stores other model and training-related parameters in `GPT_ARGS`. The specific parameters removed include:

   ```bash
   --tensor-model-parallel-size
   --pipeline-model-parallel-size
   --sequence-parallel
   --context-parallel-size
   --num-layers-per-virtual-pipeline-stage
   --recompute-xxx
   --use-distributed-optimizer
   --overlap-param-gather
   --num-layer-list
   --save
   --load
   --context-parallel-algo
   --ulysses-degree-in-cp
   --cp-attention-mask-type
   --use-cp-send-recv-overlap
   --kv-head-repeat-before-uly-alltoall
   ```

2. Explanation of the recommended value for setting the memory upper limit `--memory_limit` in strategy optimization: The current recommended value is based on empirical data. Tinker only predicts the memory overhead of Torch operators. Therefore, when setting `--memory_limit`, you must reserve memory overhead for components such as CANN and HCCL, and avoid performance degradation caused by repeated memory swapping under extreme memory usage.
3. After strategy optimization is complete, Tinker may recommend a new parallel strategy. In this case, weight parameters may require additional conversion. Ensure that the pretrained weight parameters (ckpt-related parameters) in the script match the new parallel strategy and that the file paths are correctly configured.
