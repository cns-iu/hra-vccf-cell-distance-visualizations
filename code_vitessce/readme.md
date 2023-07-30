# Repository Description

This repository is designed for visualizing cell data using Vitessce. It contains codes files that serve different purposes in the data processing and visualization pipeline.

## cell_data_view_generator.py

This Python script is responsible for generating CSV files that define the color scheme for the cell data visualization. These CSV files can be used to define the color scheme and other properties for visualizing the cell data in Vitessce.

## data_conversion.py

This Python script is used to convert raw data into a format suitable for generating an OME-TIFF file for visualization in Vitessce. The main function reads CSV files containing the raw data, filters the data based on specified values, and constructs tables for cell vertices, link vertices, and damage vertices. These tables are then saved as separate CSV files. The generated CSV files serve as input for the next step in the data processing pipeline.

## ome_tiff_generator.py

This Python script converts the processed data from the previous step into an OME-TIFF file format, which is compatible with Vitessce for visualization. It includes functions for generating cell masks and converting strings to lists. The script reads the CSV files generated in the data_conversion.py step, converts the vertices column from a string to a list format, and generates cell masks for different cell types. These masks are then combined into a stack and saved as an OME-TIFF file, which can be directly loaded into Vitessce for visualization.

## Vitessce_bitmask_VCCF_local.ipynb

This notebook generates a Vitessce visualization using data in the OME-TIFF format. There are two ways to view the visualization: locally as a data export for the HuBMAP publication page or online using vitessce.io for online preview. The `OUTPUT_LEVEL` parameter is used to determine which way to use. The script downloads the necessary image and CSV files, sets up the Vitessce configuration, and creates the visualization. The resulting visualization can be viewed on vitessce.io or exported as a JSON file for further use.

## json_layout_customizer.py

The `json_layout_customizer.py` script is designed to automatically edit and enhance the default layout of Vitessce visualization JSON files within a specified directory and its subdirectories. By targeting the "spatial" component, the script adjusts its width and aligns other components accordingly, enabling a streamlined customization of Vitessce visualizations. This is particularly useful for bulk adjustments where manual editing can be cumbersome. The spatial width can be customized using the `spatial_width` parameter (default `10.0`).

## Dependencies

This project has the following dependencies:
- pandas
- numpy
- ast
- tqdm
- skimage
- vitessce

Please ensure that these libraries are installed in your environment before running the scripts.