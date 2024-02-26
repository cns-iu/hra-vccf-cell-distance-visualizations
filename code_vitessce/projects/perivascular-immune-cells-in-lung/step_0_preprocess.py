import pandas as pd
import os

# root path
root_path = r"G:\HuBMAP\gloria" # CUSTOM 1

# List of filenames 
filenames = [
    "D11540.csv", 
    "D26512.csv",
    "D26511.csv", 
] # CUSTOM 2

# Read CSV files, add filename column, and combine
df_list = []
for filename in filenames:
    df = pd.read_csv(os.path.join(root_path, filename))
    # preview csv file contents
    # pd.set_option('display.max_columns', None)
    # print(df.head())
    # exit()
    # Extract CRCXXXXX part from the filename
    region_code = filename.split('.')[0].split('_')[0] # CUSTOM 3
    # keep columns named
    columns_to_keep = ['Centroid X µm', 'Centroid Y µm', 'Cell Type']
    # Select only the specified columns
    df = df[columns_to_keep]
    df['Region'] = region_code # CUSTOM 4    
    df_list.append(df)

combined_df = pd.concat(df_list, ignore_index=True)
combined_df['Cell Type'] = combined_df['Cell Type'].replace('Endothelial Cell', 'Endothelial')

# rename column cell_type_A to Cell Type
combined_df.rename(columns={"Cell Type": "Cell Type"}, inplace=True)
combined_df.rename(columns={"Centroid X µm": "x"}, inplace=True)
combined_df.rename(columns={"Centroid Y µm": "y"}, inplace=True)
combined_df.rename(columns={"Region": "Layer"}, inplace=True)

# Write back to the combined csv file
combined_csv_path = os.path.join(root_path, "combined_cells.csv")
combined_df.to_csv(combined_csv_path, index=False)

print(f"Combined CSV file created at: {combined_csv_path}")
