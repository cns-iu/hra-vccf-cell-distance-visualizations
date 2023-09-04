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
    'cell_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    'cell_type': ['T-Killer', 'T-Helper', 'T-Reg', 'CD68', 'vessel',
                  "T-Killer_link", 'T-Helper_link', 'T-Reg_link', 'CD68_link',
                  'DDB2', 'P53', 'KI67', 'skin'],
    'cell_color': [[255, 0, 255], [0, 0, 255], [0, 255, 0], [255, 215, 0], [255, 0, 0],
                   [255, 0, 255], [0, 0, 255], [0, 255, 0], [255, 215, 0],
                   [0, 153, 76], [153, 76, 0], [0, 255, 255], [192, 192, 192]]
}
cell_sets_data = pd.DataFrame(cell_data)

cell_sets_data.to_csv('cell_sets.csv', index=False)
