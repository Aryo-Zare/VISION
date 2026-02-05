

# %%

'''
    this program evaluates the statistical significance for :
        between 'treatment' groups.
        between 'time' points.
'''

# %% address

# F:\OneDrive - Uniklinik RWTH Aachen\kidney \ AI_stat .docx    |   414


# Name                     Version          Build            Channel
# statsmodels              0.14.5           py313h2cb717b_0  anaconda

# %% packages

import os
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
from statsmodels.stats.multitest import multipletests
import matplotlib.pyplot as plt

# %% input

# --- Input data ---

# C:\code\VISION\track\all_track.py     =>
df_track_tidy_remove_NaN_rename_back = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_remove_NaN_rename_back.pkl' )

# %% input

data_main = df_track_tidy_remove_NaN_rename_back   # your dataframe
outcome_variable = "value_yjt"
# "value"

# Ordered categories
treatments = ["DBD-HTK", "DBD-Ecosol", "DCD-HTK", "NMP"]
time_points = ["retrain_2", "pod_1", "pod_3", "pod_4", "pod_7"]
reference_time = "retrain_2"

# %% qq address

# Define the folder for saving Q-Q plots
qq_plot_folder = r"F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\stat\qq"
if not os.path.exists(qq_plot_folder):
    os.makedirs(qq_plot_folder)

# %% helper functions

# --- Helper functions ---
def get_param_index(param_name, params_list):
    try:
        return params_list.index(param_name)
    except ValueError:
        return None

def build_contrast_vs_baseline(time_point, treatment, params_list, result, reference_time=reference_time):
    """Contrast for treatment vs baseline treatment (DBD-HTK)."""
    contrast = np.zeros((1, result.k_fe))
    main_param = f"C(treatment)[T.{treatment}]"
    idx_main = get_param_index(main_param, params_list)
    if idx_main is None:
        return None
    contrast[0, idx_main] = 1
    if time_point != reference_time:
        interaction_param = f"C(treatment)[T.{treatment}]:C(time)[T.{time_point}]"
        idx_inter = get_param_index(interaction_param, params_list)
        if idx_inter is None:
            return None
        contrast[0, idx_inter] = 1
    return contrast

def build_pairwise_contrast(time_point, treatA, treatB, params_list, result, reference_time=reference_time):
    """Contrast for treatA vs treatB at a given time."""
    contrast_A = build_contrast_vs_baseline(time_point, treatA, params_list, result, reference_time)
    contrast_B = build_contrast_vs_baseline(time_point, treatB, params_list, result, reference_time)
    if contrast_A is None or contrast_B is None:
        return None
    return contrast_A - contrast_B

def build_time_contrast(treatment, timeA, timeB, params_list, result, reference_time=reference_time):
    """Contrast for timeA vs timeB within a given treatment."""
    contrastA = np.zeros((1, result.k_fe))
    contrastB = np.zeros((1, result.k_fe))

    # Time main effects
    if timeA != reference_time:
        paramA = f"C(time)[T.{timeA}]"
        idxA = get_param_index(paramA, params_list)
        if idxA is not None:
            contrastA[0, idxA] = 1
    if timeB != reference_time:
        paramB = f"C(time)[T.{timeB}]"
        idxB = get_param_index(paramB, params_list)
        if idxB is not None:
            contrastB[0, idxB] = 1

    # Treatment main effect
    if treatment != "DBD-HTK":
        paramT = f"C(treatment)[T.{treatment}]"
        idxT = get_param_index(paramT, params_list)
        if idxT is not None:
            contrastA[0, idxT] = 1
            contrastB[0, idxT] = 1

    # Interaction terms
    if treatment != "DBD-HTK":
        if timeA != reference_time:
            paramIntA = f"C(treatment)[T.{treatment}]:C(time)[T.{timeA}]"
            idxIntA = get_param_index(paramIntA, params_list)
            if idxIntA is not None:
                contrastA[0, idxIntA] = 1
        if timeB != reference_time:
            paramIntB = f"C(treatment)[T.{treatment}]:C(time)[T.{timeB}]"
            idxIntB = get_param_index(paramIntB, params_list)
            if idxIntB is not None:
                contrastB[0, idxIntB] = 1

    return contrastA - contrastB

# %% Main loop

# --- Main loop ---
results_all = []

for met in data_main['metric'].unique():
    df_met = data_main[data_main["metric"] == met].copy().reset_index(drop=True)

    try:
        formula = f"{outcome_variable} ~ C(treatment) * C(time)"
        model = smf.mixedlm(formula, data=df_met, groups=df_met["sample_ID"])
        result_metric = model.fit(reml=True)
    except Exception as e:
        print(f"Model did not converge for metric {met}: {e}")
        continue

    #======================
    # qq-plot
    
    # Generate and save the Q-Q plot for model residuals.
    # for each metric, there is one residuals data  =>  1 q-q plot.
    fig = sm.qqplot(result_metric.resid, line='45')
    # Set the overall figure size to 8 x 8 inches
    fig.set_size_inches(8, 8)
    # Get the first (and typically only) axes object from the figure
    ax = fig.axes[0]
    # Set aspect ratio to 'equal' so that one unit on the x-axis
    # is equal in length to one unit on the y-axis.
    ax.set_aspect('equal', adjustable='box')
    plt.title(f"Q-Q Plot for {met}")
    plot_filename = os.path.join(qq_plot_folder, f"qqplot_{met}.pdf")
    plt.tight_layout()
    plt.savefig(plot_filename)
    plt.close()
    
    #======================

    params_list_metric = result_metric.params.index.tolist()
    results_metric = []

    # --- Between-treatment comparisons ---
    for tp in time_points:
        for i in range(len(treatments)):
            for j in range(i+1, len(treatments)):
                tA, tB = treatments[i], treatments[j]
                contrast = build_pairwise_contrast(tp, tA, tB, params_list_metric, result_metric)
                if contrast is not None:
                    test = result_metric.t_test(contrast)
                    results_metric.append({
                        "metric": met,
                        "time_point": tp,
                        "comparison_type": "between_treatments",
                        "comparison": f"{tA} vs {tB}",
                        "contrast_estimate": test.effect.item(),
                        "p_value": test.pvalue.item()
                    })

    # --- Within-treatment time comparisons ---
    for treat in treatments:
        for i in range(len(time_points)):
            for j in range(i+1, len(time_points)):
                tpA, tpB = time_points[i], time_points[j]
                contrast = build_time_contrast(treat, tpA, tpB, params_list_metric, result_metric)
                if contrast is not None:
                    test = result_metric.t_test(contrast)
                    results_metric.append({
                        "metric": met,
                        "treatment": treat,
                        "comparison_type": "within_treatment_time",
                        "comparison": f"{tpA} vs {tpB}",
                        "contrast_estimate": test.effect.item(),
                        "p_value": test.pvalue.item()
                    })

    df_metric_results = pd.DataFrame(results_metric)
    if df_metric_results.shape[0] == 0:
        continue

    # Multiple testing corrections
    pvals_global = df_metric_results['p_value'].values
    reject_global, pvals_corr_global, _, _ = multipletests(pvals_global, alpha=0.05, method='bonferroni')
    df_metric_results['p_value_adjusted_global'] = pvals_corr_global
    df_metric_results['reject_null_global'] = reject_global

    # Per-time-point correction (only for between-treatment)
    df_metric_results['p_value_adjusted_per_tp'] = np.nan
    df_metric_results['reject_null_per_tp'] = np.nan
    if "time_point" in df_metric_results.columns:
        for t in df_metric_results['time_point'].dropna().unique():
            idx = df_metric_results['time_point'] == t
            pvals_tp = df_metric_results.loc[idx, 'p_value'].values
            reject_tp, pvals_corr_tp, _, _ = multipletests(pvals_tp, alpha=0.05, method='bonferroni')
            df_metric_results.loc[idx, 'p_value_adjusted_per_tp'] = pvals_corr_tp
            df_metric_results.loc[idx, 'reject_null_per_tp'] = reject_tp

    results_all.append(df_metric_results)

# --- Final concatenated results ---
final_results_df = pd.concat(results_all, axis=0).reset_index(drop=True)

# %% result

final_results_df.shape
    # Out[73]: (605, 11)  #  value
    # Out[24]: (605, 11)  #  value_yjt

# Save
final_results_df.to_excel(r"F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\stat\track_stat_complete_value_yjt.xlsx", index=False)

# %%'

