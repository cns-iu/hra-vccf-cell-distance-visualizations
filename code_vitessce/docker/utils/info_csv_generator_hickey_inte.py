import os
import pandas as pd

# Given data
region_names = ['reg001_CL_B004', 'reg001_SB_B004', 'reg002_CL_B004', 'reg002_SB_B004',
                'reg003_CL_B004', 'reg003_SB_B004', 'reg004_CL_B004', 'reg004_SB_B004']
rows = len(region_names)
# Region_reg001_CL_B004_mask.pyramid.ome
image_urls = [
    rf'https://storagetuzi.blob.core.windows.net/blobtuzi/hickey_inte_vccf/Region_{region}_mask.pyramid.ome.tif' for region in region_names]

# Extract image names from the URLs using os.path.basename
image_names = [os.path.basename(url) for url in image_urls]
layer_count = 3

# Create a DataFrame
df = pd.DataFrame({
    'id': range(1, rows + 1),
    'region': region_names,
    'image_name': image_names,
    'layers': [layer_count] * rows,
    'image_url': image_urls,
})

# Save to CSV
csv_path = "info.csv"
df.to_csv(csv_path, index=False)
print(f"CSV saved to {csv_path}")
