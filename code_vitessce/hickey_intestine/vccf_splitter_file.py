import pandas as pd

"""""
Author: Himani Shah (shahhi@iu.edu)

Input: CODEX_HuBMAP_alldata_Dryad.csv file path
Output: 64 .csv files will be generated based on 'unique_region' coulumn in input file
"""""

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

"""""

# Give path to your data from source : https://datadryad.org/stash/landing/show?id=doi%3A10.5061%2Fdryad.g4f4qrfrc
# (CODEX multiplexed imaging cell datasets used for using STELLAR to transfer cell type annotations to other tissues and donors)
split_source_file = r'G:\HuBMAP\Hickey\B004_training_dryad.csv'

data_new = pd.read_csv(split_source_file)

# 'OLFM4', 'FAP', 'CD25', 'CollIV', 'CK7', 'MUC6'
# These above columns have null values : 248285, 248285, 248285, 248285, 1735783, 1214947 respectively

# Store types of unique regions before splitting
# column is "unique_region"
unique_regions = data_new['unique_region'].unique()

# Store types of cell before splitting
cell_types = data_new['cell_type_A'].unique()

# Take the column 'unique_region' to split from the actual column names of data frame
column_to_split = 'unique_region'

for label in unique_regions:

    # Create another sub data frame using the value for the value of the column each time
    df_label = data_new[data_new[column_to_split] == label]

    # Define target File name and define path to target file
    split_target_file = f"{split_source_file.replace('B004_training_dryad.csv', 'intestine_new_data/Region')}_{label}.csv"

    # Write to the file using pandas to_csv
    df_label.to_csv(split_target_file, index=False, header=True, mode='w')
    
    # print the progress
    print(f"File {split_target_file} written successfully")
