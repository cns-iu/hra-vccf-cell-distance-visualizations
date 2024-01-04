import pandas as pd

# Pre-defined list of 30 colors [RGB tuples]
color_list = [
    [31, 119, 180],  # Blue
    [255, 127, 14],  # Orange
    [44, 160, 44],  # Green
    [214, 39, 40],  # Red
    [148, 103, 189],  # Purple
    [140, 86, 75],  # Brown
    [227, 119, 194],  # Pink
    [127, 127, 127],  # Gray
    [188, 189, 34],  # Olive
    [23, 190, 207],  # Cyan
    [174, 199, 232],  # Light Blue
    [255, 187, 120],  # Light Orange
    [152, 223, 138],  # Light Green
    [255, 152, 150],  # Light Red
    [197, 176, 213],  # Light Purple
    [196, 156, 148],  # Light Brown
    [247, 182, 210],  # Light Pink
    [199, 199, 199],  # Light Gray
    [219, 219, 141],  # Light Olive
    [158, 218, 229],  # Light Cyan
    [255, 127, 14],  # Orange
    [44, 160, 44],  # Green
    [31, 119, 180],  # Blue
    [214, 39, 40],  # Red
    [148, 103, 189],  # Purple
    [227, 119, 194],  # Pink
    [140, 86, 75],  # Brown
    [127, 127, 127],  # Gray
    [188, 189, 34],  # Olive
    [23, 190, 207],  # Cyan
]


def generate_obs_set_color(cell_types, use_link, csv_path=None):
    sorted_cell_types = sorted(cell_types)
    obs_set_color = []
    cell_data = {"cell_id": [], "cell_type": [], "cell_color": []}

    # Assign colors and create entries for cells and links
    for i, cell_type in enumerate(sorted_cell_types, start=1):  # Start from 1
        color = color_list[i % len(color_list)]
        # Special case for "Endothelial"
        if cell_type == "Blood endothelial":
            color = [255, 0, 0]  # Red color for Endothelial

        # Add cell information
        obs_set_color.append({"path": ["Cell Type", cell_type], "color": color})
        cell_data["cell_id"].append(i)
        cell_data["cell_type"].append(cell_type)
        cell_data["cell_color"].append(str(color).replace('(', '[').replace(')', ']'))
    
    cell_data["cell_id"].append(1 + len(sorted_cell_types))
    cell_data["cell_type"].append('Blood endothelial')
    cell_data["cell_color"].append('[255, 0, 0]')

        # Add link information if applicable
    if use_link:
        for i, cell_type in enumerate(sorted_cell_types, start=1):  # Start from 1
            color = color_list[i % len(color_list)]
            obs_set_color.append({"path": ["Cell Type", cell_type + "_link"], "color": color})
            cell_data["cell_id"].append(i + 1 + len(sorted_cell_types))  # Same ID for the link
            cell_data["cell_type"].append(cell_type + "_link")
            cell_data["cell_color"].append(str(color).replace('(', '[').replace(')', ']'))

    # Save to CSV if a path is provided
    if csv_path:
        cell_sets_data = pd.DataFrame(cell_data)
        cell_sets_data.to_csv(csv_path, index=False)
        print(f"Saved to {csv_path}")

    return obs_set_color


def main():
    cell_types = [
        "B",
        "CD4",
        "CD8_T",
        "DC",
        "Goblet",
        "Neutrophil",
        "Endothelial",
    ]  # Add more cell types as needed
    use_link = True

    obs_set_color = generate_obs_set_color(cell_types, use_link, "cell_sets.csv")


if __name__ == "__main__":
    main()
