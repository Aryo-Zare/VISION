
import cv2
import numpy as np
import matplotlib.pyplot as plt

# %%'

# --- CONFIGURATION ---
# Make sure this path is exactly correct on your computer.
image_path = r"F:\OneDrive - Uniklinik RWTH Aachen\DEXA\2025-10-7__Anne-Rix\20251007-111657_Animal_384_LT-072X_Measurement_Img.jpg"

# %% plot each RGB channel separately.

"""
Loads an image, separates its RGB channels, and plots them in a 2x2 grid.
"""
# 1. Load the image using OpenCV
img_bgr = cv2.imread(image_path)


# 2. Convert from BGR (OpenCV's default) to RGB for correct plotting
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# 3. Split the image into its individual channels
# Note: cv2.split for an RGB image returns Blue, Green, Red channels
# but since we converted to RGB, it will be R, G, B.
r_channel, g_channel, b_channel = cv2.split(img_rgb)

# %%'

# 4. Create blank images to display each channel in its own color
# To do this, we create a black canvas (all zeros) and place the
# single channel data into the correct 'slot' of the 3-channel image.

# Create the red channel visualization
red_channel_img = np.zeros_like(img_rgb)
red_channel_img[:, :, 0] = r_channel # Put red data in the red 'slot'

# Create the green channel visualization
green_channel_img = np.zeros_like(img_rgb)
green_channel_img[:, :, 1] = g_channel # Put green data in the green 'slot'

# Create the blue channel visualization
blue_channel_img = np.zeros_like(img_rgb)
blue_channel_img[:, :, 2] = b_channel # Put blue data in the blue 'slot'

# %%'


# 5. Set up the 2x2 plot using Matplotlib
fig, axes = plt.subplots(2, 2, figsize=(12, 12))

# --- Plot 1: Original Image ---
axes[0, 0].imshow(img_rgb)
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off') # Hide the x and y axis ticks

# --- Plot 2: Red Channel ---
axes[0, 1].imshow(red_channel_img)
axes[0, 1].set_title('Red Channel')
axes[0, 1].axis('off')

# --- Plot 3: Green Channel ---
axes[1, 0].imshow(green_channel_img)
axes[1, 0].set_title('Green Channel')
axes[1, 0].axis('off')

# --- Plot 4: Blue Channel ---
axes[1, 1].imshow(blue_channel_img)
axes[1, 1].set_title('Blue Channel')
axes[1, 1].axis('off')

# Adjust layout to prevent titles from overlapping
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# %%'

fig.suptitle('Image and its Individual RGB Color Channels \n'
             '20251007-111657_Animal_384'
             , fontsize=20)

# %%'

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\plot\RGB.pdf' )


# %%'
# %%'
# %%' subtraction of RGB pairs.

"""
calculates 6 channel subtraction images (A-B and B-A),
and plots them in a 2x3 grid.
"""

# 4. Calculate the subtraction images
# We use cv2.subtract and np.clip for handling negative values efficiently.
# Note: cv2.subtract automatically handles clipping to 0-255 for unsigned 8-bit images,
# but using np.clip explicitly is good practice if you were dealing with
# different data types or wanted to clip to a specific max value.
# For clarity, let's use the explicit operation that sets negatives to zero.

# R - G (Red minus Green)
rg_sub = r_channel.astype(np.int16) - g_channel.astype(np.int16) # Perform subtraction
rg_sub_clipped = np.clip(rg_sub, 0, 255).astype(np.uint8) # Clip and convert back to 8-bit

# R - B (Red minus Blue)
rb_sub = r_channel.astype(np.int16) - b_channel.astype(np.int16)
rb_sub_clipped = np.clip(rb_sub, 0, 255).astype(np.uint8)

# G - B (Green minus Blue)
gb_sub = g_channel.astype(np.int16) - b_channel.astype(np.int16)
gb_sub_clipped = np.clip(gb_sub, 0, 255).astype(np.uint8)

# G - R (Green minus Red)
gr_sub = g_channel.astype(np.int16) - r_channel.astype(np.int16)
gr_sub_clipped = np.clip(gr_sub, 0, 255).astype(np.uint8)

# B - R (Blue minus Red)
br_sub = b_channel.astype(np.int16) - r_channel.astype(np.int16)
br_sub_clipped = np.clip(br_sub, 0, 255).astype(np.uint8)

# B - G (Blue minus Green)
bg_sub = b_channel.astype(np.int16) - g_channel.astype(np.int16)
bg_sub_clipped = np.clip(bg_sub, 0, 255).astype(np.uint8)

# %%'

# 5. Set up the 2x3 plot using Matplotlib
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Channel Subtraction Images (Negative Values Clipped to 0)', fontsize=16)

# Flatten the axes array for easier iteration
axes = axes.flatten()

# Define titles and corresponding images
subtraction_data = [
    (rg_sub_clipped, 'R - G'),
    (rb_sub_clipped, 'R - B'),
    (gb_sub_clipped, 'G - B'),
    (gr_sub_clipped, 'G - R'),
    (br_sub_clipped, 'B - R'),
    (bg_sub_clipped, 'B - G'),
]

for i, (image, title) in enumerate(subtraction_data):
    axes[i].imshow(image, cmap='gray') # Subtraction results are typically viewed in grayscale
    axes[i].set_title(title)
    axes[i].axis('off') # Hide axes

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# %%'

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\plot\subtraction.pdf' )


# %%'
# %%'
# %%' subtraction of all images.

import os
import cv2
import numpy as np

# %%'

# --- CONFIGURATION ---
input_dir = r"F:\OneDrive - Uniklinik RWTH Aachen\DEXA\2025-10-7__Anne-Rix"
output_dir = r"F:\OneDrive - Uniklinik RWTH Aachen\DEXA\plot\subtraction"

"""
Processes all JPG images in an input directory, creates an R-G subtraction
image for each, and saves them to an output directory.
"""
# 1. Create the output directory if it doesn't exist.
# The 'exist_ok=True' prevents an error if the folder is already there.
# os.makedirs(output_dir, exist_ok=True)
# print(f"Output will be saved to: {output_dir}\n")

# 2. Get a list of all files in the input directory.
filenames = os.listdir(input_dir)

# 3. Loop through each file in the directory.
processed_count = 0
for filename in filenames:
    # Process only files with a .jpg extension (case-insensitive)
    if filename.lower().endswith(".jpg"):
        
        # Construct the full path to the input image
        input_path = os.path.join(input_dir, filename)

        # Load the image using OpenCV
        img_bgr = cv2.imread(input_path)

        if img_bgr is None:
            print(f"--> Skipping: Could not read image file: {filename}")
            continue

        # --- Perform the R-G Subtraction ---
        # Convert from BGR to RGB
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        
        # Split into channels
        r_channel, g_channel, _ = cv2.split(img_rgb)
        
        # Perform subtraction using 16-bit integers to avoid overflow issues
        rg_sub = r_channel.astype(np.int16) - g_channel.astype(np.int16)
        
        # Clip negative values to 0 and convert back to an 8-bit image
        rg_sub_clipped = np.clip(rg_sub, 0, 255).astype(np.uint8)
        # --- End of Subtraction Logic ---

        # 4. Construct the new filename and output path
        base_name, extension = os.path.splitext(filename)
        new_filename = f"{base_name}_RG_subtraction{extension}"
        output_path = os.path.join(output_dir, new_filename)

        # 5. Save the resulting image
        cv2.imwrite(output_path, rg_sub_clipped)
        print(f"Processed: {filename}  -->  Saved as: {new_filename}")
        processed_count += 1

print(f"\n--- DONE ---")
print(f"Successfully processed and saved {processed_count} images.")



# %%'

# ...
# Processed: 20251007-112503_Animal_363_LT-KW1x_Measurement_Img.jpg  -->  Saved as: 20251007-112503_Animal_363_LT-KW1x_Measurement_Img_RG_subtraction.jpg
# Processed: 20251007-112515_Animal_363_LT-KW1x_Measurement_Img.jpg  -->  Saved as: 20251007-112515_Animal_363_LT-KW1x_Measurement_Img_RG_subtraction.jpg

# --- DONE ---
# Successfully processed and saved 44 images.

# %%






