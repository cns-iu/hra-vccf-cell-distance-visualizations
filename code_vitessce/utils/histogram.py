import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from collections import Counter
from scipy.stats import gaussian_kde

# Function to load your data
def load_data(path):
    # Replace the following line with the actual path to your CSV file
    data = pd.read_csv(path)
    return data

file_path = r'G:\HuBMAP\spleen\new_data\vitessce_raw\Region_FSLD_nuclei.csv'
um_factor = 1.0

# read sys arg from command line
if len(sys.argv) >= 2:
    # Use the given argument as region_index
    file_path = sys.argv[1]
if len(sys.argv) >= 3:
    # Use the given argument as scale
    um_factor = float(sys.argv[2])

# Load the data
data = load_data(file_path)

# print total number of cells
print(f"Total number of cells: {len(data)}")

# Calculate the distance from the cell to the nearest blood vessel
data['distance'] = np.sqrt((data['x'] - data['xv'])**2 + (data['y'] - data['yv'])**2)

# distance * um_factor
data['distance'] = data['distance'] * um_factor

# remove those lines who distance is 0
data = data[data['distance'] != 0]

# Remove the top 1% of the data to exclude outliers
percentile_99 = np.percentile(data['distance'], 99.5)
data_filtered = data[data['distance'] <= percentile_99]

# Assuming data['distance'] is your data series
bin_width = 5
bin_range = np.arange(# start=data_filtered['distance'].min(), 
                      start=0,
                      stop=data_filtered['distance'].max() + bin_width, step=bin_width)

legend_handle = []

# Create the base figure and the first axis for the histogram
plt.figure(figsize=(10, 6))
# ax = plt.hist(data_filtered['distance'], bins=bin_range, alpha=0.4, label='All Cells')
ax = data_filtered['distance'].plot.hist(bins=bin_range, density=False, color='grey',
                                         edgecolor='w', linewidth=0.5, alpha=0.4, label='All Cells')
legend_handle.append(ax.patches[0])
# legend_handle.append(mpatches.Patch(color = ax.patches[0].get_facecolor(), edgecolor='w', label='All Cells'))
plt.xlabel(u'Distance (\u03bcm)')
plt.ylabel('Number of Cells')
# plt.title('VCCF Histogram of Cell Distances [All / Top 5]')
# plt.grid(False)

# Save default x-axis limits for final formatting because the pandas kde
# plot uses much wider limits which usually decreases readability
xlim = ax.get_xlim()

# Find the 5 most frequent cell types in the filtered data
top_types_count = Counter(data_filtered['type']).most_common()
print(top_types_count)
original_len = len(top_types_count)

# if type is larger than 20, than remove any cell count that is less than 0.5% of the total count
if len(top_types_count) > 20:
    top_types_count = [type_ for type_ in top_types_count if type_[1] > len(data_filtered) * 0.005]
    # print how many cell types are removed
    print(f"Removed {original_len - len(top_types_count)} cell types < 0.5% of total count")
elif len(top_types_count) > 40:
    top_types_count = [type_ for type_ in top_types_count if type_[1] > len(data_filtered) * 0.01]
    # print how many cell types are removed
    print(f"Removed {original_len - len(top_types_count)} cell types < 1% of total count")

top_types = [type_[0] for type_ in top_types_count]

# Use 'tab10/Dark2/Set3' colormap
base_colors = plt.cm.tab10(np.linspace(0, 1, 10)) 
additional_colors1 = plt.cm.Dark2(np.linspace(0, 1, 8)) # Example to add more colors
additional_colors2 = plt.cm.Set3(np.linspace(0, 1, 12)) # Example to add more colors
all_colors = np.vstack([base_colors, additional_colors1, additional_colors2])  # Combine the color arrays


# Draw the density curves on the second y-axis and find the maximum density value
for i in range(len(top_types)):
    cell_type = top_types[i]
    line_color = all_colors[i]
    subset = data_filtered[data_filtered['type'] == cell_type]
    # Plot pandas KDE
    # subset['distance'].plot.density(alpha=0.5, ax=ax) # same as df['var'].plot.kde()
    sub_ax = subset['distance'].hist(color=line_color ,bins=bin_range, density=False, linewidth=1.5, alpha=0.75, ax=ax, label=cell_type, histtype='step')
    legend_handle.append(mpatches.Patch(facecolor=line_color, edgecolor='none',label=cell_type))

ax.set_xlim(xlim)

# based on top_5_types counts, the length of the legend_col should be calculated to make sure each column has no more than 10 items
legend_col = len(top_types) // 15 + 1
plt.legend(handles=legend_handle, ncol=legend_col)

plt.margins(0,0)
plt.show()