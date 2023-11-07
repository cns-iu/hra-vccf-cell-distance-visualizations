import pandas as pd
import os

"""""
Author: Himani Shah (shahhi@iu.edu)

Input: CODEX_HuBMAP_alldata_Dryad.csv file path
Output: 64 .csv files will be generated based on 'unique_region' coulumn in input file
""" ""

"""""
Data description:

We performed CODEX (co-detection by indexing) multiplexed imaging on 24 sections of the human intestine from 3 donors 
(B004, B005, B006) using a panel of 47 oligonucleotide-barcoded antibodies. We also performed CODEX imaging on both 
human tonsil and Barrett's esophagus (BE) using a panel of 57 oligonucleotide-barcoded antibodies.  Subsequently images
underwent standard CODEX image processing (tile stitching, drift compensation, cycle concatenation, background 
subtraction, deconvolution, and determination of best focal plane), single cell segmentation, and column marker 
z-normalization by tissue. Output of this process were dataframes of 870,000 cells and 220,000 cells respectively with
fluorescence values quantified from each marker.

The overall structure of the datasets are individual cells segmented out in each row. Then there are columns for the 
X, Y position in pixels in the overall montage image of the dataset. There are also columns to indicate which region 
the data came from. There are also cell type labels generated from expert annotations. The other columns are the values
of the antibody staining the target protein within the tissue quantified at the single-cell level. This value is the 
per cell/area averaged fluorescent intensity that has subsequently been z normalized along each column as described above.
 
For the B004_training_dryad.csv dataset, data from donor B004 was expert annotated for cell types within the small intestine
and colon (~250,000 cells) and contains cell type labels in addition to protein marker expressions and x, y positions. Each 
donor has 4 regions from the colon and 4 regions from the small intestine. For the intra-region comparisons we looked at 
B004 regions in the colon with training 3 regions and then predicting on the fourth.

For the B0056_unnanotated_dryad.csv dataset, data from donors B005 and B006 were unnanotated samples we transferred cell 
type labels to from the B004 training dataset. This means that B0056 has the quantified and preprocessed single-cell 
quantified protein expression with x, y positions from CODEX imaging, but no cell type annotation labels associated yet. 

For the BE_Tonsil_l3.dryad.csv dataset, the tonsil and BE datasets were expert annotated for cell types from CODEX 
multiplexed imaging. The tonsil datatset was used as training to predict cell type labels in the BE dataset. 

We also include a preconstructed graph for the tonsil and BE datasets so that running a demo example of STELLAR found on 
our github (https://github.com/snap-stanford/stellar) runs faster and is included as supplementary data. 

""" ""

# Give path to your data from source : https://datadryad.org/stash/landing/show?id=doi%3A10.5061%2Fdryad.g4f4qrfrc
# (CODEX multiplexed imaging cell datasets used for using STELLAR to transfer cell type annotations to other tissues and donors)
root_path = r"G:\HuBMAP\Hickey"
file_name = r"BE_Tonsil_l3_dryad.csv"
split_source_file = os.path.join(root_path, file_name)

data_new = pd.read_csv(split_source_file)

# 'OLFM4', 'FAP', 'CD25', 'CollIV', 'CK7', 'MUC6'
# These above columns have null values : 248285, 248285, 248285, 248285, 1735783, 1214947 respectively

# Store types of unique regions before splitting
# column is "unique_region"
unique_regions = data_new["sample_name"].unique()

# Store types of cell before splitting
cell_types = data_new["cell_type"].unique()
print(cell_types)

# Take the column 'unique_region' to split from the actual column names of data frame
column_to_split = "sample_name"

for label in unique_regions:
    # Create another sub data frame using the value for the value of the column each time
    df_label = data_new[data_new[column_to_split] == label]

    # Define target File name and define path to target file
    split_target_file = f"{split_source_file.replace(file_name, 'intestine_new_data/Region')}_{label}.csv"

    # Write to the file using pandas to_csv
    df_label.to_csv(split_target_file, index=False, header=True, mode="w")

    # print the progress
    print(f"File {split_target_file} written successfully")


import math
import os
import warnings

warnings.simplefilter("ignore")

for label in unique_regions:
    # Get the path to respective Image
    root_path = r"G:\HuBMAP\Hickey\intestine_new_data"
    path = root_path + rf"/Region_{label}.csv"
    df_Region_1 = pd.read_csv(path)

    # Get coordinates x, y, Cell subtype and cellType (2D Data)
    df_Region_1 = df_Region_1[["x", "y", "cell_type"]]

    # rename column cell_type_A to Cell Type
    df_Region_1.rename(columns={"cell_type": "Cell Type"}, inplace=True)

    # Calculate μm per px
    # By dividing 4000/4536 = 0.881 and can also be 4000/4704 = 0.849, as Image size is 16mmx16mm and Image in pixel is 4704px x 4536px
    micro_per_pixel = 0.866  # Taking avg if both possibilities
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

    # Calculating nearest endothelial cell
    for i in range(len(x_list)):
        # (Source) Weber GM, Ju Y, Börner K. Considerations for Using the Vasculature as a Coordinate System to Map All the Cells in the Human Body. Front Cardiovasc Med. 2020 Mar 13;7:29. doi: 10.3389/fcvm.2020.00029. PMID: 32232057; PMCID: PMC7082726.
        min_dist = 1000  # The distance can be atmost 1mm so that cells can get oxygen
        has_near = False
        for j in range(len(xv_list)):
            if (
                abs(x_list[i] - xv_list[j]) < min_dist
                and abs(y_list[i] - yv_list[j]) < min_dist
            ):
                # Euclidean distance calculation
                dist = math.sqrt(
                    (x_list[i] - xv_list[j]) ** 2 + (y_list[i] - yv_list[j]) ** 2
                )
                if dist < min_dist:
                    has_near = True
                    min_dist = dist
                    temp_x = xv_list[j]
                    temp_y = yv_list[j]
        new_x.append(temp_x)
        new_y.append(temp_y)
        # If no endothelial cells within 1000μm distance then assign -1
        if has_near == False:
            new_dist.append(-1)
        else:
            new_dist.append(min_dist)

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
            "type": df_Region_1_immmune["Cell Type"],
            "group": "Immune",
        }
    )
    df.to_csv(
        os.path.join(root_path, "vitessce_raw", f"Region_{label}_nuclei.csv"),
        index=False,
    )


# call generate_obs_set_color in cell_data_view_generator.py
import cell_data_view_generator as cdvg

cdvg.generate_obs_set_color(cell_types, use_link=True, csv_path="cell_sets.csv")
