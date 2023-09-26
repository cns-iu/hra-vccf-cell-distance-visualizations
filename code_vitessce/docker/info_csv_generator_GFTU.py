import os
import pandas as pd

# Given data
region_names = ['00a67c839', '0749c6ccc', '1eb18739d', '5274ef79a', '5d8b53a68',
                '9e81e2693', 'a14e495cf', 'bacb03928', 'e464d2f6c', 'ff339c0b2',]
rows = len(region_names)
image_urls = [
    f'https://storagetuzi.blob.core.windows.net/blobtuzi/gftu_data/{region}_all_coordinates.pyramid.ome.tif' for region in region_names]
bg_urls = [
    f'https://storagetuzi.blob.core.windows.net/blobtuzi/gftu_data/{region}.pyramid.ome.tif' for region in region_names]
pro_names = {
    '095bf7a1f': 'HBM874.RZDW.757',
    'aa05346ff': 'HBM463.JRTB.582',
    'b9a3865fc': 'HBM636.ZPTS.368',
    'e464d2f6c': 'HBM324.ZGZM.874',
    'bacb03928': 'HBM832.FQKR.463',
    'ff339c0b2': 'HBM649.XFQG.775',
    'afa5e8098': 'HBM958.GHFM.676',
    'a14e495cf': 'HBM296.RLWW.755',
    '3589adb90': 'HBM623.RPMC.638',
    '2f6ecfcdf': 'HBM276.PGFS.693',
    '26dc41664': 'HBM849.XMPC.398',
    'd488c759a': 'HBM362.PTQJ.743',
    '5274ef79a': 'HBM673.JJRZ.435',
    '57512b7f1': 'HBM979.HDZH.896',
    'aaa6a05cc': 'HBM875.QHDJ.259',
    '5d8b53a68': 'HBM344.LLLV.539',
    '00a67c839': 'HBM627.RSGW.898',
    '0749c6ccc': 'HBM227.THVC.544',
    '0486052bb': 'HBM783.GJWP.694',
    '1e2425f28': 'HBM783.GDKK.879',
    '2ec3f1bb9': 'HBM833.DBGG.252',
    'e79de561c': 'HBM389.MBWW.346',
    '1eb18739d': 'HBM649.DLZF.463',
    'c68fe75ea': 'HBM662.PMPZ.644',
    'b2dc8411c': 'HBM879.CDHB.995',
    '9e81e2693': 'HBM984.PMZN.942',
    '4ef6695ce': 'HBM264.XSVF.528',
    '8242609fa': 'HBM676.SNVK.793',
    'cb2d976f4': 'HBM636.GVWP.354',
    '54f2eec69': 'HBM725.PDDC.788',
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
    'bg_url': bg_urls,
})

# Save to CSV
csv_path = "info.csv"
df.to_csv(csv_path, index=False)
print(f"CSV saved to {csv_path}")
