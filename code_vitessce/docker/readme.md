# Visualization Pipeline with Vitessce

## Overview

This script provides a pipeline for processing and visualizing biomedical images using the Vitessce library. It is designed to handle both local and online data sources and offers flexibility in output formats suitable for online previews or local exports.

### Purpose and Pipeline

The primary purpose of this script is to generate the visualization of biomedical images, especially in the context of the HuBMAP project. The pipeline involves:

1. **Data Acquisition**: Depending on the specified data source (`LOCAL` or `NET`), the script either accesses local files or downloads data from provided URLs.
2. **Data Processing**: Images are processed using the Vitessce library, and additional functionalities like background image processing, color scheme application, and EUI visualization are available.
3. **Visualization Generation**: The processed data is then used to generate visualizations, which can be previewed online or exported for local use.
4. **Output**: Depending on the specified output level, the visualizations are either saved locally or prepared for online preview.

## How to Use

### Parameters:

#### Required:

- `--IMG_ROOT`: Root path to images.
- `--OUTPUT_ROOT`: Output root directory where the visualizations will be saved.
- `--OUTPUT_LEVEL`: Determines the output format. Set to `0` for ONLINE PREVIEW or `1` for LOCAL EXPORT.
- `--DATA_SOURCE`: Specifies where the data is coming from. Use `LOCAL` for local directories or `NET` for online URLs.
- `--INFO_CSV`: Path to the CSV file containing hubmap data.

#### Optional:

- `--BG_ROOT`: Root path to background images. If not provided, no background images will be used.
- `--COLOR_SCHEME_CSV`: URL OR PATH to the CSV file containing cell data. This depends on the `DATA_SOURCE`. If not provided, a default color scheme will be used.
- `--EUI_SOURCE`: URL OR PATH to the EUI data. This also depends on the `DATA_SOURCE`.
- `--PROJECT_NAME`: Name for the final zip file. If not provided, the default name is 'vignette'.
- `--NO_DEL_OUTPUT`: If set, the output directory will not be deleted. Default is to delete the output directory.

### CSV File Structure

#### `info.csv`

This CSV file contains information about the images and regions. The columns in this CSV file are:

- `region`: (Required) The name of the region.
- `pro_region`: (Optional) The official/professional name of the region. If not provided, the `region` column will be used.
- `layers`: (Required) The number of layers in the image.
- `image_name`: (Required if `DATA_SOURCE` is `LOCAL`) The name of the image file.
- `image_url`: (Required if `DATA_SOURCE` is `NET`) The URL from which the image can be downloaded.
- `bg_name`: (Optional) The name of the background image file.
- `bg_url`: (Optional) The URL from which the background image can be downloaded.

#### `cell_sets.csv`

This CSV file contains information about cell types and their colors. The columns in this CSV file are:

- `cell_id`: (Required) The unique identifier for the cell.
- `cell_type`: (Required) The type or category of the cell.
- `cell_color`: (Required) The color associated with the cell type, provided as an RGB list in string format.

Example:
```cell_sets.csv
cell_id,cell_type,cell_color
1,B,"[28, 131, 86]"
2,CD4,"[133, 102, 13]"
3,CD7_Immune,"[50, 131, 254]"
```

### Command Line Examples:

Replace `CSV_URL` or `CSV_FILE` with the appropriate path or URL. More samples can be found at samples/commands.txt.

#### VCCF (Source: Network, Output: 0):

```bash
python ometif2vitessce.py --IMG_ROOT ./image --OUTPUT_ROOT ./output --OUTPUT_LEVEL 0 --DATA_SOURCE NET --INFO_CSV ./info.csv --COLOR_SCHEME_CSV CSV_URL --EUI_SOURCE CSV_URL --PROJECT_NAME VCCF
```

#### GFTU (Source: Network, Output: 1):

```bash
python ometif2vitessce.py --IMG_ROOT ./image --OUTPUT_ROOT ./output --OUTPUT_LEVEL 1 --DATA_SOURCE NET --INFO_CSV ./info.csv --COLOR_SCHEME_CSV CSV_URL --EUI_SOURCE CSV_URL --BG_ROOT ./image --PROJECT_NAME GFTU
```

#### Hickey VCCF (Source: Local, Output: 1):

```bash
python ometif2vitessce.py --IMG_ROOT ./image --OUTPUT_ROOT ./output --OUTPUT_LEVEL 1 --DATA_SOURCE LOCAL --INFO_CSV ./info.csv --COLOR_SCHEME_CSV ./image/cell_sets.csv --EUI_SOURCE ./image/eui_hickey.pyramid.ome.tif --PROJECT_NAME HICKEY_VCCF
```

## Feedback and Issues:

If you encounter any issues or have feedback, please open an issue on this repository.
