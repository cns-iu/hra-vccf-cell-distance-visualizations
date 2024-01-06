import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

# Remove the top 1% of the data to exclude outliers
percentile_99 = np.percentile(data['distance'], 99.5)
data_filtered = data[data['distance'] <= percentile_99]

# Assuming data['distance'] is your data series
bin_width = 5
bin_range = np.arange(start=data_filtered['distance'].min(), 
                      stop=data_filtered['distance'].max() + bin_width, step=bin_width)

# Create the base figure and the first axis for the histogram
plt.figure(figsize=(10, 6))
# ax = plt.hist(data_filtered['distance'], bins=bin_range, alpha=0.4, label='All Cells')
ax = data_filtered['distance'].plot.hist(bins=bin_range, density=False, edgecolor='w', linewidth=0.5, alpha=0.3, label='All Cells')
plt.xlabel('Distance')
plt.ylabel('Frequency of Cells')
# plt.title('VCCF Histogram of Cell Distances [All / Top 5]')
plt.grid(True)

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

# Draw the density curves on the second y-axis and find the maximum density value
for cell_type in top_types:
    subset = data_filtered[data_filtered['type'] == cell_type]
    # Plot pandas KDE
    # subset['distance'].plot.density(alpha=0.5, ax=ax) # same as df['var'].plot.kde()
    subset['distance'].hist(bins=bin_range, density=False, linewidth=1.5, alpha=0.6, ax=ax, label=cell_type, histtype='step')

ax.set_xlim(xlim)

# based on top_5_types counts, the length of the legend_col should be calculated to make sure each column has no more than 10 items
legend_col = len(top_types) // 15 + 1
if legend_col == 1:
    plt.legend()
else:
    plt.legend(ncol=legend_col)

plt.margins(0,0)
plt.show()