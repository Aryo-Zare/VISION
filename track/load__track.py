
# %%

# =>  F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data   \  data_track  .docx


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


# raw : 2 million rows
    # no : it is here downsampled : 200000 rows.
    # cp_av_ds_4.shape
    #     # Out[110]: (196162, 21)
# cp_av_ds_5 : bad-processed videos are removed.
# last saved in 
    # C:\code\VISION\track\remove_bad_processed.py
    # : position.py  =>  all_track.py
        # continued from : C:\code\VISION\track\all_track.py
cp_av_ds_5 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\cp_av_ds_5.pkl' )
# cp_av_ds_3.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\cp_av_ds_3.pkl' )



# aggregate _ total distance walked.
# tdt_height_group_2 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\tdt_height_group_2.pkl' )

# %%

# -7 : last saved in : all_track .py
# -6 :last saved in 
    # C:\code\VISION\track\remove_bad_processed.py
# df_aggregate_track_6 : bad-processed videos are removed.
# aggregate 
    # df_aggregate_track_5 : last saved in : all_track.py
    # df_aggregate_track_4 : last saved in : roam.py
    # df_aggregate_track_3 : last saved in : position.py
df_aggregate_track_7 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_aggregate_track_7.pkl' )


# %%
# %%

# not needed : merged with : df_aggregate_track_4
# ROI
# continued from  C:\code\VISION\track\system.py
# no removal of bad-processed videos

df_roi_data = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_roi_data.pkl' )

# %%

# not needed. unless you want the data in dictionary format.
    # the data exists in : df_aggregate_track_4
# # no removal of bad-processed videos
# same data as above ( df_roi_data ) , in json ( dictionary ) format !
# Open the JSON file containing the ROI coordinates.
# 'r' means we are opening it in "read" mode.
# why using a dictionary ?  =>  C:\code\VISION\track\position.py
path_json = r"F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\roi_definitions.json"
with open( path_json , 'r') as f:
    # The json.load() function reads the text from the file and parses it into a Python dictionary.
    roi_data = json.load(f)

# %% bbox

# not needed. unless you want the data in dictionary format.
    # the data exists in : df_aggregate_track_4
# # no removal of bad-processed videos
# bounding box
    # this is the same as the ROI but in a differnet fromat :
            # instead of the exact coordinates of the corners : 
                # only coordinate of the bottom-left corenr + width & height of the rectangle.
# Save the Bounding Boxes to a New JSON File ---
output_bbox_file = r"F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\roi_bounding_boxes.json"
with open(output_bbox_file, 'r') as f:
    roi_bboxes = json.load(f)

# %%

# explore

        len(list(roi_bboxes))
            # Out[34]: 111
        
        roi_bboxes
            # Out[33]: 
            # {'pod_1_ZC60': [264, 32, 883, 870],
            #  'pod_1_ZC61': [264, 32, 883, 870],
            #  'pod_1_ZC62': [264, 32, 883, 870],
            #  'pod_1_ZC63': [264, 32, 883, 870],
            #  ...

# %%
# %%

# last saved in :
    # C:\code\VISION\track\remove_bad_processed.py
# df_cell_count_percentage_2 : bad-processed videos are removed.
# roam.py
# for all videos.
# the amount of time the animal spent on each cell it stepped in.
    # _count_ : the number of frames for each cell.
# 7777
df_cell_count_percentage_2 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_cell_count_percentage_2.pkl' )


# not needed !
    # merged with : df_aggregate_track_2
        # 'nocw' & 'pocw' columns
# roam.py
# for all videos.
# the number of unique cells ( out of 100 total ) that the animal explored ( stepped in ).
# no removal of bad-processed videos
exploration_score = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\exploration_score.pkl' )

# %%

# these tidy dataframes are based oon : df_aggregate_track_6 :  they should be changed to be derived from : df_aggregate_track_7.
# df_track_tidy_kinematic_3  : the kinematic outlier is also removed  ( remove_bad_processed.py ).
    # & also the metric : acceleration_mean.
# bad-processed videos are removed.
    # df_track_tidy_2
    # df_track_tidy_roam__2
    # df_track_tidy_kinematic_2
# last saved in 
    # C:\code\VISION\track\remove_bad_processed.py
    
# continued from : general_track.py

df_track_tidy_2 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_2.pkl' )

df_track_tidy_roam_2 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_roam_2.pkl' )

df_track_tidy_kinematic_3 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_kinematic_3.pkl' )

# %%


