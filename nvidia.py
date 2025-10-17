
# install the package :
    # conda install conda-forge::pynvml

# %% cmd

# cmd
    # CUDA version
        # nvcc --version   
# nvidia-smi

# %%

from pynvml import \
    nvmlInit, nvmlDeviceGetCount, nvmlDeviceGetHandleByIndex, \
    nvmlDeviceGetMemoryInfo, nvmlDeviceGetName, nvmlShutdown


# if not installed :
    # ---------------------------------------------------------------------------
    # ModuleNotFoundError                       Traceback (most recent call last)
    # Cell In[2], line 1
    # ----> 1 from pynvml import nvmlInit, nvmlDeviceGetHandleByIndex, nvmlDeviceGetName, nvmlShutdown
    
    # ModuleNotFoundError: No module named 'pynvml'

# %%

# Initialize NVML
nvmlInit()

# Get handle for the GPU (Assuming GPU 0)
handle = nvmlDeviceGetHandleByIndex(0)

# Get the GPU name
gpu_name = nvmlDeviceGetName(handle)

gpu_name
    # Out[7]: 'NVIDIA RTX 2000 Ada Generation Laptop GPU'

# print(f"Graphics Card: {gpu_name}")

# Shutdown NVML
nvmlShutdown()

# %%

# in parentheses : if you put th eindex as 1 : the result : seemiingly it means that there is only 1 GPU !!
handle_2 = nvmlDeviceGetHandleByIndex(1)

    # NVMLError_InvalidArgument                 Traceback (most recent call last)
    # Cell In[8], line 1
    # ----> 1 handle_2 = nvmlDeviceGetHandleByIndex(1)
    
    # File ~\AppData\Local\miniconda3\envs\env_1\Lib\site-packages\pynvml.py:2604, in nvmlDeviceGetHandleByIndex(index)
    #    2602 fn = _nvmlGetFunctionPointer("nvmlDeviceGetHandleByIndex_v2")
    #    2603 ret = fn(c_index, byref(device))
    # -> 2604 _nvmlCheckReturn(ret)
    #    2605 return device
    
    # File ~\AppData\Local\miniconda3\envs\env_1\Lib\site-packages\pynvml.py:1042, in _nvmlCheckReturn(ret)
    #    1040 def _nvmlCheckReturn(ret):
    #    1041     if (ret != NVML_SUCCESS):
    # -> 1042         raise NVMLError(ret)
    #    1043     return ret
    
    # NVMLError_InvalidArgument: Invalid Argument

# %%

nvmlDeviceGetCount()
    # Out[10]: 1

# %%  memory

memory_info = nvmlDeviceGetMemoryInfo(handle)

memory_info.total
    # Out[13]: 8585740288

memory_info.used
    # Out[14]: 225443840

memory_info.free
    # Out[15]: 8360296448

# %%

print(f"Total Memory: {memory_info.total / (1024 ** 2):.2f} MB")
    # Total Memory: 8188.00 MB

print(f"Used Memory: {memory_info.used / (1024 ** 2):.2f} MB")
    # Used Memory: 215.00 MB

print(f"Free Memory: {memory_info.free / (1024 ** 2):.2f} MB")
    # Free Memory: 7973.00 MB

# %%
