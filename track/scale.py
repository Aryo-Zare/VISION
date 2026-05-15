
# %%

df_track_tidy_dv = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_dv.pkl' )

df_track_tidy_dv.head()
    # Out[9]: 
    #      video_id sample_ID   time    treatment     metric      value
    # 0  pod_1_ZC04      ZC04  pod_1      DBD-HTK  tdt_meter  29.903323
    # 1  pod_1_ZC05      ZC05  pod_1  DBD-Omnisol  tdt_meter  82.941499
    # 2  pod_1_ZC06      ZC06  pod_1      DBD-HTK  tdt_meter  57.402014
    # 3  pod_1_ZC07      ZC07  pod_1  DBD-Omnisol  tdt_meter  27.518746
    # 4  pod_1_ZC08      ZC08  pod_1      DBD-HTK  tdt_meter  53.931250


# %%

df_tdt = (
    df_track_tidy_dv[df_track_tidy_dv["metric"] == "tdt_meter"]
    .drop(columns=["video_id"])
    .reset_index(drop=True)
)

# %%

df_tdt.shape
    # Out[11]: (102, 5)

df_tdt.head()
    # Out[12]: 
    #   sample_ID   time    treatment     metric      value
    # 0      ZC04  pod_1      DBD-HTK  tdt_meter  29.903323
    # 1      ZC05  pod_1  DBD-Omnisol  tdt_meter  82.941499
    # 2      ZC06  pod_1      DBD-HTK  tdt_meter  57.402014
    # 3      ZC07  pod_1  DBD-Omnisol  tdt_meter  27.518746
    # 4      ZC08  pod_1      DBD-HTK  tdt_meter  53.931250


df_tdt.to_excel( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_tdt.xlsx' )


# %%

