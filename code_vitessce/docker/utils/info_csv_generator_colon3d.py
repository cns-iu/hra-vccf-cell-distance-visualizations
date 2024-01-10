import os
import pandas as pd

# Given data
image_urls = [
    rf'https://storagetuzi.blob.core.windows.net/blobtuzi/colon_3d/Region_CRC01050_mask.pyramid.ome.tif']

region_names = [f"CRC01050"]
rows = len(region_names)

# Extract image names from the URLs using os.path.basename
image_names = [os.path.basename(url) for url in image_urls]
layer_count = 5

# Create a DataFrame
df = pd.DataFrame({
    'id': range(1, rows + 1),
    'region': region_names,
    'image_name': image_names,
    # 'pro_region': [pro_names[region] for region in region_names],
    'layers': [layer_count] * rows,
    'image_url': image_urls,
})

# Save to CSV
csv_path = "info.csv"
df.to_csv(csv_path, index=False)
print(f"CSV saved to {csv_path}")
