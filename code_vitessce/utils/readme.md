# Repository Description

This folder contains utils for other folders.

## json_layout_customizer.py

The `json_layout_customizer.py` script is designed to automatically edit and enhance the default layout of Vitessce visualization JSON files within a specified directory and its subdirectories. By targeting the "spatial" component, the script adjusts its width and aligns other components accordingly, enabling a streamlined customization of Vitessce visualizations. This is particularly useful for bulk adjustments where manual editing can be cumbersome. The spatial width can be customized using the `spatial_width` parameter (default `10.0`).

## histogram.py
This script generates the histogram of the distance from each cell to the nearest endothelial cells. The parameter is for the unit length of the pixel and default is 1.0 um/pixel. Sample usage:

### Sample Commands:

```
# SPLEEN
python g:/HuBMAP/Repos/hra-vccf-cell-distance-visualizations/code_vitessce/utils/histogram.py G:\HuBMAP\spleen\new_data\vitessce_raw\Region_FSLD_nuclei.csv 0.377
# XENIUM
python g:/HuBMAP/Repos/hra-vccf-cell-distance-visualizations/code_vitessce/utils/histogram.py G:\HuBMAP\Xenium_colon_polyp\new_data\vitessce_raw\Region_17_nuclei.csv 1.0
# GLORIA 11
python g:/HuBMAP/Repos/hra-vccf-cell-distance-visualizations/code_vitessce/utils/histogram.py G:\HuBMAP\gloria\new_data\vitessce_raw\Region_D265_nuclei.csv 1.0
# GLORIA 12
python g:/HuBMAP/Repos/hra-vccf-cell-distance-visualizations/code_vitessce/utils/histogram.py G:\HuBMAP\gloria\new_data\vitessce_raw\Region_D26512_nuclei.csv 1.0
# BE1
python g:/HuBMAP/Repos/hra-vccf-cell-distance-visualizations/code_vitessce/utils/histogram.py "G:\HuBMAP\Hickey\intestine_new_data\vitessce_raw\Region_Barretts Esophagus_nuclei.csv" 0.377
# BE2
python g:/HuBMAP/Repos/hra-vccf-cell-distance-visualizations/code_vitessce/utils/histogram.py G:\HuBMAP\Hickey\intestine_new_data\vitessce_raw\Region_tonsil_nuclei.csv 0.377
# intestine
python g:/HuBMAP/Repos/hra-vccf-cell-distance-visualizations/code_vitessce/utils/histogram.py G:\HuBMAP\Hickey\Intestine_64_data\vitessce_vccf\Region_1_nuclei.csv 0.866
# skin
python g:/HuBMAP/Repos/hra-vccf-cell-distance-visualizations/code_vitessce/utils/histogram.py G:\GE\skin_12_data\region_4\nuclei_hist.csv 1.0
# colon 3d
python g:/HuBMAP/Repos/hra-vccf-cell-distance-visualizations/code_vitessce/utils/histogram.py G:\HuBMAP\colon_3d\new_data\vitessce_raw\Region_CRC01050_nuclei.csv 1.0 # raw unit length is 0.2125 but the reg data is calculated so scale is 1.0
```