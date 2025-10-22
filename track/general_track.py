
# this encompasses general codes related to the tracking project.

# %%

df_aggregate_track_5.shape
    # Out[78]: (106, 23)

# %%

# List of the identifier and grouping columns you want to keep
id_columns = ['video_id', 'sample_ID', 'time', 'treatment']

# List of the measurement columns you want to analyze
readout_parameters = [
    'tdt_meter', 
    'inner_zone_percentage',
    'velocity_mean', 
    'velocity_mean_r_ms' ,
    'velocity_max',
    'acceleration_mean',
    'acceleration_max', 
    'nocw',  # Note: I removed the extra space from your column name list
    'uniformity_index'
]

# Create the new, focused DataFrame
df_subset = df_aggregate_track_5[id_columns + readout_parameters]

# %%

# Melt the DataFrame to convert it to a long format
df_track_tidy = pd.melt(
    df_subset,
    id_vars=id_columns,              # Columns to keep as they are (identifiers)
    value_vars=readout_parameters,   # Columns to "unpivot" into rows
    var_name='metric',               # Name of the new column for the measurement type
    value_name='value'               # Name of the new column for the measurement value
)

# %%

df_track_tidy.shape
    # Out[81]: (954, 6)

df_track_tidy.columns
    # Out[45]: Index(['video_id', 'sample_ID', 'time', 'treatment', 'metric', 'value'], dtype='object')

df_track_tidy[:4]
    # Out[46]: 
    #      video_id sample_ID   time   treatment     metric     value
    # 0  pod_1_ZC04      ZC04  pod_1     DBD-HTK  tdt_meter 29.903323
    # 1  pod_1_ZC05      ZC05  pod_1  DBD-Ecosol  tdt_meter 82.941499
    # 2  pod_1_ZC06      ZC06  pod_1     DBD-HTK  tdt_meter 57.402014
    # 3  pod_1_ZC07      ZC07  pod_1  DBD-Ecosol  tdt_meter 27.518746


# %%

# Create a dictionary to define the mapping
rename_map = {
    'DBD-Ecosol': 'DBD-Omnisol'
}

# Apply the replacement to the 'treatment' column
# This finds 'DBD-Ecosol' and replaces it with 'DBD-Omnisol'
df_track_tidy['treatment'] = df_track_tidy['treatment'].replace(rename_map)
    # c:\code\vision\track\general_track.py:65: FutureWarning: 
    #     The behavior of Series.replace (and DataFrame.replace) with CategoricalDtype is deprecated. 
    #     In a future version, replace will only be used for cases that preserve the categories. 
    #     To change the categories, use ser.cat.rename_categories instead.
    #   df_track_tidy['treatment'] = df_track_tidy['treatment'].replace(rename_map)

# %%
# %%

df_track_tidy['treatment'].unique()
    # Out[50]: 
    # ['DBD-HTK', 'DBD-Omnisol', 'DCD-HTK', 'NMP']
    # Categories (4, object): ['DBD-HTK' < 'DBD-Omnisol' < 'DCD-HTK' < 'NMP']

# %%

df_track_tidy['metric'].unique()
    # Out[89]: 
    # array(['tdt_meter', 'inner_zone_percentage', 'velocity_mean',
    #        'velocity_mean_r_ms', 'velocity_max', 'acceleration_mean',
    #        'acceleration_max', 'nocw', 'uniformity_index'], dtype=object)


# %% split the dataframe.
# %% roam

# List of metrics for the "roaming" DataFrame
roaming_metrics = [
                    'inner_zone_percentage', 
                    'nocw', 
                    'uniformity_index'
]

mask_roam = df_track_tidy['metric'].isin(roaming_metrics)
df_track_tidy_roam = df_track_tidy[ mask_roam ].copy()

df_track_tidy_roam.shape
    # Out[13]: (318, 6)

# %% kinematic

# List of metrics for the "kinematic" DataFrame
# (This is all remaining metrics except 'velocity_mean')
kinematic_metrics = [
                    'tdt_meter',
                    'velocity_mean_r_ms',
                    'velocity_max',
                    'acceleration_mean',
                    'acceleration_max'
]

mask_kinematic = df_track_tidy['metric'].isin(kinematic_metrics)
df_track_tidy_kinematic = df_track_tidy[ mask_kinematic ].copy()

df_track_tidy_kinematic.shape
    # Out[15]: (530, 6)

# %%

df_track_tidy_roam['metric'].unique()
    # Out[16]: ]array(['inner_zone_percentage', 'nocw', 'uniformity_index'], dtype=object)

df_track_tidy_kinematic['metric'].unique()
    # Out[17]: 
    # array(['tdt_meter', 'velocity_mean_r_ms', 'velocity_max',
    #        'acceleration_mean', 'acceleration_max'], dtype=object)

# %% order _ roam

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
    # Out[19]: 
    # ['inner_zone_percentage', 'nocw', 'uniformity_index']
    # Categories (3, object): ['inner_zone_percentage' < 'nocw' < 'uniformity_index']

# %% order _ kinematic

kinematic_metrics = [
                    'velocity_mean_r_ms',
                    'velocity_max',
                    'acceleration_mean',
                    'acceleration_max' ,
                    'tdt_meter'
]

df_track_tidy_kinematic['metric'] = pd.Categorical(
                                        df_track_tidy_kinematic['metric'],
                                        categories= kinematic_metrics ,
                                        ordered=True
)


df_track_tidy_kinematic['metric'].unique()
    # Out[47]: 
    # ['tdt_meter', 'velocity_mean_r_ms', 'velocity_max', 'acceleration_mean', 'acceleration_max']
    # Categories (5, object): ['velocity_mean_r_ms' < 'velocity_max' < 'acceleration_mean' < 'acceleration_max' <
    #                          'tdt_meter']

# %%

df_track_tidy_roam['treatment'].unique()
    # Out[23]: 
    # ['DBD-HTK', 'DBD-Omnisol', 'DCD-HTK', 'NMP']
    # Categories (4, object): ['DBD-HTK' < 'DBD-Omnisol' < 'DCD-HTK' < 'NMP']

df_track_tidy_kinematic['treatment'].unique()
    # Out[24]: 
    # ['DBD-HTK', 'DBD-Omnisol', 'DCD-HTK', 'NMP']
    # Categories (4, object): ['DBD-HTK' < 'DBD-Omnisol' < 'DCD-HTK' < 'NMP']

# %%

df_track_tidy.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy.pkl' )

df_track_tidy_roam.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_roam.pkl' )

df_track_tidy_kinematic.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_kinematic.pkl' )


# %%

