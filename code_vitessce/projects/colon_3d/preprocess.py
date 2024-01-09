import pandas as pd
import os

# root path
root_path = r"D:\HuBMAP\colon_3d"

# List of filenames
filenames = [
    "Reg_Celltype_CRC01002.csv", "Reg_Celltype_CRC01007.csv", "Reg_Celltype_CRC01014.csv", 
    "Reg_Celltype_CRC01020.csv", "Reg_Celltype_CRC01025.csv", "Reg_Celltype_CRC01029.csv", 
    "Reg_Celltype_CRC01034.csv", "Reg_Celltype_CRC01039.csv", "Reg_Celltype_CRC01044.csv", 
    "Reg_Celltype_CRC01049.csv", "Reg_Celltype_CRC01050.csv", "Reg_Celltype_CRC01051.csv", 
    "Reg_Celltype_CRC01052.csv", "Reg_Celltype_CRC01054.csv", "Reg_Celltype_CRC01059.csv", 
    "Reg_Celltype_CRC01064.csv", "Reg_Celltype_CRC01069.csv", "Reg_Celltype_CRC01074.csv", 
    "Reg_Celltype_CRC01078.csv", "Reg_Celltype_CRC01084.csv", "Reg_Celltype_CRC01086.csv", 
    "Reg_Celltype_CRC01091.csv", "Reg_Celltype_CRC01097.csv", "Reg_Celltype_CRC01102.csv", 
    "Reg_Celltype_CRC01106.csv"
]

# Read CSV files, add filename column, and combine
df_list = []
for filename in filenames:
    df = pd.read_csv(os.path.join(root_path, filename))
    # Extract CRCXXXXX part from the filename
    crc_code = filename.split('.')[0].split('_')[2]
    df['Layer'] = crc_code
    df_list.append(df)

combined_df = pd.concat(df_list, ignore_index=True)

# Read Celltype_reference_table.csv
ref_df = pd.read_csv(os.path.join(root_path, "Celltype_reference_table.csv"))

# Create a dictionary for mapping NewType to Name and Category
ref_dict = ref_df.set_index('NewType')[['Name', 'Category']].to_dict('index')

# Add new columns "Cell Type" and "Category" to the combined csv file
combined_df['Cell Type'] = combined_df['NewType'].map(lambda x: ref_dict.get(x, {}).get('Name', ''))
combined_df['Category'] = combined_df['NewType'].map(lambda x: ref_dict.get(x, {}).get('Category', ''))

# Write back to the combined csv file
combined_csv_path = os.path.join(root_path, "combined_cells.csv")
combined_df.to_csv(combined_csv_path, index=False)

print(f"Combined CSV file created at: {combined_csv_path}")
