#  Preview: Vasculature CCF Visualization

HuBMAP Atlas Previews demonstrate functionality and resources that will become available in future HuBMAP portal releases. Previews may rely on externally hosted data or analysis results that were generated with processing pipelines that are not yet integrated into the HuBMAP data infrastructure.


### Description

This preview showcases a novel visualization in support of a vasculature-based common coordinate system (VCCF), see paper on “[Considerations for Using the Vasculature as a Coordinate System to Map All the Cells in the Human Body](https://doi.org/10.3389/fcvm.2020.00029)”.

Experimental data from the “[Human Digital Twin: Automated Cell Type Distance Computation and 3D Atlas Construction in Multiplexed Skin Biopsies](https://www.biorxiv.org/content/10.1101/2022.03.30.486438v1)” paper, is used to compute distances of different cell types to the nearest blood vessel using 3D volumes of digital skin biopsy data generated using multiplexed imaging of sequential skin sections from younger and older patients (n=12; 22-72 years). Skin biopsies were collected from patients from different anatomical regions and different sun exposure effects (mild, moderate and marked). Samples underwent multiplexed imaging with 18 biomarkers covering nine cell types (epithelial, fibroblast, immune cells (macrophage, T-helper, T-killer, T-reg), endothelial, myoepithelial and nerve) markers of UV damage (p53, DDB2) and proliferation (Ki67). Following classification of cells into epithelial, endothelial, immune and markers of damage, the tissue data was reconstructed into 3D volumes. The reconstructed 3D cell data was used to compute distance distributions and network layouts of major immune cells to the nearest blood vessel in support of a vasculature based common coordinate framework and compared across age groups. Further, analysis of cell damage and proliferation markers (p53, Ki67 and DDB2) in the epithelial layer and their distance provided new insights into the effects of aging on skin.


### Atlas Details

Vascular pathways in human have been studied in much detail. Constructing a vasculature-based coordinate system makes sense biologically as almost every living cell must be within a small distance to a blood vessel (100µm to 1mm, depending on the tissue) in order to receive oxygen. This Preview showcases a 3D interactive visualization of distances from cell nuclei of different cell types different cell types (T-regulatory, T-helper, and macrophages/CD68) to vasculature and skin surface tissue cells and compute violin plot comparisons across donor groups. For example, Region 5 for an UV exposed sample from the neck of a 33-year-old female (HuBMAP sample ID: HBM499.VJVR.265). Segmented blood vessels are rendered in red, T-regulatory cells in cyan, T-helper cells in blue, T-killer cells in dark red, and macrophages in yellow. The closest distance between an immune cell and a blood vessel is indicated by a gray line. The 3D visualization is interactive and available for all 10 tissue blocks used in the paper. Distance distributions for all three cell types are given below the 3D visualization.  


### Experimental Data Details

The experimental skin data used here is detailed in the “[Human Digital Twin: Automated Cell Type Distance Computation and 3D Atlas Construction in Multiplexed Skin Biopsies](https://www.biorxiv.org/content/10.1101/2022.03.30.486438v1)” paper.

### Contributors
**Skin Data:** Soumya Ghose, Chrystal Chadwick, Elizabeth McDonough, Sanghee Cho, Johnhan Ho, Arivarasan Karunamurthy, Anup Sood, Yousef Al-Kofahi, Louis Falo & Fiona Ginty

**Vasculature CCF Visualization:** Yingnan Ju & Katy Börner


### Attribution

| Group  | Creator                          |
|--------|----------------------------------|
| RTI-GE | Fiona Ginty (fiona.ginty@ge.com) |
| MC-IU  | Katy Börner (katy@indiana.edu)   |


### Visualization

<div class="tabs-nav">
  <ul class="nav nav-tabs">
    <li class="active"><a data-toggle="tab" href="#region1">Region 1</a></li>
    <li><a data-toggle="tab" href="#region2">Region 2</a></li>
    <li><a data-toggle="tab" href="#region3">Region 3</a></li>
    <li><a data-toggle="tab" href="#region4">Region 4</a></li>
    <li><a data-toggle="tab" href="#region5">Region 5</a></li>
    <li><a data-toggle="tab" href="#region7">Region 7</a></li>
    <li><a data-toggle="tab" href="#region8">Region 8</a></li>
    <li><a data-toggle="tab" href="#region9">Region 9</a></li>
    <li><a data-toggle="tab" href="#region10">Region 10</a></li>
    <li><a data-toggle="tab" href="#region11">Region 11</a></li>
    <li><a data-toggle="tab" href="#violincell">Violin Cell</a></li>
    <li><a data-toggle="tab" href="#violinCellAll">Violin Cell All Region</a></li>
    <li><a data-toggle="tab" href="#ViolinDamage">Violin Damage</a></li>
     <li><a data-toggle="tab" href="#ViolinDamageAll">Violin Damage All Region</a></li>
  </ul>

  <div class="tab-content">
    <div id="region1" class="tab-pane fade in active">
      <h3>Region 1</h3>
      <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_1.html" >
      <img src="../img/region1.png" alt="region1" style="width:100%">
        </a>
      <p> Open the visualization in <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_1.html" >new window.</a>  
    </div>
    <div id="region2" class="tab-pane fade">
      <h3>Region 2</h3>
        <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_2.html" >
      <img src="../img/region2.png" alt="region2" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_2.html" >new window.</a>
  </div>
    <div id="region3" class="tab-pane fade">
      <h3>Region 3</h3>
        <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_3.html" >
      <img src="../img/region3.png" alt="region3" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_3.html" >new window.</a>
    </div>
    <div id="region4" class="tab-pane fade">
      <h3>Region 4</h3>
        <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_4.html" >
      <img src="../img/region4.png" alt="region4" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_4.html" >new window.</a>
    </div>
    <div id="region5" class="tab-pane fade">
      <h3>Region 5</h3>
        <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_5.html" >
      <img src="../img/region5.png" alt="region5" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_5.html" >new window.</a>
    </div>
    <div id="region7" class="tab-pane fade">
      <h3>Region 7</h3>
        <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_7.html" >
      <img src="../img/region7.png" alt="region7" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_7.html" >new window.</a>
    </div>
    <div id="region8" class="tab-pane fade">
      <h3>Region 8</h3>
        <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_8.html" >
      <img src="../img/region8.png" alt="region8" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_8.html" >new window.</a>
    </div>
    <div id="region9" class="tab-pane fade">
      <h3>Region 9</h3>
        <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_9.html" >
      <img src="../img/region9.png" alt="region9" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_9.html" >new window.</a>
    </div>
    <div id="region10" class="tab-pane fade">
      <h3>Region 10</h3>
        <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_10.html" >
      <img src="../img/region10.png" alt="region10" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_10.html" >new window.</a>
    </div>
    <div id="region11" class="tab-pane fade">
      <h3>Region 11</h3>
        <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_11.html" >
      <img src="../img/region11.png" alt="region11" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/region_11.html" >new window.</a>
    </div>
    <div id="violincell" class="tab-pane fade">
        <h3>Violin Cell</h3>
        <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/violin_cell.html" >
        <img src="../img/violincell.png" alt="violincell" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/violin_cell.html" >new window.</a>
    </div>
    <div id="violinCellAll" class="tab-pane fade">
        <h3>Violin Cell All Region</h3>
        <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/violin_cell_all_region.html" >
        <img src="../img/violinCellAll.png" alt="violinCellAll" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/violin_cell_all_region.html" >new window.</a>
    </div>
    <div id="ViolinDamage" class="tab-pane fade">
        <h3>Violin Damage</h3>
        <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/epidermis/violin_damage_epidermis.html" >
        <img src="../img/violinDamage.png" alt="ViolinDamage" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/epidermis/violin_damage_epidermis.html" >new window.</a>
    </div>
    <div id="ViolinDamageAll" class="tab-pane fade">
        <h3>Violin Damage All Region</h3>
        <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/epidermis/violin_damage_all_region_epidermis.html" >
        <img src="../img/violinDamageAll.png" alt="ViolinDamageAll" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://hubmapconsortium.github.io/vccf-visualization-release/html/epidermis/violin_damage_all_region_epidermis.html" >new window.</a>
    </div>
</div>

Try all the 10 skin samples [here](https://hubmapconsortium.github.io/vccf-visualization-release/).
