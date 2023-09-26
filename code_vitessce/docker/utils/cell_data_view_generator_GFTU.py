import pandas as pd

# cell color
#     obs_set_color = [
#     {"path": ["Cell Type", "vessel"], "color": [255, 0, 0]},
#     {"path": ["Cell Type", "T-Killer"], "color": [255, 0, 255]},
#     {"path": ["Cell Type", "T-Killer_link"], "color": [255, 0, 255]},
#     {"path": ["Cell Type", "T-Helper"], "color": [0, 0, 255]},
#     {"path": ["Cell Type", "T-Helper_link"], "color": [0, 0, 255]},
#     {"path": ["Cell Type", "T-Reg"], "color": [0, 255, 0]},
#     {"path": ["Cell Type", "T-Reg_link"], "color": [0, 255, 0]},
#     {"path": ["Cell Type", "CD68"], "color": [255, 215, 0]},
#     {"path": ["Cell Type", "CD68_link"], "color": [255, 215, 0]},
#     {"path": ["Cell Type", "DDB2"], "color": [0, 153, 76]},
#     {"path": ["Cell Type", "P53"], "color": [153, 76, 0]},
#     {"path": ["Cell Type", "KI67"], "color": [0, 255, 255]},
#     {"path": ["Cell Type", "skin"], "color": [192, 192, 192]},
# ]

cell_data = {
    'cell_id': [1, 2, 3, 4, 5, 6],
    'cell_type': ["Ground Truth", 'Tom', 'Gleb', 'Whats goin on', 'Deeplive.exe', 'Deepflash2'],
    'cell_color': [[255, 255, 0], [0, 0, 0], [255, 128, 0], [0, 0, 255], [0, 255, 0], [153, 0, 153]]
}
cell_sets_data = pd.DataFrame(cell_data)

cell_sets_data.to_csv('cell_sets.csv', index=False)
