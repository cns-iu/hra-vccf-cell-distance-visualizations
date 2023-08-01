import pandas as pd

cell_dict = {'B': 1, 'CD4+ T cell': 2, 'CD57+ Enterocyte': 3, 'CD66+ Enterocyte': 4, 'CD7+ Immune': 5, 'CD8+ T': 6,
             'Cycling TA': 7, 'DC': 8, 'Enterocyte': 9, 'Goblet': 10, 'ICC': 11, 'Lymphatic': 12,
             'M1 Macrophage': 13, 'M2 Macrophage': 14, 'MUC1+ Enterocyte': 15, 'NK': 16, 'Nerve': 17, 'Neuroendocrine': 18,
             'Neutrophil': 19, 'Paneth': 20, 'Plasma': 21, 'Smooth muscle': 22, 'Stroma': 23, 'TA': 24,
             'B_link': 1, 'CD4+ T cell_link': 2, 'CD57+ Enterocyte_link': 3,
             'CD66+ Enterocyte_link': 4, 'CD7+ Immune_link': 5, 'CD8+ T_link': 6,
             'Cycling TA_link': 7, 'DC_link': 8, 'Enterocyte_link': 9,
             'Goblet_link': 10, 'ICC_link': 11, 'Lymphatic_link': 12,
             'M1 Macrophage_link': 13, 'M2 Macrophage_link': 14, 'MUC1+ Enterocyte_link': 15,
             'NK_link': 16, 'Nerve_link': 17, 'Neuroendocrine_link': 18,
             'Neutrophil_link': 19, 'Paneth_link': 20, 'Plasma_link': 21,
             'Smooth muscle_link': 22, 'Stroma_link': 23, 'TA_link': 24,
             'Endothelial': 25}

cell_data = {
    'cell_id': list(cell_dict.values()),
    'cell_type': list(cell_dict.keys())
}

print(cell_data)

cell_sets_data = pd.DataFrame(cell_data)

cell_sets_data.to_csv('cell_sets.csv', index=False)
