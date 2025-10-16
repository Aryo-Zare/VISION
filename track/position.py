
# %%

# adding the bounding-box data for inner & outer zones to the big dataframe.

# df_roi_data ; from : system.py
# cp_av_ds : from : all_track .py

# Perform a left merge
cp_av_ds_2 = pd.merge(
            left=cp_av_ds,
            right=df_roi_data[[ 'video_id' , 'outer_roi' , 'inner_roi' ]], # 1 : bottom
            on='video_id',
            how='left'
)
# 1 : # Select only the columns you need from the right table.

cp_av_ds_2.columns
    # Out[51]: 
    # Index(['video_id', 'time', 'sample_ID', 'x', 'y', 'x_smooth', 'y_smooth', 'dx',
    #        'dy', 'distance', 'outer_roi', 'inner_roi'],
    #       dtype='object')

cp_av_ds_2.shape
    # Out[52]: (196341, 12)

cp_av_ds_2[:3]
    # Out[53]: 
    #      video_id   time sample_ID    x    y   x_smooth   y_smooth        dx  \
    # 0  pod_1_ZC04  pod_1      ZC04  763  420        NaN        NaN       NaN   
    # 1  pod_1_ZC04  pod_1      ZC04  819  391 818.800000 391.000000       NaN   
    # 2  pod_1_ZC04  pod_1      ZC04  856  368 858.400000 365.400000 39.600000   
    
    #           dy  distance                                          outer_roi  \
    # 0        NaN       NaN  [[183, 66], [1130, 66], [1130, 1001], [183, 10...   
    # 1        NaN       NaN  [[183, 66], [1130, 66], [1130, 1001], [183, 10...   
    # 2 -25.600000 47.154215  [[183, 66], [1130, 66], [1130, 1001], [183, 10...   
    
    #                                           inner_roi  
    # 0  [[419, 299], [893, 299], [893, 767], [419, 767]]  
    # 1  [[419, 299], [893, 299], [893, 767], [419, 767]]  
    # 2  [[419, 299], [893, 299], [893, 767], [419, 767]]  

cp_av_ds_2.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\cp_av_ds_2.pkl' )


# %%

# Here is the second script with detailed annotations, 
    # explaining how it uses the ROI definitions to analyze your trajectory data.
## Phase 2: Classifying Your Trajectory Data (Annotated)
# This script's job is to take your two sources of data—the pig's coordinates (cp_av_ds) and the arena boundaries you just defined \
    # (roi_definitions.json)—and combine them to produce your final results. 
    # It will check every single coordinate point and label it based on its location.
        # if the point is in the inner or outer zone !
# for phase 1 ( ROI determination for each video )  =>  system.py
# Import necessary libraries
import pandas as pd  # Pandas is used for loading and manipulating your main data table (the DataFrame).
import numpy as np   # NumPy is needed for creating arrays, which is the format OpenCV prefers for coordinates.
import json        # The json library is needed to load the ROI data from the file we created in the first script.
import cv2         # We only need one specific function from OpenCV here: cv2.pointPolygonTest.

# %%

# --- Load Data ---
# First, you need to have your master DataFrame loaded into a variable.
# For this example, we assume it's already in memory and named 'cp_av_ds'.
# If you were running this script separately, you would load it from a file like this:
# cp_av_ds = pd.read_csv("path/to/your/master_data.csv")

# Open the JSON file containing the ROI coordinates.
# 'r' means we are opening it in "read" mode.
path_json = r"F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\roi_definitions.json"
with open( path_json , 'r') as f:
    # The json.load() function reads the text from the file and parses it into a Python dictionary.
    roi_data = json.load(f)

# %%

type(roi_data)
    # Out[14]: dict


list(roi_data)[:4]
    # Out[16]: ['pod_1_ZC60', 'pod_1_ZC61', 'pod_1_ZC62', 'pod_1_ZC63']

# nested dictionary.
roi_data['pod_1_ZC60']
    # Out[17]: 
    # {'outer_roi': [[264, 32], [1147, 32], [1147, 902], [264, 902]],
    #  'inner_roi': [[484, 249], [926, 249], [926, 684], [484, 684]]}

# %% explore dictionary

test_dict = { 'a':4 , 'b':5  }

test_dict.items()
    # Out[24]: dict_items([('a', 4), ('b', 5)])

# %% explore dictionary

test_dict_2 = {
                'outer_roi': [[264, 32], [1147, 32], [1147, 902], [264, 902]],
                'inner_roi': [[484, 249], [926, 249], [926, 684], [484, 684]]
              }


test_dict_2.items()
# Out[25]: dict_items([('outer_roi', [[264, 32], [1147, 32], [1147, 902], [264, 902]]), ('inner_roi', [[484, 249], [926, 249], [926, 684], [484, 684]])])

# %%

a , b = test_dict_2.items()

a
    # Out[29]: ('outer_roi', [[264, 32], [1147, 32], [1147, 902], [264, 902]])

b
    # Out[30]: ('inner_roi', [[484, 249], [926, 249], [926, 684], [484, 684]])

# %%


test_dict_3 = {
                "pod_1_ZC60": {
                                'outer_roi': [[264, 32], [1147, 32], [1147, 902], [264, 902]],
                                'inner_roi': [[484, 249], [926, 249], [926, 684], [484, 684]]
                              } ,
                
                "pod_1_ZC61": {
                                'outer_roi': [[264, 32], [1147, 32], [1147, 902], [264, 902]],
                                'inner_roi': [[484, 249], [926, 249], [926, 684], [484, 684]]
                              }
              }

test_dict_3.items()
# Out[32]: dict_items([('pod_1_ZC60', {'outer_roi': [[264, 32], [1147, 32], [1147, 902], [264, 902]], 'inner_roi': [[484, 249], [926, 249], [926, 684], [484, 684]]}), ('pod_1_ZC61', {'outer_roi': [[264, 32], [1147, 32], [1147, 902], [264, 902]], 'inner_roi': [[484, 249], [926, 249], [926, 684], [484, 684]]})])

a , b = test_dict_3.items()

a
    # Out[34]: 
    # ('pod_1_ZC60',
    #  {'outer_roi': [[264, 32], [1147, 32], [1147, 902], [264, 902]],
    #   'inner_roi': [[484, 249], [926, 249], [926, 684], [484, 684]]})

b
    # Out[35]: 
    # ('pod_1_ZC61',
    #  {'outer_roi': [[264, 32], [1147, 32], [1147, 902], [264, 902]],
    #   'inner_roi': [[484, 249], [926, 249], [926, 684], [484, 684]]})

type(a)
    # Out[39]: tuple

# %%

# it unpacked the tuple !
video_id , rois = a

video_id
    # Out[37]: 'pod_1_ZC60'

rois
    # Out[38]: 
    # {'outer_roi': [[264, 32], [1147, 32], [1147, 902], [264, 902]],
    #  'inner_roi': [[484, 249], [926, 249], [926, 684], [484, 684]]}

type(rois)
    # Out[40]: dict

# %%

# --- Prepare Data for OpenCV ---
# The lists of coordinates in our JSON file need to be converted into NumPy arrays.
# OpenCV functions are highly optimized and expect their inputs in this specific format for maximum speed.
# We loop through each video_id and its corresponding ROI data in our dictionary.
for video_id, rois in roi_data.items():
    # Overwrite the 'outer_roi' list with a NumPy array version of itself.
    # We specify dtype=np.int32 because OpenCV geometric functions expect 32-bit integers.
    rois['outer_roi'] = np.array(rois['outer_roi'], dtype=np.int32)
    # Do the same for the 'inner_roi' list.
    rois['inner_roi'] = np.array(rois['inner_roi'], dtype=np.int32)

# %%

# --- Define the Core Logic in a Function ---
# It's good practice to put the main classification logic into a function.
# This makes the code cleaner and easier to understand.
# This function will be applied to every single row of our DataFrame.
def classify_location(row):
    """
    Takes a row from the DataFrame and determines if the point (x, y)
    is in the center, periphery, or outside of the defined ROIs for that video.
    - row: A single row of the DataFrame, which you can access like a dictionary (e.g., row['x']).
    """
    # Get the unique identifier for the video from the current row.
    video_id = row['video_id']
    # Create a tuple of the (x, y) coordinates for the current row.
    # This is the point we want to test.
    point = (row['x'], row['y'])

    # Safety check: If for some reason we don't have an ROI for this video_id,
    # we'll label it and skip the rest of the logic.
    if video_id not in roi_data:
        return 'no_roi'

    # Retrieve the pre-loaded and converted NumPy arrays for this specific video's ROIs.
    rois = roi_data[video_id]

    # This is the key OpenCV function. It checks if a point is inside a polygon (contour).
    #   - rois['inner_roi']: The polygon we are testing against.
    #   - point: The (x, y) coordinate to check.
    #   - False: This argument, 'measureDist', tells the function we don't need the exact
    #            distance to the polygon edge. We only care if it's inside or outside.
    #            This is slightly faster.
    #
    # The function returns:
    #   - A positive value (> 0) if the point is INSIDE the polygon.
    #   - Zero (0) if the point is EXACTLY ON the edge of the polygon.
    #   - A negative value (< 0) if the point is OUTSIDE the polygon.
    #
    # So, we test the most specific region first: the center.
    if cv2.pointPolygonTest(rois['inner_roi'], point, False) >= 0:
        return 'center'

    # If the point was not in the center, we then check if it's in the larger, outer region.
    # If it is, that means it must be in the periphery.
    elif cv2.pointPolygonTest(rois['outer_roi'], point, False) >= 0:
        return 'periphery'

    # If the point is not inside the inner ROI and not inside the outer ROI,
    # then it must be outside the defined open-field area.
    else:
        return 'outside'

# %%


# --- Apply the Function to the Entire DataFrame ---
# The .apply() method is a powerful tool in Pandas. It runs a function on every row (or column) of the DataFrame.
#   - classify_location: The function we want to run. We pass the function object itself, without parentheses.
#   - axis=1: This is crucial. It tells .apply() to operate on a row-by-row basis.
#             (axis=0 would operate on columns).
# The result of .apply() is a new Pandas Series (like a single column) containing the return
# value from the function for each row. We assign this new Series to a new 'location' column
# in our DataFrame.
print("Classifying all trajectory points... (This may take a while for large datasets)")
cp_av_ds['location'] = cp_av_ds.apply(classify_location, axis=1)

print("\nClassification complete!")
print("Here's a preview of the DataFrame with the new 'location' column:")
print( cp_av_ds.head() )
    #      video_id   time sample_ID    x    y   x_smooth   y_smooth        dx  \
    # 0  pod_1_ZC04  pod_1      ZC04  763  420        NaN        NaN       NaN   
    # 1  pod_1_ZC04  pod_1      ZC04  819  391 818.800000 391.000000       NaN   
    # 2  pod_1_ZC04  pod_1      ZC04  856  368 858.400000 365.400000 39.600000   
    # 3  pod_1_ZC04  pod_1      ZC04  897  344 896.600000 344.600000 38.200000   
    # 4  pod_1_ZC04  pod_1      ZC04  917  331 917.000000 331.000000 20.400000   
    
    #           dy  distance   location  
    # 0        NaN       NaN     center  
    # 1        NaN       NaN     center  
    # 2 -25.600000 47.154215     center  
    # 3 -20.800000 43.495747  periphery  
    # 4 -13.600000 24.517749  periphery 


cp_av_ds['location'].unique()
    # Out[60]: array(['center', 'periphery', 'outside'], dtype=object)


# here, there are also values outside the open-field zone.
    # this is probably related to where the center-of-gravity of the pig was outside the dewarped camera captured open-field area.
    # hence, this corresponds to the periphery zone.
cp_av_ds['location'].value_counts()
    # Out[61]: 
    # location
    # periphery    152929
    # center        40313
    # outside        3099
    # Name: count, dtype: int64

# %%

# 1. First, define your mapping in a Python dictionary.
#    This clearly states that 'center' becomes 'inner', and the other two become 'outer'.
location_to_zone_map = {
                        'center': 'inner',
                        'periphery': 'outer',
                        'outside': 'outer'
}

# 2. Create the new 'zone' column by applying this map to the 'location' column.
cp_av_ds['zone'] = cp_av_ds['location'].map(location_to_zone_map)

# Let's check the result!
cp_av_ds[['video_id', 'location', 'zone']].head()
    # Out[62]: 
    #      video_id   location   zone
    # 0  pod_1_ZC04     center  inner
    # 1  pod_1_ZC04     center  inner
    # 2  pod_1_ZC04     center  inner
    # 3  pod_1_ZC04  periphery  outer
    # 4  pod_1_ZC04  periphery  outer

cp_av_ds['zone'].value_counts()
    # Out[63]: 
    # zone
    # outer    156028
    # inner     40313
    # Name: count, dtype: int64

# %%

# --- Final Analysis: Calculate Time/Probability ---
# Now that every point is classified, we can aggregate the results.
# We group the DataFrame by 'video_id' to analyze each video separately.
# Then, for each video group, we apply .value_counts() to the 'location' column.
# This counts the number of times 'center', 'periphery', and 'outside' appear for each video.
# Since each row represents one frame, this count is equivalent to the time spent in each zone.
zone_counts = cp_av_ds.groupby('video_id')['zone'].value_counts()

zone_counts[:4]
    # Out[65]: 
    # video_id    zone 
    # pod_1_ZC04  outer    1571
    #             inner     229
    # pod_1_ZC05  outer    1702
    #             inner      98
    # Name: count, dtype: int64

# To get percentages, we do almost the same thing but add 'normalize=True'.
# .value_counts(normalize=True) returns the proportion (e.g., 0.65) instead of the count.
# We then multiply by 100 (.mul(100)) and round to 2 decimal places (.round(2)) for readability.
zone_percentages = cp_av_ds.groupby('video_id')['zone'].value_counts(normalize=True).mul(100).round(2)

zone_percentages[:4]
    # Out[67]: 
    # video_id    zone 
    # pod_1_ZC04  outer   87.280000
    #             inner   12.720000
    # pod_1_ZC05  outer   94.560000
    #             inner    5.440000
    # Name: proportion, dtype: float64

# %%

# location_counts = cp_av_ds.groupby('video_id')['location'].value_counts()

# location_counts[:4]
#     # Out[58]: 
#     # video_id    location 
#     # pod_1_ZC04  periphery    1571
#     #             center        229
#     # pod_1_ZC05  periphery    1690
#     #             center         98
#     # Name: count, dtype: int64

# # To get percentages, we do almost the same thing but add 'normalize=True'.
# # .value_counts(normalize=True) returns the proportion (e.g., 0.65) instead of the count.
# # We then multiply by 100 (.mul(100)) and round to 2 decimal places (.round(2)) for readability.
# location_percentages = cp_av_ds.groupby('video_id')['location'].value_counts(normalize=True).mul(100).round(2)

# print("\n--- Frame Counts per Location for Each Video ---")
# print(location_counts.head(10)) # Print the first 10 results as an example

# print("\n--- Percentage of Time Spent per Location (%) ---")
# print(location_percentages.head(10)) # Print the first 10 results as an example

# %%

# 1. Convert the multi-index Series to a DataFrame.
#    This will create columns: 'video_id', 'zone', and 'proportion'.
# how is the name 'proportion' being made for this column ?  automatic ?
zone_df = zone_percentages.reset_index()

zone_df[:4]
    # Out[69]: 
    #      video_id   zone  proportion
    # 0  pod_1_ZC04  outer   87.280000
    # 1  pod_1_ZC04  inner   12.720000
    # 2  pod_1_ZC05  outer   94.560000
    # 3  pod_1_ZC05  inner    5.440000

# 2. Filter this DataFrame to keep only the rows where the 'zone' is 'inner'.
#    We use .copy() to ensure we are working with a new DataFrame and avoid any SettingWithCopyWarning.

mask_inner = zone_df['zone'] == 'inner'
inner_zone_df = zone_df[ mask_inner ]
inner_zone_df[:4]
    # Out[70]: 
    #      video_id   zone  proportion
    # 1  pod_1_ZC04  inner   12.720000
    # 3  pod_1_ZC05  inner    5.440000
    # 5  pod_1_ZC06  inner   14.280000
    # 8  pod_1_ZC08  inner   12.280000

# 3. Rename the 'proportion' column to your desired name.
inner_zone_df.rename(columns={'proportion': 'inner_zone_percentage'}, inplace=True)

# 4. Drop the 'zone' column as it's no longer needed (all values are 'inner').
inner_zone_df.drop(columns=['zone'], inplace=True)

inner_zone_df[:4]
    # Out[73]: 
    #      video_id  inner_zone_percentage
    # 1  pod_1_ZC04              12.720000
    # 3  pod_1_ZC05               5.440000
    # 5  pod_1_ZC06              14.280000
    # 8  pod_1_ZC08              12.280000

# %%

# now before merging with the aggregate dataframe, adding a 'video_id' column to it fro easier merging !
# Remove the '.png' extension and create the 'video_id' column
tdt_height_group_2['video_id'] = tdt_height_group_2['file_name'].str.replace('.png', '', regex=False)

tdt_height_group_2.head()
    # Out[80]: 
    #     time sample_ID    tdt_pixel       file_name  sample_png_height  tdt_meter  \
    # 0  pod_1      ZC04  9637.413800  pod_1_ZC04.png                564  29.903323   
    # 1  pod_1      ZC05 26730.860213  pod_1_ZC05.png                564  82.941499   
    # 2  pod_1      ZC06 18499.849050  pod_1_ZC06.png                564  57.402014   
    # 3  pod_1      ZC07  8868.898625  pod_1_ZC07.png                564  27.518746   
    # 4  pod_1      ZC08 17381.271351  pod_1_ZC08.png                564  53.931250   
    
    #     treatment    video_id  
    # 0     DBD-HTK  pod_1_ZC04  
    # 1  DBD-Ecosol  pod_1_ZC05  
    # 2     DBD-HTK  pod_1_ZC06  
    # 3  DBD-Ecosol  pod_1_ZC07  
    # 4     DBD-HTK  pod_1_ZC08  

# %%



# Perform a left merge
df_aggregate = pd.merge(
                        left=tdt_height_group_2,
                        right=inner_zone_df, # 1 : bottom
                        on='video_id',
                        how='left'
)
# 1 : # Select only the columns you need from the right table.

df_aggregate.head()
    # Out[82]: 
    #     time sample_ID    tdt_pixel       file_name  sample_png_height  tdt_meter  \
    # 0  pod_1      ZC04  9637.413800  pod_1_ZC04.png                564  29.903323   
    # 1  pod_1      ZC05 26730.860213  pod_1_ZC05.png                564  82.941499   
    # 2  pod_1      ZC06 18499.849050  pod_1_ZC06.png                564  57.402014   
    # 3  pod_1      ZC07  8868.898625  pod_1_ZC07.png                564  27.518746   
    # 4  pod_1      ZC08 17381.271351  pod_1_ZC08.png                564  53.931250   
    
    #     treatment    video_id  inner_zone_percentage  
    # 0     DBD-HTK  pod_1_ZC04              12.720000  
    # 1  DBD-Ecosol  pod_1_ZC05               5.440000  
    # 2     DBD-HTK  pod_1_ZC06              14.280000  
    # 3  DBD-Ecosol  pod_1_ZC07                    NaN  
    # 4     DBD-HTK  pod_1_ZC08              12.280000  


df_aggregate.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_aggregate.pkl' )


# %%

