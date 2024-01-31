import pandas as pd
import os

# CUSTOM 1
root_path = r"G:\HuBMAP\gloria"
file_name = r"combined_cells.csv"
split_source_file = os.path.join(root_path, file_name)

data_new = pd.read_csv(split_source_file)

unique_regions = data_new["Layer"].unique()

# Store types of cell before splitting
cell_types = data_new["Cell Type"].unique()
print(cell_types)

# call generate_obs_set_color in cell_data_view_generator.py
import cell_data_view_generator as cdvg

cdvg.generate_obs_set_color(cell_types, use_link=True, csv_path="cell_sets.csv")

# Take the column 'unique_region' to split from the actual column names of data frame
column_to_split = "Layer"

for label in unique_regions:
    # Create another sub data frame using the value for the value of the column each time
    df_label = data_new[data_new[column_to_split] == label]

    # Define target File name and define path to target file
    split_target_file = f"{split_source_file.replace(file_name, 'new_data/Region')}_{label}.csv"

    # Write to the file using pandas to_csv
    df_label.to_csv(split_target_file, index=False, header=True, mode="w")

    # print the progress
    print(f"File {split_target_file} written successfully")


import os
import warnings
from tqdm import tqdm
import numpy as np

warnings.simplefilter("ignore")

root_path = os.path.join(root_path, "new_data")

for label in unique_regions:
    # Get the path to respective Image
    path = root_path + rf"/Region_{label}.csv"
    df_Region_1 = pd.read_csv(path)

    # Get coordinates x, y, Cell subtype and cellType (2D Data)
    df_Region_1 = df_Region_1[["x", "y", "Cell Type"]]

    # Calculate μm per px
    # By dividing 4000/4536 = 0.881 and can also be 4000/4704 = 0.849, as Image size is 16mmx16mm and Image in pixel is 4704px x 4536px
    micro_per_pixel = 1  # Taking avg if both possibilities
    scale = micro_per_pixel  # to convert given pixel in micro meter unit
    df_Region_1["x"] = scale * df_Region_1["x"]
    df_Region_1["y"] = scale * df_Region_1["y"]

    # Create two data frames each for endothelial cells and all other cells
    df_Region_1_vessel = df_Region_1.loc[df_Region_1["Cell Type"] == "Endothelial"]
    df_Region_1_immmune = df_Region_1.loc[df_Region_1["Cell Type"] != "Endothelial"]

    # Define list variables to store
    x_list = []
    y_list = []
    xv_list = []
    yv_list = []
    new_x = []
    new_y = []
    new_dist = []

    # Storing the scaled values
    x_list = df_Region_1_immmune["x"].values.tolist()
    y_list = df_Region_1_immmune["y"].values.tolist()
    xv_list = df_Region_1_vessel["x"].values.tolist()
    yv_list = df_Region_1_vessel["y"].values.tolist()

    print(len(x_list), len(y_list))
    print(len(xv_list), len(yv_list))
    temp_x = 0
    temp_y = 0    
    
    # new calculation
    # Convert your lists to NumPy arrays
    x_list_np = np.array(x_list)
    y_list_np = np.array(y_list)
    xv_list_np = np.array(xv_list)
    yv_list_np = np.array(yv_list)

    # Preallocate arrays for results
    new_x = np.empty_like(x_list_np)
    new_y = np.empty_like(y_list_np)
    new_dist = np.empty_like(x_list_np, dtype=float)

    # Calculating nearest endothelial cell
    for i in tqdm(range(len(x_list_np)), desc="Processing"):
        min_dist = 250  # The distance can be at most 1mm so that cells can get oxygen
        has_near = False
        
        # Compute squared differences
        dx = x_list_np[i] - xv_list_np
        dy = y_list_np[i] - yv_list_np
        dist_squared = dx**2 + dy**2
        
        # Find the index of the closest cell
        valid_indices = np.where(dist_squared < min_dist**2)[0]
        if valid_indices.size > 0:
            closest_index = valid_indices[dist_squared[valid_indices].argmin()]
            has_near = True
            min_dist = np.sqrt(dist_squared[closest_index])
            new_x[i] = xv_list_np[closest_index]
            new_y[i] = yv_list_np[closest_index]
        else:
            new_x[i] = x_list_np[i]
            new_y[i] = y_list_np[i]
            new_dist[i] = -1

        if has_near:
            new_dist[i] = min_dist
        else:
            new_dist[i] = -1

    x_min, x_max = min(x_list), max(x_list)
    y_min, y_max = min(y_list), max(y_list)

    margin_index = 0.05
    x_margin = (x_max - x_min) * margin_index
    y_margin = (y_max - y_min) * margin_index

    # Add values to new columns keeping track of nearest endothelial cell coordinates
    df_Region_1_immmune["XV"] = new_x
    df_Region_1_immmune["YV"] = new_y
    df_Region_1_immmune["MinDistance"] = new_dist

    # Save the data frame to csv file for vitessce
    df = pd.DataFrame(
        {
            "x": xv_list,
            "y": yv_list,
        }
    )
    df.to_csv(
        os.path.join(root_path, "vitessce_raw", f"Region_{label}_vessels.csv"),
        index=False,
    )

    df = pd.DataFrame(
        {
            "x": x_list,
            "y": y_list,
            "xv": new_x,
            "yv": new_y,
            'distance': new_dist,
            "type": df_Region_1_immmune["Cell Type"],
            "group": "Nuclei",
        }
    )
    df.to_csv(
        os.path.join(root_path, "vitessce_raw", f"Region_{label}_nuclei.csv"),
        index=False,
    )