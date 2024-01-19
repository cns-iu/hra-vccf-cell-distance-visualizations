import pandas as pd
import os

# root path
root_path = r"D:\HubMap\LN" # CUSTOM 1

# List of filenames 
filenames = [
    "LN00837_celltype_location.csv", 
    "LN27766_celltype_location.csv", 
    "LN00560_celltype_location.csv", 
    "LN24336_celltype_location.csv", 
    "LN22921_celltype_location.csv"
] # CUSTOM 2

# Read CSV files, add filename column, and combine
df_list = []
for filename in filenames:
    df = pd.read_csv(os.path.join(root_path, filename))
    # Extract CRCXXXXX part from the filename
    crc_code = filename.split('.')[0].split('_')[0] # CUSTOM 3
    df['Layer'] = crc_code # CUSTOM 4
    df_list.append(df)

combined_df = pd.concat(df_list, ignore_index=True)
combined_df['celltype'] = combined_df['celltype'].replace('Endo', 'Endothelial')

# rename column cell_type_A to Cell Type
combined_df.rename(columns={"celltype": "Cell Type"}, inplace=True)
combined_df.rename(columns={"x": "x"}, inplace=True)
combined_df.rename(columns={"y": "y"}, inplace=True)    
combined_df.rename(columns={"cell_size": "Size"}, inplace=True)
combined_df.rename(columns={"Layer": "Layer"}, inplace=True)

# Write back to the combined csv file
combined_csv_path = os.path.join(root_path, "combined_cells.csv")
combined_df.to_csv(combined_csv_path, index=False)

print(f"Combined CSV file created at: {combined_csv_path}")
