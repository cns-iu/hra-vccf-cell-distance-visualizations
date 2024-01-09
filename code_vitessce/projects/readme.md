# Project Folder

## Overview

This repository contains a collection of scripts designed for individual projects, each tailored to specific project needs. The focus is on maintaining ease of use and efficiency by avoiding the complexities of a one-size-fits-all approach. Each project has its unique folder containing all the necessary scripts.

### General Template

In the "general" folder, there is a template script that might suit most projects with simple CSV structures. However, due to varying project requirements and CSV file formats, customization is often necessary. To minimize confusion and facilitate future re-runs of the scripts when data is updated, it's practical to maintain separate folders for each project.

## Scripts Description

### `step_0_preprocess.py`

This script requires the most customization. It's instrumental in unifying different data formats into a similar format, which is crucial for the subsequent steps.

### `step_1_vccf_splitter_file.py`

This script is designed to split a large dataset into smaller regions and calculate distances.

### `cell_data_view_generator.py`

Called by `step_1_vccf_splitter_file.py`, this script generates views for cell data. It does not require manual execution as it's part of the automated pipeline.

### `step_2_data_conversion.py`

This script is responsible for building the vector representations for the shapes used in visualizations. 

### `step_3_ome_tiff_generator.py`

This script is tasked with creating OME-TIFF files, which are essential for Vitessce visualizations. It is the final step in preparing data for visual analysis before using the docker to generate Vitessce json format data.

## Usage

Each folder of scripts is tailored to specific project needs and might require adjustments to work with different datasets. Users are encouraged to refer to individual script documentation and comments for detailed usage instructions.

---
