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
    obs_set_color = []
    for i, cell_type in enumerate(cell_types):
        # Special case for "Endothelial"
        if cell_type == "Endothelial":
            # Red color for Endothelial
            obs_set_color.append(
                {"path": ["Cell Type", cell_type], "color": (255, 0, 0)}
            )
        else:
            color = color_list[i % len(color_list)]
            obs_set_color.append({"path": ["Cell Type", cell_type], "color": color})
            if use_link:
                obs_set_color.append(
                    {"path": ["Cell Type", cell_type + "_link"], "color": color}
                )
    if csv_path:
        save_to_csv(obs_set_color, filename=csv_path)
        print(f"Saved to {csv_path}")
    return obs_set_color


def save_to_csv(obs_set_color, filename="cell_sets.csv"):
    cell_data = {"cell_id": [], "cell_type": [], "cell_color": []}

    for idx, item in enumerate(obs_set_color, 1):
        cell_data["cell_id"].append(idx)
        cell_data["cell_type"].append(item["path"][1])
        cell_data["cell_color"].append(item["color"])

    cell_sets_data = pd.DataFrame(cell_data)
    cell_sets_data.to_csv(filename, index=False)


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
