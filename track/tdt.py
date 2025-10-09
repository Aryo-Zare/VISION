
# tdt : total distance traveled.


# %%' 

# point is a dataframe

# window_size : Adjust based on the noise level
def process_df_track ( 
                        df=None , 
                        window_size = None , 
                        downsample_factor = None , 
                        fps = 30 ,
                        m_pix = None # meter/pixel : pixel to meter conversion factor.
) :

# %%%' time

    # adding a time column.
    
    # Assuming you already have your DataFrame 'df' with the 'x' and 'y' columns
    # Create a 'time_ms' column by computing the timestamp for each row
    # np.arange(len(df)) * (1000 / fps)
        # first phrase : putting a frame number foreach row
        # 2nd phrase : conversion factor for frame-ms
    df['time_ms'] = np.arange(len(df)) * (1000 / fps)
    
    # Optionally, if you want to round to 2 decimal places:
    df['time_ms'] = df['time_ms'].round(2)
    
# %%%' low-pass filter
    
    # Step 1: Apply a moving average to smooth the data
    df['x_smooth'] = df['x'].rolling( window=window_size, center=True ).mean()
    df['y_smooth'] = df['y'].rolling( window=window_size, center=True ).mean()
    
    # Step 2: Downsample the smoothed data (e.g., every 10th frame)
    # reset_index : the reason for resetting the index may be : 
            # after downsampling, if the old index is preserved, it will be like : 0 , 10 , 20 , ...
            # because only the remaining indices are shown. 
    df_2 = df.iloc[::downsample_factor].reset_index(drop=True)

# %%%' x&y differences

    # Step 3: Calculate x&y differences on downsampled data
    # diff : the difference of :
        # each x[i] & x[i+1]
        # each y[i] & y[i+1]
    
    df_2['dx'] = df_2['x_smooth'].diff()
    df_2['dy'] = df_2['y_smooth'].diff()
    
    # Distance traveled between each 2 consequative rows ( in pixels ) .
    df_2['distance'] = np.sqrt( df_2['dx']**2 + df_2['dy']**2 )
    
    # conversion from pixel to meter.
    # df_2['distance_m'] = df_2['distance'] * m_pix
    
    # total distance traveled in pixels.
    tdt_pixel = df_2['distance'].sum() 
    
    # total distance traveled in meter.
    tdt_m = tdt_pixel * m_pix
    
# %%%'

    return df_2 , tdt_m

# %%'
# %%'

df_ZC60 = pd.read_csv( r'U:\VISION\track\data\retrain_2\P067_ZC60_OF2ReTr_Video_1_04_06_2023_11_35_42_1\center_points.csv' )
df_ZC61 = pd.read_csv( r'U:\VISION\track\data\retrain_2\P067_ZC61_OF2ReTr_Video_1_28_06_2023_11_01_15_1\center_points.csv' )
df_ZC62 = pd.read_csv( r'U:\VISION\track\data\retrain_2\P067_ZC62_OF2ReTr_Video_1_04_07_2023_10_52_25_1\center_points.csv' )
df_ZC63 = pd.read_csv( r'U:\VISION\track\data\retrain_2\P067_ZC63_OF2ReTr_Video_1_23_07_2023_10_57_39_1\center_points.csv' )
df_ZC64 = pd.read_csv( r'U:\VISION\track\data\retrain_2\P067_ZC64_OF2ReTr_Video_1_30_07_2023_11_01_35_1\center_points.csv' )


df_ZC = [ df_ZC61 , df_ZC62 , df_ZC63 , df_ZC64 ]


# pixel-meter conversion ( length ).
# for each video, there is a slight difference !
# 14 tiles = 175 cm
# ZC60
m_pix_ZC60 = 1.75 / 558
m_pix_ZC61 = 1.75 / 555
m_pix_ZC62 = 1.75 / 554
m_pix_ZC63 = 1.75 / 558 
m_pix_ZC64 = 1.75 / 564

m_pix_ZC = [ m_pix_ZC61 , m_pix_ZC62 , m_pix_ZC63 , m_pix_ZC64 ]

# %%'

df_2 , tdt_m = process_df_track ( 
                                    df=df_ZC60 , 
                                    window_size = 5 , 
                                    downsample_factor = 10 , 
                                    fps = 30 ,
                                    m_pix = m_pix # meter/pixel : pixel to meter conversion factor.
)

# %%

# for ZC-60
tdt_m
# Out[21]: np.float64(89.77442300793965)]

# %%'
# %%' multiple pigs

tdt_m_ZC = []

for df , m_pix in zip( df_ZC , m_pix_ZC ) :
    df_result , tdt_m = process_df_track ( 
                                        df=df , 
                                        window_size = 5 , 
                                        downsample_factor = 10 , 
                                        fps = 30 ,
                                        m_pix = m_pix # meter/pixel : pixel to meter conversion factor.
    )
    tdt_m_ZC.append( tdt_m )

# %%

tdt_m_ZC
    # Out[37]: 
    # [np.float64(67.81510930781798),
    #  np.float64(106.7969286049404),
    #  np.float64(25.468853985365772),   # this pig was sitting on the ground for a long time, hence the less distance walked relative tothe others !
    #  np.float64(53.89482543962337)]

# %%





