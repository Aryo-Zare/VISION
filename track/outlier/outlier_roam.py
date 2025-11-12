


# %%

# Define a custom palette for the hue levels in the desired order
custom_palette = { 
                    "DBD-HTK": "green", 
                    "DBD-Omnisol": "blue", 
                    'DCD-HTK' : 'black' ,
                    "NMP": "red" 
}


# %%

# Create a FacetGrid where each facet corresponds to a specific metric
g = sns.FacetGrid( 
                    df_track_tidy_roam_2 , 
                    col="metric", 
                    col_wrap=1, 
                    sharex=False , 
                    sharey=False ,  # this value is True by default !! : change it to False !!
                    height=6, 
                    aspect=1.6
)

# %%'

# g
# pointplot
g.map_dataframe( 
                    sns.stripplot ,      # pointplot
                    x='time' , 
                    y='value' ,  # 'value' or 'value_bc'
                    hue="treatment",
                    palette=custom_palette ,
                    marker="o" ,  
                    # estimator='mean' ,    
                    # errorbar='sd' ,
                    dodge= 0.2
) 

# %% Legend

g.add_legend()  # , bbox_to_anchor=(1.05, 0.5), borderaxespad=0 , loc='center left'

g._legend.set_title("" )  # group _ the original legend title is the column name ( treatment )

# Increase the font size of the legend title
# g._legend.get_title().set_fontsize(20)  # Adjust the size as needed

for text in g._legend.texts:
    text.set_fontsize(20)  # Adjust as needed


# %%'

# # Add a legend to clearly indicate which color corresponds to which group.
# g.add_legend()  # , bbox_to_anchor=(1.05, 0.5), borderaxespad=0 , loc='center left'
# g._legend.set_title("group" )
# # Increase the font size of the legend title
# g._legend.get_title().set_fontsize(20)  # Adjust the size as needed

# for text in g._legend.texts:
#     text.set_fontsize(20)  # Adjust as needed

# %%'

for ax in g.axes.flat:
    plt.setp(ax.get_xticklabels(), rotation=45, fontsize=16)

# Remove automatic axis ( row & column in the grid ) labels from all subplots
g.set_axis_labels("", "")

# Set the x-axis label for the bottom-right subplot to "stage"
g.axes.flat[-1].set_xlabel("Time" , loc='right' , fontsize=24 )

# %%'

# as this rewrites the tiles :
    # first check the plot without running this cell to make sure each plot corresponds to your desired order-title.

new_titles = [ 
                    'percent time animal resided in the inner-zone', 
                    'percentage of total number of grid-cells walked', 
                    'uniformity index'
            ]

for ax , i in zip( g.axes.flat , new_titles ):
    ax.set_title( i , fontsize=20 )

# %%'

unit = [ '% time' , '% grid-cells' , '' ]

for ax , i in zip( g.axes.flat , unit ) :
    ax.set_ylabel( i , loc='top' , fontsize=20 )

# %%'

# x= : the x location of the text in figure coordinates.
plt.suptitle( 'Roaming behavior of animal in the open-field' , x=0.4 , fontsize=24 )

# %% add subplot indexing letters

# add subplot indexing letters.

# import string

# Suppose g is your FacetGrid / catplot result
# this works for any number of subplots : you do not need to right a list of letter numbers based on the number of subplots.
letters = list(string.ascii_uppercase)  # ['A','B','C','D',...]

# ha , va : text alignment relative to the (x, y) coordinates you gave :
    # ha='right' means the right edge of the letter is anchored at x=-0.1.
    # va='bottom' means the bottom edge of the letter is anchored at y=1.05.
# That combination places the letter just above and slightly to the left of the subplot, with the text extending leftward and upward from that anchor point.
for ax, letter in zip(g.axes.flatten(), letters):
    ax.text(
            -0.1, 1.05, letter,        # position relative to each axis.
            transform=ax.transAxes,    # use axes fraction coords
            fontsize=20, fontweight='bold',
            va='bottom', ha='right'
    )

# transform=ax.transAxes :
    # By default, when you call ax.text(x, y, ...), Matplotlib interprets x and y in data coordinates (the same units as your plotted data).
        # Example: if your y‑axis goes from 0 to 100, then ax.text(0, 120, "label") would place text above the data range.
    # transform=ax.transAxes tells Matplotlib: “Interpret (x, y) in axes fraction coordinates instead of data coordinates.”
        # In this coordinate system:
            # (0, 0) = bottom‑left corner of the subplot’s axes
            # (1, 1) = top‑right corner of the subplot’s axes
        # Values can go slightly outside that range (e.g. -0.1, 1.05) to nudge text just beyond the axes.

# %%'

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.82 , 1] )

# %%'

# bc : baseline corrected

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\vision\track\plot\outlier\outlier_roam_2.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\vision\track\plot\outlier\outlier_roam_2.svg' )

# %%'
# %%

import plotly.express as px

# %%

# you should explicitly set the x-axis order.
    # plotly does not undertand pandas cat orders !
# Get the correct category order from your DataFrame
time_order = df_track_tidy_roam_2['time'].cat.categories.tolist()
# time_order
#     # Out[27]: ['retrain_2', 'pod_1', 'pod_3', 'pod_4', 'pod_7']

# This one command replaces your entire FacetGrid and g.map_dataframe code
fig = px.strip(
    df_track_tidy_roam_2,
    x='time',
    y='value',
    color='treatment',      # Replaces 'hue'
    facet_row='metric',     # Replaces 'col' (facet_row is often better for long plots)
    hover_data=['video_id'], # <-- This is the magic!
    color_discrete_map=custom_palette , # Pass your palette here
    category_orders={'time': time_order}  # Explicitly set the x-axis order
)

# This updates the y-axes to be independent, just like your 'sharey=False'
fig.update_yaxes(matches=None)
# This shows the plot in your notebook or a new browser tab

# %%

file_path = r'F:\OneDrive - Uniklinik RWTH Aachen\vision\track\plot\outlier\outlier_roam_2.html'
fig.write_html(file_path)


# %%

