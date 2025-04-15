

# %%

point = pd.read_csv( r'U:\VISION\track\results-7\center_points.csv' )

point.shape
    # Out[7]: (449, 2)

point[:4]
    # Out[8]: 
    #      x    y
    # 0  323  160
    # 1  323  159
    # 2  323  159
    # 3  322  159

# %%

plt.plot( point.iloc[:,0] , point.iloc[:,1] )
plt.title('coordinates _ movement')
plt.savefig( r'U:\VISION\track\results-7\1\coordinate.pdf' )

# %%

dva = pd.read_csv( r'U:\VISION\track\results-7\distance_velocity_acceleration.csv' )

dva.shape
    # Out[16]: (449, 4)

dva.columns
    # Out[19]: 
    # Index(['time_s', 'cumulative_distance_pixels', 'velocity_pixels_per_s',
    #        'acceleration_pixels_per_s2'],
    #       dtype='object')


# 0 : index 0 = start
    # this ratifies using 0 as the first index.
# the sampling ate is 30 Hz.
dva[:8]
    # Out[24]: 
    #      time_s  ...  acceleration_pixels_per_s2
    # 0  0.000000  ...                         0.0
    # 1  0.033333  ...                       900.0
    # 2  0.066667  ...                      -900.0
    # 3  0.100000  ...                       900.0
    # 4  0.133333  ...                         0.0
    # 5  0.166667  ...                      -900.0
    # 6  0.200000  ...                         0.0
    # 7  0.233333  ...                       900.0
    
    # [8 rows x 4 columns]

dva.iloc[28:32,0]
    # Out[26]: 
    # 28    0.933333
    # 29    0.966667
    # 30    1.000000
    # 31    1.033333
    # Name: time_s, dtype: float64

# %%
# %%


# Assume df is your DataFrame with 'time', 'x', and 'y' columns
# df = df.sort_values('time')

# Step 1: Apply a moving average to smooth the data
window_size = 5  # Adjust based on the noise level
point['x_smooth'] = point['x'].rolling(window=window_size, center=True).mean()
point['y_smooth'] = point['y'].rolling(window=window_size, center=True).mean()

# Step 2: Downsample the smoothed data (e.g., every 10th frame)
downsample_factor = 10
# reset_index : the reason for resetting the index may be : 
        # after downsampling, if the old index is preserved, it will be like : 0 , 10 , 20 , ...
        # because only the remaining indices are shown. 
point_downsampled = point.iloc[::downsample_factor].reset_index(drop=True)

# %%

point_downsampled.shape
    # Out[10]: (45, 4)

point_downsampled[:4]
    # Out[11]: 
    #      x    y  x_smooth  y_smooth
    # 0  323  160       NaN       NaN
    # 1  322  160     322.4     159.6
    # 2  327  162     327.6     165.0
    # 3  333  167     333.4     168.4

# %%

# Step 3: Calculate differences for velocity estimation on downsampled data
df_downsampled['dt'] = df_downsampled['time'].diff()

point_downsampled['dx'] = point_downsampled['x_smooth'].diff()
point_downsampled['dy'] = point_downsampled['y_smooth'].diff()

# Distance and velocity calculation
point_downsampled['distance'] = np.sqrt( point_downsampled['dx']**2 + point_downsampled['dy']**2 )

# %%

point_downsampled['distance'][:5]
    # Out[16]: 
    # 0         NaN
    # 1         NaN
    # 2    7.496666
    # 3    6.723095
    # 4    4.841487
    # Name: distance, dtype: float64

# %%

plt.plot( point_downsampled['distance'] )

# %%

df_downsampled['velocity'] = df_downsampled['distance'] / df_downsampled['dt']
df_downsampled['velocity'] = df_downsampled['velocity'].fillna(0)

# %%






