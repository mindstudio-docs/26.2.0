# Ascend Affinity CPU Binding Tool

The Ascend affinity CPU binding tool allows users to implement CPU core binding based on CPU affinity policies by simply running the tool without modifying any code, thereby improving inference or training performance.

The CPU binding tool is applicable to Arm server environments. It can be used to mitigate host_bound issues caused by CPU resource scheduling during training or inference tasks. For scenarios that are not host_bound, the tool has no significant improvement effect.

## Precautions

Before using the CPU binding tool, manually run `npu-smi info -t topo`. If output similar to the following appears, the environment supports CPU core binding. Otherwise, upgrade the environment's HDK package to Ascend HDK 23.0.RC2 or later.

            NPU0   NPU1    NPU2    NPU3    NPU4    NPU5    NPU6    NPU7    NPUx   CPU Affinity 
    NPU0    X      HCCS    HCCS    HCCS    HCCS    HCCS    HCCS    HCCS    ...    xx-xx
    NPU1    HCCS   X       HCCS    HCCS    HCCS    HCCS    HCCS    HCCS    ...    xx-xx
    NPU2    HCCS   HCCS    X       HCCS    HCCS    HCCS    HCCS    HCCS    ...    xx-xx
    NPU3    HCCS   HCCS    HCCS    X       HCCS    HCCS    HCCS    HCCS    ...    xx-xx
    NPU4    HCCS   HCCS    HCCS    HCCS    X       HCCS    HCCS    HCCS    ...    xx-xx
    NPU5    HCCS   HCCS    HCCS    HCCS    HCCS    X       HCCS    HCCS    ...    xx-xx
    NPU6    HCCS   HCCS    HCCS    HCCS    HCCS    HCCS    X       HCCS    ...    xx-xx
    NPU7    HCCS   HCCS    HCCS    HCCS    HCCS    HCCS    HCCS    X       ...    xx-xx
    NPUx    ...    ...     ...     ...     ...     ...     ...     ...     ...    ...

## How to Use

1. Execute the following command to perform CPU affinity binding:

   - Directly execute the CPU affinity binding command

    ```bash
    python3 bind_core.py -app="inference/train cmd"
    ```

   `-app` or `--application`: Configures the execution command for the training or inference program. Enclose the execution command in quotation marks.
   `-t` or `--time`: Sets the waiting time before CPU affinity binding, in seconds.

   This mode automatically launches the training or inference task, detects the task process, and performs CPU affinity binding.

   - Manually launch the training or inference task and then perform CPU affinity binding

   ```bash
   python3 bind_core.py
   ```

   This mode loops to search (loops 5 times, 10s each time; if the process is not found, it exits directly) for task processes using the NPU and performs CPU affinity binding.

2. Logs of the CPU affinity binding process are saved to bind_core_timestamp.log in the current path.

3. If the inference or training process requires some preprocessing time after being launched before actually executing the task, you can set the `-t/--time` parameter (in seconds, maximum value 10000) when executing the CPU affinity binding command. The CPU Affinity Tool will perform the binding action after the configured delay. For example: `python3 bind_core.py -app="cmd" -t=10`, after configuration, the tool will perform the CPU affinity binding operation after 10 seconds.
