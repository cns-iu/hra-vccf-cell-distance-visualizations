import os
import pandas as pd

region_names = ['CRC01002','CRC01007','CRC01014','CRC01020','CRC01025','CRC01029','CRC01034','CRC01039','CRC01044','CRC01049','CRC01050','CRC01051','CRC01052','CRC01054','CRC01059','CRC01064','CRC01069','CRC01074','CRC01078','CRC01084','CRC01086','CRC01091','CRC01097','CRC01102','CRC01106']
rows = len(region_names)

# Given data
image_urls = [rf'https://storagetuzi.blob.core.windows.net/blobtuzi/colon_3d/Region_{region}_mask.pyramid.ome.tif' for region in region_names]

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
