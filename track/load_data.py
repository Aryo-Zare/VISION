
# %%

# for the rest of the analysis : you need :
    # cp_av_ds : to extract the read-out parameters.
        # raw : this has 2 million rows, containing the x&y coordinates of every frame of all videos.
        # all parameters here are in pixels ( not meters ).
    # df_aggregate : to be merged with the above dataframe for the categories.
        # aggregate : tdt : total distance traveled.
        # aside from 'tdt_...' column, the rest of the columns give you good groupings :
            # time', 'sample_ID', 'sample_png_height', 'treatment'
            # these can be merged with other read-out parameters : velocity ... : extracted from : cp_av_ds
    # both the above dataframes are in :   C:\code\VISION\track\all_track.py


# %%

# continued from : C:\code\VISION\track\all_track.py

# raw : 2 million rows
# last saved in : position.py  =>  all_track.py

cp_av_ds_3.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\cp_av_ds_3.pkl' )


cp_av_ds_3 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\cp_av_ds_3.pkl' )

# aggregate _ total distance walked.
# tdt_height_group_2 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\tdt_height_group_2.pkl' )

# %%

# aggregate 
# last saved in : position.py
df_aggregate_track_2 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_aggregate_track_2.pkl' )

# %%
# %%

# ROI
# continued from  C:\code\VISION\track\system.py

df_roi_data = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_roi_data.pkl' )

# %%

# same data as above ( df_roi_data ) , in json ( dictionary ) format !
# Open the JSON file containing the ROI coordinates.
# 'r' means we are opening it in "read" mode.
# why using a dictionary ?  =>  C:\code\VISION\track\position.py
path_json = r"F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\roi_definitions.json"
with open( path_json , 'r') as f:
    # The json.load() function reads the text from the file and parses it into a Python dictionary.
    roi_data = json.load(f)

# %% bbox

# this is the same as the ROI but in a differnet fromat :
        # instead of the exact coordinates of the corners : 
            # only coordinate of the bottom-left corenr + width & hwight of the rectangle.
# Save the Bounding Boxes to a New JSON File ---
output_bbox_file = r"F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\roi_bounding_boxes.json"
with open(output_bbox_file, 'r') as f:
    roi_bboxes = json.load(f)

# %%
# %%

# roam.py
# for all videos.
# the number of unique cells ( out of 100 total ) that the animal explored ( stepped in ).
exploration_score = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\exploration_score.pkl' )


# roam.py
# for all videos.
# the amount of time the animal spent on each cell it stepped in.
    # _count_ : the number of frames for each cell.
# 7777
df_cell_count_percentage = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_cell_count_percentage.pkl' )

# %%


