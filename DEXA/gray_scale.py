
# %%

import cv2
import matplotlib.pyplot as plt
from skimage import io

# %%

# We'll try to use scikit-image as a fallback
try:
    from skimage import io
    SKIMAGE_AVAILABLE = True
except ImportError:
    SKIMAGE_AVAILABLE = False
    print("Warning: scikit-image is not installed. The script will rely solely on OpenCV.")

# --- CONFIGURATION ---
IMAGE_PATHS = [
    r"U:\data\VTK Frog__2025-9-23__Renee\20250923-101916_Animal_384_LT-072X_Measurement_Img(Ori).tif",
    r"U:\data\VTK Frog__2025-9-23__Renee\20250923-102024_Animal_384_LT-072X_Measurement_Img(Ori).tif"
]

def load_image_robustly(path):
    """
    Tries to load an image, first with OpenCV, then with scikit-image as a fallback.
    """
    image = None
    try:
        # First attempt: OpenCV. IMREAD_UNCHANGED is best for scientific data.
        image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        if image is None:
            # cv2.imread fails silently by returning None, so we raise an error.
            raise IOError("OpenCV could not read the file (returned None).")
        print(f"Successfully loaded with OpenCV: {path.split('\\')[-1]}")
        return image
    except Exception as e_cv2:
        print(f"OpenCV failed: {e_cv2}.")
        if SKIMAGE_AVAILABLE:
            print("--> Now trying with scikit-image...")
            try:
                # Second attempt: scikit-image (which now uses imagecodecs)
                image = io.imread(path)
                print(f"Successfully loaded with scikit-image: {path.split('\\')[-1]}")
                return image
            except Exception as e_sk:
                print(f"Scikit-image also failed: {e_sk}")
                return None
        else:
            return None


def demonstrate_thresholding_for_fat(image_path):
    """
    Loads a grayscale X-ray and demonstrates the unreliability of thresholding.
    """
    image = load_image_robustly(image_path)
    
    if image is None:
        print(f"\nERROR: Failed to load image from path: {image_path}\n")
        return

      # --- These are ARBITRARY thresholds for demonstration ---
    # Fat is less dense, so it appears darker (lower pixel values) in an X-ray.
    # We will test a few "assumed" thresholds for what might be considered "fat".
    assumed_fat_threshold_low = 50
    assumed_fat_threshold_medium = 100
    assumed_fat_threshold_high = 150

    # Apply the thresholds. We are creating a "mask" where pixels below the
    # threshold are white (255) and all others are black (0).
    # This is the "segmented fat" image.
    _, fat_mask_low = cv2.threshold(image, assumed_fat_threshold_low, 255, cv2.THRESH_BINARY_INV)
    _, fat_mask_medium = cv2.threshold(image, assumed_fat_threshold_medium, 255, cv2.THRESH_BINARY_INV)
    _, fat_mask_high = cv2.threshold(image, assumed_fat_threshold_high, 255, cv2.THRESH_BINARY_INV)

    fig, axes = plt.subplots(2, 2, figsize=(14, 14))
    fig.suptitle(f"Demonstrating Thresholding on:\n{image_path.split('\\')[-1]}", fontsize=16)

    axes[0, 0].imshow(image, cmap='gray')
    axes[0, 0].set_title('Original Grayscale X-Ray')
    axes[0, 0].axis('off')

    axes[0, 1].hist(image.ravel(), bins=256, range=[np.min(image), np.max(image)])
    axes[0, 1].set_title('Pixel Intensity Histogram')
    axes[0, 1].set_xlabel('Pixel Intensity')
    axes[0, 1].set_ylabel('Pixel Count')

    axes[1, 0].imshow(fat_mask_low, cmap='gray')
    axes[1, 0].set_title(f'Assumed "Fat" (Pixels < {assumed_fat_threshold_low})')
    axes[1, 0].axis('off')

    axes[1, 1].imshow(fat_mask_high, cmap='gray')
    axes[1, 1].set_title(f'Assumed "Fat" (Pixels < {assumed_fat_threshold_high})')
    axes[1, 1].axis('off')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# --- Main execution loop ---
if __name__ == "__main__":
    for path in IMAGE_PATHS:
        demonstrate_thresholding_for_fat(path)

# %%

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\plot\grayscale\lateral_2.pdf' )

# %%
# %%

# --- CONFIGURATION ---
# We will do this for one image as a demonstration
IMAGE_PATH = r"U:\data\VTK Frog__2025-9-23__Renee\20250923-101916_Animal_384_LT-072X_Measurement_Img(Ori).tif"

IMAGE_PATH = r"U:\data\VTK Frog__2025-9-23__Renee\20250923-102024_Animal_384_LT-072X_Measurement_Img(Ori).tif"


# %%

# --- CALIBRATION STANDARDS (from CT Hounsfield Units) ---
# We use average values for this model
HU_FAT = -120  # Average HU for fat
HU_MUSCLE = 45   # Average HU for muscle
HU_BONE = 1000 # HU for cortical bone

def select_points_and_get_average(image, tissue_name):
    """
    Displays an image and prompts the user to select points.
    Returns the average pixel intensity of the selected points.
    """
    plt.imshow(image, cmap='gray')
    plt.title(f'Select 3-5 points for {tissue_name}, then press ENTER', fontsize=12)
    plt.draw()

    # Get user input. ginput will wait for clicks.
    # The user can left-click to add points. Pressing Enter finalizes the selection.
    points = plt.ginput(n=-1, timeout=0, show_clicks=True)
    plt.close()

    if not points:
        print("No points selected. Aborting.")
        return None

    # Extract pixel values at the selected coordinates
    pixel_values = [image[int(y), int(x)] for x, y in points]
    
    average_intensity = np.mean(pixel_values)
    print(f"Selected {tissue_name} points. Average pixel intensity: {average_intensity:.2f}")
    return average_intensity


def perform_pseudo_calibration(image_path):
    """
    Main function to run the interactive calibration and segmentation.
    """
    try:
        # Using cv2.IMREAD_UNCHANGED is best for scientific TIFFs
        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        if image is None:
            raise IOError("OpenCV could not read the file.")
    except Exception as e:
        print(f"ERROR loading image: {e}")
        return

    # --- Step 1 & 2: Interactive Point Selection ---
    print("--- INTERACTIVE CALIBRATION ---")
    pixel_bone = select_points_and_get_average(image, "BONE")
    if pixel_bone is None: return
    
    pixel_muscle = select_points_and_get_average(image, "MUSCLE")
    if pixel_muscle is None: return

    # --- Step 3: Linear Calibration (y = mx + c) ---
    # We have two points: (pixel_muscle, HU_MUSCLE) and (pixel_bone, HU_BONE)
    # y = HU value, x = pixel intensity
    
    # Calculate slope (m)
    m = (HU_BONE - HU_MUSCLE) / (pixel_bone - pixel_muscle)
    
    # Calculate y-intercept (c)
    c = HU_BONE - m * pixel_bone
    
    print("\n--- CALIBRATION RESULTS ---")
    print(f"Linear model created: HU = {m:.2f} * Pixel_Value + {c:.2f}")

    # --- Step 4: Predict Pixel Value for Fat ---
    # We want to find x when y = HU_FAT.  x = (y - c) / m
    predicted_pixel_fat = (HU_FAT - c) / m
    
    # Let's create a plausible range around this prediction.
    # This is an arbitrary range for visualization.
    fat_range_width = 20 # pixels
    fat_min = predicted_pixel_fat - (fat_range_width / 2)
    fat_max = predicted_pixel_fat + (fat_range_width / 2)
    
    print(f"Predicted pixel intensity for fat (HU={HU_FAT}): {predicted_pixel_fat:.2f}")
    print(f"Using segmentation range: {fat_min:.2f} to {fat_max:.2f}")

    # --- Step 5: Segment the Image ---
    # Use cv2.inRange to create a mask of pixels within our calculated fat range
    fat_mask = cv2.inRange(image, int(fat_min), int(fat_max))

    # --- Step 6: Display Final Results ---
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    fig.suptitle('Calibration based on bone & muscle pixel-intensity values \n and the resulting "Fat" Segmentation', fontsize=20)
    
    axes[0].imshow(image, cmap='gray')
    axes[0].set_title('Original X-Ray')
    axes[0].axis('off')
    
    axes[1].imshow(fat_mask, cmap='gray')
    axes[1].set_title(f'Segmented "Fat" ') # (Pixels in range {int(fat_min)}-{int(fat_max)})
    axes[1].axis('off')
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


# --- Main execution ---
if __name__ == "__main__":
    perform_pseudo_calibration(IMAGE_PATH)


# %%

plt.suptitle('Calibration and Resulting "Fat" Segmentation', fontsize=16)

# %%

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\plot\grayscale\pseudo_calibration_supine.pdf' )


# %%

