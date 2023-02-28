import pandas as pd
import numpy as np

data_new = pd.read_csv('/Users/himanishah/Desktop/VCCF_Computations/doi_10.5061_dryad.pk0p2ngrf__v5/CODEX_HuBMAP_alldata_Dryad.csv')
# 'OLFM4', 'FAP', 'CD25', 'CollIV', 'CK7', 'MUC6'
# These above columns have null values : 248285, 248285, 248285, 248285, 1735783, 1214947 respectively
unique_regions = data_new.iloc[:,56].unique()
cell_types = data_new.iloc[:,64].unique()

indx_val = 56
split_source_file = '/Users/himanishah/Desktop/VCCF_Computations/doi_10.5061_dryad.pk0p2ngrf__v5/CODEX_HuBMAP_alldata_Dryad.csv'
## Take the column to split from the actual column names of data frame
column_to_split = 'unique_region'
i = 1
for label in unique_regions:
    ## Create another sub data frame using the value for the value of the column each time
    df_label = data_new[data_new[column_to_split] == label]
    ## Define target File name
    split_target_file = f"{split_source_file.replace('/doi_10.5061_dryad.pk0p2ngrf__v5/CODEX_HuBMAP_alldata_Dryad.csv', '/Intestine_64_data/Region')}_{i}.csv"

    ## Write to the file using pandas to_csv
    df_label.to_csv(split_target_file, index=False, header=True, mode='a')
    i = i +1
