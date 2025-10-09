

# the first frames of all videos are already extacted by :  system.py / extract the 1st frame _ all videos
# here, they are more conveniently organized ( renamed & placed in other folders )

# %%' extract & copy "first_frame.png" 
# extract & copy "first_frame.png" to a destination directory while \
        # preserving ( recreating ) that file's parent folder structure within the destination folder.
# F:\OneDrive - Uniklinik RWTH Aachen\IT\system__python \ AI__system__python .docx

import shutil
from pathlib import Path

# %%'

# --- Configuration ---
# Please set your source and destination folders here.
# Using raw strings (r"...") is a good practice for Windows paths.
source_folder = Path(r"U:\data\track_data")
# 1st create this folder in Windows-Explorer.
destination_folder = Path(r"F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\first_frame")
file_to_copy = "first_frame.png"  # this is the file names & actually a kind of pattern to be searched ( .rglob ) later below.

# --- Script Logic ---
print(f"🚀 Starting the copy process...")
print(f"Source: {source_folder}")
print(f"Destination: {destination_folder}")
print("-" * 30)

# Check if the source folder exists
if not source_folder.is_dir():
    print(f"❌ Error: Source folder not found at '{source_folder}'")
else:
    # Use rglob() to recursively find all files with the specified name
    # The '**' part means it will search in the current directory and all subdirectories.
    # the list contains the full path of each file, including the file's name itself ( first_frame.png ).
    files_found = list(source_folder.rglob(f"**/{file_to_copy}"))
    
    if not files_found:
        print(f"🤷 No files named '{file_to_copy}' were found in the source directory.")
    else:
        print(f"✅ Found {len(files_found)} file(s) to copy.")
        
        for source_file_path in files_found:
            # Determine the file's path relative to the source folder's root
            # Example: U:\data\track_data\folder_1\file.png -> folder_1\file.png
            relative_path = source_file_path.relative_to(source_folder)
            
            # Create the full destination path
            # Example: F:\...\extract + folder_1\file.png
            destination_file_path = destination_folder / relative_path
            
            # Create the necessary parent directories in the destination
            # The .parent attribute gets the directory containing the file
            # exist_ok=True prevents an error if the directory already exists
            destination_file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy the file, preserving metadata (like timestamps)
            shutil.copy2(source_file_path, destination_file_path)
            
            print(f"  -> Copied: {destination_file_path}")
            
        print("-" * 30)
        print("🎉 All files copied successfully!")


# %%

# 🚀 Starting the copy process...
# Source: U:\data\track_data
# Destination: F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\first_frame
# ------------------------------
# ✅ Found 111 file(s) to copy.
#   -> Copied: F:\OneDrive - Unik
#   ...
# ------------------------------
# 🎉 All files copied successfully!
  

# %%' copy the .png files
# copy the .png files to a new folder :
    # get rid of each file being in a separate folder.
    # change the name of the file to represent time-group ( retrain_2 , ... ) & animal label ( ZCnn ).
# # F:\OneDrive - Uniklinik RWTH Aachen\IT\system__python \ AI__system__python .docx

# %%'

import shutil
import re
from pathlib import Path

# %%'


# --- Configuration ---
# Source directory (populated by the first script)
source_folder = Path(r"F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\first_frame")

# Corrected final destination for the renamed and summarized files
# 1st create this folder in Windows-Explorer.
destination_folder_2 = Path(r"F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\first_frame_2")

file_to_find = "first_frame.png"

# --- Script Logic ---
print("🚀 Starting the rename and copy process...")
print(f"Source: {source_folder}")
print(f"Final Destination: {destination_folder_2}")
print("-" * 30)

# Check if the source folder exists
if not source_folder.is_dir():
    print(f"❌ Error: Source folder not found at '{source_folder}'")
else:
    # Recursively find all 'first_frame.png' files
    files_to_process = list(source_folder.rglob(f"**/{file_to_find}"))
    
    if not files_to_process:
        print(f"🤷 No files named '{file_to_find}' were found in the source directory.")
    else:
        print(f"✅ Found {len(files_to_process)} file(s) to process.")
        
        # Ensure the base destination directory exists
        destination_folder_2.mkdir(exist_ok=True)
        
        for source_file_path in files_to_process:
            try:
                # Get the names of the parent folders
                folder_2_name = source_file_path.parent.name
                folder_1_name = source_file_path.parent.parent.name
                
                # Use a regular expression to find the 'ZC##' pattern
                match = re.search(r'ZC\d{2}', folder_2_name)
                
                if match:
                    # The pattern was found, e.g., 'ZC04'
                    zc_code = match.group(0)
                    
                    # Construct the new filename, e.g., "pod_4_ZC04.png"
                    new_filename = f"{folder_1_name}_{zc_code}.png"
                    
                    # Construct the new destination folder path, e.g., ".../center_point/pod_4"
                    new_destination_folder = destination_folder_2 / folder_1_name
                    
                    # Create this folder if it doesn't exist
                    new_destination_folder.mkdir(parents=True, exist_ok=True)
                    
                    # Construct the full final path for the new file
                    final_file_path = new_destination_folder / new_filename
                    
                    # Copy the original file to the new location with the new name
                    # note : final_file_path : contains the file name & extension !
                        # this may not always be the case when copying files !
                    shutil.copy2(source_file_path, final_file_path)
                    
                    print(f"  -> Created: {final_file_path}")
                    
                else:
                    print(f"  -> ⚠️  Warning: Could not find 'ZC##' pattern in '{folder_2_name}'. Skipping file.")

            except IndexError:
                print(f"  -> ⚠️  Warning: File is not in a 'folder_1/folder_2' structure. Skipping {source_file_path}")

        print("-" * 30)
        print("🎉 All files processed successfully!")

# %%

# 🚀 Starting the rename and copy process...
# Source: F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\first_frame
# Final Destination: F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\first_frame_2
# ------------------------------
# ✅ Found 111 file(s) to process.
#   -> Created: F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\first_frame_2\retrain_2\retrain_2_ZC60.png
# ...
# ------------------------------
# 🎉 All files processed successfully!

# %%

# F:\temp\zc-15_inconcordance  :  the same animal does not have the same dimensions.

# %%

# next : =>  system .py

