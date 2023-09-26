import os
import pandas as pd

# Given data
region_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
rows = len(region_names)
image_urls = [
    rf'https://storagetuzi.blob.core.windows.net/blobtuzi/vccf_data/cell_table_region_{region}.ome.tif' for region in region_names]
pro_names = {
    '1': "HBM732.FZVZ.656",
    '2': "HBM747.SPWK.779",
    '3': "HBM398.NCVN.256",
    '4': "HBM746.VTDZ.959",
    '5': "HBM875.SBHJ.939",
    '6': "HBM867.NMXL.794",
    '7': "HBM666.JCGS.862",
    '8': "HBM592.JGSQ.253",
    '9': "HBM494.XDQW.356",
    '10': "HBM238.ZKPC.934",
    '11': "HBM975.FVCG.922",
    '12': "HBM674.XQFQ.364",
}

# Extract image names from the URLs using os.path.basename
image_names = [os.path.basename(url) for url in image_urls]
layer_count = 6

# Create a DataFrame
df = pd.DataFrame({
    'id': range(1, rows + 1),
    'region': region_names,
    'image_name': image_names,
    'pro_region': [pro_names[region] for region in region_names],
    'layers': [layer_count] * rows,    
    'image_url': image_urls,
})

# Save to CSV
csv_path = "info.csv"
df.to_csv(csv_path, index=False)
print(f"CSV saved to {csv_path}")
