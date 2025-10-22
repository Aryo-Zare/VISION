
# this program explores the roaming behavior of the animal
    # the probablity of standing on various spots ( grid ) in the open-field.
    # heatmap !

# %%'

# determine a grid on the open-field.
# at each frame, determine to which grid cell it belongs to.

# %%

# --- 1. Configuration ---
# Define the grid size. A 10x10 grid is a good starting point.
GRID_SIZE = (10, 10) # (columns, rows)

# %%'


# ---  Define a function that operates on a single row ( of a dataframe ) ---
    # technical ( related to how the function is written )
        # this function can then be applied to the dataframe.
        # This function now expects the entire row object as its first argument.
        # Additional parameters (roi_bboxes, grid_size) can be passed through .apply().
def get_grid_cell_from_row(row, roi_definitions, grid_size):
    """
        Calculates the grid cell for a given DataFrame row.
        - row: A pandas Series representing one row of the DataFrame.
        - roi_definitions: The dictionary of bounding boxes.
        - grid_size: A tuple (grid_cols, grid_rows).
    """
    # Extract the necessary values from the row.
    x = row['x']
    y = row['y']
    video_id = row['video_id']
    
    # Get the bounding box for this video.
    roi_bbox = roi_definitions.get(video_id)
    
    # If there's no bounding box for this video, we can't proceed.
    if roi_bbox is None:
        return None

    min_x, min_y, width, height = roi_bbox

    # If the point is outside the bounding box, return None.
    if not (min_x <= x < min_x + width and min_y <= y < min_y + height):
        return None

    # Normalize coordinates and calculate the grid cell index.
    relative_x = (x - min_x) / width
    relative_y = (y - min_y) / height
    col = int(relative_x * grid_size[0])
    row = int(relative_y * grid_size[1])

    return (col, row)


# %%'


# --- 3. Apply this to your cp_av_ds_3 ---

# %%'

# First, we need the bounding box for each video's ROI.
# We can pre-calculate this from your df_roi_data DataFrame.
# Calculate Bounding Boxes from the DataFrame ---
# We create a dictionary for efficient lookups !
roi_bboxes = {}
for _ , row in df_roi_data.iterrows():
    # Convert outer_roi points to a NumPy array to easily find min/max
    points = np.array(row['outer_roi'])
    min_x, min_y = points.min(axis=0)
    max_x, max_y = points.max(axis=0)
    width = max_x - min_x
    height = max_y - min_y
    # Store the result as a simple list in the dictionary
    roi_bboxes[row['video_id']] = [int(min_x), int(min_y), int(width), int(height)]

print(f"Successfully calculated {len(roi_bboxes)} bounding boxes.")
# Successfully calculated 111 bounding boxes.

# %%'

# Save the Bounding Boxes to a New JSON File ---
output_bbox_file = r"F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\roi_bounding_boxes.json"
with open(output_bbox_file, 'w') as f:
    # json.dump() writes the dictionary to the file in a structured way.
    json.dump(roi_bboxes, f, indent=4)

# %%'

# --- 3. Add Bounding Boxes to the cp_av_ds_3 DataFrame ---
# The most efficient way to do this is using the .map() method.
# It uses the 'video_id' from each row to look up the corresponding
# bounding box in our 'roi_bboxes' dictionary.
cp_av_ds_3['roi_bbox'] = cp_av_ds_3['video_id'].map(roi_bboxes)

# --- 4. Verify the Result ---
cp_av_ds_3[:4]
Out[14]: 
#      video_id   time sample_ID    x    y   x_smooth   y_smooth        dx  \
# 0  pod_1_ZC04  pod_1      ZC04  763  420        NaN        NaN       NaN   
# 1  pod_1_ZC04  pod_1      ZC04  819  391 818.800000 391.000000       NaN   
# 2  pod_1_ZC04  pod_1      ZC04  856  368 858.400000 365.400000 39.600000   
# 3  pod_1_ZC04  pod_1      ZC04  897  344 896.600000 344.600000 38.200000   

#           dy  distance   location   zone  \
# 0        NaN       NaN     center  inner   
# 1        NaN       NaN     center  inner   
# 2 -25.600000 47.154215     center  inner   
# 3 -20.800000 43.495747  periphery  outer   

#                                            outer_roi  \
# 0  [[183, 66], [1130, 66], [1130, 1001], [183, 10...   
# 1  [[183, 66], [1130, 66], [1130, 1001], [183, 10...   
# 2  [[183, 66], [1130, 66], [1130, 1001], [183, 10...   
# 3  [[183, 66], [1130, 66], [1130, 1001], [183, 10...   

#                                           inner_roi  sample_png_height  \
# 0  [[419, 299], [893, 299], [893, 767], [419, 767]]         564.000000   
# 1  [[419, 299], [893, 299], [893, 767], [419, 767]]         564.000000   
# 2  [[419, 299], [893, 299], [893, 767], [419, 767]]         564.000000   
# 3  [[419, 299], [893, 299], [893, 767], [419, 767]]         564.000000   

#    diff_distance_pixel  velocity_meter_s  diff_velocity_meter_s  \
# 0                  NaN               NaN                    NaN   
# 1                  NaN               NaN                    NaN   
# 2                  NaN          0.438936                    NaN   
# 3            -3.658468          0.404881              -0.034055   

#    acceleration_meter_s2             roi_bbox  
# 0                    NaN  [183, 66, 947, 935]  
# 1                    NaN  [183, 66, 947, 935]  
# 2                    NaN  [183, 66, 947, 935]  
# 3              -0.102165  [183, 66, 947, 935]  

# %%'

# Now, create a new 'grid_cell' column in your main trajectory DataFrame.
# The .apply() method can pass your function directly.
# Any extra arguments for your function are passed after the axis specification.
cp_av_ds_3['grid_cell'] = cp_av_ds_3.apply(
                                get_grid_cell_from_row,          # Pass the function name (without parentheses)
                                axis=1,                          # Specify row-wise operation
                                roi_definitions=roi_bboxes,      # Pass the bbox dictionary as an argument
                                grid_size=GRID_SIZE              # Pass the grid size tuple as an argument
)


# %%'

cp_av_ds_3[:4]
    # Out[22]: 
    #      video_id   time sample_ID    x    y   x_smooth   y_smooth        dx  \
    # 0  pod_1_ZC04  pod_1      ZC04  763  420        NaN        NaN       NaN   
    # 1  pod_1_ZC04  pod_1      ZC04  819  391 818.800000 391.000000       NaN   
    # 2  pod_1_ZC04  pod_1      ZC04  856  368 858.400000 365.400000 39.600000   
    # 3  pod_1_ZC04  pod_1      ZC04  897  344 896.600000 344.600000 38.200000   
    
    #           dy  distance   location   zone  \
    # 0        NaN       NaN     center  inner   
    # 1        NaN       NaN     center  inner   
    # 2 -25.600000 47.154215     center  inner   
    # 3 -20.800000 43.495747  periphery  outer   
    
    #                                            outer_roi  \
    # 0  [[183, 66], [1130, 66], [1130, 1001], [183, 10...   
    # 1  [[183, 66], [1130, 66], [1130, 1001], [183, 10...   
    # 2  [[183, 66], [1130, 66], [1130, 1001], [183, 10...   
    # 3  [[183, 66], [1130, 66], [1130, 1001], [183, 10...   
    
    #                                           inner_roi  sample_png_height  \
    # 0  [[419, 299], [893, 299], [893, 767], [419, 767]]         564.000000   
    # 1  [[419, 299], [893, 299], [893, 767], [419, 767]]         564.000000   
    # 2  [[419, 299], [893, 299], [893, 767], [419, 767]]         564.000000   
    # 3  [[419, 299], [893, 299], [893, 767], [419, 767]]         564.000000   
    
    #    diff_distance_pixel  velocity_meter_s  diff_velocity_meter_s  \
    # 0                  NaN               NaN                    NaN   
    # 1                  NaN               NaN                    NaN   
    # 2                  NaN          0.438936                    NaN   
    # 3            -3.658468          0.404881              -0.034055   
    
    #    acceleration_meter_s2             roi_bbox grid_cell  
    # 0                    NaN  [183, 66, 947, 935]    (6, 3)  
    # 1                    NaN  [183, 66, 947, 935]    (6, 3)  
    # 2                    NaN  [183, 66, 947, 935]    (7, 3)  
    # 3              -0.102165  [183, 66, 947, 935]    (7, 2)  


# these are the columns & rows of each cell that the animal stood at each frame.
cp_av_ds_3['grid_cell'][:4]
    # Out[39]: 
    # 0    (6, 3)
    # 1    (6, 3)
    # 2    (7, 3)
    # 3    (7, 2)
    # Name: grid_cell, dtype: object

# %%' coverage

# count the number of unique cells visited.
# We use .nunique() which counts unique non-null values.
exploration_score = cp_av_ds_3.groupby('video_id')['grid_cell'].nunique().reset_index()

# nocw : number of cells walked ( out of 100 cells [ 10 * 10 grid ] ).
exploration_score.rename(columns={'grid_cell': 'nocw'}, inplace=True)

exploration_score.shape
    # Out[26]: (111, 2)

exploration_score[:4]
    # Out[27]: 
    #      video_id  nocw
    # 0  pod_1_ZC04    49
    # 1  pod_1_ZC05    70
    # 2  pod_1_ZC06    79
    # 3  pod_1_ZC07    35

# %%'

# You can also express this as a percentage of total cells.
# pocw : percentage of cells walked ( out of 100 cells [ 10 * 10 grid ] ).
    # this doesnot take into account the time spent in each cell !
total_cells = GRID_SIZE[0] * GRID_SIZE[1]
exploration_score['pocw'] = (exploration_score['nocw'] / total_cells) * 100

exploration_score[:4]
    # Out[30]: 
    #      video_id  nocw      pocw
    # 0  pod_1_ZC04    49 49.000000
    # 1  pod_1_ZC05    70 70.000000
    # 2  pod_1_ZC06    79 79.000000
    # 3  pod_1_ZC07    35 35.000000

# %%'

df_aggregate_track_2 = pd.merge(
                                    df_aggregate_track, 
                                    exploration_score, 
                                    on=['video_id']
)

df_aggregate_track_2.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_aggregate_track_2.pkl' )


# %%'

exploration_score.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\exploration_score.pkl' )

# %%'
# %%' number of frames  

# Count the number of frames ( amount of time spent ) spent in each cell.
# the amount of time the animal spent on each cell it stepped in.
    # _count_ : the number of frames for each cell.
cell_counts_all_videos = cp_av_ds_3.groupby('video_id')['grid_cell'].value_counts().reset_index()

# 2025-10-16 _ Thursday _ 12:51 
# as only cells in which an animal has once stood are written in ' cp_av_ds_3 ' , there is no cell here where the count would be 0.
    # the count is at least 1 ( 1 frame with the animal in that cell ).
cell_counts_all_videos.shape
    # Out[48]: (7777, 3)     # 2025-10-16 _ Thursday _ 12:51 

cell_counts_all_videos[:4]
    # Out[49]: 
    #      video_id grid_cell  count
    # 0  pod_1_ZC04    (3, 1)    220
    # 1  pod_1_ZC04    (8, 2)    206
    # 2  pod_1_ZC04    (7, 4)    199
    # 3  pod_1_ZC04    (6, 1)    192

# %%' percentage of time

# perhaps the more important is the percentage of time the animal spent on each grid.
    # relative to the total 10 minutes time of the video.
# The recommended, readable, and efficient way to write the code
cell_percentages_df = (
                        cp_av_ds_3.groupby('video_id')['grid_cell']
                        .value_counts(normalize=True)
                        .mul(100)
                        .round(2)
                        .reset_index(name='percentage')
)

cell_percentages_df[:4]
    # Out[51]: 
    #      video_id grid_cell  percentage
    # 0  pod_1_ZC04    (3, 1)   12.220000
    # 1  pod_1_ZC04    (8, 2)   11.440000
    # 2  pod_1_ZC04    (7, 4)   11.060000
    # 3  pod_1_ZC04    (6, 1)   10.670000

# %%'

df_cell_count_percentage = pd.merge(
                                    cell_counts_all_videos, 
                                    cell_percentages_df, 
                                    on=['video_id', 'grid_cell']
)

# %%'

df_cell_count_percentage.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_cell_count_percentage.pkl' )

# %%'

df_cell_count_percentage.shape
    # Out[55]: (7777, 4)

df_cell_count_percentage[:4]
    # Out[54]: 
    #      video_id grid_cell  count  percentage
    # 0  pod_1_ZC04    (3, 1)    220   12.220000
    # 1  pod_1_ZC04    (8, 2)    206   11.440000
    # 2  pod_1_ZC04    (7, 4)    199   11.060000
    # 3  pod_1_ZC04    (6, 1)    192   10.670000

# %%'
# %%' entropy

# this section explores the evenness of visiting the open-field.

# %% shannon

# --- 1. Define a function to calculate entropy for one video's data ---
def calculate_shannon_entropy(series):
    """Calculates the Shannon's Entropy for a pandas Series of proportions."""
    # Convert percentages to proportions (e.g., 25.5 -> 0.255)
    proportions = series / 100
    
    # The core entropy formula: H = -Σ(p * log2(p))
    # We filter out p=0 to avoid log(0) errors, though it shouldn't happen with value_counts.
    proportions = proportions[proportions > 0]
    
    return -np.sum(proportions * np.log2(proportions))

# %%'

# --- 2. Calculate Entropy for Each Video ---
# We group by video_id and apply our function to the 'percentage' column for each group.
entropy_per_video = (
                    df_cell_count_percentage.groupby('video_id')['percentage']
                    .apply(calculate_shannon_entropy)
                    .reset_index(name='shannon_entropy')
)

entropy_per_video.shape
    # Out[25]: (111, 2)

entropy_per_video[:4]
    # Out[26]: 
    #      video_id  shannon_entropy
    # 0  pod_1_ZC04         4.095035
    # 1  pod_1_ZC05         5.046960
    # 2  pod_1_ZC06         5.018722
    # 3  pod_1_ZC07         4.473029

# %%'

df_aggregate_track_3 = pd.merge(
                                    df_aggregate_track_2 , 
                                    entropy_per_video , 
                                    on=['video_id']
)

df_aggregate_track_3.shape
    # Out[28]: (108, 16)

df_aggregate_track_3.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_aggregate_track_3.pkl' )


# %%' uniformity_index


# --- 4. Merge the Data and Calculate the Uniformity Index ---
# Merge the entropy results with the cell counts.
df_aggregate_track_3 = pd.merge(entropy_per_video, cells_visited_per_video)

# Calculate the maximum possible entropy for the number of cells visited (H_max = log2(N)).
# We add a check to avoid log2(1) which is 0 and would cause division by zero.
df_aggregate_track_3['max_entropy'] = np.log2(df_aggregate_track_3['nocw'])
df_aggregate_track_3['max_entropy'].replace(0, np.nan, inplace=True) # Replace 0 with NaN

# The Uniformity Index is the actual entropy divided by the maximum possible entropy.
# We fill any NaN results (from the above step) with 0. 
    # A single visited cell has 0 uniformity.
df_aggregate_track_3['uniformity_index'] = (
                df_aggregate_track_3['shannon_entropy'] / df_aggregate_track_3['max_entropy']
).fillna(0)


df_aggregate_track_3.iloc[ :4 , -5:]
    # Out[33]: 
    #    nocw      pocw  shannon_entropy  max_entropy  uniformity_index
    # 0    49 49.000000         4.095035     5.614710          0.729341
    # 1    70 70.000000         5.046960     6.129283          0.823418
    # 2    79 79.000000         5.018722     6.303781          0.796145
    # 3    35 35.000000         4.473029     5.129283          0.872057


df_aggregate_track_3.shape
    # Out[34]: (108, 18)

# %%'

df_aggregate_track_3.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_aggregate_track_3.pkl' )

# %%'
# %% organization

# not the correct way of merging : 
    # colmmon columns are also merged with aded column name suffix ; -x , -y !

                df_aggregate_track_4 = pd.merge(
                                                    df_aggregate_track_3 , 
                                                    df_roi_data , 
                                                    on=['video_id']
                )
    
                    # Out[24]: 
                    # Index(['time_x', 'sample_ID_x', 'tdt_pixel', 'file_name', 'sample_png_height',
                    #        'tdt_meter', 'treatment', 'video_id', 'inner_zone_percentage',
                    #        'velocity_mean', 'velocity_max', 'acceleration_mean',
                    #        'acceleration_max', 'nocw', 'pocw', 'shannon_entropy', 'max_entropy',
                    #        'uniformity_index', 'outer_roi', 'inner_roi', 'time_y', 'sample_ID_y'],
                    #       dtype='object')
                
                df_aggregate_track_4.shape
                    # Out[21]: (108, 22)


# %% organization

# organization : merging data.

# Select only the key column ('video_id') and the columns you want to add
# from the right DataFrame.
right_df_subset = df_roi_data[['video_id', 'inner_roi', 'outer_roi']]

# Perform a left merge.
# This keeps all columns and rows from the left DataFrame ('df_aggregate_track_3')
# and adds the selected columns from the right one, matching on 'video_id'.
df_aggregate_track_4 = pd.merge(
    df_aggregate_track_3, 
    right_df_subset, 
    on='video_id', 
    how='left'
)


df_aggregate_track_4.shape
    # Out[27]: (108, 20)


df_aggregate_track_4.columns
    # Out[28]: 
    # Index(['time', 'sample_ID', 'tdt_pixel', 'file_name', 'sample_png_height',
    #        'tdt_meter', 'treatment', 'video_id', 'inner_zone_percentage',
    #        'velocity_mean', 'velocity_max', 'acceleration_mean',
    #        'acceleration_max', 'nocw', 'pocw', 'shannon_entropy', 'max_entropy',
    #        'uniformity_index', 'inner_roi', 'outer_roi'],
    #       dtype='object')

# %%'

df_aggregate_track_4.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_aggregate_track_4.pkl' )

# %% organization

# organization : merging data.

# Create a new column 'bbox_roi' in your DataFrame.
# The .map() method looks up each 'video_id' in the 'roi_bboxes' dictionary
# and places the corresponding value in the new column.
df_aggregate_track_4['bbox_roi'] = df_aggregate_track_4['video_id'].map(roi_bboxes)

df_aggregate_track_4.shape
    # Out[36]: (108, 21)

df_aggregate_track_4.columns
    # Out[37]: 
    # Index(['time', 'sample_ID', 'tdt_pixel', 'file_name', 'sample_png_height',
    #        'tdt_meter', 'treatment', 'video_id', 'inner_zone_percentage',
    #        'velocity_mean', 'velocity_max', 'acceleration_mean',
    #        'acceleration_max', 'nocw', 'pocw', 'shannon_entropy', 'max_entropy',
    #        'uniformity_index', 'inner_roi', 'outer_roi', 'bbox_roi'],
    #       dtype='object')

# %%'

df_aggregate_track_4.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_aggregate_track_4.pkl' )

# %%'


