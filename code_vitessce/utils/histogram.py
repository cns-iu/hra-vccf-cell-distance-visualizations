import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from scipy.stats import gaussian_kde

# Function to load your data
def load_data():
    # Replace the following line with the actual path to your CSV file
    data = pd.read_csv(r'G:\HuBMAP\spleen\new_data\vitessce_raw\Region_FSLD_nuclei.csv')
    return data

# Load the data
data = load_data()

# Calculate the distance from the cell to the nearest blood vessel
data['distance'] = np.sqrt((data['x'] - data['xv'])**2 + (data['y'] - data['yv'])**2)

# Remove the top 1% of the data to exclude outliers
percentile_99 = np.percentile(data['distance'], 99.5)
data_filtered = data[data['distance'] <= percentile_99]

# Assuming data['distance'] is your data series
bin_width = 10
bin_range = np.arange(start=data_filtered['distance'].min(), 
                      stop=data_filtered['distance'].max() + bin_width, step=bin_width)

# Create the base figure and the first axis for the histogram
plt.figure(figsize=(10, 6))
ax1 = plt.gca()  # Get current axis
ax1.hist(data_filtered['distance'], bins=bin_range, alpha=0.4, label='All Cells')
ax1.set_xlabel('Distance')
ax1.set_ylabel('Frequency of All Cells')
ax1.set_title('Histogram of Cell Distances to Nearest Blood Vessel')
plt.grid(True)

# Find the 5 most frequent cell types in the filtered data
top_5_types = Counter(data_filtered['type']).most_common(5)
top_5_types = [type_[0] for type_ in top_5_types]

# Create a second y-axis for the density curves
ax2 = ax1.twinx()
ax2.set_ylabel('Frequency of Top 5 cells')

# Initialize a variable to store the maximum density value
max_density_value = 0

# Draw the density curves on the second y-axis and find the maximum density value
for cell_type in top_5_types:
    subset = data_filtered[data_filtered['type'] == cell_type]
    density = gaussian_kde(subset['distance'])
    xs = np.linspace(0, percentile_99, 200)
    scale_factor = len(subset)  # The count of observations for each cell type
    scaled_density = density(xs) * scale_factor
    ax2.plot(xs, scaled_density, label=f'{cell_type}')
    max_density_value = max(max_density_value, max(scaled_density))

# Set the y-axis limit of ax2
ax2.set_ylim(0, max_density_value * 3)

# Add legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()