# Utils Folder Overview

This `utils` directory contains a collection of utility scripts designed to facilitate the processing and handling of cell data and project information for various projects. 

## Files Description

### Outdated Cell Data View Generators
- **cell_data_view_generator_GFTU.py**
- **cell_data_view_generator_hickey.py**

  These scripts were previously used to quickly generate `cell_sets.csv` for the GFTU and Hickey projects. They are now outdated, as the `cell_sets.csv` file generation is handled by the new `cell_data_view_generator.py` in each project folder. This new script is called by `vccf_splitter_file.py` when splitting the raw CSV file.

### Info CSV Generators
- **info_csv_generator_GFTU.py**
- **info_csv_generator_VCCF.py**
- **info_csv_generator_gloria.py**
- **info_csv_generator_hickey.py**
- **info_csv_generator_hickey_inte.py**
- **info_csv_generator_spleen.py**
- **info_csv_generator_xenium.py**

  These scripts are used to generate `info.csv` files, which are necessary in creating Vitessce JSON files via Docker. While `info.csv` can be manually created and written, these generators are particularly useful for handling large datasets with multiple rows and simple file name patterns. Due to the simple structure and function of these scripts, they are created for each individual project instead of creating one general file working for all possible project but with complex parameters. This will keep the ease of use and efficiency of the project.

## Usage Notes

- The outdated `cell_data_view_generator` scripts are kept for historical reference but are not recommended for current use.
- For generating `info.csv` files, use the project-specific `info_csv_generator` scripts. These are straightforward and tailored to the unique requirements of each project.
