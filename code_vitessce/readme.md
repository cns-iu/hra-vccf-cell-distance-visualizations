# Repository Description

This repository is designed for visualizing cell data using Vitessce. It contains codes files that serve different purposes in the data processing and visualization pipeline.

## cell_data_view_generator.py

This Python script is responsible for generating CSV files that define the color scheme for the cell data visualization. These CSV files can be used to define the color scheme and other properties for visualizing the cell data in Vitessce.

## data_conversion.py

This Python script is used to convert raw data into a format suitable for generating an OME-TIFF file for visualization in Vitessce. The main function reads CSV files containing the raw data, filters the data based on specified values, and constructs tables for cell vertices, link vertices, and damage vertices. These tables are then saved as separate CSV files. The generated CSV files serve as input for the next step in the data processing pipeline.

## ome_tiff_generator.py

This Python script converts the processed data from the previous step into an OME-TIFF file format, which is compatible with Vitessce for visualization. It includes functions for generating cell masks and converting strings to lists. The script reads the CSV files generated in the data_conversion.py step, converts the vertices column from a string to a list format, and generates cell masks for different cell types. These masks are then combined into a stack and saved as an OME-TIFF file, which can be directly loaded into Vitessce for visualization.

## Dependencies

This project has the following dependencies:
- pandas
- numpy
- ast
- tqdm
- skimage
- vitessce

Please ensure that these libraries are installed in your environment before running the scripts.