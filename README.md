# hra-vccf-cell-distance-visualizations
VCCF cell distance visualizations extended to other organs, based on work on skin data.

###  Preview: Vasculature CCF Visualization

HuBMAP Atlas Previews demonstrate functionality and resources that will become available in future HuBMAP portal releases. Previews may rely on externally hosted data or analysis results that were generated with processing pipelines that are not yet integrated into the HuBMAP data infrastructure.


### Description

This preview showcases a novel visualization in support of a vasculature-based common coordinate system (VCCF), see paper on “[Considerations for Using the Vasculature as a Coordinate System to Map All the Cells in the Human Body](https://doi.org/10.3389/fcvm.2020.00029)”.

Experimental data from the “[High Resolution Single Cell Maps Reveals Distinct Cell Organization and Function Across Different Regions of the Human Intestine](https://www.biorxiv.org/content/early/2021/11/25/2021.11.25.469203)” paper, is used to compute distances of different cell types to the nearest blood vessel using 2D volumes of digital intestine biopsy data generated using multiplexed imaging on 64 sections of the human intestine (~16 mm2) from 8 donors (B004, B005, B006, B008, B009, B010, B011, and B012) using a panel of 57 oligonucleotide-barcoded antibodies. Subsequently, images underwent standard CODEX image processing (tile stitching, drift compensation, cycle concatenation, background subtraction, deconvolution, and determination of best focal plane), single cell segmentation, and column marker z-normalization by tissue. The outputs of this process were data frames of 2.6 million cells with 57 antibody fluorescence values quantified from each marker. Each cell has its cell type, cellular neighborhood, community of neighborhooods, and tissue unit defined with x, y coordinates representing pixel location in the original image. This data was taken from  8 donors with 8 individual tissue regions (64 tissues imaged) across 2.6 million cells, with 25 cell types, 20 multicellular neighborhoods, 10 communities of neighborhoods, and 3 tissue segments could be used to understand the cellular interactions, composition, and structure of the human intestine from the duodenum to the sigmoid colon and understand differences between different areas of the intestine. 

### Atlas Details

This Preview showcases a 2D interactive visualization of distances from cell nuclei of different cell types(NK, M1 Macrophage, CD8+ T, DC, M2 Macrophage, B, Neutrophil, Plasma, CD4+ T cell, CD7+ Immune) to vasculature across donor groups.  


### Experimental Data Details

The experimental skin data used here is detailed in the “[High Resolution Single Cell Maps Reveals Distinct Cell Organization and Function Across Different Regions of the Human Intestine](https://www.biorxiv.org/content/early/2021/11/25/2021.11.25.469203)” paper.

### Contributors
**Intestine Data:** 

**Vasculature CCF Visualization:** 


### Attribution

| Group  | Creator                          |
|--------|----------------------------------|
|  |  |
|   |    |


### Visualization

<div class="tabs-nav">
  <ul class="nav nav-tabs">
    <li class="active"><a data-toggle="tab" href="#region1">Region 1</a></li>
    <li><a data-toggle="tab" href="#region2">Region 2</a></li>
    <li><a data-toggle="tab" href="#region3">Region 3</a></li>
    <li><a data-toggle="tab" href="#region4">Region 4</a></li>
    <li><a data-toggle="tab" href="#region5">Region 5</a></li>
    <li><a data-toggle="tab" href="#region2">Region 6</a></li>
    <li><a data-toggle="tab" href="#region7">Region 7</a></li>
    <li><a data-toggle="tab" href="#region8">Region 8</a></li>
    <li><a data-toggle="tab" href="#region9">Region 9</a></li>
    <li><a data-toggle="tab" href="#region10">Region 10</a></li>
    <li><a data-toggle="tab" href="#region2">Region 11</a></li>
    <li><a data-toggle="tab" href="#region2">Region 12</a></li>
    <li><a data-toggle="tab" href="#region3">Region 13</a></li>
    <li><a data-toggle="tab" href="#region4">Region 14</a></li>
    <li><a data-toggle="tab" href="#region5">Region 15</a></li>
    <li><a data-toggle="tab" href="#region7">Region 16</a></li>
    <li><a data-toggle="tab" href="#region8">Region 17</a></li>
    <li><a data-toggle="tab" href="#region9">Region 18</a></li>
    <li><a data-toggle="tab" href="#region10">Region 19</a></li>
    <li><a data-toggle="tab" href="#region2">Region 20</a></li>
    <li><a data-toggle="tab" href="#region2">Region 21</a></li>
    <li><a data-toggle="tab" href="#region2">Region 22</a></li>
    <li><a data-toggle="tab" href="#region3">Region 23</a></li>
    <li><a data-toggle="tab" href="#region4">Region 24</a></li>
    <li><a data-toggle="tab" href="#region5">Region 25</a></li>
    <li><a data-toggle="tab" href="#region7">Region 26</a></li>
    <li><a data-toggle="tab" href="#region8">Region 27</a></li>
    <li><a data-toggle="tab" href="#region9">Region 28</a></li>
    <li><a data-toggle="tab" href="#region10">Region 29</a></li>
    <li><a data-toggle="tab" href="#region2">Region 30</a></li>
    <li><a data-toggle="tab" href="#region2">Region 31</a></li>
    <li><a data-toggle="tab" href="#region2">Region 32</a></li>
    <li><a data-toggle="tab" href="#region3">Region 33</a></li>
    <li><a data-toggle="tab" href="#region4">Region 34</a></li>
    <li><a data-toggle="tab" href="#region5">Region 35</a></li>
    <li><a data-toggle="tab" href="#region7">Region 36</a></li>
    <li><a data-toggle="tab" href="#region8">Region 37</a></li>
    <li><a data-toggle="tab" href="#region9">Region 38</a></li>
    <li><a data-toggle="tab" href="#region10">Region 39</a></li>
    <li><a data-toggle="tab" href="#region2">Region 40</a></li>
    <li><a data-toggle="tab" href="#region2">Region 41</a></li>
    <li><a data-toggle="tab" href="#region2">Region 42</a></li>
    <li><a data-toggle="tab" href="#region3">Region 43</a></li>
    <li><a data-toggle="tab" href="#region4">Region 44</a></li>
    <li><a data-toggle="tab" href="#region5">Region 45</a></li>
    <li><a data-toggle="tab" href="#region7">Region 46</a></li>
    <li><a data-toggle="tab" href="#region8">Region 47</a></li>
    <li><a data-toggle="tab" href="#region9">Region 48</a></li>
    <li><a data-toggle="tab" href="#region10">Region 49</a></li>
    <li><a data-toggle="tab" href="#region2">Region 50</a></li>
    <li><a data-toggle="tab" href="#region2">Region 51</a></li>
    <li><a data-toggle="tab" href="#region2">Region 52</a></li>
    <li><a data-toggle="tab" href="#region3">Region 53</a></li>
    <li><a data-toggle="tab" href="#region4">Region 54</a></li>
    <li><a data-toggle="tab" href="#region5">Region 55</a></li>
    <li><a data-toggle="tab" href="#region7">Region 56</a></li>
    <li><a data-toggle="tab" href="#region8">Region 57</a></li>
    <li><a data-toggle="tab" href="#region9">Region 58</a></li>
    <li><a data-toggle="tab" href="#region10">Region 59</a></li>
    <li><a data-toggle="tab" href="#region2">Region 60</a></li>
    <li><a data-toggle="tab" href="#region2">Region 61</a></li>
    <li><a data-toggle="tab" href="#region2">Region 62</a></li>
    <li><a data-toggle="tab" href="#region3">Region 63</a></li>
    <li><a data-toggle="tab" href="#region4">Region 64</a></li>

  </ul>

  <div class="tab-content">
    
    <div id="region1" class="tab-pane fade in active">
      <h3>Region 1</h3>
      <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_1.html" >
      <img src="/images_vccf/Region_1.png" alt="region1" style="width:100%">
        </a>
      <p> Open the visualization in <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_1.html" >new window.</a>  
    </div>
    
    <div id="region2" class="tab-pane fade">
      <h3>Region 2</h3>
        <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_2.html" >
      <img src="/images_vccf/Region_2.png" alt="region2" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_2.html" >new window.</a>
  </div>
    
    <div id="region3" class="tab-pane fade">
      <h3>Region 3</h3>
        <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_3.html" >
      <img src="/images_vccf/Region_3.png" alt="region3" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_3.html" >new window.</a>
    </div>
    
    <div id="region4" class="tab-pane fade">
      <h3>Region 4</h3>
        <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_4.html" >
      <img src="/images_vccf/Region_4.png" alt="region4" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_4.html" >new window.</a>
    </div>
    
    <div id="region5" class="tab-pane fade">
      <h3>Region 5</h3>
        <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_5.html" >
      <img src="/images_vccf/Region_5.png" alt="region5" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_5.html" >new window.</a>
    </div>
    
    <div id="region6" class="tab-pane fade">
      <h3>Region 6</h3>
        <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_6.html" >
      <img src="/images_vccf/Region_6.png" alt="region6" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_6.html" >new window.</a>
    </div>
    
    <div id="region7" class="tab-pane fade">
      <h3>Region 7</h3>
        <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_7.html" >
      <img src="/images_vccf/Region_7.png" alt="region7" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_7.html" >new window.</a>
    </div>
    
    <div id="region8" class="tab-pane fade">
      <h3>Region 8</h3>
        <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_8.html" >
      <img src="/images_vccf/Region_8.png" alt="region8" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_8.html" >new window.</a>
    </div>
    
    <div id="region9" class="tab-pane fade">
      <h3>Region 9</h3>
        <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_9.html" >
      <img src="/images_vccf/Region_9.png" alt="region9" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_9.html" >new window.</a>
    </div>
    
    <div id="region10" class="tab-pane fade">
      <h3>Region 10</h3>
        <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_10.html" >
      <img src="/images_vccf/Region_10.png" alt="region10" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://htmlpreview.github.io/?https://github.com/shahhi/hra-vccf-cell-distance-visualizations/blob/main/html_vccf/region_10.html" >new window.</a>
    </div>
    
    
  
</div>


