

# %%

# import cv2 as cv
img = cv2.imread(r"U:\\steps.jpg")

cv2.imshow("Display window", img)
k = cv2.waitKey(0) # Wait for a keystroke in the window

# %%

# Specify the path to your PNG image
image_path = r'U:\VISION\track\data\P067_ZC60_OF2ReTr_Video_1_04_06_2023_11_35_42_1\first_frame.png'

# Load the image using OpenCV
img = cv2.imread(image_path)

img.shape
    # Out[10]: (960, 1280, 3)

# %%

# Verify that the image has been loaded successfully
# if img is None:
#     print("Error: Unable to load the image. Check your file path.")
# else:
#     # Extract dimensions: for a color image, it returns (height, width, channels)
#     height, width = img.shape[:2]  # Reads the first two elements (height and width)
#     channels = img.shape[2] if len(img.shape) == 3 else 1  # For grayscale, channels implicitly equal 1

#     print(f"Image dimensions:\nWidth: {width}px\nHeight: {height}px\nChannels: {channels}")


# %%

import cv2, os
from pathlib import Path

# %%

# Configuration
SRC_DIR  = Path(r"U:\home_cage\notocord _ tse\2025-7-15")
OUT_DIR  = SRC_DIR / "compressed"
MIN_KB, MAX_KB = 200, 500
QUALITY_STEPS  = list(range(100,  0, -5))  # try 100,95,90,…,5

OUT_DIR.mkdir(parents=True, exist_ok=True)

def compress_with_range(src_path: Path, dst_path: Path):
    img = cv2.imread(str(src_path))
    if img is None:
        print(f"✗ Failed to read {src_path.name}")
        return

    chosen_buf = None
    chosen_q   = None

    for q in QUALITY_STEPS:
        success, buf = cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, q])
        if not success:
            continue

        size_kb = len(buf) / 1024
        # Accept the first quality that lands us in the band
        if MIN_KB <= size_kb <= MAX_KB:
            chosen_buf, chosen_q = buf, q
            break

    # If none lands in the band, fall back to the smallest file we saw
    if chosen_buf is None:
        # pick the last buffer tested
        chosen_buf, chosen_q = buf, q

    # Write out
    with open(dst_path, 'wb') as f:
        f.write(chosen_buf)

    print(f"✓ {dst_path.name}: {len(chosen_buf)//1024} KB @ Q={chosen_q}")

def batch_compress_folder(src_folder: Path, out_folder: Path):
    exts = {".jpg", ".jpeg", ".png", ".bmp"}
    for path in src_folder.iterdir():
        if path.suffix.lower() in exts and path.is_file():
            dst = out_folder / (path.stem + ".jpg")
            compress_with_range(path, dst)

if __name__ == "__main__":
    batch_compress_folder(SRC_DIR, OUT_DIR)

# %%

'''
        
        ✓ 20250715_132122.jpg: 425 KB @ Q=5
        ✓ 20250715_133213.jpg: 443 KB @ Q=10
        ✓ 20250715_133709.jpg: 484 KB @ Q=15
        ✓ 20250715_133922.jpg: 444 KB @ Q=10
        ✓ 20250715_134154.jpg: 493 KB @ Q=5
        ✓ 20250715_135039.jpg: 493 KB @ Q=10
        ✓ 20250715_153512.jpg: 490 KB @ Q=45
        ✓ 20250715_153541.jpg: 480 KB @ Q=65
        ✓ 20250715_153603.jpg: 471 KB @ Q=60
        ✓ 20250715_155549.jpg: 472 KB @ Q=65
        ✓ 20250715_155852.jpg: 481 KB @ Q=60
        ✓ 20250715_155930.jpg: 492 KB @ Q=60
        ✓ 20250715_173254.jpg: 484 KB @ Q=65
        ✓ 20250715_173911.jpg: 484 KB @ Q=70
        ✓ 20250715_174213.jpg: 478 KB @ Q=55
        ✓ 20250715_175853.jpg: 493 KB @ Q=5
        ✓ 20250715_180211.jpg: 483 KB @ Q=30
        ✓ 20250715_180216.jpg: 484 KB @ Q=35

'''

# %%

