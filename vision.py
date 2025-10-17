
# in the pytorch installation interactive table : I selected: cuda 12.6, despite the fact that my version was 12.8



# %%

import torch

torch.cuda.is_available()
    # Out[2]: True

# %%

import deeplabcut
    # Loading DLC 3.0.0rc7...
    # C:\Users\azare\AppData\Local\miniconda3\envs\env_4\lib\site-packages\deeplabcut\gui\__init__.py:15: 
        # PythonQtWarning: Selected binding 'pyside6' could not be found; falling back to 'pyqt5'
    #   import qtpy  # Necessary unused import to properly store the env variable
    # DLC loaded in light mode; you cannot use any GUI (labeling, relabeling and standalone GUI)

# %%
    
# env_12
import deeplabcut
    # Loading DLC 3.0.0rc7...
    # DLC loaded in light mode; you cannot use any GUI (labeling, relabeling and standalone GUI)
    # C:\Users\azare\AppData\Local\miniconda3\envs\env_12\lib\site-packages\deeplabcut\gui\__init__.py:15: 
        # PythonQtWarning: Selected binding 'pyside6' could not be found; falling back to 'pyqt5'
    #   import qtpy  # Necessary unused import to properly store the env variable

# %%