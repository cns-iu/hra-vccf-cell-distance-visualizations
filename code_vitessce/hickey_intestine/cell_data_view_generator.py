import pandas as pd

obs_set_color = [
    {"path": ["Cell Type", "B"], "color": [28, 131, 86]},
    {"path": ["Cell Type", "CD4"], "color": [133, 102, 13]},
    {"path": ["Cell Type", "CD7_Immune"], "color": [50, 131, 254]},
    {"path": ["Cell Type", "CD8_T"], "color": [226, 226, 226]},
    {"path": ["Cell Type", "DC"], "color": [247, 225, 160]},
    {"path": ["Cell Type", "Enterocyte"], "color": [46, 217, 255]},
    {"path": ["Cell Type", "Enterocyte_CD57p"], "color": [46, 217, 255]},
    {"path": ["Cell Type", "Enterocyte_ITLN1p"], "color": [46, 217, 255]},
    {"path": ["Cell Type", "Goblet"], "color": [254, 175, 22]},
    {"path": ["Cell Type", "ICC"], "color": [177, 13, 161]},
    {"path": ["Cell Type", "Lymphatic"], "color": [176, 0, 104]},
    {"path": ["Cell Type", "Macrophage"], "color": [28, 190, 79]},
    {"path": ["Cell Type", "Nerve"], "color": [192, 117, 166]},
    {"path": ["Cell Type", "Neuroendocrine"], "color": [50, 90, 155]},
    {"path": ["Cell Type", "Neutrophil"], "color": [86, 86, 86]},
    {"path": ["Cell Type", "Paneth"], "color": [248, 161, 159]},
    {"path": ["Cell Type", "Plasma"], "color": [120, 42, 182]},
    {"path": ["Cell Type", "SmoothMuscle"], "color": [252, 28, 191]},
    {"path": ["Cell Type", "Stroma"], "color": [251, 228, 38]},
    {"path": ["Cell Type", "TA"], "color": [246, 34, 46]},
    {"path": ["Cell Type", "Endothelial"], "color": [170, 13, 254]},
    {"path": ["Cell Type", "B_link"], "color": [28, 131, 86]},
    {"path": ["Cell Type", "CD4_link"], "color": [133, 102, 13]},
    {"path": ["Cell Type", "CD7_Immune_link"], "color": [50, 131, 254]},
    {"path": ["Cell Type", "CD8_T_link"], "color": [226, 226, 226]},
    {"path": ["Cell Type", "DC_link"], "color": [247, 225, 160]},
    {"path": ["Cell Type", "Enterocyte_link"], "color": [192, 192, 192]},
    {"path": ["Cell Type", "Enterocyte_CD57p_link"], "color": [46, 217, 255]},
    {"path": ["Cell Type", "Enterocyte_ITLN1p_link"], "color": [46, 217, 255]},
    {"path": ["Cell Type", "Goblet_link"], "color": [254, 175, 22]},
    {"path": ["Cell Type", "ICC_link"], "color": [177, 13, 161]},
    {"path": ["Cell Type", "Lymphatic_link"], "color": [176, 0, 104]},
    {"path": ["Cell Type", "Macrophage_link"], "color": [28, 190, 79]},
    {"path": ["Cell Type", "Nerve_link"], "color": [192, 117, 166]},
    {"path": ["Cell Type", "Neuroendocrine_link"], "color": [50, 90, 155]},
    {"path": ["Cell Type", "Neutrophil_link"], "color": [86, 86, 86]},
    {"path": ["Cell Type", "Paneth_link"], "color": [248, 161, 159]},
    {"path": ["Cell Type", "Plasma_link"], "color": [120, 42, 182]},
    {"path": ["Cell Type", "SmoothMuscle_link"], "color": [252, 28, 191]},
    {"path": ["Cell Type", "Stroma_link"], "color": [251, 228, 38]},
    {"path": ["Cell Type", "TA_link"], "color": [246, 34, 46]},
    {"path": ["Cell Type", "Endothelial_link"], "color": [170, 13, 254]},
    {"path": ["Cell Type", "vessel"], "color": [170, 13, 254]}]


cell_data = {
    'cell_id': [],
    'cell_type': [],
    'cell_color': []
}

for idx, item in enumerate(obs_set_color, 1):
    cell_data['cell_id'].append(idx)
    cell_data['cell_type'].append(item['path'][1])
    cell_data['cell_color'].append(item['color'])

cell_sets_data = pd.DataFrame(cell_data)

cell_sets_data.to_csv('cell_sets.csv', index=False)
