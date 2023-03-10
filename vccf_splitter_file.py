import pandas as pd

"""""
Author: Himani Shah (shahhi@iu.edu)

Input: CODEX_HuBMAP_alldata_Dryad.csv file path
Output: 64 .csv files will be generated based on 'unique_region' coulumn in input file
"""""

# Give path to your data from source : https://www.biorxiv.org/content/10.1101/2021.11.25.469203v1 (High Resolution Single Cell Maps Reveals Distinct Cell Organization and Function Across Different Regions of the Human Intestine)
split_source_file = '/Users/himanishah/Desktop/VCCF_Computations/doi_10.5061_dryad.pk0p2ngrf__v5/CODEX_HuBMAP_alldata_Dryad.csv'

data_new = pd.read_csv(split_source_file)

# 'OLFM4', 'FAP', 'CD25', 'CollIV', 'CK7', 'MUC6'
# These above columns have null values : 248285, 248285, 248285, 248285, 1735783, 1214947 respectively

# Store types of unique regions before splitting
unique_regions = data_new.iloc[:,56].unique()

# Store types of cell before splitting
cell_types = data_new.iloc[:,64].unique()



# Take the column 'unique_region' to split from the actual column names of data frame
column_to_split = 'unique_region'
i = 1
for label in unique_regions:

    # Create another sub data frame using the value for the value of the column each time
    df_label = data_new[data_new[column_to_split] == label]

    # Define target File name and define path to target file
    split_target_file = f"{split_source_file.replace('/doi_10.5061_dryad.pk0p2ngrf__v5/CODEX_HuBMAP_alldata_Dryad.csv', '/Intestine_64_data/Region')}_{i}.csv"

    # Write to the file using pandas to_csv
    df_label.to_csv(split_target_file, index=False, header=True, mode='a')
    i = i +1
