
# the reason for naming it all_track : in contrast to other versions, now all videos are processed !
# oop !
# F:\OneDrive - Uniklinik RWTH Aachen\VISION\track \ AI_track .docx

# %%'

from pathlib import Path

# %%''


# %%'

# continued from : system.py / height (pixel)
image_height_analysis_opencv = pd.read_csv ( 
            r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\first_frame_3\image_height_analysis_opencv.csv' )

# %%''

image_height_analysis_opencv[:4]
    # Out[9]: 
    #         file_name  sample_png_height  \
    # 0  pod_1_ZC14.png                569   
    # 1  pod_3_ZC14.png                569   
    # 2  pod_4_ZC14.png                569   
    # 3  pod_7_ZC14.png                569   
    
    #                                          folder_path  
    # 0  F:\OneDrive - Uniklinik RWTH Aachen\VISION\tra...  
    # 1  F:\OneDrive - Uniklinik RWTH Aachen\VISION\tra...  
    # 2  F:\OneDrive - Uniklinik RWTH Aachen\VISION\tra...  
    # 3  F:\OneDrive - Uniklinik RWTH Aachen\VISION\tra...  

image_height_analysis_opencv.shape
    # Out[10]: (111, 3)


# %%'

# --- 1. Specify the path to your folder containing the CSV files ---
# Replace '.' with the actual path if your script is not in the same parent directory.
# For example: data_folder = Path("C:/Users/YourUser/Documents/Pig_Project/pig_trajectories")
# pooled : all files in the following direcotory are pooled : F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\center_point
    # continued from : system.py / copy the .csv files
    # there are 111 csv files !
data_folder = Path( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\center_point__pooled' )

data_folder
    # Out[13]: WindowsPath('F:/OneDrive - Uniklinik RWTH Aachen/VISION\track/center_point__pooled')

# --- 2. Find all CSV files and prepare a list to hold the data ---
# Using .glob('*.csv') is a robust way to find all files ending with .csv
# you hould type 'r' before the root folder when defining it : Path( r'F:\OneD ...
    # otherwise, withoout throwing any error, the following command will result in an empty : csv_files : folder !
csv_files = list(data_folder.glob('*.csv'))
print(f"Found {len(csv_files)} CSV files to process.")
# Found 111 CSV files to process.

# %%'

all_data_list = []

# --- 3. Loop through each CSV, read it, and add a video identifier ---
for csv_file in csv_files:
    # Read the current CSV file into a DataFrame
    # Assuming the columns are named 'x' and 'y'. If not, adjust accordingly.
    # e.g., df = pd.read_csv(csv_file, names=['x', 'y']) if there are no headers.
    df = pd.read_csv(csv_file)

    # This is the key step: Add a new column with the video's name.
    # path.stem gives you the filename without the extension (e.g., "video_01" from "video_01.csv")
    df['video_id'] = csv_file.stem

    # Add the DataFrame for this video to our list
    all_data_list.append(df)

# --- 4. Concatenate all DataFrames in the list into one master DataFrame ---
if all_data_list:
    master_df = pd.concat(all_data_list, ignore_index=True)

    # Reorder columns to have 'video_id' first for better readability
    master_df = master_df[['video_id', 'x', 'y']]

    print("\nSuccessfully created the master DataFrame!")
    print("\nHere are the first few rows:")
    print(master_df.head())

    print("\nAnd the last few rows (showing data from another video):")
    print(master_df.tail())

    print("\nDataFrame Info:")
    master_df.info()

else:
    print("No CSV files were processed. The list is empty.")

# %%'

# The output from the above cell.
'''
        Successfully created the master DataFrame!
        
        Here are the first few rows:
             video_id    x    y
        0  pod_1_ZC04  763  420
        1  pod_1_ZC04  768  418
        2  pod_1_ZC04  774  415
        3  pod_1_ZC04  782  412
        4  pod_1_ZC04  788  409
        
        And the last few rows (showing data from another video):
                       video_id     x    y
        1962727  retrain_2_ZC68  1056  913
        1962728  retrain_2_ZC68  1056  913
        1962729  retrain_2_ZC68  1056  913
        1962730  retrain_2_ZC68  1056  913
        1962731  retrain_2_ZC68  1056  913
        
        DataFrame Info:
        <class 'pandas.core.frame.DataFrame'>
        RangeIndex: 1962732 entries, 0 to 1962731
        Data columns (total 3 columns):
         #   Column    Dtype 
        ---  ------    ----- 
         0   video_id  object
         1   x         int64 
         2   y         int64 
        dtypes: int64(2), object(1)
        memory usage: 44.9+ MB

'''

# %%'

master_df.shape
    # Out[22]: (1962732, 3)

# cp_av = center-points _ all videos.
master_df.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\cp_av.pkl' )

# %% Split 'video_id' into 'time' and 'sample_ID' columns ---

# The .str accessor lets us apply string methods to the entire column.
# .rsplit('_', n=1) splits the string from the right at the first underscore it finds.

# rsplit: It splits from the right side of the string.
# '_': It uses the underscore as the delimiter.
# n=1: It performs a maximum of 1 split. 
    # This is crucial because it ensures only the last underscore is used \ 
    # leaving the rest of the time string intact (e.g., 'retrain_2').
# expand=True: This command takes the list of split strings (which will have two elements: ['retrain_2', 'ZC68']) 
    # and expands it into separate DataFrame columns.
master_df[['time', 'sample_ID']] = master_df['video_id'].str.rsplit( pat='_', n=1, expand=True)

master_df[:4]
    # Out[28]: 
    #      video_id    x    y   time sample_ID
    # 0  pod_1_ZC04  763  420  pod_1      ZC04
    # 1  pod_1_ZC04  768  418  pod_1      ZC04
    # 2  pod_1_ZC04  774  415  pod_1      ZC04
    # 3  pod_1_ZC04  782  412  pod_1      ZC04

# Reorder columns for better readability
master_df = master_df[['video_id', 'time', 'sample_ID', 'x', 'y']] 

print(master_df.tail())
    #                video_id       time sample_ID     x    y
    # 1962727  retrain_2_ZC68  retrain_2      ZC68  1056  913
    # 1962728  retrain_2_ZC68  retrain_2      ZC68  1056  913
    # 1962729  retrain_2_ZC68  retrain_2      ZC68  1056  913
    # 1962730  retrain_2_ZC68  retrain_2      ZC68  1056  913
    # 1962731  retrain_2_ZC68  retrain_2      ZC68  1056  913

# %%'

# cp_av = center-points _ all videos.
master_df.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\cp_av.pkl' )

# %%'

# cp_av : center oints , all videos
cp_av = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\cp_av.pkl' )


# %%''
# %%''
# %% groupby

# here, on a big dataframe with multiple categories inside, instead of performing a 'for loop', the : groupby : function is used.

# --- 1. Define Parameters (as in your function) ---
# You should adjust these values based on your experimental setup and noise level.
window_size = 5          # How many frames to average over. Adjust as needed. 
downsample_factor = 10    # Set to 1 to disable downsampling, or >1 to use it.
# m_pix = 0.01             # Example meter-to-pixel conversion factor.
    # was not used !
fps = 30                 # Frames per second of the video source. 

# %%'

# 1. Define a clear, reusable function
def smooth_rolling_mean(series, window):
    """Calculates the centered rolling mean for a series."""
    return series.rolling( window=window , center=True ).mean()

# --- 2. Apply the Rolling Window (Low-pass Filter) FOR EACH VIDEO ---
print("Applying smoothing filter to x and y coordinates...")

# 2. Pass the function and its arguments to .transform()
# We group by 'video_id' to ensure the rolling mean is calculated separately for each video.
# The .transform() method is a neat way to apply the function and keep the result's shape the same as the original DataFrame.
cp_av['x_smooth'] = cp_av.groupby('video_id')['x'].transform( smooth_rolling_mean, window=window_size )
cp_av['y_smooth'] = cp_av.groupby('video_id')['y'].transform( smooth_rolling_mean, window=window_size )

# %%'

cp_av.shape
    # Out[14]: (1962732, 7)

cp_av[:4]
    # Out[15]: 
    #      video_id   time sample_ID    x    y   x_smooth   y_smooth
    # 0  pod_1_ZC04  pod_1      ZC04  763  420        NaN        NaN
    # 1  pod_1_ZC04  pod_1      ZC04  768  418        NaN        NaN
    # 2  pod_1_ZC04  pod_1      ZC04  774  415 775.000000 414.800000
    # 3  pod_1_ZC04  pod_1      ZC04  782  412 781.200000 412.000000

# %%'

# --- 3. Downsample the data FOR EACH VIDEO (Optional) ---
# Applying a function to each group is the safest way to downsample.
print(f"Downsampling data by a factor of {downsample_factor}...")
# We apply a function to each group that selects every Nth row.
# cp_av_ds : ds : downsampled.
cp_av_ds = cp_av.groupby('video_id').apply(
                                            lambda x: x.iloc[::downsample_factor], 
                                            include_groups=True
).reset_index(drop=True)


# include_groups=True    =>
    # c:\code\vision\track\all_track.py:237: DeprecationWarning: 
    #     DataFrameGroupBy.apply operated on the grouping columns. 
    #     This behavior is deprecated, and in a future version of pandas the grouping columns will be excluded from the operation. 
    #     Either pass `include_groups=False` to exclude the groupings or explicitly select the grouping columns after groupby to silence this warning.
    #   cp_av_ds = cp_av.groupby('video_id').apply(
# if : include_groups=False : or :
        # cp_av_ds = cp_av.groupby('video_id').apply(lambda x: x.iloc[::downsample_factor]).reset_index(drop=True) 
    # => the 'video_id' column would be excluded from the output dataframe.


# %%'

cp_av_ds.shape
    # Out[21]: (196341, 7)

cp_av_ds[:4]
    # Out[22]: 
    #      video_id   time sample_ID    x    y   x_smooth   y_smooth
    # 0  pod_1_ZC04  pod_1      ZC04  763  420        NaN        NaN
    # 1  pod_1_ZC04  pod_1      ZC04  819  391 818.800000 391.000000
    # 2  pod_1_ZC04  pod_1      ZC04  856  368 858.400000 365.400000
    # 3  pod_1_ZC04  pod_1      ZC04  897  344 896.600000 344.600000

# %%'

# --- 4. Calculate Differences and Distance on Processed Data ---
# .diff() must also be grouped to prevent calculating a large jump between the last point of one video
# and the first point of the next video.
cp_av_ds['dx'] = cp_av_ds.groupby('video_id')['x_smooth'].diff()
cp_av_ds['dy'] = cp_av_ds.groupby('video_id')['y_smooth'].diff()

# Calculate the distance using the Pythagorean theorem, just like in your function.
cp_av_ds['distance'] = np.sqrt(cp_av_ds['dx']**2 + cp_av_ds['dy']**2) 

# %%'

cp_av_ds.shape
    # Out[17]: (196341, 10)

cp_av_ds[:8]
    # Out[19]: 
    #      video_id   time sample_ID    x    y   x_smooth   y_smooth        dx  \
    # 0  pod_1_ZC04  pod_1      ZC04  763  420        NaN        NaN       NaN   
    # 1  pod_1_ZC04  pod_1      ZC04  819  391 818.800000 391.000000       NaN   
    # 2  pod_1_ZC04  pod_1      ZC04  856  368 858.400000 365.400000 39.600000   
    # 3  pod_1_ZC04  pod_1      ZC04  897  344 896.600000 344.600000 38.200000   
    # 4  pod_1_ZC04  pod_1      ZC04  917  331 917.000000 331.000000 20.400000   
    # 5  pod_1_ZC04  pod_1      ZC04  928  324 928.200000 323.800000 11.200000   
    # 6  pod_1_ZC04  pod_1      ZC04  936  329 936.400000 328.800000  8.200000   
    # 7  pod_1_ZC04  pod_1      ZC04  941  328 941.000000 328.000000  4.600000   
    
    #           dy  distance  
    # 0        NaN       NaN  
    # 1        NaN       NaN  
    # 2 -25.600000 47.154215  
    # 3 -20.800000 43.495747  
    # 4 -13.600000 24.517749  
    # 5  -7.200000 13.314654  
    # 6   5.000000  9.604166  
    # 7  -0.800000  4.669047  

# %%'

cp_av_ds.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\cp_av_ds.pkl' )

# %%'

# --- 5. Calculate Total Distance Traveled Per Video ---
print("Aggregating total distance per video...")
# Sum the distances for each video group.
tdt = cp_av_ds.groupby([ 'time' , 'sample_ID' ])['distance'].sum().reset_index()

tdt.shape
    # Out[33]: (111, 3)

tdt[:4]
    # Out[31]: 
    #     time sample_ID     distance
    # 0  pod_1      ZC04  9637.413800
    # 1  pod_1      ZC05 26730.860213
    # 2  pod_1      ZC06 18499.849050
    # 3  pod_1      ZC07  8868.898625

tdt.rename( columns={'distance' : 'tdt_pixel'}, inplace=True )

# %%'

tdt.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\tdt.pkl' )

# %%'

# to add the height data to the tdt data :
    
image_height_analysis_opencv_2 = image_height_analysis_opencv.copy()

# 1. Remove the '.png' extension from the file names
# .str.removesuffix() is perfect for this
video_id_col = image_height_analysis_opencv_2['file_name'].str.removesuffix('.png')

type(video_id_col)
    # Out[40]: pandas.core.series.Series

video_id_col[:4]
    # Out[41]: 
    # 0    pod_1_ZC14
    # 1    pod_3_ZC14
    # 2    pod_4_ZC14
    # 3    pod_7_ZC14
    # Name: file_name, dtype: object


# 2. Split the cleaned name into 'time' and 'sample_ID'
# We use the same .rsplit() method as before to split on the last underscore
image_height_analysis_opencv_2[['time', 'sample_ID']] = video_id_col.str.rsplit('_', n=1, expand=True)

image_height_analysis_opencv_2[:4]
    #                                          folder_path   time sample_ID  
    # 0  F:\OneDrive - Uniklinik RWTH Aachen\VISION\tra...  pod_1      ZC14  
    # 1  F:\OneDrive - Uniklinik RWTH Aachen\VISION\tra...  pod_3      ZC14  
    # 2  F:\OneDrive - Uniklinik RWTH Aachen\VISION\tra...  pod_4      ZC14  
    # 3  F:\OneDrive - Uniklinik RWTH Aachen\VISION\tra...  pod_7      ZC14  

# %%'

# Merge 'tdt' and the prepared 'height_df'
# The 'on' parameter tells Pandas to match rows using both 'time' and 'sample_ID'
tdt_height = pd.merge( 
                        tdt , 
                        image_height_analysis_opencv_2 , 
                        on=[ 'time' , 'sample_ID' ] 
)

# Drop the original file and path columns if you no longer need them
tdt_height_2 = tdt_height.drop(columns=['folder_path'])


tdt_height_2.shape
    # Out[52]: (111, 5)

tdt_height_2[:4]
    # Out[53]: 
    #     time sample_ID    tdt_pixel       file_name  sample_png_height
    # 0  pod_1      ZC04  9637.413800  pod_1_ZC04.png                564
    # 1  pod_1      ZC05 26730.860213  pod_1_ZC05.png                564
    # 2  pod_1      ZC06 18499.849050  pod_1_ZC06.png                564
    # 3  pod_1      ZC07  8868.898625  pod_1_ZC07.png                564


# converting pixel to meter.
# for each video, there is a slight difference in height !
# 14 tiles = 1.75 m
# The formula is applied row by row automatically by pandas.
tdt_height_2['tdt_meter'] = tdt_height_2['tdt_pixel'] * (1.75 / tdt_height_2['sample_png_height'])

tdt_height_2.shape
# Out[56]: ](111, 6)

tdt_height_2[:4]
    # Out[57]: 
    #     time sample_ID    tdt_pixel       file_name  sample_png_height  tdt_meter
    # 0  pod_1      ZC04  9637.413800  pod_1_ZC04.png                564  29.903323
    # 1  pod_1      ZC05 26730.860213  pod_1_ZC05.png                564  82.941499
    # 2  pod_1      ZC06 18499.849050  pod_1_ZC06.png                564  57.402014
    # 3  pod_1      ZC07  8868.898625  pod_1_ZC07.png                564  27.518746

# %%'

tdt_height_2.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\tdt_height_2.pkl' )

tdt_height_2 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\tdt_height_2.pkl' )

# %%'

# now the groupings of treatments must be added.
# first, wait, getting the groupings from the original file.

# the non-standard 'ZC6' entry was renamed to 'ZC06' via Excel itself.
overview_2 = pd.read_excel( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\overview_2.xlsx' , header=[0,1] )  # , index_col=0 


# bg : blood gass
df_treatment_groups = overview_2.iloc[ : , [ 0,1 ] ]

df_treatment_groups[:4]
    # Out[13]: 
    #           Sample ID:          Treatment
    #   Unnamed: 0_level_1 Unnamed: 1_level_1
    # 0               ZC04            DBD-HTK
    # 1               ZC05         DBD-Ecosol
    # 2               ZC06            DBD-HTK
    # 3               ZC07         DBD-Ecosol

new_header = ['sample_ID', 'treatment' ]

# assigining the newheaders.
df_treatment_groups.columns = new_header

# the number of rows here is less than 82 !
    # see below : the end of the excel file has empty rows assigned as NaN here.
df_treatment_groups.shape
    # Out[17]: (82, 2)

df_treatment_groups[:4]
    # Out[16]: 
    #   sample_ID   treatment
    # 0      ZC04     DBD-HTK
    # 1      ZC05  DBD-Ecosol
    # 2      ZC06     DBD-HTK
    # 3      ZC07  DBD-Ecosol

df_treatment_groups[-4:]
    # Out[34]: 
    #    sample_ID treatment
    # 78       NaN       NaN
    # 79       NaN       NaN
    # 80       NaN       NaN
    # 81       NaN       NaN

# %%' 

# didn't work because of duplicates in df_treatment_groups !

            # Perform a left merge
            tdt_height_group = pd.merge(
                        left=tdt_height_2,
                        right=df_treatment_groups[['sample_ID', 'treatment']], # Select only the columns you need from the right table.
                        on='sample_ID',
                        how='left'
            )
            
            tdt_height_group.shape
                # Out[19]: (115, 7)
            
            
            tdt_height_group[:4]
                # Out[21]: 
                #     time sample_ID    tdt_pixel       file_name  sample_png_height  tdt_meter  \
                # 0  pod_1      ZC04  9637.413800  pod_1_ZC04.png                564  29.903323   
                # 1  pod_1      ZC05 26730.860213  pod_1_ZC05.png                564  82.941499   
                # 2  pod_1      ZC06 18499.849050  pod_1_ZC06.png                564  57.402014   
                # 3  pod_1      ZC06 18499.849050  pod_1_ZC06.png                564  57.402014   
                
                #     treatment  
                # 0     DBD-HTK  
                # 1  DBD-Ecosol  
                # 2     DBD-HTK  
                # 3     DBD-HTK  

# %%'

# Check for duplicates in the key column of the right dataframe
id_counts = df_treatment_groups['sample_ID'].value_counts()

id_counts
    # Out[23]: 
    # sample_ID
    # ZC06    2
    # ZC04    1
    # ZC05    1
    # ZC07    1
    # ZC08    1
    #        ..
    # ZC65    1
    # ZC66    1
    # ZC67    1
    # ZC68    1
    # ZC69    1
    # Name: count, Length: 65, dtype: int64

# there are duplicates !
print(id_counts[id_counts > 1])
    # sample_ID
    # ZC06    2
    # Name: count, dtype: int64

# %%'

# exploring the duplicate entry.

mask_dup = df_treatment_groups['sample_ID'] == 'ZC06'

dup = df_treatment_groups[ mask_dup ]

dup
    # Out[25]: 
    #   sample_ID treatment
    # 2      ZC06   DBD-HTK
    # 8      ZC06   DBD-HTK

# %%'

# Create a dataframe with only one entry per sample_ID
df_treatment_groups_unique = df_treatment_groups.drop_duplicates(subset=['sample_ID'])

# the number of rows are much less than the original becasue of emty rows (NaN values ) at the end of the excel sheet !
df_treatment_groups_unique.shape
    # Out[27]: (66, 2)

df_treatment_groups.shape
    # Out[28]: (82, 2)

# %%'

# --- Best Practice: Clean the DataFrame ---

# 1. Drop any row where 'sample_ID' is missing (NaN)
df_treatment_groups_clean = df_treatment_groups.dropna(subset=['sample_ID'])

df_treatment_groups_clean.shape
    # Out[36]: (66, 2)

# 2. Now, with a clean dataset, safely drop the actual duplicates like 'ZC06'
df_treatment_groups_clean_unique = df_treatment_groups_clean.drop_duplicates(subset=['sample_ID'])

df_treatment_groups_clean_unique.shape
    # Out[38]: (65, 2)

df_treatment_groups_clean_unique['treatment'].unique()
    # Out[46]: 
    # array(['DBD-HTK', 'DBD-Ecosol', '-', 'DCD-HTK', 'DCD-Ecoflow', 'TBB',
    #        'DBD-Ecoflow', 'DCD-Ecosol', 'NMP'], dtype=object)

df_treatment_groups_clean_unique.shape
    # Out[52]: (65, 2)

# %%'

# possible unnecessary, as there will be no drop-out !

df_treatment_groups_clean_unique_2 = df_treatment_groups_clean_unique.dropna(subset=['treatment'])

df_treatment_groups_clean_unique_2.shape
    # Out[57]: (65, 2)

# %%'

# Perform a left merge
tdt_height_group = pd.merge(
            left=tdt_height_2,
            right=df_treatment_groups_clean_unique[['sample_ID', 'treatment']], # 1 : bottom
            on='sample_ID',
            how='left'
)
# 1 : # Select only the columns you need from the right table.

tdt_height_group.shape
    # Out[40]: (111, 7)

tdt_height_group.columns
    # Out[41]: 
    # Index(['time', 'sample_ID', 'tdt_pixel', 'file_name', 'sample_png_height',
    #        'tdt_meter', 'treatment'],
    #       dtype='object')


tdt_height_group[:4]
    # Out[42]: 
    #     time sample_ID    tdt_pixel       file_name  sample_png_height  tdt_meter  \
    # 0  pod_1      ZC04  9637.413800  pod_1_ZC04.png                564  29.903323   
    # 1  pod_1      ZC05 26730.860213  pod_1_ZC05.png                564  82.941499   
    # 2  pod_1      ZC06 18499.849050  pod_1_ZC06.png                564  57.402014   
    # 3  pod_1      ZC07  8868.898625  pod_1_ZC07.png                564  27.518746   
    
    #     treatment  
    # 0     DBD-HTK  
    # 1  DBD-Ecosol  
    # 2     DBD-HTK  
    # 3  DBD-Ecosol  

# %%'

tdt_height_group.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\tdt_height_group.pkl' )

# %%'

tdt_height_group['treatment'].unique()
    # Out[47]: array(['DBD-HTK', 'DBD-Ecosol', 'DCD-HTK', 'NMP', nan, '-'], dtype=object)

# %%'

# after plotting, in the legend of treatments : - : emerged as a category !
# Here, I want to get more info about them !

mask_unknown = tdt_height_group['treatment'].isin( [ np.nan, '-' ] )
tdt_height_group_unknown = tdt_height_group[ mask_unknown ]
tdt_height_group_unknown.shape
    # Out[60]: (3, 7)

# %%'

tdt_height_group_unknown
    # Out[61]: 
    #          time sample_ID    tdt_pixel           file_name  sample_png_height  \
    # 92  retrain_2      ZC12 27527.173427  retrain_2_ZC12.png                571   
    # 93  retrain_2      ZC13 47172.606809  retrain_2_ZC13.png                575   
    # 97  retrain_2      ZC18 59333.557997  retrain_2_ZC18.png                574   
    
    #     tdt_meter treatment  
    # 92  84.365243       NaN  
    # 93 143.568803         -  
    # 97 180.894994         -  


# %%'

# Create a boolean mask to identify the rows to KEEP.
# A row is kept if its 'treatment' value is NOT NaN AND it is NOT equal to '-'.
mask_to_keep = (tdt_height_group['treatment'].notna()) & (tdt_height_group['treatment'] != '-')

# Apply the mask to your DataFrame to get the cleaned version.
tdt_height_group_2 = tdt_height_group[mask_to_keep]

# %%'

# 3 entries deleted, as expected.
tdt_height_group_2.shape
    # Out[63]: (108, 7)

# %%'

# Verify the result by checking the unique values and their counts.
tdt_height_group_2.head()
    # Out[67]: 
    #     time sample_ID    tdt_pixel       file_name  sample_png_height  tdt_meter  \
    # 0  pod_1      ZC04  9637.413800  pod_1_ZC04.png                564  29.903323   
    # 1  pod_1      ZC05 26730.860213  pod_1_ZC05.png                564  82.941499   
    # 2  pod_1      ZC06 18499.849050  pod_1_ZC06.png                564  57.402014   
    # 3  pod_1      ZC07  8868.898625  pod_1_ZC07.png                564  27.518746   
    # 4  pod_1      ZC08 17381.271351  pod_1_ZC08.png                564  53.931250   
    
    #     treatment  
    # 0     DBD-HTK  
    # 1  DBD-Ecosol  
    # 2     DBD-HTK  
    # 3  DBD-Ecosol  
    # 4     DBD-HTK 


tdt_height_group_2['treatment'].value_counts()
    # Out[65]: 
    # treatment
    # NMP           37
    # DBD-Ecosol    30
    # DCD-HTK       23
    # DBD-HTK       18
    # Name: count, dtype: int64


tdt_height_group_2['time'].unique()
    # Out[69]: array(['pod_1', 'pod_3', 'pod_4', 'pod_7', 'retrain_2'], dtype=object)

# %%'

# order the categories to be ready for plotting.
treatment_order = [ 'DBD-HTK', 'DBD-Ecosol', 'DCD-HTK', 'NMP' ]
tdt_height_group_2['treatment'] = pd.Categorical(
                                            tdt_height_group_2['treatment'],
                                            categories=treatment_order,
                                            ordered=True
)

# %%'

time_order = [ 'retrain_2' , 'pod_1', 'pod_3', 'pod_4', 'pod_7' ]
tdt_height_group_2['time'] = pd.Categorical(
                                            tdt_height_group_2['time'],
                                            categories=time_order,
                                            ordered=True
)

# %%'

# this is because of a previous mistake !
tdt_height_group_2 = tdt_height_group_2.drop(columns=['metric'])

tdt_height_group_2.columns
Out[77]: 
Index(['time', 'sample_ID', 'tdt_pixel', 'file_name', 'sample_png_height',
       'tdt_meter', 'treatment'],
      dtype='object')

# %%'

tdt_height_group_2.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\tdt_height_group_2.pkl' )

tdt_height_group_2 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\tdt_height_group_2.pkl' )


# %%'

tdt_height_group_2.columns
    # Out[10]: 
    # Index(['time', 'sample_ID', 'tdt_pixel', 'file_name', 'sample_png_height',
    #        'tdt_meter', 'treatment'],
    #       dtype='object')

# %%'

# Perform a left merge
cp_av_ds_3 = pd.merge(
                        left=cp_av_ds_2,
                        right=df_aggregate[[ 'video_id' , 'sample_png_height' ]], # 1 : bottom
                        on='video_id',
                        how='left'
)
# 1 : # Select only the columns you need from the right table.
    # this includes the common ( on ) column !

cp_av_ds_3[:4]
    # Out[87]: 
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
    
    #                                           inner_roi  sample_png_height  
    # 0  [[419, 299], [893, 299], [893, 767], [419, 767]]         564.000000  
    # 1  [[419, 299], [893, 299], [893, 767], [419, 767]]         564.000000  
    # 2  [[419, 299], [893, 299], [893, 767], [419, 767]]         564.000000  
    # 3  [[419, 299], [893, 299], [893, 767], [419, 767]]         564.000000  

# %%'

# 1/3 : 1/3 s : downsample data by factor 10 : original data : 30-frames / second.
cp_av_ds_3['velocity_meter_s'] = ( cp_av_ds_3['distance'] * (1.75 / cp_av_ds_3['sample_png_height']) ) / ( 1/3 )

cp_av_ds_3['diff_velocity_meter_s'] = cp_av_ds_3.groupby('video_id')['velocity_meter_s'].diff()

cp_av_ds_3['acceleration_meter_s2'] = cp_av_ds_3['diff_velocity_meter_s'] / ( 1/3 )

# %%'

cp_av_ds_3.shape
    # Out[93]: (196341, 19)

cp_av_ds_3.columns
    # Out[94]: 
    # Index(['video_id', 'time', 'sample_ID', 'x', 'y', 'x_smooth', 'y_smooth', 'dx',
    #        'dy', 'distance', 'location', 'zone', 'outer_roi', 'inner_roi',
    #        'sample_png_height', 'diff_distance_pixel', 'velocity_meter_s',
    #        'diff_velocity_meter_s', 'acceleration_meter_s2'],
    #       dtype='object')

cp_av_ds_3[:4]
    # Out[95]: 
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
    # 2                  NaN               NaN                    NaN   
    # 3            -3.658468         -0.034055                    NaN   
    
    #    acceleration_meter_s2  
    # 0                    NaN  
    # 1                    NaN  
    # 2                    NaN  
    # 3                    NaN  


cp_av_ds_3.iloc[ 10:14 , -4: ]
    # Out[98]: 
    #     diff_distance_pixel  velocity_meter_s  diff_velocity_meter_s  \
    # 10            -0.821854         -0.007650              -0.007650   
    # 11             0.821854          0.007650               0.015300   
    # 12            -0.821854         -0.007650              -0.015300   
    # 13            -1.214214         -0.011303              -0.003652   
    
    #     acceleration_meter_s2  
    # 10              -0.022951  
    # 11               0.045901  
    # 12              -0.045901  
    # 13              -0.010957  

# %%'

cp_av_ds_3.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\cp_av_ds_3.pkl' )

# %%'

# Use .groupby() to group the data by each unique 'video_id'.
# Then, use .agg() to specify the calculations for your columns of interest.
kinematics_summary = cp_av_ds_3.groupby('video_id').agg(
                                                        # For the velocity column, calculate both mean and max
                                                        velocity_mean =('velocity_meter_s', 'mean'),
                                                        velocity_max =('velocity_meter_s', 'max'),
                                                        
                                                        # For the acceleration column, also calculate mean and max
                                                        acceleration_mean =('acceleration_meter_s2', 'mean'),
                                                        acceleration_max =('acceleration_meter_s2', 'max')
).reset_index() # .reset_index() converts 'video_id' from an index back into a column.


# %%'

kinematics_summary[:4]
    # Out[105]: 
    #      video_id  velocity_mean  velocity_max  acceleration_mean  \
    # 0  pod_1_ZC04       0.049894      0.890042          -0.000662   
    # 1  pod_1_ZC05       0.138390      1.698155          -0.000092   
    # 2  pod_1_ZC06       0.095776      0.903762          -0.000186   
    # 3  pod_1_ZC07       0.045941      0.416664           0.000096   
    
    #    acceleration_max  
    # 0          1.260429  
    # 1          1.555279  
    # 2          1.045949  
    # 3          0.568699 

kinematics_summary.shape
    # Out[107]: (111, 5)

kinematics_summary.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\kinematics_summary.pkl' )

# %%'

cp_av_ds_3['distance'].min()
    # Out[102]: 0.0

# %%'

# Perform a left merge
df_aggregate_track = pd.merge(
                                left=df_aggregate,
                                right=kinematics_summary, # 1 : bottom
                                on='video_id',
                                how='left'
)
# 1 : # Select only the columns you need from the right table.

# %%'

df_aggregate_track.shape
    # Out[110]: (108, 13)

df_aggregate_track.columns
    # Out[111]: 
    # Index(['time', 'sample_ID', 'tdt_pixel', 'file_name', 'sample_png_height',
    #        'tdt_meter', 'treatment', 'video_id', 'inner_zone_percentage',
    #        'velocity_mean', 'velocity_max', 'acceleration_mean',
    #        'acceleration_max'],
    #       dtype='object')

# %%'

df_aggregate_track.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_aggregate_track.pkl' )

# %% removing the video_ids with low number of frames.

# removing the video_ids with low number of frames.

frame_counts = cp_av_ds_3['video_id'].value_counts()

frame_counts.shape
    # Out[53]: (111,)

frame_counts[:4]
    # Out[54]: 
    # video_id
    # pod_1_ZC04    1800
    # pod_4_ZC67    1800
    # pod_7_ZC20    1800
    # pod_7_ZC19    1800
    # Name: count, dtype: int64

frame_counts.min()
    # Out[55]: 16

frame_counts.max()
    # Out[56]: 1800

# Sort ascending and get first 4
frame_counts.sort_values(ascending=True)[:25]
    # Out[64]: 
    # video_id
    # pod_7_ZC66          16
    # pod_4_ZC20         163
    # pod_3_ZC17        1789
    # pod_1_ZC60        1794
    # pod_7_ZC68        1797
    # pod_1_ZC69        1797
    # retrain_2_ZC65    1799
    # retrain_2_ZC64    1799
    # retrain_2_ZC63    1799
    # pod_3_ZC68        1799
    # retrain_2_ZC61    1799
    # pod_1_ZC63        1799
    # pod_4_ZC68        1799
    # pod_3_ZC65        1799
    # pod_1_ZC62        1799
    # pod_1_ZC65        1799
    # retrain_2_ZC67    1799
    # pod_3_ZC61        1799
    # pod_4_ZC63        1799
    # pod_7_ZC63        1799
    # pod_3_ZC63        1799
    # pod_1_ZC09        1800
    # pod_1_ZC10        1800
    # pod_1_ZC11        1800
    # pod_1_ZC14        1800
    # Name: count, dtype: int64

frame_counts.sort_values(ascending=False)[:4]
    # Out[58]: 
    # video_id
    # pod_1_ZC04    1800
    # pod_1_ZC11    1800
    # pod_1_ZC15    1800
    # pod_1_ZC17    1800
    # Name: count, dtype: int64

cp_av_ds_3.shape
    # Out[66]: (196341, 21)

# %% check if these video_ids exist in the aggregate datafram.

# check if these video_ids exist in the aggregate datafram.

# List of the video IDs you want to check for
ids_to_check = ['pod_7_ZC66', 'pod_4_ZC20']

# For fast lookups, convert the 'video_id' column to a Python set
unique_video_ids = set(df_aggregate_track_4['video_id'])

print("--- Checking for Video ID existence ---")

# Loop through your list and check if each ID is in the set
for video_id in ids_to_check:
    is_present = video_id in unique_video_ids
    print(f"Is '{video_id}' present in the 'video_id' column? {is_present}")

# %%'
# %% remove the abnormal videos.

# remove the abnormal videos.

# 1. Define the list of video_ids you want to remove
ids_to_remove = ['pod_7_ZC66', 'pod_4_ZC20']

# %%'

# The '~' operator inverts the boolean mask, so we are KEEPING all rows
# where the 'video_id' is NOT IN our list.
mask_remove_original_df = ~cp_av_ds_3['video_id'].isin(ids_to_remove)
cp_av_ds_4 = cp_av_ds_3[ mask_remove_original_df ]

cp_av_ds_4.shape
    # Out[68]: (196162, 21)

cp_av_ds_4.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\cp_av_ds_4.pkl' )

# %%'

df_aggregate_track_4.shape
    # Out[69]: (108, 21)

# Apply the same logic to the aggregate dataframe
mask_remove_aggregate_df = ~df_aggregate_track_4['video_id'].isin(ids_to_remove)
df_aggregate_track_5 = df_aggregate_track_4[ mask_remove_aggregate_df ]

df_aggregate_track_5.shape
    # Out[70]: (106, 21)

# %%'
# %%'

frame_counts = cp_av_ds_4['video_id'].value_counts()

frame_counts.shape
    # Out[72]: (109,)

frame_counts[:4]
    # Out[73]: 
    # video_id
    # pod_1_ZC04    1800
    # pod_4_ZC67    1800
    # pod_7_ZC20    1800
    # pod_7_ZC19    1800
    # # Name: count, dtype: int64

# %%'

# Create a new column 'frame_count' in your aggregate DataFrame.
# The .map() method uses the 'video_id' from each row to look up the
# corresponding value in the 'frame_counts' Series.
# tnf : total number of frames : per video.
df_aggregate_track_5['tnf'] = df_aggregate_track_5['video_id'].map(frame_counts)

# %%'

# velocity_mean_r_ms : 
    # r : ratio : calculated via division of total distance traveled during the whole video / the time of the whole video in 's'.
    # this is in contrast to 'velocity_mean', where it is the mean of velocity from inividiual steps.
    # hence, this should be more accurate !
    # mean velocity in m/s : 
    # note, the data here is downsampled by factor-10, hence division by 3 in the last part of the line.
df_aggregate_track_5['velocity_mean_r_ms'] = df_aggregate_track_5['tdt_meter'] / ( df_aggregate_track_5['tnf'] / 3 )

# %%' comparison

# comparing the 2 types of velocity estimations.
    # very similar !
df_aggregate_track_5[[ 'velocity_mean_r_ms' , 'velocity_mean' ]][:4]
    # Out[76]: 
    #    velocity_mean_r_ms  velocity_mean
    # 0            0.049839       0.049894
    # 1            0.138236       0.138390
    # 2            0.095670       0.095776
    # 3            0.045865       0.045941


# %%' rename a treatment entry

rename_map = {
    'DBD-Ecosol': 'DBD-Omnisol'
}

# Apply the replacement to the 'treatment' column
# This finds 'DBD-Ecosol' and replaces it with 'DBD-Omnisol'
df_aggregate_track_5['treatment'] = df_aggregate_track_5['treatment'].replace(rename_map)

# note : cp_av_ds_4 : does not have any 'treatment' column. Hence, no need for renaming it !

# %%'

df_aggregate_track_5.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_aggregate_track_5.pkl' )

# %%'
# %%' acceleration spitting

# as in a bound area, positive & negaive accelerations balance each-other  : mean of the acceleration is almost 0.
    # the proper way of evaluating acceleration is dividing it to '+' & '-' values.

# --- 1. Define your custom aggregation functions ---

def mean_positive(series):
    """Calculates the mean of only the positive values."""
    return series[series > 0].mean()

def max_positive(series):
    """Calculates the max of only the positive values."""
    # Check for empty series to avoid warnings
    if series[series > 0].empty:
        return np.nan
    return series[series > 0].max()

def mean_negative(series):
    """Calculates the mean of only the negative values."""
    return series[series < 0].mean()

def min_negative(series):
    """Calculates the min (most negative value) of only the negative values."""
    # Check for empty series to avoid warnings
    if series[series < 0].empty:
        return np.nan
    return series[series < 0].min()

# %%'

# cp_av_ds_5 : last modified : =>  load_track.py

# --- 2. Apply all functions in one groupby.agg() call ---

# Aggregating acceleration metrics per 'video_id'

# Group by 'video_id' as requested
acceleration_summary_by_sample = cp_av_ds_5.groupby('video_id').agg(
                    # Column to aggregate on: 'acceleration_meter_s2'
                    # New column name   = (Column to use ,          Function to apply)
                    accel_pos_mean_ms2  = ('acceleration_meter_s2', mean_positive ),
                    accel_pos_max_ms2   = ('acceleration_meter_s2', max_positive ),
                    accel_neg_mean_ms2  = ('acceleration_meter_s2', mean_negative ),
                    accel_neg_min_ms2   = ('acceleration_meter_s2', min_negative )
).reset_index() # .reset_index() converts 'video_id' from an index to a column.

# %%'

acceleration_summary_by_sample[:4]
    # Out[70]: 
    #      video_id  accel_pos_mean_ms2  accel_pos_max_ms2  accel_neg_mean_ms2  \
    # 0  pod_1_ZC04            0.068233           1.260429           -0.066345   
    # 1  pod_1_ZC05            0.157006           1.555279           -0.146170   
    # 2  pod_1_ZC06            0.121301           1.045949           -0.115078   
    # 3  pod_1_ZC07            0.074588           0.568699           -0.076213   
    
    #    accel_neg_min_ms2  
    # 0          -0.791237  
    # 1          -1.610288  
    # 2          -0.955969  
    # 3          -0.662565  

# %%'

# pre-check
df_aggregate_track_6.shape
    # Out[73]: (103, 23)

# %%'

# Perform a left merge
# 'df_aggregate_track_6' is the left DataFrame (all rows will be kept)
# 'acceleration_summary_by_sample' is the right DataFrame
df_aggregate_track_7 = pd.merge(
                                df_aggregate_track_6, 
                                acceleration_summary_by_sample, 
                                on='video_id', 
                                how='left'
)


# %%'

# --- Verify the result ---

df_aggregate_track_7.shape
    # Out[75]: (103, 27)

list( df_aggregate_track_7.columns )
    # Out[11]: 
    # ['time',
    #  'sample_ID',
    #  'tdt_pixel',
    #  'file_name',
    #  'sample_png_height',
    #  'tdt_meter',
    #  'treatment',
    #  'video_id',
    #  'inner_zone_percentage',
    #  'velocity_mean',
    #  'velocity_max',
    #  'acceleration_mean',
    #  'acceleration_max',
    #  'nocw',
    #  'pocw',
    #  'shannon_entropy',
    #  'max_entropy',
    #  'uniformity_index',
    #  'inner_roi',
    #  'outer_roi',
    #  'bbox_roi',
    #  'tnf',
    #  'velocity_mean_r_ms',
    #  'accel_pos_mean_ms2',
    #  'accel_pos_max_ms2',
    #  'accel_neg_mean_ms2',
    #  'accel_neg_min_ms2']

# the old velocity calculations are not needed.
df_aggregate_track_7.drop( columns=[ 'acceleration_mean' , 'acceleration_max' ] , inplace=True )

# %% remove the 4th bad-processed video.

# the 3 main bad-processed videos are already removed from this video ( remove_bad_processed.py ).
# however, the one remaining with jittering bounding-box size, that makes trouble in maximum velocity & maxium acceleration has not been removed.
    # here, this video is removed :

mask_keep = df_aggregate_track_7['video_id'] != 'pod_3_ZC22'
df_aggregate_track_8 = df_aggregate_track_7[ mask_keep ]
df_aggregate_track_8.shape
    # Out[16]: (102, 25)

# %%'

df_aggregate_track_8.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_aggregate_track_8.pkl' )


# %%'
# %%' tidy

# tidy format.

# %%'

# List of the identifier and grouping columns you want to keep
id_columns = ['video_id', 'sample_ID', 'time', 'treatment']

# List of the measurement columns you want to analyze
readout_parameters = [
                        'tdt_meter', 
                        'velocity_mean', 
                        'velocity_mean_r_ms' ,
                        'velocity_max',
                        
                        'accel_pos_mean_ms2',
                        'accel_pos_max_ms2',
                        'accel_neg_mean_ms2',
                        'accel_neg_min_ms2' ,
                         
                        'inner_zone_percentage',
                        'nocw',  # Note: I removed the extra space from your column name list
                        'uniformity_index'
]

# Create the new, focused DataFrame
df_subset = df_aggregate_track_8[ id_columns + readout_parameters ]

# %%'

# Melt the DataFrame to convert it to a long format
df_track_tidy = pd.melt(
                        df_subset,
                        id_vars=id_columns,              # Columns to keep as they are (identifiers)
                        value_vars=readout_parameters,   # Columns to "unpivot" into rows
                        var_name='metric',               # Name of the new column for the measurement type
                        value_name='value'               # Name of the new column for the measurement value
)

# %%'

df_track_tidy.shape
    # Out[12]: (1122, 6)

df_track_tidy.columns
    # Out[13]: Index(['video_id', 'sample_ID', 'time', 'treatment', 'metric', 'value'], dtype='object')

df_track_tidy[:4]
    # Out[14]: 
    #      video_id sample_ID   time    treatment     metric     value
    # 0  pod_1_ZC04      ZC04  pod_1      DBD-HTK  tdt_meter 29.903323
    # 1  pod_1_ZC05      ZC05  pod_1  DBD-Omnisol  tdt_meter 82.941499
    # 2  pod_1_ZC06      ZC06  pod_1      DBD-HTK  tdt_meter 57.402014
    # 3  pod_1_ZC07      ZC07  pod_1  DBD-Omnisol  tdt_meter 27.518746

# %%' rename

# # Create a dictionary to define the mapping
# rename_map = {
#     'DBD-Ecosol': 'DBD-Omnisol'
# }

# # Apply the replacement to the 'treatment' column
# # This finds 'DBD-Ecosol' and replaces it with 'DBD-Omnisol'
# df_track_tidy['treatment'] = df_track_tidy['treatment'].replace(rename_map)
#     # c:\code\vision\track\general_track.py:65: FutureWarning: 
#     #     The behavior of Series.replace (and DataFrame.replace) with CategoricalDtype is deprecated. 
#     #     In a future version, replace will only be used for cases that preserve the categories. 
#     #     To change the categories, use ser.cat.rename_categories instead.
#     #   df_track_tidy['treatment'] = df_track_tidy['treatment'].replace(rename_map)

# %%'
# %%'

df_track_tidy['treatment'].unique()
    # Out[15]: 
    # ['DBD-HTK', 'DBD-Omnisol', 'DCD-HTK', 'NMP']
    # Categories (4, object): ['DBD-HTK' < 'DBD-Omnisol' < 'DCD-HTK' < 'NMP']

# %%'

list( df_track_tidy['metric'].unique() )
    # Out[17]: 
    # ['tdt_meter',
    #  'velocity_mean',
    #  'velocity_mean_r_ms',
    #  'velocity_max',
    #  'accel_pos_mean_ms2',
    #  'accel_pos_max_ms2',
    #  'accel_neg_mean_ms2',
    #  'accel_neg_min_ms2',
    #  'inner_zone_percentage',
    #  'nocw',
    #  'uniformity_index']


# %%' split the dataframe.

# this is to make them ready for creating separate figures.
    # each figure with subplots corresponding to the selected metrics.

# %%' roam

# List of metrics for the "roaming" DataFrame
roaming_metrics = [
                    'inner_zone_percentage', 
                    'nocw', 
                    'uniformity_index'
]

mask_roam = df_track_tidy['metric'].isin(roaming_metrics)
df_track_tidy_roam = df_track_tidy[ mask_roam ].copy()

df_track_tidy_roam.shape
    # Out[19]: (306, 6)

# %% kinematic
# %%' distance & velocity kinematic

# List of metrics for the "kinematic" DataFrame
# (This is all remaining metrics except 'velocity_mean')
# dv : distance & velocity
dv_metrics = [
                    'tdt_meter',
                    'velocity_mean_r_ms',
                    'velocity_max'
]

mask_dv = df_track_tidy['metric'].isin( dv_metrics )
df_track_tidy_dv = df_track_tidy[ mask_dv ].copy()

df_track_tidy_dv.shape
    # Out[21]: (306, 6)

# %% acceleration

acceleration_metrics = [
             'accel_pos_mean_ms2',
             'accel_pos_max_ms2',
             'accel_neg_mean_ms2',
             'accel_neg_min_ms2'
]

mask_acceleration = df_track_tidy['metric'].isin( acceleration_metrics )
df_track_tidy_acceleration = df_track_tidy[ mask_acceleration ].copy()

df_track_tidy_acceleration.shape
    # Out[22]: (408, 6)


# %%'

df_track_tidy_roam['metric'].unique()
    # Out[16]: ]array(['inner_zone_percentage', 'nocw', 'uniformity_index'], dtype=object)

df_track_tidy_kinematic['metric'].unique()
    # Out[17]: 
    # array(['tdt_meter', 'velocity_mean_r_ms', 'velocity_max',
    #        'acceleration_mean', 'acceleration_max'], dtype=object)

# %%' order _ roam

roaming_metrics = [
                    'inner_zone_percentage', 
                    'nocw', 
                    'uniformity_index'
]

df_track_tidy_roam['metric'] = pd.Categorical(
                                        df_track_tidy_roam['metric'],
                                        categories= roaming_metrics,
                                        ordered=True
)


df_track_tidy_roam['metric'].unique()
    # Out[23]: 
    # ['inner_zone_percentage', 'nocw', 'uniformity_index']
    # Categories (3, object): ['inner_zone_percentage' < 'nocw' < 'uniformity_index']

# %%' order _ dv

dv_metrics = [
                    'velocity_mean_r_ms',
                    'velocity_max',
                    'tdt_meter'
]

df_track_tidy_dv['metric'] = pd.Categorical(
                                        df_track_tidy_dv['metric'],
                                        categories= dv_metrics ,
                                        ordered=True
)


df_track_tidy_dv['metric'].unique()
    # Out[24]: 
    # ['tdt_meter', 'velocity_mean_r_ms', 'velocity_max']
    # Categories (3, object): ['velocity_mean_r_ms' < 'velocity_max' < 'tdt_meter']

# %% order _ acceleration

acceleration_metrics = [
                         'accel_pos_mean_ms2',
                         'accel_pos_max_ms2',
                         'accel_neg_mean_ms2',
                         'accel_neg_min_ms2'
]

df_track_tidy_acceleration['metric'] = pd.Categorical(
                                        df_track_tidy_acceleration['metric'],
                                        categories= acceleration_metrics ,
                                        ordered=True
)


df_track_tidy_acceleration['metric'].unique()
    # Out[25]: 
    # ['accel_pos_mean_ms2', 'accel_pos_max_ms2', 'accel_neg_mean_ms2', 'accel_neg_min_ms2']
    # Categories (4, object): ['accel_pos_mean_ms2' < 'accel_pos_max_ms2' < 'accel_neg_mean_ms2' <
    #                          'accel_neg_min_ms2']

# %%'

# the categorixal order of 'treatment' is intact.

df_track_tidy_roam['treatment'].unique()
    # Out[26]: 
    # ['DBD-HTK', 'DBD-Omnisol', 'DCD-HTK', 'NMP']
    # Categories (4, object): ['DBD-HTK' < 'DBD-Omnisol' < 'DCD-HTK' < 'NMP']

df_track_tidy_dv['treatment'].unique()
    # Out[27]: 
    # ['DBD-HTK', 'DBD-Omnisol', 'DCD-HTK', 'NMP']
    # Categories (4, object): ['DBD-HTK' < 'DBD-Omnisol' < 'DCD-HTK' < 'NMP']

df_track_tidy_acceleration['treatment'].unique()
    # Out[28]: 
    # ['DBD-HTK', 'DBD-Omnisol', 'DCD-HTK', 'NMP']
    # Categories (4, object): ['DBD-HTK' < 'DBD-Omnisol' < 'DCD-HTK' < 'NMP']

# %%' save

df_track_tidy.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy.pkl' )

df_track_tidy_roam.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_roam.pkl' )

df_track_tidy_dv.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_dv.pkl' )

df_track_tidy_acceleration.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_acceleration.pkl' )

# %% load

df_track_tidy = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy.pkl' )

df_track_tidy_roam = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_roam.pkl' )

df_track_tidy_dv = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_dv.pkl' )

df_track_tidy_acceleration = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_acceleration.pkl' )


# %%' mixed-effects model

# preparing the data for the  mixed-effects model analysis.

# the time column is already ordered.
df_track_tidy['time'].unique()
    # Out[39]: 
    # ['pod_1', 'pod_3', 'pod_4', 'pod_7', 'retrain_2']
    # Categories (5, object): ['retrain_2' < 'pod_1' < 'pod_3' < 'pod_4' < 'pod_7']

# %%'

df_track_tidy.shape
    # Out[42]: (1122, 6)

# 1. Drop any row where 'sample_ID' is missing (NaN)
df_track_tidy_remove_NaN = df_track_tidy.dropna( subset=['value'] )

df_track_tidy_remove_NaN.shape
    # Out[43]: (1119, 6)

# %% rename back

df_track_tidy_remove_NaN_rename_back = df_track_tidy_remove_NaN.copy()

rename_back_map = {
    'DBD-Omnisol': 'DBD-Ecosol'
}

# Apply the replacement to the 'treatment' column
df_track_tidy_remove_NaN_rename_back['treatment'] = df_track_tidy_remove_NaN['treatment'].replace(rename_back_map)

# %%'

df_track_tidy_remove_NaN_rename_back[:4]
    # Out[10]: 
    #      video_id sample_ID   time   treatment     metric      value
    # 0  pod_1_ZC04      ZC04  pod_1     DBD-HTK  tdt_meter  29.903323
    # 1  pod_1_ZC05      ZC05  pod_1  DBD-Ecosol  tdt_meter  82.941499
    # 2  pod_1_ZC06      ZC06  pod_1     DBD-HTK  tdt_meter  57.402014
    # 3  pod_1_ZC07      ZC07  pod_1  DBD-Ecosol  tdt_meter  27.518746

# %%'

df_track_tidy_remove_NaN_rename_back.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_remove_NaN_rename_back.pkl' )

# %%'
# %%'
# %%' yjt

# Yeo-Johnson transformation , separate for each metric.
# from sklearn.preprocessing import PowerTransformer

df = df_track_tidy_remove_NaN_rename_back.copy()

df["value_yjt"] = np.nan  # initialize column

for met in df["metric"].unique():
    idx = df["metric"] == met   #  masking index
    values = df.loc[idx, "value"].values.reshape(-1, 1)

    pt = PowerTransformer(method="yeo-johnson", standardize=False)
    transformed = pt.fit_transform(values)

    df.loc[idx, "value_yjt"] = transformed.flatten()

# %%'

df_track_tidy_remove_NaN_rename_back["value_yjt"] = df["value_yjt"]

df_track_tidy_remove_NaN_rename_back.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_remove_NaN_rename_back.pkl' )


# %%'


df.groupby("metric")[ 'value' ].describe()
    # Out[65]: 
    #                            count      mean       std       min       25%  \
    # metric                                                                     
    # accel_neg_mean_ms2    102.000000 -0.141530  0.063342 -0.477355 -0.166142   
    # accel_neg_min_ms2     102.000000 -1.793011  0.893730 -5.478501 -2.357411   
    # accel_pos_max_ms2     102.000000  1.883353  0.886270  0.568699  1.251439   
    # accel_pos_mean_ms2    102.000000  0.153234  0.069975  0.029021  0.111301   
    # inner_zone_percentage  99.000000 20.498182 15.902554  0.440000  9.170000   
    # nocw                  102.000000 71.323529 18.115778 14.000000 63.250000   
    # tdt_meter             102.000000 66.841603 36.068883  8.156513 46.675913   
    # uniformity_index      102.000000  0.780591  0.108102  0.146816  0.755712   
    # velocity_max          102.000000  1.343577  0.594923  0.416664  0.905302   
    # velocity_mean         102.000000  0.111564  0.060196  0.013609  0.077891   
    # velocity_mean_r_ms    102.000000  0.111427  0.060123  0.013594  0.077804   
    
    #                             50%       75%        max  
    # metric                                                
    # accel_neg_mean_ms2    -0.132673 -0.106754  -0.026065  
    # accel_neg_min_ms2     -1.579624 -1.155073  -0.651349  
    # accel_pos_max_ms2      1.600231  2.430844   4.433050  
    # accel_pos_mean_ms2     0.144667  0.184537   0.503716  
    # inner_zone_percentage 17.070000 28.085000  77.610000  
    # nocw                  75.000000 83.000000  96.000000  
    # tdt_meter             60.539106 81.753953 239.051215  
    # uniformity_index       0.805021  0.833940   0.922784  
    # velocity_max           1.164709  1.724112   3.147192  
    # velocity_mean          0.101039  0.136427   0.398862  
    # velocity_mean_r_ms     0.100899  0.136275   0.398419  

df.groupby("metric")["value_yjt"].describe()
    # Out[66]: 
    #                            count        mean         std        min  \
    # metric                                                                
    # accel_neg_mean_ms2    102.000000   -0.092686    0.025660  -0.171558   
    # accel_neg_min_ms2     102.000000   -0.655469    0.123686  -0.945530   
    # accel_pos_max_ms2     102.000000    0.717916    0.140334   0.387307   
    # accel_pos_mean_ms2    102.000000    0.099200    0.027996   0.026767   
    # inner_zone_percentage  99.000000    4.315029    1.676639   0.383044   
    # nocw                  102.000000 9952.504668 4470.224569 233.978623   
    # tdt_meter             102.000000   10.206797    2.665292   3.503967   
    # uniformity_index      102.000000   86.693095   34.082018   0.341245   
    # velocity_max          102.000000    0.576839    0.115442   0.300806   
    # velocity_mean         102.000000    0.074674    0.026467   0.013008   
    # velocity_mean_r_ms    102.000000    0.074585    0.026436   0.012993   
    
    #                               25%          50%          75%          max  
    # metric                                                                    
    # accel_neg_mean_ms2      -0.107250    -0.092715    -0.079555    -0.024144  
    # accel_neg_min_ms2       -0.761686    -0.654579    -0.566693    -0.409734  
    # accel_pos_max_ms2        0.622213     0.700766     0.831730     1.000860  
    # accel_pos_mean_ms2       0.083190     0.100004     0.116757     0.181433  
    # inner_zone_percentage    3.215481     4.372092     5.473950     8.283815  
    # nocw                  6920.481249 10229.334172 12912.075334 18047.639791  
    # tdt_meter                8.944468    10.141297    11.686826    18.965284  
    # uniformity_index        64.112039    88.867651   107.176034   187.140917  
    # velocity_max             0.494355     0.563625     0.670643     0.819004  
    # velocity_mean            0.060983     0.074007     0.090687     0.149137  
    # velocity_mean_r_ms       0.060915     0.073910     0.090586     0.148965  


# %% descriptive

df_track_tidy_roam['sample_ID'].nunique()
# Out[13]: 25

df_track_tidy_roam['metric'].value_counts()
    # Out[14]: 
    # metric
    # inner_zone_percentage    102
    # nocw                     102
    # uniformity_index         102
    # Name: count, dtype: int64


# this is probably because of different time-points per group.
df_track_tidy_roam['treatment'].value_counts()
    # Out[15]: 
    # treatment
    # NMP            105
    # DBD-Omnisol     87
    # DCD-HTK         60
    # DBD-HTK         54
    # Name: count, dtype: int64



df_track_tidy_roam.groupby('treatment')['sample_ID'].nunique()
    # C:\Users\azare\AppData\Local\Temp\ipykernel_40508\2795833093.py:1: FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.
    #   df_track_tidy_roam.groupby('treatment')['sample_ID'].nunique()
    # Out[16]: 
    # treatment
    # DBD-HTK         4
    # DBD-Omnisol     6
    # DCD-HTK         5
    # NMP            10
    # Name: sample_ID, dtype: int64

df_track_tidy_roam.groupby('treatment', observed=True)['sample_ID'].nunique()
    # Out[17]: 
    # treatment
    # DBD-HTK         4
    # DBD-Omnisol     6
    # DCD-HTK         5
    # NMP            10
    # Name: sample_ID, dtype: int64

# %%% separate

df_track_tidy_roam.groupby('treatment', observed=True)['sample_ID'].nunique()
    # Out[19]: 
    # treatment
    # DBD-HTK         4
    # DBD-Omnisol     6
    # DCD-HTK         5
    # NMP            10
    # Name: sample_ID, dtype: int64


df_track_tidy_dv.groupby('treatment', observed=True)['sample_ID'].nunique()
    # Out[22]: 
    # treatment
    # DBD-HTK         4
    # DBD-Omnisol     6
    # DCD-HTK         5
    # NMP            10
    # Name: sample_ID, dtype: int64

df_track_tidy_acceleration.groupby('treatment', observed=True)['sample_ID'].nunique()
    # Out[24]: 
    # treatment
    # DBD-HTK         4
    # DBD-Omnisol     6
    # DCD-HTK         5
    # NMP            10
    # Name: sample_ID, dtype: int64

# %%'


