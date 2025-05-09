
# env_20


# %%

import os
import numpy as np
import torch
import matplotlib.pyplot as plt
from PIL import Image

# %%

torch.cuda.is_available()
    # Out[2]: True

# %%

# you should change your working directoy, otherwise you would get an error while running 
os.chdir("C:\\test")

pwd
    # Out[4]: 'C:\\test'

# %%

# despite the fact that by : conda list PIL : the package shows installed, it may not be properly configured !
    # hence the following error
    # to resolve this, reinstall PIL

# from PIL import Image
    # [autoreload of platform failed: Traceback (most recent call last):
    #   File "C:\Users\azare\AppData\Local\miniconda3\envs\env_19\Lib\site-packages\IPython\extensions\autoreload.py", line 276, in check
    #     superreload(m, reload, self.old_objects)
    #     ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #   File "C:\Users\azare\AppData\Local\miniconda3\envs\env_19\Lib\site-packages\IPython\extensions\autoreload.py", line 500, in superreload
    #     update_generic(old_obj, new_obj)
    #     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
    #   File "C:\Users\azare\AppData\Local\miniconda3\envs\env_19\Lib\site-packages\IPython\extensions\autoreload.py", line 397, in update_generic
    #     update(a, b)
    #     ~~~~~~^^^^^^
    #   File "C:\Users\azare\AppData\Local\miniconda3\envs\env_19\Lib\site-packages\IPython\extensions\autoreload.py", line 365, in update_class
    #     update_instances(old, new)
    #     ~~~~~~~~~~~~~~~~^^^^^^^^^^
    #   File "C:\Users\azare\AppData\Local\miniconda3\envs\env_19\Lib\site-packages\IPython\extensions\autoreload.py", line 323, in update_instances
    #     object.__setattr__(ref, "__class__", new)
    #     ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
    # TypeError: __class__ assignment: 'uname_result' object layout differs from 'uname_result'
    # ]

# %%

# select the device for computation
if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")
print(f"using device: {device}")

if device.type == "cuda":
    # use bfloat16 for the entire notebook
    torch.autocast("cuda", dtype=torch.bfloat16).__enter__()
    # turn on tfloat32 for Ampere GPUs (https://pytorch.org/docs/stable/notes/cuda.html#tensorfloat-32-tf32-on-ampere-devices)
    if torch.cuda.get_device_properties(0).major >= 8:
        torch.backends.cuda.matmul.allow_tf32 = True
        torch.backends.cudnn.allow_tf32 = True
elif device.type == "mps":
    print(
        "\nSupport for MPS devices is preliminary. SAM 2 is trained with CUDA and might "
        "give numerically different outputs and sometimes degraded performance on MPS. "
        "See e.g. https://github.com/pytorch/pytorch/issues/84936 for a discussion."
    )



# using device: cuda

# %%

def show_mask(mask, ax, obj_id=None, random_color=False):
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        cmap = plt.get_cmap("tab10")
        cmap_idx = 0 if obj_id is None else obj_id
        color = np.array([*cmap(cmap_idx)[:3], 0.6])
    h, w = mask.shape[-2:]
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    ax.imshow(mask_image)


def show_points(coords, labels, ax, marker_size=200):
    pos_points = coords[labels==1]
    neg_points = coords[labels==0]
    ax.scatter(pos_points[:, 0], pos_points[:, 1], color='green', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)
    ax.scatter(neg_points[:, 0], neg_points[:, 1], color='red', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)


def show_box(box, ax):
    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='green', facecolor=(0, 0, 0, 0), lw=2))

# %%

from sam2.build_sam import build_sam2_video_predictor

# this error happns if you do not change your working directory ( see above ).
        # ---------------------------------------------------------------------------
        # RuntimeError                              Traceback (most recent call last)
        # Cell In[7], line 1
        # ----> 1 from sam2.build_sam import build_sam2_video_predictor
        
        # File ~\sam2\sam2\build_sam.py:25
        #      17 # Check if the user is running Python from the parent directory of the sam2 repo
        #      18 # (i.e. the directory where this repo is cloned into) -- this is not supported since
        #      19 # it could shadow the sam2 package and cause issues.
        #      20 if os.path.isdir(os.path.join(sam2.__path__[0], "sam2")):
        #      21     # If the user has "sam2/sam2" in their path, they are likey importing the repo itself
        #      22     # as "sam2" rather than importing the "sam2" python package (i.e. "sam2/sam2" directory).
        #      23     # This typically happens because the user is running Python from the parent directory
        #      24     # that contains the sam2 repo they cloned.
        # ---> 25     raise RuntimeError(
        #      26         "You're likely running Python from the parent directory of the sam2 repository "
        #      27         "(i.e. the directory where https://github.com/facebookresearch/sam2 is cloned into). "
        #      28         "This is not supported since the `sam2` Python package could be shadowed by the "
        #      29         "repository name (the repository is also named `sam2` and contains the Python package "
        #      30         "in `sam2/sam2`). Please run Python from another directory (e.g. from the repo dir "
        #      31         "rather than its parent dir, or from your home directory) after installing SAM 2."
        #      32     )
        #      35 HF_MODEL_ID_TO_FILENAMES = {
        #      36     "facebook/sam2-hiera-tiny": (
        #      37         "configs/sam2/sam2_hiera_t.yaml",
        #    (...)
        #      67     ),
        #      68 }
        #      71 def build_sam2(
        #      72     config_file,
        #      73     ckpt_path=None,
        #    (...)
        #      78     **kwargs,
        #      79 ):
        
        # RuntimeError: ' You''re likely running Python from the parent directory of the sam2 repository (i.e. the directory where https://github.com/facebookresearch/sam2 is cloned into). '
        # 'This is not supported since the `sam2` Python package could be shadowed by the repository name (the repository is also named `sam2` and contains the Python package in `sam2/sam2`). '
        # 'Please run Python from another directory (e.g. from the repo dir rather than its parent dir, or from your home directory) after installing SAM 2.'


# problematic working directory :
# pwd
    # Out[8]: 'C:\\Users\\azare'

# %%


sam2_checkpoint = r'C:\Users\azare\sam2\checkpoints\sam2.1_hiera_large.pt'
model_cfg = r'C:\Users\azare\sam2\sam2\configs\sam2.1\sam2.1_hiera_l.yaml'

predictor = build_sam2_video_predictor(model_cfg, sam2_checkpoint, device=device)


# %%

# `video_dir` a directory of JPEG frames with filenames like `<frame_index>.jpg`
video_dir = r'U:\VISION\track\sam-2\bedroom'

# scan all the JPEG frame names in this directory
frame_names = [
    p for p in os.listdir(video_dir)
    if os.path.splitext(p)[-1] in [".jpg", ".jpeg", ".JPG", ".JPEG"]
]

frame_names.sort(key=lambda p: int(os.path.splitext(p)[0]))

# %%

# explore

len(frame_names)
    # Out[19]: 200

frame_names[:4]
    # Out[20]: ['00000.jpg', '00001.jpg', '00002.jpg', '00003.jpg']

# %%

# take a look the first video frame
frame_idx = 0
plt.figure(figsize=(9, 6))
plt.title(f"frame {frame_idx}")

plt.imshow(Image.open(os.path.join(video_dir, frame_names[frame_idx])))

# %%

plt.savefig( r'U:\VISION\track\sam-2\bedroom\1\jump.jpg' )

# %%
# %%
# %%


inference_state = predictor.init_state(video_path=video_dir)
    # frame loading (JPEG): 100%|██████████| 200/200 [00:23<00:00,  8.68it/s]

# %%
# %%
# %%


ann_frame_idx = 0  # the frame index we interact with
ann_obj_id = 4  # give a unique id to each object we interact with (it can be any integers)

# Let's add a box at (x_min, y_min, x_max, y_max) = (300, 0, 500, 400) to get started
box = np.array([ 291 , 2 , 526 , 395 ], dtype=np.float32)
_ , out_obj_ids, out_mask_logits = predictor.add_new_points_or_box(
        inference_state=inference_state,
        frame_idx=ann_frame_idx,
        obj_id=ann_obj_id,
        box=box,
)

    # C:\Users\azare\sam2\sam2\sam2_video_predictor.py:786: UserWarning: cannot import name '_C' from 'sam2' (C:\Users\azare\sam2\sam2\__init__.py)
    
    # Skipping the post-processing step due to the error above. 
    # You can still use SAM 2 and it's OK to ignore the error above, 
    # although some post-processing functionality may be limited 
    # (which doesn't affect the results in most cases; see https://github.com/facebookresearch/sam2/blob/main/INSTALL.md).
    #   pred_masks_gpu = fill_holes_in_mask_scores(

# %%

type(out_obj_ids)
    # Out[36]: list

len(out_obj_ids)
    # 1

out_obj_ids
    # Out[38]: [4]

# %%

type(out_mask_logits)
    # Out[40]: torch.Tensor

# shape equals the dimension of the image.
out_mask_logits.shape
    # Out[41]: torch.Size([1, 1, 540, 960])

out_mask_logits
    # Out[39]: 
    # tensor([[[[-16.0000, -16.0000, -16.1458,  ..., -16.5313, -16.7500, -16.7500],
    #           [-16.1847, -16.1847, -16.2338,  ..., -16.2498, -16.2618, -16.2618],
    #           [-16.5995, -16.5995, -16.4313,  ..., -15.6176, -15.1655, -15.1655],
    #           ...,
    #           [-15.8114, -15.8114, -15.4703,  ..., -15.6742, -15.0891, -15.0891],
    #           [-14.7743, -14.7743, -14.7197,  ..., -15.4816, -14.9410, -14.9410],
    #           [-14.3125, -14.3125, -14.3854,  ..., -15.3958, -14.8750, -14.8750]]]],
    #        device='cuda:0')

# %%


# show the results on the current (interacted) frame
plt.figure(figsize=(9, 6))
plt.title(f"frame {ann_frame_idx}")
plt.imshow(Image.open(os.path.join(video_dir, frame_names[ann_frame_idx])))
show_box(box, plt.gca())
show_mask((out_mask_logits[0] > 0.0).cpu().numpy(), plt.gca(), obj_id=out_obj_ids[0])

# %%

plt.savefig( r'U:\VISION\track\sam-2\bedroom\1\jump_mask.jpg' )

# %%

# run propagation throughout the video and collect the results in a dict

# video_segments contains the per-frame segmentation results
video_segments = {}  

for out_frame_idx, out_obj_ids, out_mask_logits in predictor.propagate_in_video(inference_state):
    video_segments[out_frame_idx] = {
                                        out_obj_id: (out_mask_logits[i] > 0.0).cpu().numpy()
                                        for i , out_obj_id in enumerate(out_obj_ids)
                                    }


    # warning
    '''

        propagate in video:   0%|          | 0/200 [00:00<?, ?it/s]C:\Users\azare\sam2\sam2\sam2_video_predictor.py:786: 
            UserWarning: cannot import name '_C' from 'sam2' (C:\Users\azare\sam2\sam2\__init__.py)
        
        Skipping the post-processing step due to the error above. 
        You can still use SAM 2 and it's OK to ignore the error above, 
        although some post-processing functionality may be limited (which doesn't affect the results in most cases; 
                                                                    see https://github.com/facebookresearch/sam2/blob/main/INSTALL.md).
          pred_masks_gpu = fill_holes_in_mask_scores(
        propagate in video: 100%|██████████| 200/200 [00:43<00:00,  4.58it/s]
    
    '''

# %%

out_frame_idx
    # Out[44]: 199

out_obj_ids
    # Out[45]: [4]

out_mask_logits.shape
    # Out[46]: torch.Size([1, 1, 540, 960])

# %%


# render the segmentation results every few frames
# 1 : no skip !
vis_frame_stride = 1
# plt.close("all")

# Define the path template
save_path_template = r'U:\VISION\track\sam-2\bedroom\3\{}.jpg'

for out_frame_idx in range( 0, len(frame_names), vis_frame_stride ):
    plt.figure(figsize=(6, 4))
    plt.title(f"frame {out_frame_idx}")
    plt.imshow(Image.open(os.path.join(video_dir, frame_names[out_frame_idx])))
    
    # this loop is probably only needed when there are more than one mask (box) : multi-object segmentation.
    for out_obj_id, out_mask in video_segments[out_frame_idx].items():
        show_mask(out_mask, plt.gca(), obj_id=out_obj_id)
    
    save_path = save_path_template.format(out_frame_idx)
    plt.savefig(save_path)
    plt.close()


# %%




# %%

