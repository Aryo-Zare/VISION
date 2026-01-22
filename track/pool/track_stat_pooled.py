
# %% packages

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
from statsmodels.stats.multitest import multipletests

# %% input

# C:\code\VISION\track\all_track.py     =>
df_track_tidy_remove_NaN_rename_back = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\data\df_track_tidy_remove_NaN_rename_back.pkl' )

data_main = df_track_tidy_remove_NaN_rename_back
outcome_variable = 'value'
# "value"

time_points = ["retrain_2", "pod_1", "pod_3", "pod_4", "pod_7"]
reference_time = "retrain_2"

# %%

# Define the folder for saving Q-Q plots
qq_plot_folder = r"F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\pool\qq"
if not os.path.exists(qq_plot_folder):
    os.makedirs(qq_plot_folder)

# %% helper

def get_param_index(param_name, params_list):
    try:
        return params_list.index(param_name)
    except ValueError:
        return None

def build_time_contrast(timeA, timeB, params_list, result, reference_time):
    contrast = np.zeros((1, result.k_fe))

    if timeA != reference_time:
        idxA = get_param_index(f"C(time)[T.{timeA}]", params_list)
        if idxA is not None:
            contrast[0, idxA] += 1

    if timeB != reference_time:
        idxB = get_param_index(f"C(time)[T.{timeB}]", params_list)
        if idxB is not None:
            contrast[0, idxB] -= 1

    return contrast

# %% main loop

results_all = []

for met in data_main["metric"].unique():

    df_met = data_main[data_main["metric"] == met].copy().reset_index(drop=True)

    try:
        model = smf.mixedlm(
            f"{outcome_variable} ~ C(time)",
            data=df_met,
            groups=df_met["sample_ID"]
        )
        result = model.fit(reml=True)
    except Exception as e:
        print(f"Model failed for metric {met}: {e}")
        continue

    #======================
    # qq-plot
    
    # Generate and save the Q-Q plot for model residuals.
    # for each metric, there is one residuals data  =>  1 q-q plot.
    fig = sm.qqplot(result.resid, line='45')
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
    
    params_list = result.params.index.tolist()
    results_metric = []

    # pairwise time comparisons
    for i in range(len(time_points)):
        for j in range(i + 1, len(time_points)):
            tA, tB = time_points[i], time_points[j]
            contrast = build_time_contrast(tA, tB, params_list, result, reference_time)

            test = result.t_test(contrast)

            results_metric.append({
                "metric": met,
                "comparison_type": "time_only",
                "comparison": f"{tA} vs {tB}",
                "contrast_estimate": test.effect.item(),
                "p_value": test.pvalue.item()
            })

    df_res = pd.DataFrame(results_metric)

    # multiple testing correction per metric
    reject, pvals_corr, _, _ = multipletests(
        df_res["p_value"].values,
        alpha=0.05,
        method="bonferroni"
    )

    df_res["p_value_adjusted"] = pvals_corr
    df_res["reject_null"] = reject

    results_all.append(df_res)

# %% final output

final_results_df = pd.concat(results_all, axis=0).reset_index(drop=True)

final_results_df.to_excel(
    r"F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\pool\track_stat_time_only_value_yjt.xlsx",
    index=False
)

# %% warnings

# C:\Users\azare\AppData\Local\miniconda3\envs\env_24\Lib\site-packages\statsmodels\regression\mixed_linear_model.py:2237: ConvergenceWarning: The MLE may be on the boundary of the parameter space.
#   warnings.warn(msg, ConvergenceWarning)
# C:\Users\azare\AppData\Local\miniconda3\envs\env_24\Lib\site-packages\statsmodels\regression\mixed_linear_model.py:2237: ConvergenceWarning: The MLE may be on the boundary of the parameter space.
#   warnings.warn(msg, ConvergenceWarning)
# C:\Users\azare\AppData\Local\miniconda3\envs\env_24\Lib\site-packages\statsmodels\regression\mixed_linear_model.py:2237: ConvergenceWarning: The MLE may be on the boundary of the parameter space.
#   warnings.warn(msg, ConvergenceWarning)
# C:\Users\azare\AppData\Local\miniconda3\envs\env_24\Lib\site-packages\statsmodels\regression\mixed_linear_model.py:2237: ConvergenceWarning: The MLE may be on the boundary of the parameter space.
#   warnings.warn(msg, ConvergenceWarning)
# C:\Users\azare\AppData\Local\miniconda3\envs\env_24\Lib\site-packages\statsmodels\base\model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
#   warnings.warn("Maximum Likelihood optimization failed to "
# C:\Users\azare\AppData\Local\miniconda3\envs\env_24\Lib\site-packages\statsmodels\regression\mixed_linear_model.py:2200: ConvergenceWarning: Retrying MixedLM optimization with lbfgs
#   warnings.warn(
# C:\Users\azare\AppData\Local\miniconda3\envs\env_24\Lib\site-packages\statsmodels\regression\mixed_linear_model.py:2237: ConvergenceWarning: The MLE may be on the boundary of the parameter space.
#   warnings.warn(msg, ConvergenceWarning)
# C:\Users\azare\AppData\Local\miniconda3\envs\env_24\Lib\site-packages\statsmodels\regression\mixed_linear_model.py:2237: ConvergenceWarning: The MLE may be on the boundary of the parameter space.
#   warnings.warn(msg, ConvergenceWarning)


# %%'

