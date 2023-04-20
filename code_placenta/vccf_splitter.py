import pandas as pd

"""""
Author: Himani Shah (shahhi@iu.edu)

Input: Supplementary_table_3_single_cells_updated.csv file path
Output: 209 .csv files will be generated based on 'Point' coulumn in input file
"""""

# Give path to your data 
split_source_file = '/u/shahhi/vccf_computations_data/Supplementary_table_3_single_cells_updated.csv'

data = pd.read_csv(split_source_file)

data_new = data[data['overlap_decidua'] == 1.0]
# 477747 rows out of 495349 rows left after the filter

unique_images = data_new['Point'].unique()
print(unique_images)

# Take the column 'Point' to split from the actual column names of data frame
column_to_split = 'Point'
i = 1
for label in unique_images:

    # Create another sub data frame using the value for the value of the column each time
    df_label = data_new[data_new[column_to_split] == label]

    # Define target File name and define path to target file
    split_target_file = f"{split_source_file.replace('/Supplementary_table_3_single_cells_updated.csv', '/Placenta_209_data/Image')}_{i}.csv"

    # Write to the file using pandas to_csv
    df_label.to_csv(split_target_file, index=False, header=True, mode='a')
    i = i +1
