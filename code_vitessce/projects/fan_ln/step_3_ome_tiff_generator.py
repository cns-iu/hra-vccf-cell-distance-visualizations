import os
import sys
import pandas as pd
import numpy as np
import ast
from tqdm import tqdm
from skimage.draw import polygon, line
from tifffile import TiffWriter
from skimage.morphology import disk, dilation

def multiplex_img_to_ome_tiff(img_arr, channel_names, output_path, axes="CYX"):
    """
    Convert a multiplexed image to OME-TIFF.

    :param img_arr: The image as a 3D, 4D, or 5D array.
    :type img_arr: np.array
    :param list[str] channel_names: A list of channel names to include in the omero.channels[].label NGFF metadata field.
    :param str output_path: The path to save the Zarr store.
    :param str axes: The array axis ordering. By default, "CYX"
    """
    tiff_writer = TiffWriter(output_path, ome=True)
    tiff_writer.write(
        img_arr,
        metadata={
            'axes': axes,
            'Channel': {'Name': channel_names},
        },
        compression='zlib'
    )
    tiff_writer.close()


def generate_cell_mask(mask, value, vertices, is_line=False):
    if is_line:
        # Loop over pairs of vertices
        for i in range(len(vertices) - 1):
            rr, cc = line(
                int(vertices[i][1]),
                int(vertices[i][0]),
                int(vertices[i + 1][1]),
                int(vertices[i + 1][0]),
            )
            mask[rr, cc] = value
    else:
        rr, cc = polygon([v[1] for v in vertices], [v[0] for v in vertices])
        mask[rr, cc] = value


def convert_str_to_list(row):
    return [list(i) for i in ast.literal_eval(row)]


def generate_mask_arr(type_list, table, mask_shape, is_line=False):
    # initialize an empty mask for each cell type
    masks = {cell_type: np.zeros(mask_shape, dtype=np.uint8) for cell_type in type_list}
    for index, row in tqdm(table.iterrows(), total=len(table), desc="Processing rows"):
        generate_cell_mask(
            masks[row["type"]],
            color_dict[row["type"]],
            row["vertices"],
            is_line=is_line,
        )

    # Create an ordered list of masks
    mask_list = [masks[cell_type] for cell_type in type_list]

    # make the line thicker by dilation
    if is_line:
        for i in range(len(mask_list)):
            selem = disk(1)
            mask_list[i] = dilation(mask_list[i], selem)

    # Stack masks into a 3D array. The new array has shape (n, m, len(cell_types)),
    # where n and m are the dimensions of the original masks.
    bitmask_stack = np.dstack(mask_list)
    return bitmask_stack


def vertices_str2list(table, zoom_scale):
    table["vertices"] = table["vertices"].apply(convert_str_to_list)
    table["vertices"] = table["vertices"].apply(
        lambda x: [[int(i[0] * zoom_scale), int(i[1] * zoom_scale)] for i in x]
    )


# Default region_index
region_index = "LN00837"

scale = 1

# Check if at least one command-line argument is given
if len(sys.argv) >= 2:
    # Use the given argument as region_index
    region_index = sys.argv[1]
if len(sys.argv) >= 3:
    # Use the given argument as scale
    scale = float(sys.argv[2])

# Construct the path to the nuclei file
nuclei_root_path = r"D:\HubMap\LN\new_data\vitessce_raw" # CUSTOM 1
nuclei_file_name = f"Region_{region_index}_nuclei_table.csv"
link_file_name = f"Region_{region_index}_link_table.csv"
nuclei_file_path = os.path.join(nuclei_root_path, nuclei_file_name)
link_file_path = os.path.join(nuclei_root_path, link_file_name)

cell_table = pd.read_csv(nuclei_file_path)
link_table = pd.read_csv(link_file_path)

# convert the vertices column from string to list
vertices_str2list(cell_table, scale)
vertices_str2list(link_table, scale)

cell_types = ['FDC', 'ILC', 'Monocytes', 'DC_pDC', 'Endothelial', 'T_CD8+_cytotoxic',
 'Macrophages_M2', 'B_mem', 'T_CD4+_TfH_GC', 'T_TfR', 'T_CD4+_naive',
 'B_plasma', 'VSMC', 'NK', 'T_Treg', 'B_Cycling', 'B_naive', 'B_GC_DZ',
 'Macrophages_M1', 'B_GC_LZ', 'T_CD4+', 'B_preGC', 'B_activated', 'B_IFN',
 'DC_cDC2', 'T_CD4+_TfH', 'T_CD8+_naive', 'DC_CCR7+', 'T_CD8+_CD161+',
 'DC_cDC1', 'B_GC_prePB', 'T_TIM3+', 'NKT', 'Mast'] # CUSTOM 2
sorted_cell_types = sorted(cell_types)

is_link_color = False
if is_link_color:
    color_dict = {cell: idx + 1 for idx, cell in enumerate(sorted_cell_types)}
    color_dict.update(
        {cell + "_link": idx + 1 for idx, cell in enumerate(sorted_cell_types)}
    )
else:
    color_dict = {cell: idx + 1 for idx, cell in enumerate(sorted_cell_types)}
    color_dict.update(
        {
            cell + "_link": len(sorted_cell_types) + idx + 2
            for idx, cell in enumerate(sorted_cell_types)
        }
    )
color_dict["vessel"] = len(sorted_cell_types) + 1

print(color_dict)

# determine the shape of your canvas
height = (cell_table["y"].max() + 30) * scale
width = (cell_table["x"].max() + 30) * scale
shape = (height, width)
shape = tuple(map(int, shape))
print(shape)

print("Generating cell masks...")
groups = sorted(cell_table["group"].unique().tolist())
cell_mask_stack_list = []
for group in groups:
    print(f"\tGenerating {group} masks...")
    cell_types = sorted(
        cell_table[cell_table["group"] == group]["type"].unique().tolist()
    )
    filtered_cell_table = cell_table[cell_table["type"].isin(cell_types)]
    cell_mask_stack = generate_mask_arr(
        cell_types,
        filtered_cell_table,
        shape,
        is_line=True if group != "Nuclei" else False,
    )
    cell_mask = np.amax(cell_mask_stack, axis=2)[:, :, np.newaxis]
    cell_mask_stack_list.append(cell_mask)
print("Generating link masks...")
link_types = sorted(link_table["type"].unique().tolist())
link_mask_stack = generate_mask_arr(link_types, link_table, shape, is_line=True)
link_mask = np.amax(link_mask_stack, axis=2)[:, :, np.newaxis]
cell_mask_stack_list.append(link_mask)

layer_combine = True

mask_stack = np.dstack(cell_mask_stack_list)
index = groups.index("vessel")
groups[index] = "Endothelial"
groups.append("Link")
final_types = groups
assert len(final_types) == mask_stack.shape[2]

# Ensure the axes are in the CYX order by transposing the array
bitmask_arr = np.transpose(mask_stack, (2, 0, 1))

# Save the masks
print("Saving masks...")

tif_name = f"Region_{region_index}_mask.ome.tif"
multiplex_img_to_ome_tiff(
    bitmask_arr, final_types, os.path.join(nuclei_root_path, tif_name), axes="CYX"
)

# PS code
# $params = @('LN00560', 'LN00837', 'LN22921', 'LN24336', 'LN27766')

# foreach ($param in $params) {
#     Write-Host "Running python .\ome_tiff_generator.py $param"
#     python .\ome_tiff_generator.py $param
# }

# Linux pyramid commands
# $params = @('LN00560', 'LN00837', 'LN22921', 'LN24336', 'LN27766')

# foreach ($param in $params) {
#     Write-Host "Running Pyramiding $param"
#     C:\Users\yiju\Desktop\bftools\bfconvert.bat -tilex 512 -tiley 512 -pyramid-resolutions 6 -pyramid-scale 2 -compression LZW D:\HubMap\LN\new_data\vitessce_raw\Region_${param}_mask.ome.tif D:\HubMap\LN\new_data\vitessce_raw\ln_data\Region_${param}_mask.pyramid.ome.tif
# }

# C:\Users\yiju\Desktop\bftools\bfconvert.bat -tilex 512 -tiley 512 -pyramid-resolutions 6 -pyramid-scale 2 -compression LZW D:\HubMap\LN\new_data\vitessce_raw\Region_LN00837_mask.ome.tif D:\HubMap\LN\new_data\vitessce_raw\ln_data\Region_LN00837_mask.pyramid.ome.tif
