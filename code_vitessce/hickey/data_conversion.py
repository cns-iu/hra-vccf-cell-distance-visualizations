import os
import sys
import pandas as pd
import numpy as np


def generate_cross_vertices(x, y, radius):
    # Vertices at the ends of the cross
    vertices = [
        (x, y),  # Center
        (x - radius, y),  # Left
        (x + radius, y),  # Right
        (x, y),  # Center
        (x, y + radius),  # Up
        (x, y - radius),  # Down
        (x, y),  # Center
    ]
    return vertices


def generate_cell_vertices(x, y, radius, num_vertices=12):
    angles = np.linspace(0, 2 * np.pi, num_vertices+1)
    vertices = [
        (x + np.cos(angle) * radius, y + np.sin(angle) * radius) for angle in angles
    ]
    return vertices


def generate_random_cell_vertices(x, y, radius, num_vertices=12):
    angles = np.linspace(0, 2 * np.pi, num_vertices+1)
    vertices = []
    # Add randomness to radius and angle
    random_radius = np.random.uniform(0.9 * radius, 1.1 * radius)
    for angle in angles:
        random_angle = np.random.uniform(-0.2, 0.2)  # adjust as needed
        vertices.append(
            (
                x + np.cos(angle + random_angle) * random_radius,
                y + np.sin(angle + random_angle) * random_radius,
            )
        )
    vertices.append(vertices[0])
    return vertices


def generate_link_vertices(x, y, vx, vy):
    return [(x, y), (vx, vy)]


def main():
    # Default region_index
    region_index = 3
    scale = 1
    universal_size = 8

    # Check if at least one command-line argument is given
    if len(sys.argv) >= 2:
        # Use the given argument as region_index
        region_index = int(sys.argv[1])
    if len(sys.argv) >= 3:
        # Use the given argument as scale
        scale = float(sys.argv[2])

    # Construct the path to the nuclei file
    nuclei_root_path = r"G:\HuBMAP\Hickey\Intestine_64_data\vitessce_raw"
    nuclei_file_name = f"Region_{region_index}_nuclei.csv"
    vessel_file_name = f"Region_{region_index}_vessels.csv"
    nuclei_file_path = os.path.join(nuclei_root_path, nuclei_file_name)
    vessel_file_path = os.path.join(nuclei_root_path, vessel_file_name)

    # read the vessel csv file
    vessel_df = pd.read_csv(vessel_file_path)
    # add a new 'type' column with 'vessel' as its value
    vessel_df["type"] = "vessel"
    # construct the 'cell' table for the vessel data and generate vertices
    # Here I used a fixed radius for 'vessel', adjust as needed
    vessel_df["vertices"] = vessel_df.apply(
        lambda row: generate_random_cell_vertices(row["x"], row["y"], radius=universal_size), axis=1)
    vessel_df["group"] = "vessel"
    final_cell_table = pd.concat([vessel_df], ignore_index=True)

    # read the csv file
    nuclei_df = pd.read_csv(nuclei_file_path)

    # construct the 'link' table and generate vertices
    link_table = nuclei_df[["type", "x", "y", "xv", "yv", "group"]].copy()
    link_table["vertices"] = link_table.apply(lambda row: generate_link_vertices(
        row["x"], row["y"], row["xv"], row["yv"]), axis=1)
    link_table["type"] = link_table["type"].apply(lambda x: x + "_link")

    groups = nuclei_df["group"].unique()

    for group in groups:
        # filter out the rows where type is one of the specified values
        cell_types = nuclei_df[nuclei_df["group"] == group]["type"].unique()
        filtered_df = nuclei_df[nuclei_df["type"].isin(cell_types)]

        # construct the 'cell' table and generate vertices
        cell_table = filtered_df[["type", "x", "y"]].copy()
        if group == "Epithelial":
            cell_table["vertices"] = cell_table.apply(
                lambda row: generate_cross_vertices(row["x"], row["y"], universal_size), axis=1)
        elif group == "Immune":
            cell_table["vertices"] = cell_table.apply(
                lambda row: generate_cell_vertices(row["x"], row["y"], universal_size), axis=1)
        elif group == "Stromal":
            cell_table["vertices"] = cell_table.apply(
                lambda row: generate_cell_vertices(row["x"], row["y"], universal_size, num_vertices=4), axis=1)
        else:
            print("unknown group: ", group)
        cell_table["group"] = group

        # append the vessel data to the cell_table
        final_cell_table = pd.concat(
            [final_cell_table, cell_table], ignore_index=True)

    # Save the tables to .csv files
    final_cell_table.to_csv(os.path.join(nuclei_root_path,
                                         f"Region_{region_index}_nuclei_table.csv"), index=False)
    link_table.to_csv(os.path.join(nuclei_root_path,
                      f"Region_{region_index}_link_table.csv"), index=False)


if __name__ == "__main__":
    main()
