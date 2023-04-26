There are two .py files:

## vccf_splitter_file.py - Used to divide the main csv file into 64 sub csv files based on the ‘unique_region’ column. This column indicates donor id and their region.

steps to run this file:- 
* Give input .csv file path.
* Give target path to the generated 64 .csv files.

## vccf_visualization.py  - This file contains code for 2D VCCF Visualization and generated .html output file. 

steps to run this file:- 
* Give input arg.sys parameter with region number (Range of region is 1 to 64)
* Give a target path to the generated .html files for respective regions.
