import os
import pandas as pd

region_names = ['LN00560', 'LN00837', 'LN22921', 'LN24336', 'LN27766']
rows = len(region_names)

# Given data
image_urls = [rf'https://storagetuzi.blob.core.windows.net/blobtuzi/ln_data/Region_{region}_mask.pyramid.ome.tif' for region in region_names]

# Extract image names from the URLs using os.path.basename
image_names = [os.path.basename(url) for url in image_urls]
layer_count = 3

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
