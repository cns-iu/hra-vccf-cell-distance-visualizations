import argparse
from vitessce import CsvWrapper, DataType
from IPython.display import display, HTML
import os
import json
import shutil
import pandas as pd
import ast

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


def download_imgs(folder, image_urls):
    full_paths = []
    for url in image_urls:
        # Extract the original file name from the URL
        original_file_name = os.path.basename(url)
        img_full_path = os.path.join(folder, original_file_name)
        full_paths.append(img_full_path)
        download_file(url, img_full_path)
    return full_paths


def reformat_layout(json_data, spatial_width=10.0, max_width=12.0, silent=True):

    # Update the "spatial" component
    for component in json_data['layout']:
        if component['component'] == 'spatial' and component['w'] < spatial_width:
            if not silent:
                print(
                    f"\tUpdating 'spatial' component 'width' from {component['w']} to {spatial_width}")
            component['w'] = spatial_width

    # Update other components based on the new width of the "spatial" component
    for component in json_data['layout']:
        if component['component'] != 'spatial' and component['x'] == 6:
            if not silent:
                print(
                    f"\tUpdating '{component['component']}' component 'x' from {component['x']} to {spatial_width}")
                print(
                    f"\tUpdating '{component['component']}' component 'width' from {component['w']} to 2")
            component['x'] = spatial_width
            component['w'] = max_width - spatial_width


def vitessce_main(output_folder, OUTPUT_LEVEL, img_path, img_url, region_id, official_region_id, layer_count,
                  csv_url=None, csv_path=None, options=None, bg_path=None, bg_url=None):
    vc = VitessceConfig(schema_version="1.0.15",
                        name='Transcriptomics example')

    if OUTPUT_LEVEL == 1:
        # LOCAL
        if bg_path:
            dataset = vc.add_dataset(name='Tissue Blocks').add_object(
                MultiImageWrapper(image_wrappers=[
                    OmeTiffWrapper(img_path=img_path, is_bitmask=True,
                                   name=f"Region {region_id} Visualization"),
                    OmeTiffWrapper(img_path=bg_path,
                                   name=f"Region {region_id} Background"),
                ])).add_object(CsvWrapper(csv_path=csv_path, data_type=DataType.OBS_SETS.value, options=options))
        else:
            dataset = vc.add_dataset(name='Cell segmentations').add_object(
                OmeTiffWrapper(img_path=img_path, is_bitmask=True,
                               name=f"Region {region_id} Visualization")
            ).add_object(CsvWrapper(csv_path=csv_path, data_type=DataType.OBS_SETS.value, options=options))
    else:
        # ONLINE PREVIEW
        if bg_url:
            dataset = vc.add_dataset(name='Cell segmentations').add_object(
                MultiImageWrapper(
                    image_wrappers=[
                        OmeTiffWrapper(img_url=img_url, is_bitmask=True,
                                       name=f"Region {region_id} Visualization"),
                        OmeTiffWrapper(img_url=bg_url,
                                       name=f"Region {region_id} Background"),
                    ])).add_object(CsvWrapper(csv_url=csv_url, data_type=DataType.OBS_SETS.value, options=options))
        else:
            dataset = vc.add_dataset(name='Cell segmentations').add_object(
                OmeTiffWrapper(img_url=img_url, is_bitmask=True,
                               name=f"Region {region_id} Visualization")
            ).add_object(CsvWrapper(csv_url=csv_url, data_type=DataType.OBS_SETS.value, options=options))

    spatial_plot = vc.add_view(cm.SPATIAL, dataset=dataset)
    layer_controller = vc.add_view(cm.LAYER_CONTROLLER, dataset=dataset)

    channels_list = [
        {
            "selection": {"c": i, "t": 0, "z": 0},
            "color": [0, 0, 0],
            "visible": True,
            "slider": [i, i+1]
        }
        for i in range(layer_count)
    ]

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
        "channels": channels_list
    }]

    if csv_path:
        cell_sets_view = vc.add_view(cm.OBS_SETS, dataset=dataset)
        # read cvd using pd
        cell_sets_data = pd.read_csv(csv_path)
        # using cell_type and cell_color to generate obs_set_color
        # Convert the cell_color from string format "[255,0,0]" to a list [255, 0, 0]
        cell_sets_data['color_list'] = cell_sets_data['cell_color'].apply(
            lambda x: ast.literal_eval(x))

        # Generate the obs_set_color dictionary
        obs_set_color = []
        for index, row in cell_sets_data.iterrows():
            obs_set_color.append({
                "path": ["Cell Type", row['cell_type']],
                "color": row['color_list']
            })

    vc.link_views(
        [spatial_plot, layer_controller],
        [ct.SPATIAL_ZOOM, ct.SPATIAL_TARGET_X,
            ct.SPATIAL_TARGET_Y, ct.SPATIAL_SEGMENTATION_LAYER],
        [-4, 7500, 7500, spatial_segmentation_layer_value]
    )

    if csv_path:
        vc.link_views(
            [cell_sets_view, spatial_plot, layer_controller],
            [ct.OBS_SET_COLOR],
            [obs_set_color]
        )

    if csv_path:
        vc.layout(spatial_plot | (layer_controller / cell_sets_view))
    else:
        vc.layout(spatial_plot | layer_controller)

    web_url = vc.web_app()
    # print(f"View on Vitessce.io: {web_url}")
    # url is too long so do NOT print it
    print(f"URL is too long to print. View on Vignette json file")

    PATH_TO_EXPORT_DIRECTORY = os.path.join(
        output_folder, "data", f"vignette_{region_id}")
    VIGNETTE_DIR = os.path.join(
        output_folder, "vignettes", f"vignette_{region_id}")
    # Export Vitessce config to JSON
    os.makedirs(VIGNETTE_DIR, exist_ok=True)
    # Export Vitessce config to JSON
    os.makedirs(PATH_TO_EXPORT_DIRECTORY, exist_ok=True)
    config_dict = vc.export(
        to="files", base_url=f"{BASE_URL_PLACEHOLDER}/vignette_{region_id}", out_dir=PATH_TO_EXPORT_DIRECTORY)
    reformat_layout(config_dict)
    # Use `open` to create a new empty file at ./exported_data/vitessce.json
    with open(os.path.join(VIGNETTE_DIR, "vitessce.json"), "w") as f:
        json.dump(config_dict, f)
    vignette_md = f"""
---
name: Visualization for {official_region_id}
figures:
    - name: "Visualization"
      file: vitessce.json
---
This vignette visualizes Region {official_region_id} segmentation.
    """
    with open(os.path.join(VIGNETTE_DIR, "description.md"), "w") as f:
        f.write(vignette_md)


def vitessce_eui(output_folder, OUTPUT_LEVEL, region_id, eui_img_full_path, eui_url):
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
    vc.layout(spatial)

    web_url = vc.web_app()
    # print(f"View on Vitessce.io: {web_url}")
    # url is too long so do NOT print it
    print(f"URL is too long to print. View on Vignette json file")

    PATH_TO_EXPORT_DIRECTORY = os.path.join(
        output_folder, "data", f"vignette_{region_id}")
    VIGNETTE_DIR = os.path.join(
        output_folder, "vignettes", f"vignette_{region_id}")
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
name: Explore Tissue Data in 3D using the Exploration User Interface
figures:
    - name: "Visualization"
      file: vitessce.json
---
    All HuBMAP tissue datasets used in this study can be spatially explored in their three-dimensional size, position, and rotation in the context of the Human Reference Atlas using the Exploration User Interface (EUI): [https://hubmapconsortium.github.io/hra-registrations/23-hbm-flagship-ginty/](https://hubmapconsortium.github.io/hra-registrations/23-hbm-flagship-ginty/)
"""
    with open(os.path.join(VIGNETTE_DIR, "description.md"), "w") as f:
        f.write(vignette_md)


def main(args):
    """
    This function processes the visualization based on the provided arguments.

    Parameters:
        Required:
            - IMG_ROOT (str): The root directory where images are stored.
            - OUTPUT_ROOT (str): The root directory where output files will be saved.
            - OUTPUT_LEVEL (int): Determines the output level. 
                                0 indicates ONLINE PREVIEW, 
                                1 indicates LOCAL EXPORT.
            - DATA_SOURCE (str): Specifies the source of the data. 
                                'LOCAL' means the data will be read from a local directory, 
                                'NET' means the data will be downloaded from the provided URLs.
            - INFO_CSV (str): Path to the CSV file containing hubmap data.
        Optional:
            - BG_ROOT (str): The directory where background images are stored.
            - COLOR_SCHEME_CSV (str, optional): URL OR PATH to the CSV file containing cell data, depending on the DATA_SOURCE.
                                                If not provided, a default scheme (random) will be used.
            - EUI_SOURCE (str, optional): URL OR PATH to the EUI data, depending on the DATA_SOURCE.
            - PROJECT_NAME',(str, optional): Project name for the final zip file. If not provided, the default name is 'vignette'.

    The function will process the images and generate visualizations based on the provided arguments.
    """

    # Check if IMG_ROOT is provided
    assert args.IMG_ROOT, "IMG_ROOT directory not provided."
    IMG_ROOT = args.IMG_ROOT
    print("IMG_ROOT: ", IMG_ROOT)

    # Check if OUTPUT_ROOT is provided
    assert args.OUTPUT_ROOT, "OUTPUT_ROOT directory not provided."
    OUTPUT_ROOT = args.OUTPUT_ROOT
    print("OUTPUT_ROOT: ", OUTPUT_ROOT)

    # Check if OUTPUT_LEVEL is provided and valid
    assert args.OUTPUT_LEVEL in [0, 1], "Invalid OUTPUT_LEVEL. Must be 0 or 1."
    OUTPUT_LEVEL = args.OUTPUT_LEVEL
    print("OUTPUT_LEVEL: ", OUTPUT_LEVEL)

    # Check if DATA_SOURCE is provided and valid
    assert args.DATA_SOURCE in [
        'LOCAL', 'NET'], "Invalid DATA_SOURCE. Must be 'LOCAL' or 'NET'."
    DATA_SOURCE = args.DATA_SOURCE
    print("DATA_SOURCE: ", DATA_SOURCE)

    if DATA_SOURCE == 'LOCAL':
        assert OUTPUT_LEVEL == 1, "OUTPUT_LEVEL must be 1 (LOCAL EXPORT) when DATA_SOURCE is LOCAL."

    # Check if INFO_CSV is provided
    assert args.INFO_CSV, "INFO_CSV file not provided."
    INFO_CSV = args.INFO_CSV

    # check if BG_ROOT is provided and valid
    if args.BG_ROOT:
        BG_ROOT = args.BG_ROOT
        print("BG_ROOT (optional): ", BG_ROOT)

    # COLOR_SCHEME_CSV, EUI_URL, and EUI_PATH are optional, so no checks are needed for them
    if args.COLOR_SCHEME_CSV:
        COLOR_SCHEME_CSV = args.COLOR_SCHEME_CSV
        print("COLOR_SCHEME_CSV (optional): ", COLOR_SCHEME_CSV)
    if args.EUI_SOURCE:
        EUI_SOURCE = args.EUI_SOURCE
        print("EUI_SOURCE (optional): ", EUI_SOURCE)

    # PROJECT_NAME is optional
    FINAL_ZIP_NAME = 'vignette'
    if args.PROJECT_NAME:
        FINAL_ZIP_NAME += '_' + args.PROJECT_NAME
        print("PROJECT_NAME (optional): ", args.PROJECT_NAME)

    # create a directory to store images if it doesn't exist
    print("Creating image directory...", IMG_ROOT)
    os.makedirs(IMG_ROOT, exist_ok=True)
    if BG_ROOT:
        print("Creating background image directory...", BG_ROOT)
        os.makedirs(BG_ROOT, exist_ok=True)

    # Read the INFO CSV file for image URLs, region names, and official region names
    print("Reading CSV file...")
    info_df = pd.read_csv(INFO_CSV)
    REGION_NAMES = info_df['region'].tolist()
    # detect if column 'pro_region' exists
    if 'pro_region' in info_df.columns:
        PRO_REGION_NAMES = info_df['pro_region'].tolist()
    else:
        PRO_REGION_NAMES = info_df['region'].tolist()
    LAYER_COUNTS = info_df['layers'].tolist()
    if DATA_SOURCE == 'LOCAL':
        IMAGE_NAMES = info_df['image_name'].tolist()
        IMAGE_URLS = []
        if BG_ROOT:
            BG_NAMES = info_df['bg_name'].tolist()
            BG_URLS = []
    else:
        IMAGE_URLS = info_df['image_url'].tolist()
        if BG_ROOT:
            BG_URLS = info_df['bg_url'].tolist()
    # print columns read from the csv
    print("Columns read from the CSV file: ")
    print('\t', info_df.columns.tolist())

    # Download each image
    if DATA_SOURCE == 'LOCAL':
        print("Using local images...")
        img_full_paths = []
        bg_full_paths = []
        for IMAGE_NAME in IMAGE_NAMES:
            img_full_paths.append(os.path.join(IMG_ROOT, IMAGE_NAME))
    else:
        print("Downloading images...")
        img_full_paths = download_imgs(IMG_ROOT, IMAGE_URLS)

    # Download each background image
    if BG_ROOT:
        if DATA_SOURCE == 'LOCAL':
            print("Using local background images...")
            bg_full_paths = []
            for BG_NAME in BG_NAMES:
                bg_full_paths.append(os.path.join(BG_ROOT, BG_NAME))
        else:
            print("Downloading background images...")
            bg_full_paths = download_imgs(BG_ROOT, BG_URLS)

    # Print the list of full paths
    print("IMAGE PATHS: ")
    for path in img_full_paths:
        print('\t', path)
    if BG_ROOT:
        print("BACKGROUND IMAGE PATHS: ")
        for path in bg_full_paths:
            print('\t', path)

    # color scheme part files
    if COLOR_SCHEME_CSV:
        if DATA_SOURCE == 'LOCAL':
            csv_path = COLOR_SCHEME_CSV
            csv_url = None
        else:
            print("Downloading color scheme file...")
            csv_url = COLOR_SCHEME_CSV
            csv_path = os.path.join(
                IMG_ROOT, os.path.basename(COLOR_SCHEME_CSV))
            download_file(csv_url, csv_path)
        print("CSV PATH: ", csv_path)
        options = {
            "obsIndex": "cell_id",
            "obsSets": [
                {
                    "name": "Cell Type",
                    "column": "cell_type"
                }
            ]
        }

    # eui part
    if EUI_SOURCE:
        if DATA_SOURCE == 'LOCAL':
            eui_path = EUI_SOURCE
            eui_url = None
        else:
            print("Downloading EUI image...")
            eui_url = EUI_SOURCE
            eui_path = os.path.join(IMG_ROOT, os.path.basename(EUI_SOURCE))
            download_file(eui_url, eui_path)
        print("EUI PATH: ", eui_path)

    # Generate visualizations
    print("Generating visualizations...")
    for idx in range(len(REGION_NAMES)):
        region_name = REGION_NAMES[idx]
        official_region_id = PRO_REGION_NAMES[idx]
        img_path = img_full_paths[idx]
        layer_count = LAYER_COUNTS[idx]
        bg_path = bg_full_paths[idx] if BG_ROOT else None
        if len(IMAGE_URLS) > 0:
            img_url = IMAGE_URLS[idx]
        else:
            img_url = None
        if len(BG_URLS) > 0:
            bg_url = BG_URLS[idx]
        else:
            bg_url = None

        print(" - Region: ", region_name)
        print(" - Filepath: ", img_path)
        if BG_ROOT:
            print(" - Background Filepath: ", bg_path)
        print(" - Image URL: ", img_url)
        print(" - Official Region ID: ", official_region_id)
        print(" - Layer Count: ", layer_count)

        vitessce_main(output_folder=OUTPUT_ROOT, OUTPUT_LEVEL=OUTPUT_LEVEL,
                      img_path=img_path,
                      img_url=img_url,
                      region_id=region_name, official_region_id=official_region_id,
                      layer_count=layer_count,
                      csv_url=csv_url if COLOR_SCHEME_CSV else None,
                      csv_path=csv_path if COLOR_SCHEME_CSV else None,
                      options=options if COLOR_SCHEME_CSV else None,
                      bg_path=bg_path if BG_ROOT else None,
                      bg_url=bg_url if BG_ROOT else None
                      )

    # EUI
    if EUI_SOURCE:
        print("Generating EUI visualization...")
        vitessce_eui(output_folder=OUTPUT_ROOT, OUTPUT_LEVEL=OUTPUT_LEVEL, region_id=str(len(REGION_NAMES)+1),
                     eui_img_full_path=eui_path,
                     eui_url=eui_url)

    # Zip the output folder
    print("Zipping the output folder...")
    shutil.make_archive(FINAL_ZIP_NAME, 'zip', OUTPUT_ROOT)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some parameters.')
    parser.add_argument('--IMG_ROOT', type=str, required=True,
                        help='Root path to images')
    parser.add_argument('--OUTPUT_ROOT', type=str, required=True,
                        help='Output root directory')
    parser.add_argument('--OUTPUT_LEVEL', type=int,
                        choices=[0, 1], required=True,
                        help='Output level (0 for ONLINE PREVIEW, 1 for LOCAL EXPORT)')
    parser.add_argument('--DATA_SOURCE', type=str,
                        choices=['LOCAL', 'NET'], required=True,
                        help='Data source (LOCAL or NET)')
    parser.add_argument('--INFO_CSV', type=str, required=True,
                        help='Path to hubmap CSV file')
    parser.add_argument('--BG_ROOT', type=str,
                        help='Root path to background images')
    parser.add_argument('--COLOR_SCHEME_CSV', type=str,
                        help='Path to cell data CSV file (optional)', default=None)
    parser.add_argument('--EUI_SOURCE', type=str,
                        help='URL OR PATH to EUI data (optional)', default=None)
    parser.add_argument('--PROJECT_NAME', type=str,
                        help='Project name for the final zip file (optional)', default=None)

    args = parser.parse_args()
    main(args)
