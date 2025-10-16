
# %%

# this is for 1 video.
# Let's create a heatmap for one specific video as an example.
video_to_plot = 'pod_1_ZC60' # Change this to any video_id
video_data = cp_av_ds_3[cp_av_ds_3['video_id'] == video_to_plot]

# Count the number of frames spent in each cell.
cell_counts = video_data['grid_cell'].value_counts().reset_index()
cell_counts.columns = ['grid_cell', 'count']

# %%

# the animal stood on 50 out of 100 cels in this video.
cell_counts.shape
    # Out[34]: (50, 2)]

cell_counts[:4]
    # Out[35]: 
    #   grid_cell  count
    # 0    (2, 8)    230
    # 1    (5, 1)    211
    # 2    (3, 8)    198
    # 3    (1, 8)    121

# %%

# Create an empty grid (filled with zeros) to store our heatmap data.
heatmap_data = np.zeros(GRID_SIZE).T # Transpose to match (row, col) indexing

# Fill the grid with the counts.
for _ , row in cell_counts.iterrows():
    c , r = row['grid_cell'] # c,r : column & row
    heatmap_data[ r, c ] = row['count']  # r , c were defined in the above cell.
                                            # they are the index of the grid.

# %%

heatmap_data.shape
    # Out[40]: (10, 10)

heatmap_data
    # Out[42]: 
    # array([[  0.,   0.,   0.,   6.,  68.,  18.,   0.,   0.,   0.,   0.],
    #        [  0.,   0.,   1.,  47.,  62., 211., 105.,  10.,   0.,   0.],
    #        [  0.,   1.,   2.,  47.,  61.,   4.,   3.,   0.,   0.,   0.],
    #        [  0.,   2.,   4.,   4.,   4.,   4.,   0.,   0.,   0.,   0.],
    #        [  0.,   3.,   6.,  38.,  19.,   2.,   0.,   0.,   0.,   0.],
    #        [  0.,   2.,   6.,  15.,   4.,   1.,   0.,   0.,   0.,   0.],
    #        [  0.,  29.,  34.,   5.,   1.,   0.,   0.,   0.,   0.,   0.],
    #        [  0.,  18.,  82.,  73.,   1.,   7.,   0.,   0.,   0.,   0.],
    #        [ 95., 121., 230., 198.,   9., 101.,   0.,   0.,   0.,   0.],
    #        [  0.,   2.,   8.,   1.,   3.,  16.,   0.,   0.,   0.,   0.]])


# 10 minute * 60 second/minute * 30 frames/s = 18000 frames
    # after downsampling by factor 10 : 1800 frames per video.
heatmap_data.sum()
    # Out[43]: np.float64(1794.0)

# %%

# Plot the heatmap.
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, cmap='viridis', linewidths=.5)
plt.title(f"Heatmap of Pig Location for {video_to_plot}")
plt.xlabel("Grid Column")
plt.ylabel("Grid Row")

# %%

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\vision\track\plot\roam\heatmap__pod_1_ZC60.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\vision\track\plot\roam\heatmap__pod_1_ZC60.svg' )

# %%
# %%
# %%
# %%

import random

# %%


# Assume 'df_cell_count_percentage' is your DataFrame with columns:
# 'video_id', 'grid_cell', 'count', 'percentage'
# Assume GRID_SIZE is defined, e.g., GRID_SIZE = (10, 10)
GRID_SIZE = (10, 10)


# --- 1. Select Two Random, Unique Video IDs ---
# Get a list of all unique video IDs from the DataFrame
all_video_ids = df_cell_count_percentage['video_id'].unique()

# Randomly choose 2 unique IDs from the list
videos_to_plot = random.sample(list(all_video_ids), 2)

    
print(f"Randomly selected videos to plot: {videos_to_plot}")


# --- 2. Create the Figure and Subplots (Axes) ---
# plt.subplots() is the standard way to create a figure with a grid of plots.
# It returns the figure object and an array of axes objects.
# figsize=(16, 7) sets the overall size of the figure in inches (width, height).
fig, axes = plt.subplots(1, 2, figsize=(20, 10))


# --- 3. Loop Through the Selected Videos and Plot ---
# We use enumerate to get both the index (0, 1) and the video_id.
# The index is used to select the correct subplot axis (axes[0] or axes[1]).
for i, video_id in enumerate(videos_to_plot):
    # Select the data for the current video
    video_data = df_cell_count_percentage[df_cell_count_percentage['video_id'] == video_id]
    
    #explore
    # video_data.columns
    #     # Out[59]: Index(['video_id', 'grid_cell', 'count', 'percentage'], dtype='object')
    
    # Get the current subplot axis
    ax = axes[i]
    
    # Create an empty grid to store the percentage data for the heatmap
    heatmap_data = np.zeros(GRID_SIZE).T  # Transpose to match (row, col) indexing
    
    # Fill the grid with the percentage values
    for _, row in video_data.iterrows():
        # Make sure grid_cell is a tuple before trying to unpack
        if isinstance(row['grid_cell'], tuple) and len(row['grid_cell']) == 2:
            col, r = row['grid_cell']
            heatmap_data[r, col] = row['percentage']
            
    # Draw the heatmap on the current axis 'ax'
    sns.heatmap(
                heatmap_data, 
                ax=ax,               # Crucial: This tells seaborn which subplot to draw on
                cmap='viridis',      # Color map for the heatmap
                annot=False,          # Show the percentage values on the cells
                # fmt=".1f",           # Format the annotation to one decimal place
                linewidths=.5,
                vmin=0,              # Set a fixed minimum for the color scale
                vmax=video_data['percentage'].max() , # Set a fixed max for consistent colors
                cbar_kws={'label': '% time'} # Add a label to the color bar
    )
    
    # Set the title and labels for this specific subplot
    ax.set_title(f"{video_id}")
    ax.set_xlabel("Grid Column")
    ax.set_ylabel("Grid Row")

plt.suptitle( 'Time Spent (%) on each cell of the open-field in 2 randomly selected videos' )

# --- 4. Display the Final Plot ---
# Adjust the layout to prevent titles from overlapping
plt.tight_layout()


# %%

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\vision\track\plot\roam\heatmap__random.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\vision\track\plot\roam\heatmap__random.svg' )


# %%

