
# %%

# removing bad-processed videos.
    # F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\bad_processing

# %%

cp_av_ds_4.shape
    # Out[17]: (196162, 21)

df_cell_count_percentage.shape
    # Out[18]: (7777, 4)

df_aggregate_track_5.shape
    # Out[19]: (106, 23)

df_track_tidy.shape
    # Out[20]: (954, 6)

df_track_tidy_roam.shape
    # Out[43]: (318, 6)

df_track_tidy_kinematic.shape
    # Out[44]: (530, 6)

# %%

# 1. Define the list of video_ids you want to remove
videos_to_remove = ['pod_4_ZC21', 'pod_4_ZC63', 'pod_7_ZC09']

# %%

# mask

mask_for_cp_av_ds_4 = cp_av_ds_4['video_id'].isin( videos_to_remove )

mask_for_df_cell_count_percentage = df_cell_count_percentage['video_id'].isin( videos_to_remove )

mask_for_df_aggregate_track_5 = df_aggregate_track_5['video_id'].isin( videos_to_remove )

mask_for_df_track_tidy = df_track_tidy['video_id'].isin( videos_to_remove )


mask_for_df_track_tidy_roam = df_track_tidy_roam['video_id'].isin( videos_to_remove )

mask_for_df_track_tidy_kinematic = df_track_tidy_kinematic['video_id'].isin( videos_to_remove )


# %%

cp_av_ds_5 = cp_av_ds_4[ ~ mask_for_cp_av_ds_4 ]

df_cell_count_percentage_2 = df_cell_count_percentage[ ~ mask_for_df_cell_count_percentage ]

df_aggregate_track_6 = df_aggregate_track_5[ ~ mask_for_df_aggregate_track_5 ]

df_track_tidy_2 = df_track_tidy[ ~ mask_for_df_track_tidy ]


df_track_tidy_roam_2 = df_track_tidy_roam[ ~ mask_for_df_track_tidy_roam ]

df_track_tidy_kinematic_2 = df_track_tidy_kinematic[ ~ mask_for_df_track_tidy_kinematic ]


# %%

cp_av_ds_5.shape
    # Out[30]: (190763, 21)

df_cell_count_percentage_2.shape
    # Out[31]: (7633, 4)

df_aggregate_track_6.shape
    # Out[32]: (103, 23)

df_track_tidy_2.shape
    # Out[33]: (927, 6)

df_track_tidy_roam_2.shape
    # Out[41]: (309, 6)

df_track_tidy_kinematic_2.shape
    # Out[42]: (515, 6)

# %%

cp_av_ds_5.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\cp_av_ds_5.pkl' )

df_cell_count_percentage_2.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_cell_count_percentage_2.pkl' )

df_aggregate_track_6.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_aggregate_track_6.pkl' )

df_track_tidy_2.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_2.pkl' )

df_track_tidy_roam_2.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_roam_2.pkl' )

df_track_tidy_kinematic_2.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_kinematic_2.pkl' )


# %%
# %%

df_track_tidy_kinematic_2.shape
    # Out[51]: (515, 6)

mask_to_remove = (
                    (
                        ( df_track_tidy_kinematic_2['video_id'] == 'pod_3_ZC22' ) &
                        ( df_track_tidy_kinematic_2['metric'].isin( ['velocity_max', 'acceleration_max'] ) )
                    ) |
                        ( df_track_tidy_kinematic_2['metric'] == 'acceleration_mean' ) # 'acceleration_mean' is naturally 0 & is not needed.
)


df_track_tidy_kinematic_3 = df_track_tidy_kinematic_2[ ~ mask_to_remove  ]

df_track_tidy_kinematic_3.shape
    # Out[55]: (410, 6)

# This line re-scans the column and drops any categories that no longer have any data.
df_track_tidy_kinematic_3['metric'] = df_track_tidy_kinematic_3['metric'].cat.remove_unused_categories()

df_track_tidy_kinematic_3.shape
    # Out[62]: (410, 6)
    
df_track_tidy_kinematic_3.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_kinematic_3.pkl' )


# %%

