

# %%'

point_1 = pd.read_csv( r'U:\VISION\track\data\P067_ZC60_OF2ReTr_Video_1_04_06_2023_11_35_42_1\center_points.csv' )

point_2 = pd.read_csv( r'U:\VISION\track\data\P067_ZC61_OF2ReTr_Video_1_28_06_2023_11_01_15_1\center_points.csv' )

# %%'

# U:\VISION\track\results-7\center_points.csv

point_downsampled.to_csv( r'U:\VISION\track\results-7\point_downsampled.csv'  )

point_downsampled = pd.read_csv( r'U:\VISION\track\results-7\point_downsampled.csv'  )

# %%'

point.shape
    # Out[8]: (17992, 2)   # 10 minute video
    # Out[7]: (449, 2)

point[:4]
    # Out[8]: 
    #      x    y
    # 0  323  160
    # 1  323  159
    # 2  323  159
    # 3  322  159

point_downsampled.columns 
    # Out[10]: 
    # Index(['Unnamed: 0', 'x', 'y', 'xm', 'ym', 'x_smooth', 'y_smooth', 'dx', 'dy',
    #        'distance', 'distance_m', 'velocity_ms', 'time_s', 'acc_ms2'],
    #       dtype='object')

# %%'

point['x'].min()
    # Out[19]: 315

# %%'

# 1000 pixels = 2.5 m

# %% m _ xy

# pixel to meter
point['xm'] = point['x'] * 0.0025
point['ym'] = point['y'] * 0.0025

# %%'

point_1['xm'] = point_1['x'] * 0.0025
point_1['ym'] = point_1['y'] * 0.0025

# %%'

point_2['xm'] = point_2['x'] * 0.0025
point_2['ym'] = point_2['y'] * 0.0025

# %% Trajectory
# single plot

# Trajectory
# if loading 'point_downsampled' from the beginning, you should not use it instead of 'point' here.
    # reason : it's downsampled & will result a low-resolution trajectory !
        # we do not need downsampling for trajectory plotting !

fig , ax = plt.subplots( figsize =(13,10) )


# the y coordinates of video-images are rendered from top to bottom.
# hence, here, the y coordinates are mirrored (-) to conform to the video !!
plt.plot( point['xm'] , -point['ym'] , linewidth=8 )   # , linewidth=16 

# plt.plot( point.iloc[:,0] , point.iloc[:,1] )

# the y coordinates of video-images are rendered from top to bottom.
# hence, here, the y coordinates are mirrored (-) to conform to the video !!
# plt.plot( point.iloc[:,0] , -point.iloc[:,1] )

plt.title('Movement trajectory of a pig in a 10 minute video \n' +
          ' retraining_2 : P067_ZC60_OF2ReTr_Video_1_04_06_2023_11_35_42_1.mp4 ' , 
          fontsize=20)

plt.xlabel( 'door side (m)'  , loc='right' )
plt.ylabel( 'barrier side (m)' , loc='top' )

fig.tight_layout()

# %%'
# %% double

fig , ax = plt.subplots( 2,1 , figsize=(16,12) , sharex=True )

# %%'


# the y coordinates of video-images are rendered from top to bottom.
# hence, here, the y coordinates are mirrored (-) to conform to the video !!
ax[0].plot( point_1['xm'] , -point_1['ym'] , linewidth=8 )   # , linewidth=16 

# plt.plot( point.iloc[:,0] , point.iloc[:,1] )

# the y coordinates of video-images are rendered from top to bottom.
# hence, here, the y coordinates are mirrored (-) to conform to the video !!
# plt.plot( point.iloc[:,0] , -point.iloc[:,1] )

ax[0].set_title('P067_ZC60_OF2ReTr_Video_1_04_06_2023_11_35_42_1.mp4 ' , 
          fontsize=20)

ax[0].set_xlabel( 'door side (m)'  , loc='right' )
ax[0].set_ylabel( 'barrier side (m)' , loc='top' )

# %%'

ax[1].plot( point_2['xm'] , -point_2['ym'] , linewidth=8 )   # , linewidth=16 

# plt.plot( point.iloc[:,0] , point.iloc[:,1] )

# the y coordinates of video-images are rendered from top to bottom.
# hence, here, the y coordinates are mirrored (-) to conform to the video !!
# plt.plot( point.iloc[:,0] , -point.iloc[:,1] )

ax[1].set_title( 'P067_ZC61_OF2ReTr_Video_1_28_06_2023_11_01_15_1.mp4 ' , 
          fontsize=20)

ax[1].set_xlabel( 'door side (m)'  , loc='right' )
ax[1].set_ylabel( 'barrier side (m)' , loc='top' )


# %%'

fig.suptitle( 'Movement trajectories in 10 minute videos \n retraining_2 ' )

fig.tight_layout()

# %%%'

plt.savefig( r'U:\VISION\track\test\trajectory_2.pdf' )
# plt.savefig( r'U:\VISION\track\results-7\2\trajectory_3.svg' )


# 250 - 800 : the span of x & y coordinates, according to the figure.

# %%'
# %% Emil's analysis. 

# Emil's analysis.
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

# %%'
# %% low-pass filter

# filtering 
# downsampling

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

# %%'

point_downsampled.shape
    # Out[10]: (45, 4)

point_downsampled[:4]
    # Out[11]: 
    #      x    y  x_smooth  y_smooth
    # 0  323  160       NaN       NaN
    # 1  322  160     322.4     159.6
    # 2  327  162     327.6     165.0
    # 3  333  167     333.4     168.4

# %%' distance

# Step 3: Calculate differences for velocity estimation on downsampled data

point_downsampled['dx'] = point_downsampled['x_smooth'].diff()
point_downsampled['dy'] = point_downsampled['y_smooth'].diff()

# Distance  
point_downsampled['distance'] = np.sqrt( point_downsampled['dx']**2 + point_downsampled['dy']**2 )

# conversion from pixel to meter.
point_downsampled['distance_m'] = point_downsampled['distance'] * 0.025



# 15s video
# 45 frames
time_range = np.linspace( 0 , 15 , num=45 )
time_range.shape
    # Out[30]: (45,)
time_range[:4]
    # Out[28]: array([0.        , 0.34090909, 0.68181818, 1.02272727])
time_range[-4:]
    # Out[31]: array([13.97727273, 14.31818182, 14.65909091, 15.        ])

point_downsampled['time_s'] = time_range

# %%'

# this is the distance the animal traveled per frame.
point_downsampled['distance'][:5]
    # Out[16]: 
    # 0         NaN
    # 1         NaN
    # 2    7.496666
    # 3    6.723095
    # 4    4.841487
    # Name: distance, dtype: float64

# %% plot _ velocity _ pixel

# I did not divide by time, as time is a fixed number & the units here are arbitrary.

fig , ax = plt.subplots( figsize =(15,12) )

plt.plot( point_downsampled['distance'] )
plt.title('velocity of movement \n moving average with a window of 5 \n downsampled by factor 10 \n arbitrary units')

plt.xlabel('time' , loc='right')
plt.ylabel('velocity' , loc='top')

fig.tight_layout()

# %%%'

plt.savefig( r'U:\VISION\track\results-7\1\velocity_3.pdf' )

# %% velocity in m/s

# velocity in m/s
# the data is downsampled : each 'distance' datapoint corresponds to the distance traveled in 10 frames ( 1/3 s )
point_downsampled['velocity_ms'] = point_downsampled['distance_m'] / ( 1/3 )

# point_downsampled['velocity_ms'] = point_downsampled['distance_m'] / ( 1/3 )


# not performed ( original from the interface ).
# df_downsampled['velocity'] = df_downsampled['distance'] / df_downsampled['dt']
# df_downsampled['velocity'] = df_downsampled['velocity'].fillna(0)

# %% plot _ velocity _ m/s

# velocity _ m/s

fig , ax = plt.subplots( figsize =(15,12) )

plt.plot( point_downsampled['time_s'] , point_downsampled['velocity_ms'] , linewidth=16 )
plt.title('velocity of movement')

plt.xlabel('time (s)' , loc='right')
plt.ylabel('velocity (m/s)' , loc='top')

fig.tight_layout()

# %%'

plt.savefig( r'U:\VISION\track\results-7\2\velocity_ms.pdf' )

# %% acceleration 

# again, as the denominator ( dt ) is equal among all rows, I discarded this.
point_downsampled['acc'] = point_downsampled['distance'].diff()

# acceleration in m/s^2
# 1/3 s : refer to the explanation in one of the above cells.
point_downsampled['acc_ms2'] = point_downsampled['velocity_ms'].diff() / ( 1/3 )

# %%%'

# force : this is an indicatoin of the stamina of the animal.

fig , ax = plt.subplots( figsize =(15,12) )

plt.plot( point_downsampled['time_s'] , point_downsampled['acc_ms2'] , linewidth=16)

plt.title('Acceleration')

plt.xlabel('time (s)' , loc='right')
# The \mathrm{} ensures that "m/s" appears in upright text rather than italicized math mode.
plt.ylabel( r'Acceleration $(\mathrm{m/s^2})$'  , loc='top')
#Italicized
# plt.ylabel( r'Acceleration $(m/s^2)$'  , loc='top')    

fig.tight_layout()

# %%'

plt.savefig( r'U:\VISION\track\results-7\2\acceleration.pdf' )

# %% presentation !
# %%%'
# %%%'

fig , ax = plt.subplots( 2,1 , figsize=(8,12) , sharex=True )

# %%%'

ax[0].plot( point_downsampled['time_s'] , point_downsampled['velocity_ms'] , linewidth=14 )
ax[0].set_title('Velocity')

ax[0].set_xlabel('time (s)' , loc='right')
ax[0].set_ylabel('Velocity (m/s)' , loc='top')

# %%%'

ax[1].plot( point_downsampled['time_s'] , point_downsampled['acc_ms2'] , linewidth=14)

ax[1].set_title('Acceleration')

ax[1].set_xlabel('time (s)' , loc='right')
# The \mathrm{} ensures that "m/s" appears in upright text rather than italicized math mode.
ax[1].set_ylabel( r'Acceleration $(\mathrm{m/s^2})$'  , loc='top')
#Italicized
# plt.ylabel( r'Acceleration $(m/s^2)$'  , loc='top')    

# %%'

# fig.suptitle( 'Velocity & acceleration of movement' , fontsize=24 )

fig.tight_layout()

# %%'

# velocity & acceleration
plt.savefig( r'U:\VISION\track\results-7\2\va.pdf' )
plt.savefig( r'U:\VISION\track\results-7\2\va.svg' )


# %% multi-plot
# %%%'
# %%%%'

# the initial intention was to include 3 plots ( including the trajectory, which has different dimmensions than the other 2 plots ).

# Create figure and specify GridSpec
fig = plt.figure(figsize=(14, 12))
gs = gridspec.GridSpec(2, 2, width_ratios=[1.1, 1], height_ratios=[1, 1])

# %%%'

# First plot (rectangle, spanning full y-axis)
ax1 = plt.subplot(gs[:, 0])  # Spans both rows in the first column
ax1.plot( point['xm'] , -point['ym'] , linewidth=16 )

# plt.plot( point.iloc[:,0] , point.iloc[:,1] )

# the y coordinates of video-images are rendered from top to bottom.
# hence, here, the y coordinates are mirrored (-) to conform to the video !!
# plt.plot( point.iloc[:,0] , -point.iloc[:,1] )

ax1.set_title('Movement trajectory of a pig in a 15s test video')

ax1.set_xlabel( 'door side (m)'  , loc='right' )
ax1.set_ylabel( 'barrier side (m)' , loc='top' )

# %%%'


ax1.set_title("Rectangle-shaped plot")

# Second plot (square, top half of right column)
ax2 = plt.subplot(gs[0, 1])  # Occupies top half of right column
ax2.set_title("Square-shaped plot 1")

# %%%'

# Third plot (square, bottom half of right column)
ax3 = plt.subplot(gs[1, 1])  # Occupies bottom half of right column
ax3.set_title("Square-shaped plot 2")

# %%%'


# Show plot
plt.tight_layout()

# %%'






