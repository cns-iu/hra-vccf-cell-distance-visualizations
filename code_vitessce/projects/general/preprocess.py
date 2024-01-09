import pandas as pd
import os

# root path
root_path = r"G:\HuBMAP\colon_3d" # CUSTOM 1

# List of filenames 
filenames = [
    "Celltype_CRC01002.csv", "Celltype_CRC01007.csv", "Celltype_CRC01014.csv", 
    "Celltype_CRC01020.csv", "Celltype_CRC01025.csv", "Celltype_CRC01029.csv", 
    "Celltype_CRC01034.csv", "Celltype_CRC01039.csv", "Celltype_CRC01044.csv", 
    "Celltype_CRC01049.csv", "Celltype_CRC01050.csv", "Celltype_CRC01051.csv", 
    "Celltype_CRC01052.csv", "Celltype_CRC01054.csv", "Celltype_CRC01059.csv", 
    "Celltype_CRC01064.csv", "Celltype_CRC01069.csv", "Celltype_CRC01074.csv", 
    "Celltype_CRC01078.csv", "Celltype_CRC01084.csv", "Celltype_CRC01086.csv", 
    "Celltype_CRC01091.csv", "Celltype_CRC01097.csv", "Celltype_CRC01102.csv", 
    "Celltype_CRC01106.csv"
] # CUSTOM 2

# Read CSV files, add filename column, and combine
df_list = []
for filename in filenames:
    df = pd.read_csv(os.path.join(root_path, filename))
    # Extract CRCXXXXX part from the filename
    crc_code = filename.split('.')[0].split('_')[1] # CUSTOM 3
    df['Layer'] = crc_code # CUSTOM 4
    df_list.append(df)

combined_df = pd.concat(df_list, ignore_index=True)

# CUSTOM 5

# Read Celltype_reference_table.csv
ref_df = pd.read_csv(os.path.join(root_path, "Celltype_reference_table.csv"))

# Create a dictionary for mapping NewType to Name and Category
ref_dict = ref_df.set_index('NewType')[['Name', 'Category']].to_dict('index')

# Add new columns "Cell Type" and "Category" to the combined csv file
combined_df['Cell Type'] = combined_df['NewType'].map(lambda x: ref_dict.get(x, {}).get('Name', ''))
combined_df['Category'] = combined_df['NewType'].map(lambda x: ref_dict.get(x, {}).get('Category', ''))

# CUSTOM 6

# rename column cell_type_A to Cell Type
combined_df.rename(columns={"Cell Type": "Cell Type"}, inplace=True)
combined_df.rename(columns={"X": "x"}, inplace=True)
combined_df.rename(columns={"Y": "y"}, inplace=True)    
combined_df.rename(columns={"Category": "Category"}, inplace=True)
combined_df.rename(columns={"Layer": "Layer"}, inplace=True)

# Write back to the combined csv file
combined_csv_path = os.path.join(root_path, "combined_cells.csv")
combined_df.to_csv(combined_csv_path, index=False)

print(f"Combined CSV file created at: {combined_csv_path}")
