

# %%

# %% Imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %% Load data
df_track_tidy_dv = pd.read_pickle(
    r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_dv.pkl'
)

# %%

print(df_track_tidy_dv["metric"].unique())
    # ['tdt_meter', 'velocity_mean_r_ms', 'velocity_max']
    # Categories (3, object): ['velocity_mean_r_ms' < 'velocity_max' < 'tdt_meter']

# %% Keep only plot C data:
# metric = Total distance walked
# treatments = DBD-HTK and DCD-HTK only
df_plot = df_track_tidy_dv.copy()

# Keep only relevant metric
metric_name = "tdt_meter"


df_plot = df_plot[
    (df_plot["metric"] == metric_name) &
    (df_plot["treatment"].isin(["DBD-HTK", "DCD-HTK"]))
].copy()


# remove unused categorical levels
# convert categorical to string
df_plot["treatment"] = df_plot["treatment"].astype(str)
df_plot["time"] = df_plot["time"].astype(str)

# %% Rename retrain_2 to baseline


df_plot["time"] = df_plot["time"].replace({"retrain_2": "baseline"})

time_order = ["baseline", "pod_1", "pod_3", "pod_4", "pod_7"]



# %% Define custom palette with requested RGB colors
custom_palette = {
    "DCD-HTK": (255/255, 96/255, 0/255),   # orange
    "DBD-HTK": (0/255, 0/255, 128/255)     # navy
}

# %% Create standalone plot
plt.figure(figsize=(10, 6))

ax = sns.pointplot(
    data=df_plot,
    x="time",
    y="value",
    hue="treatment",
    order=time_order,
    palette=custom_palette,
    marker="o",
    estimator="mean",
    errorbar="sd",
    dodge=0.2
)

# %% Formatting
plt.xticks(rotation=45, fontsize=16)
plt.yticks(fontsize=16)

ax.set_xlabel("Time", fontsize=20, loc="right")
ax.set_ylabel("$m$", fontsize=20, loc="top")
ax.set_title("Total distance walked", fontsize=20)

# Legend
legend = plt.legend(title="", fontsize=16)
for text in legend.get_texts():
    text.set_fontsize(16)

plt.tight_layout()

# %% Save

plt.savefig(
    r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\abstract__scand-las\distance.pdf'
)
plt.savefig(
    r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\abstract__scand-las\distance.svg'
)

# %%

