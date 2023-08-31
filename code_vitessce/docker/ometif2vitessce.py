from vitessce import CsvWrapper, DataType
from IPython.display import display, HTML
import os
import json
import shutil
import pandas as pd

from vitessce import (
    VitessceConfig,
    Component as cm,
    CoordinationType as ct,
    FileType as ft,
    ViewType as vt,
    AnnDataWrapper,
    MultiImageWrapper,
    OmeTiffWrapper,
    BASE_URL_PLACEHOLDER,
)


def download_file(url, destination):
    os.system(f"curl -L -o {destination} {url}")


def vitessce_main(ROOT, OUTPUT_LEVEL, filepath, img_url, region_id, official_region_id=None, csv_url=None, csv_path=None, options=None):
    vc = VitessceConfig(schema_version="1.0.15",
                        name='Transcriptomics example')

    if official_region_id is None:
        official_region_id = region_id

    if OUTPUT_LEVEL == 1:
        # LOCAL
        dataset = vc.add_dataset(name='Cell segmentations').add_object(
            OmeTiffWrapper(img_path=filepath, is_bitmask=True,
                           name=f"Region {region_id} Segmentations")
        ).add_object(CsvWrapper(csv_path=csv_path, data_type=DataType.OBS_SETS.value, options=options))
    else:
        # ONLINE PREVIEW
        dataset = vc.add_dataset(name='Cell segmentations').add_object(
            OmeTiffWrapper(img_url=img_url, is_bitmask=True,
                           name=f"Region {region_id} Segmentations")
        ).add_object(CsvWrapper(csv_url=csv_url, data_type=DataType.OBS_SETS.value, options=options))

    spatial_plot = vc.add_view(cm.SPATIAL, dataset=dataset)
    layer_controller = vc.add_view(cm.LAYER_CONTROLLER, dataset=dataset)

    spatial_segmentation_layer_value = [{
        "type": "bitmask",
        "index": 0,
        "visible": True,
        "colormap": None,
        "opacity": 1,
        "domainType": "Min/Max",
        "transparentColor": None,
        "renderingMode": "Additive",
        "use3d": False,
        "channels": [
            # VCCF
                {"selection": {"c": 0, "t": 0, "z": 0}, "color": [
                    0, 0, 0], "visible":True, "slider":[0, 1]},
                {"selection": {"c": 1, "t": 0, "z": 0}, "color": [
                    0, 0, 0], "visible":True, "slider":[1, 2]},
                {"selection": {"c": 2, "t": 0, "z": 0}, "color": [
                    0, 0, 0], "visible":True, "slider":[2, 3]},
                {"selection": {"c": 3, "t": 0, "z": 0}, "color": [
                    0, 0, 0], "visible":True, "slider":[3, 4]},
                {"selection": {"c": 4, "t": 0, "z": 0}, "color": [
                    0, 0, 0], "visible":True, "slider":[4, 5]},
                {"selection": {"c": 5, "t": 0, "z": 0}, "color": [
                    0, 0, 0], "visible":True, "slider":[5, 6]},
        ]
    }]
    cell_sets_view = vc.add_view(cm.OBS_SETS, dataset=dataset)
    obs_set_color = [
        {"path": ["Cell Type", "vessel"], "color": [255, 0, 0]},
        {"path": ["Cell Type", "T-Killer"], "color": [255, 0, 255]},
        {"path": ["Cell Type", "T-Killer_link"], "color": [255, 0, 255]},
        {"path": ["Cell Type", "T-Helper"], "color": [0, 0, 255]},
        {"path": ["Cell Type", "T-Helper_link"], "color": [0, 0, 255]},
        {"path": ["Cell Type", "T-Reg"], "color": [0, 255, 0]},
        {"path": ["Cell Type", "T-Reg_link"], "color": [0, 255, 0]},
        {"path": ["Cell Type", "CD68"], "color": [255, 215, 0]},
        {"path": ["Cell Type", "CD68_link"], "color": [255, 215, 0]},
        {"path": ["Cell Type", "DDB2"], "color": [0, 153, 76]},
        {"path": ["Cell Type", "P53"], "color": [153, 76, 0]},
        {"path": ["Cell Type", "KI67"], "color": [0, 255, 255]},
        {"path": ["Cell Type", "skin"], "color": [192, 192, 192]},
    ]
    vc.link_views(
        [spatial_plot, layer_controller],
        [ct.SPATIAL_ZOOM, ct.SPATIAL_TARGET_X,
            ct.SPATIAL_TARGET_Y, ct.SPATIAL_SEGMENTATION_LAYER],
        [-4, 7500, 7500, spatial_segmentation_layer_value]
    )
    vc.link_views(
        [cell_sets_view, spatial_plot, layer_controller],
        [ct.OBS_SET_COLOR],
        [obs_set_color]
    )
    vc.layout(spatial_plot | (layer_controller / cell_sets_view))

    web_url = vc.web_app()
    display(HTML(f'View on Vitessce.io'))
    # FULL CODE:
    # display(HTML(f'View on Vitessce.io'))
    # THIS LINE WILL BE MODIFIED WHEN SAVED TO GITHUB

    PATH_TO_EXPORT_DIRECTORY = os.path.join(
        ROOT, "data", f"vignette_{region_id}")
    VIGNETTE_DIR = os.path.join(ROOT, "vignettes", f"vignette_{region_id}")
    # Export Vitessce config to JSON
    os.makedirs(VIGNETTE_DIR, exist_ok=True)
    # Export Vitessce config to JSON
    os.makedirs(PATH_TO_EXPORT_DIRECTORY, exist_ok=True)
    config_dict = vc.export(
        to="files", base_url=f"{BASE_URL_PLACEHOLDER}/vignette_{region_id}", out_dir=PATH_TO_EXPORT_DIRECTORY)
    # Use `open` to create a new empty file at ./exported_data/vitessce.json
    with open(os.path.join(VIGNETTE_DIR, "vitessce.json"), "w") as f:
        json.dump(config_dict, f)
    vignette_md = f"""
---
name: VCCF Visualization for {official_region_id}
figures:
    - name: "Visualization"
      file: vitessce.json
---
This vignette visualizes Region {official_region_id}. The image shows the segmentation of vasculature and immune cells, and the links between them.
    """
    with open(os.path.join(VIGNETTE_DIR, "description.md"), "w") as f:
        f.write(vignette_md)


def vitessce_eui(ROOT, OUTPUT_LEVEL, region_id, eui_img_full_path, eui_url):
    vc = VitessceConfig(schema_version="1.0.15", name='EUI')
    if OUTPUT_LEVEL == 1:
        # LOCAL
        dataset = vc.add_dataset(name='Tissue Blocks in EUI').add_object(
            OmeTiffWrapper(img_path=eui_img_full_path, name='EUI')
        )
    else:
        # ONLINE PREVIEW
        dataset = vc.add_dataset(name='Tissue Blocks in EUI').add_object(
            OmeTiffWrapper(img_url=eui_url, name='EUI')
        )
    spatial = vc.add_view(vt.SPATIAL, dataset=dataset)
    status = vc.add_view(vt.STATUS, dataset=dataset)
# Try changing the prop below to False
    lc = vc.add_view(vt.LAYER_CONTROLLER, dataset=dataset).set_props(
        disableChannelsIfRgbDetected=False)
# vc.layout(spatial | (lc / status))
    vc.layout(spatial)
    web_url = vc.web_app()
    display(HTML(f'View on Vitessce.io'))

    PATH_TO_EXPORT_DIRECTORY = os.path.join(ROOT, "data", f"vignette_13")
    VIGNETTE_DIR = os.path.join(ROOT, "vignettes", f"vignette_13")
# Export Vitessce config to JSON
    os.makedirs(VIGNETTE_DIR, exist_ok=True)
# Export Vitessce config to JSON
    os.makedirs(PATH_TO_EXPORT_DIRECTORY, exist_ok=True)
    config_dict = vc.export(
        to="files", base_url=f"{BASE_URL_PLACEHOLDER}/vignette_13", out_dir=PATH_TO_EXPORT_DIRECTORY)
# Use `open` to create a new empty file at ./exported_data/vitessce.json
    with open(os.path.join(VIGNETTE_DIR, "vitessce.json"), "w") as f:
        json.dump(config_dict, f)
    vignette_md = f"""
---
name: Explore Tissue Data in 3D using the Exploration User Interface
figures:
    - name: "Visualization"
      file: vitessce.json
---
    All HuBMAP tissue datasets used in this study can be spatially explored in their three-dimensional size, position, and rotation in the context of the Human Reference Atlas using the Exploration User Interface (EUI): [https://hubmapconsortium.github.io/hra-registrations/23-hbm-flagship-ginty/](https://hubmapconsortium.github.io/hra-registrations/23-hbm-flagship-ginty/)
"""
    with open(os.path.join(VIGNETTE_DIR, "description.md"), "w") as f:
        f.write(vignette_md)


def download_imgs(folder, image_urls):
    full_paths = []
    for url in image_urls:
        # Extract the original file name from the URL
        original_file_name = os.path.basename(url)
        img_full_path = os.path.join(folder, original_file_name)
        full_paths.append(img_full_path)
        download_file(url, img_full_path)
    return full_paths


if __name__ == '__main__':
    # Define the image directory
    img_path = './images'

    # Define the output root directory
    OUTPUT = "hubmap-publication-page"

    # LOCAL=1, ONLINE=0
    OUTPUT_LEVEL = 0

    # Define the official names of the regions
    hubmap_names = {
        1: "HBM732.FZVZ.656",
        2: "HBM747.SPWK.779",
        3: "HBM398.NCVN.256",
        4: "HBM746.VTDZ.959",
        5: "HBM875.SBHJ.939",
        6: "HBM867.NMXL.794",
        7: "HBM666.JCGS.862",
        8: "HBM592.JGSQ.253",
        9: "HBM494.XDQW.356",
        10: "HBM238.ZKPC.934",
        11: "HBM975.FVCG.922",
        12: "HBM674.XQFQ.364",
    }

    # define the ID names of the regions
    region_names = ['1', '2', '3', '4', '5',
                    '6', '7', '8', '9', '10', '11', '12']

    # Define the URLs of the images
    image_urls = [
        rf'https://storagetuzi.blob.core.windows.net/blobtuzi/vccf_data/cell_table_region_{region}.ome.tif' for region in region_names]

    # define the optional color scheme for the cell sets
    cell_data = {
        'cell_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        'cell_type': ['T-Killer', 'T-Helper', 'T-Reg', 'CD68', 'vessel',
                      "T-Killer_link", 'T-Helper_link', 'T-Reg_link', 'CD68_link',
                      'DDB2', 'P53', 'KI67', 'skin']
    }

    # define EUI part
    eui_url = 'https://storagetuzi.blob.core.windows.net/blobtuzi/eui/eui_VCCF.pyramid.ome.tif'

    # create a directory to store images if it doesn't exist
    os.makedirs(img_path, exist_ok=True)

    # Download each image
    print("Downloading images...")
    img_full_paths = download_imgs(img_path, image_urls)

    # Print the list of full paths
    print("IMAGE PATHS: ")
    for path in img_full_paths:
        print('\t', path)

    # color scheme part files
    print("Downloading color scheme file...")
    csv_url = "https://storagetuzi.blob.core.windows.net/blobtuzi/vccf_data/cell_sets.csv"
    csv_path = os.path.join(img_path, 'cell_sets.csv')
    download_file(csv_url, csv_path)
    print("CSV PATH: ", csv_path)

    # eui part
    print("Downloading EUI image...")
    eui_original_file_name = os.path.basename(eui_url)
    eui_full_path = os.path.join(img_path, eui_original_file_name)
    download_file(eui_url, f"./images/{eui_original_file_name}")
    print("EUI PATH: ", eui_full_path)

    # Create a dataframe from the cell data and make necessary options
    cell_sets_data = pd.DataFrame(cell_data)
    options = {
        "obsIndex": "cell_id",
        "obsSets": [
            {
                    "name": "Cell Type",
                    "column": "cell_type"
            }
        ]
    }

    for region_name in region_names:  # 1 to 12 inclusive
        idx = region_names.index(region_name)
        filepath = img_full_paths[idx]
        img_url = image_urls[idx]

        print(region_names)
        print(filepath)
        vitessce_main(ROOT=OUTPUT, OUTPUT_LEVEL=OUTPUT_LEVEL, filepath=filepath, img_url=img_url,
                      region_id=region_name,
                      official_region_id=hubmap_names[int(region_name)],
                      csv_url=csv_url, csv_path=csv_path, options=options)

    # LOCAL=1, ONLINE=0

    vitessce_eui(ROOT=OUTPUT, OUTPUT_LEVEL=OUTPUT_LEVEL, region_id='13',
                 eui_img_full_path=eui_full_path, eui_url=eui_url)

    shutil.make_archive('vignette_VCCF', 'zip', OUTPUT)
