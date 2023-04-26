
import pandas as pd
import numpy as np
import math
import plotly.express as px
import os
from plotly.graph_objs import *
import sys
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
# import plotly.io as pio
import warnings
warnings.simplefilter('ignore')


# # Give path to your data from source : https://www.biorxiv.org/content/10.1101/2021.11.25.469203v1 (High Resolution Single Cell Maps Reveals Distinct Cell Organization and Function Across Different Regions of the Human Intestine)
# split_source_file = '/Users/himanishah/Desktop/VCCF_Computations/doi_10.5061_dryad.pk0p2ngrf__v5/CODEX_HuBMAP_alldata_Dryad.csv'

# data_new = pd.read_csv(split_source_file)

# # 'OLFM4', 'FAP', 'CD25', 'CollIV', 'CK7', 'MUC6'
# # These above columns have null values : 248285, 248285, 248285, 248285, 1735783, 1214947 respectively

# # Store types of unique regions before splitting using vccf_splitter.py


unique_regions = ['B004_Ascending', 'B005_Ascending' ,'B006_Ascending' ,'B009_Right', 'B010_Right', 'B011_Right', 'B012_Right', 'B008_Right' ,
                  'B004_Descending','B005_Descending' ,'B006_Descending' ,'B009_Left' ,'B012_Left' ,'B011_Left','B010_Left' ,'B008_Left' ,'B005_Duodenum' ,
                  'B004_Duodenum' ,'B006_Duodenum','B009_Duodenum' ,'B011_Duodenum' ,'B012_Duodenum' ,'B010_Duodenum','B008_Duodenum', 
                  'B004_Ileum', 'B005_Ileum' ,'B006_Ileum', 'B009_Ileum', 'B010_Ileum' ,'B011_Ileum' ,'B012_Ileum', 'B008_Ileum', 'B006_Mid-jejunum', 
                  'B004_Mid-jejunum', 'B005_Mid-jejunum', 'B009_Mid jejunum', 'B011_Mid jejunum' ,'B012_Mid jejunum', 'B010_Mid jejunum','B008_Mid jejunum' ,
                  'B004_Proximal Jejunum', 'B005_Proximal Jejunum','B006_Proximal Jejunum' ,'B011_Proximal jejunum', 'B009_Proximal jejunum','B010_Proximal jejunum' ,'B012_Proximal jejunum', 'B008_Proximal jejunum',
                  'B004_Descending - Sigmoid' ,'B005_Descending - Sigmoid', 'B006_Descending - Sigmoid', 'B009_Sigmoid' ,'B011_Sigmoid' ,'B010_Sigmoid','B012_Sigmoid' ,'B008_Sigmoid', 
                  'B004_Transverse' ,'B005_Transverse','B006_Transverse', 'B009_Trans' ,'B010_Trans', 'B011_Trans' ,'B012_Trans','B008_Trans']


# Take input Region number within Range 1 to 64
region_index = sys.argv[1]

# Get the path to respective Image
path = r'/Users/himanishah/Desktop/VCCF_Computations/Intestine_64_data/Region_' + str(region_index) + '.csv'
df_Region_1 = pd.read_csv(path)

# Get coordinates x, y, Cell subtype and cellType (2D Data)
df_Region_1 = df_Region_1[['x', 'y', 'Cell Type', 'Cell subtype']]
# Calculate μm per px 
# By dividing 4000/4536 = 0.881 and can also be 4000/4704 = 0.849, as Image size is 16mmx16mm and Image in pixel is 4704px x 4536px
micro_per_pixel = 0.866 # Taking avg if both possibilities 
scale =  micro_per_pixel # to convert given pixel in micro meter unit
df_Region_1['x'] =  scale * df_Region_1['x']
df_Region_1['y'] =  scale * df_Region_1['y']

# Create two data frames each for endothelial cells and all other cells
df_Region_1_vessel = df_Region_1.loc[df_Region_1['Cell Type'] == 'Endothelial']
df_Region_1_immmune = df_Region_1.loc[df_Region_1['Cell Type'] != 'Endothelial']

# Define list variables to store 
x_list = []
y_list = []
xv_list = []
yv_list = []
new_x = []
new_y = []
new_dist = []

# Storing the scaled values
x_list = df_Region_1_immmune['x'].values.tolist()
y_list = df_Region_1_immmune['y'].values.tolist()
xv_list = df_Region_1_vessel['x'].values.tolist()
yv_list = df_Region_1_vessel['y'].values.tolist()

print(len(x_list))
print(len(y_list))
print(len(xv_list))
print(len(yv_list))
temp_x = 0
temp_y = 0

# Calculating nearest endothelial cell
for i in range(len(x_list)):
    # (Source) Weber GM, Ju Y, Börner K. Considerations for Using the Vasculature as a Coordinate System to Map All the Cells in the Human Body. Front Cardiovasc Med. 2020 Mar 13;7:29. doi: 10.3389/fcvm.2020.00029. PMID: 32232057; PMCID: PMC7082726.
    min_dist = 1000 # The distance can be atmost 1mm so that cells can get oxygen 
    has_near = False
    for j in range(len(xv_list)):
        if abs(x_list[i] - xv_list[j]) < min_dist and abs(y_list[i] - yv_list[j]) < min_dist:
            # Euclidean distance calculation
            dist = math.sqrt((x_list[i] - xv_list[j]) ** 2 + (y_list[i] - yv_list[j]) ** 2 )
            if dist < min_dist:
                has_near = True
                min_dist = dist
                temp_x = xv_list[j]
                temp_y = yv_list[j]
    new_x.append(temp_x)
    new_y.append(temp_y)
    # If no endothelial cells within 1000μm distance then assign -1 
    if has_near == False:
        new_dist.append(-1)
    else:
        new_dist.append(min_dist)

x_min, x_max = min(x_list), max(x_list)
y_min, y_max = min(y_list), max(y_list)

margin_index = 0.05
x_margin = (x_max - x_min) * margin_index
y_margin = (y_max - y_min) * margin_index

# Add values to new columns keeping track of nearest endothelial cell coordinates
df_Region_1_immmune['XV'] = new_x
df_Region_1_immmune['YV'] = new_y
df_Region_1_immmune['MinDistance'] = new_dist

# Take all cells with positive distance
new_line_df = df_Region_1_immmune.loc[df_Region_1_immmune['MinDistance'] > 0 ]

# This function generates line
def generate_one_line_df(df, key):
    line_x = [None] * (len(df) * 2)
    line_y = [None] * (len(df) * 2)
    
    line_x[::2] = df[f"X{key}"]
    line_y[::2] = df[f"Y{key}"]
    
    line_x[1::2] = df["x"]
    line_y[1::2] = df["y"]
    
    l_data = dict()
    l_data["x"] = line_x
    l_data["y"] = line_y
    
    l_df = pd.DataFrame(l_data)
    l_gap = (l_df.iloc[1::2]
             .assign(x=np.nan, y=np.nan)
             .rename(lambda x: x + .5))
    l_df_one = pd.concat([l_df, l_gap], sort=False).sort_index().reset_index(drop=True)
    l_df_one.loc[l_df_one.isnull().any(axis=1), :] = np.nan
    return l_df_one


df_Region_1_immmune_one = generate_one_line_df(new_line_df, key='V')

# Initialize color values for up to 26 cell types
color_c = []
color_c = px.colors.qualitative.Alphabet

#Epithelial
# 'Enterocyte': 'Enterocyte',
# 'MUC1+ Enterocyte' :  'MUC1+ Enterocyte',
# 'TA': 'TA',
# 'CD66+ Enterocyte': 'CD66+ Enterocyte',
# 'Paneth': 'Paneth',
# 'Goblet': 'Goblet',
# 'Neuroendocrine': 'Neuroendocrine',
# 'CD57+ Enterocyte': 'CD57+ Enterocyte',
# 'Cycling TA': 'Cycling TA',

#stromal
# 'Smooth muscle': 'Smooth muscle',
# 'Lymphatic': 'Lymphatic',
# 'Endothelial': 'Endothelial',
# 'Stroma': 'Stroma',
# 'Nerve': 'Nerve',
# 'ICC': 'ICC',

#Immune
# 'NK':  'NK',
# 'M1 Macrophage': 'M1 Macrophage',
# 'CD8+ T': 'CD8+ T',
# 'DC': 'DC',
# 'M2 Macrophage': 'M2 Macrophage',
# 'B': 'B',
# 'Neutrophil': 'Neutrophil',
# 'Plasma': 'Plasma',
# 'CD4+ T cell':'CD4+ T cell',
# 'CD7+ Immune': 'CD7+ Immune',

# Create cell dictionary storing colour, shape and cell subtype information
cell_dict = {
    'NK': {
        'legend': "NK",
        'full': "NK",
        'short': "NK",
        'group': "Immune Cells",
        'color': color_c[10],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'M1 Macrophage': {
        'legend': "M1 Macrophage",
        'full': "M1 Macrophage",
        'short': "M1 Macrophage",
        'group': "Immune Cells",
        'color': color_c[9],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
  
    'CD8+ T': {
        'legend': "CD8+ T",
        'full': "CD8+ T",
        'short': "CD8+ T",
        'group': "Immune Cells",
        'color': color_c[8],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'DC': {
        'legend': "DC",
        'full': "DC",
        'short': "DC",
        'group': "Immune Cells",
        'color': color_c[7],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'M2 Macrophage': {
        'legend': "M2 Macrophage",
        'full': "M2 Macrophage",
        'short': "M2 Macrophage",
        'group': "Immune Cells",
        'color': color_c[6],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'B': {
        'legend': "B",
        'full': "B",
        'short': "B",
        'group': "Immune Cells",
        'color': color_c[5],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'Neutrophil': {
        'legend': "Neutrophil",
        'full': "Neutrophil",
        'short': "Neutrophil",
        'group': "Immune Cells",
        'color': color_c[4],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'Plasma': {
        'legend': "Plasma",
        'full': "Plasma",
        'short': "Plasma",
        'group': "Immune Cells",
        'color': color_c[3],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'CD4+ T cell': {
        'legend': "CD4+ T cell",
        'full': "CD4+ T cell",
        'short': "CD4+ T cell",
        'group': "Immune Cells",
        'color': color_c[2],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'CD7+ Immune': {
        'legend': "CD7+ Immune",
        'full': "CD7+ Immune",
        'short': "CD7+ Immune",
        'group': "Immune Cells",
        'color': color_c[1],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'Cycling TA': {
        'legend': "Cycling TA",
        'full': "Cycling TA",
        'short': "Cycling TA",
        'group': "Epithelial",
        'color': color_c[11],
        'marker': 'cross',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'CD57+ Enterocyte': {
        'legend': "CD57+ Enterocyte",
        'full': "CD57+ Enterocyte",
        'short': "CD57+ Enterocyte",
        'group': "Epithelial",
        'color': color_c[12],
        'marker': 'cross',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'Neuroendocrine': {
        'legend': "Neuroendocrine",
        'full': "Neuroendocrine",
        'short': "Neuroendocrine",
        'group': "Epithelial",
        'color': color_c[13],
        'marker': 'cross',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'Goblet': {
        'legend': "Goblet",
        'full': "Goblet",
        'short': "Goblet",
        'group': "Epithelial",
        'color': color_c[14],
        'marker': 'cross',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'Paneth': {
        'legend': "Paneth",
        'full': "Paneth",
        'short': "Paneth",
        'group': "Epithelial",
        'color': color_c[15],
        'marker': 'cross',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'CD66+ Enterocyte': {
        'legend': "CD66+ Enterocyte",
        'full': "CD66+ Enterocyte",
        'short': "CD66+ Enterocyte",
        'group': "Epithelial",
        'color': color_c[16],
        'marker': 'cross',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'TA': {
        'legend': "TA",
        'full': "TA",
        'short': "TA",
        'group': "Epithelial",
        'color': color_c[17],
        'marker': 'cross',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'MUC1+ Enterocyte': {
        'legend': "MUC1+ Enterocyte",
        'full': "MUC1+ Enterocyte",
        'short': "MUC1+ Enterocyte",
        'group': "Epithelial",
        'color': color_c[18],
        'marker': 'cross',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'Enterocyte': {
        'legend': "Enterocyte",
        'full': "Enterocyte",
        'short': "Enterocyte",
        'group': "Epithelial",
        'color': color_c[19],
        'marker': 'cross',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'ICC': {
        'legend': "ICC",
        'full': "ICC",
        'short': "ICC",
        'group': "stromal",
        'color': color_c[20],
        'marker': 'diamond-open',
        'size': 10,
        'histogram_location': [3, 1],
    },

    'Nerve': {
        'legend': "Nerve",
        'full': "Nerve",
        'short': "Nerve",
        'group': "stromal",
        'color': color_c[21],
        'marker': 'diamond-open',
        'size': 10,
        'histogram_location': [3, 1],
    },

    'Smooth muscle': {
        'legend': "Smooth muscle",
        'full': "Smooth muscle",
        'short': "Smooth muscle",
        'group': "stromal",
        'color': color_c[22],
        'marker': 'diamond-open',
        'size': 10,
        'histogram_location': [3, 1],
    },

    'Lymphatic': {
        'legend': "Lymphatic",
        'full': "Lymphatic",
        'short': "Lymphatic",
        'group': "stromal",
        'color': color_c[23],
        'marker': 'diamond-open',
        'size': 10,
        'histogram_location': [3, 1],
    },

    'Stroma': {
        'legend': "Stroma",
        'full': "Stroma",
        'short': "Stroma",
        'group': "stromal",
        'color': color_c[24],
        'marker': 'diamond-open',
        'size': 10,
        'histogram_location': [3, 1],
    },

    'Endothelial': {
        'legend': "Endothelial cell",
        'full': "Endothelial cell",
        'short': "Endothelial",
        'group': 'Vessel',
        'color': color_c[0],
        'marker': 'circle-open',
        'size': 16.83,
        'histogram_location': [0, 0],
    },
  
    '2d': {
        'legend': "2D",
        'group': 'Vessel',
        'color':color_c[25],
        'marker': 'diamond',
        'size': 5,
        'histogram_location': [0, 0],
    }
 
}

# Define functions to generate scatter plots
# Reference code from line 450 to 695: https://github.com/hubmapconsortium/vccf-visualization-2022
def generate_nuclei_scatter(df, ct, visible=True, show_legend=True, legend_group=""):
    return go.Scatter(x=df[df['Cell Type'] == ct]["x"],
                        y=df[df['Cell Type'] == ct]["y"],
                        name=cell_dict[cell_type]['legend'],
                        # text = df[df['Cell Type'] == ct]['Cell Type'].apply(lambda x: f'Cell Type: {x}<br>x: {x}'),
                        # hovertemplate="%{text}<extra></extra>",
                        mode="markers",
                        # text=df[df['Cell Type'] == ct]['Cell Type'],
                        hovertemplate='Cell Type: <br>X: %{x}<br>Y: %{y}',
                        showlegend=show_legend,
                        legendgroup=legend_group,
                        legendgrouptitle_text=legend_group,
                        marker=dict(
                            color= cell_dict[ct]["color"],
                            symbol=cell_dict[ct]['marker'],
                            opacity=0.75,
                            line=dict(
                                color= cell_dict[ct]["color"],
                                width=0
                            )),
                        visible=visible)

def generate_other_scatter(df, key, name, symbol_name, visible=True, show_legend=True, legend_group=""):
    return go.Scatter(x=df[f"X{key}"], y=df[f"Y{key}"],
                        name=name,
                        # text=df[df['Cell Type'] == ct]['Cell Type'].apply(lambda x: f'Cell Type: {x}<br>x: %{x:$,.0f}<br>y: %{y:.0%}'),
                        # hovertemplate="%{text}<extra></extra>",
                        mode="markers",
                        hovertemplate='Cell Type: <br>X: %{x}<br>Y: %{y}',
                        showlegend=show_legend,
                        legendgroup=legend_group,
                        legendgrouptitle_text=legend_group,
                        marker=dict(        
                            color=cell_dict[symbol_name]["color"],
                            symbol=cell_dict[symbol_name]['marker'],
                            opacity=0.5,
                            line=dict(
                                color=cell_dict[symbol_name]["color"],
                                width=0)),
                        visible=visible)

def generate_line(df, name, color, visible=True, opacity=0.5, width=1, show_legend=True, legend_group=""):
    return go.Scatter(x=df["x"],
                        y=df["y"],
                        name=name,
                        # text=df[df['Cell Type'] == ct]['Cell Type'].apply(lambda x: f'Cell Type: {x}<br>x: %{x:$,.0f}<br>y: %{y:.0%}'),
                        # hovertemplate="%{text}<extra></extra>",
                        mode="lines",
                        opacity=opacity,
                        showlegend=show_legend,
                        legendgroup=legend_group,
                        legendgrouptitle_text=legend_group,
                        line=dict(
                            color=color,
                            width=width, ),
                        visible=visible)

immune_cell_types = df_Region_1_immmune['Cell Type'].unique()
traces_n = []
nuclei_type_list = df_Region_1[df_Region_1['Cell subtype'] == 'Immune']['Cell Type'].unique()

for cell_type in set(immune_cell_types):
    
    traces_n.append(generate_nuclei_scatter(df_Region_1_immmune, cell_type,
                                            legend_group=cell_dict[cell_type]['group']))
trace_v = generate_other_scatter(df_Region_1_immmune, key='V', name=cell_dict['Endothelial']['legend'], symbol_name='Endothelial', visible=True,
                                 legend_group="Endothelial")

traces_vessel_line = generate_line(df_Region_1_immmune_one, name=f"Distance-{cell_dict['Endothelial']['legend']}",
                                   color=cell_dict['Endothelial']['color'], visible=True, legend_group="Link")

traces_n.extend([trace_v, traces_vessel_line])
main_fig_count = len(traces_n)

# image_hyperlink = f'https://raw.githubusercontent.com/hubmapconsortium/vccf-visualization-release/main/vheimages/S002_VHE_region_0{region_index:02d}.jpg'
main_subtitle = f'<br><sup>Region {region_index} / Donor {unique_regions[int(region_index) - 1]}  </sup>'
# main_subtitle = f'<br><sup>Region {region_index} / Donor {unique_regions[region_index]}  <a href="{image_hyperlink}">Virtual H&E Image Preview</a></sup>'
# main_subtitle = f'<br> {unique_regions[region_index]} <sup>Region {region_index} </sup>'
hist_subtitle = '<br><sup>Histogram</sup>'
horizontal_spacing = 0.03
figure = make_subplots(
    rows=3, cols=2,
    column_widths=[1.0, 0],
    row_heights=[0.7, 0.2, 0.1],
    specs=[
        [{"type": "Scatter", "colspan": 2}, None, ],
        [{"type": "Histogram"}, None],  # {"type": "Histogram"}
        [{"type": "Scatter"}, None],  # {"type": "Scatter"}
    ],
    horizontal_spacing=horizontal_spacing, vertical_spacing=0.03, shared_xaxes=True,
    subplot_titles=[f'Vascular Common Coordinate Framework 2D Visualization {main_subtitle}', f'Distance to Endothelial Cells{hist_subtitle}', ],  
)

for trace_n in traces_n:
    figure.add_trace(trace_n,1,1)

import plotly.graph_objects as go
for cell_list, col in zip([nuclei_type_list, ],
                                          [1, ]):
    print(cell_list,  col)
    hist_data = []
    hist_names = []
    
    for cell_type in cell_list:
        data = df_Region_1_immmune[df_Region_1_immmune['Cell Type'] == cell_type]["MinDistance"]
        print(cell_type, data.size)
        if data.size > 5:
            hist_data.append(data)
            hist_names.append(cell_type)
        
    fig2 = ff.create_distplot(hist_data, hist_names, histnorm='probability')  # , curve_type='normal')

    for i in range(len(hist_data)):
             
            figure.add_trace(go.Histogram(
                x=df_Region_1_immmune[df_Region_1_immmune['Cell Type'] == hist_names[i]]["MinDistance"],
                # xbins=100,
                opacity=0.6,
                marker=dict(color=cell_dict[hist_names[i]]['color']),
                showlegend=False,
                name=cell_dict[hist_names[i]]['legend'],
                bingroup='overlay'
            ), row=2, col=col)
            line = fig2['data'][len(hist_data) + i]
            line['y'] = line['y'] * len(hist_data[i])
            if not any(y > 1e5 for y in line['y']):
                figure.add_trace(go.Scatter(line,
                                     line=dict(color=cell_dict[hist_names[i]]['color'], width=2), showlegend=False,
                                     ), row=2, col=col)
            df_Region_1_immmune[f'{hist_names[i]}_pos'] = 0.1 * (i + 1)
            figure.add_trace(go.Scatter(x=df_Region_1_immmune[df_Region_1_immmune['Cell Type'] == hist_names[i]]["MinDistance"],
                                    y=df_Region_1_immmune[f'{hist_names[i]}_pos'],
                                    mode='markers',
                                    opacity=0.6,
                                    marker=dict(color=cell_dict[hist_names[i]]['color'], symbol='line-ns-open'),
                                    showlegend=False,
                                    ), row=3, col=col)

    # some manual adjustments on the rugplot
    figure.update_yaxes(range=[0, 0.1 * (len(hist_names) + 1)],
                     tickvals=[0.1 * (i + 1) for i in range(len(hist_names))], ticktext=hist_names, 
                     row=3, col=col)
    figure.update_xaxes(tickfont=dict(color='rgba(0,0,0,0)', size=1), row=2, col=col)
 
# Invisble scale for keep space instant
invisible_scale = go.Scatter(
    name="",
    visible=True,
    showlegend=False,
    opacity=0,
    hoverinfo='none',
    x=[x_min - x_margin, x_max + x_margin],
    y=[y_min - y_margin, y_max + y_margin],
    
)
figure.add_trace(invisible_scale)

# Add dropdown
histogram_layout_buttons = list([
    dict(
        args=["barmode", "overlay"],
        label="Overlaid",
        method="relayout"
    ),
    dict(
        args=["barmode", "relative"],
        label="Stacked",
        method="relayout"
    ),
    dict(
        args=["barmode", "group"],
        label="Grouped",
        method="relayout"
    )
])
layer_select_buttons = []

# layout update
for annotation in figure['layout']['annotations'][:1]:
    annotation['x'] = 0
    annotation['xanchor'] = "left"
    annotation['y'] = 1
    annotation['yanchor'] = "top"
    annotation['font'] = dict(
        family="Arial, Bahnschrift",
        size=24, )
for annotation in figure['layout']['annotations'][1:]:
    annotation['x'] += 0.35 - horizontal_spacing
    annotation['xanchor'] = "right"
    annotation['y'] -= 0.05
    annotation['font'] = dict(
        family="Arial, Bahnschrift",
        size=18, )

background_color = 'rgb(240,246,255)'
figure.update_yaxes(rangemode='tozero', tickfont=dict(size=12), row=2)
figure.update_yaxes(rangemode='tozero', tickfont=dict(size=8), row=3)
figure.update_xaxes(rangemode='tozero', tickfont=dict(size=12), row=2)
figure.update_xaxes(rangemode='tozero', tickfont=dict(size=12), row=3)
figure.update_xaxes(ticklabelposition="outside", side="bottom",
                 title=dict(text="Distance (μm)", standoff=5, font_size=14), row=3, )
figure.update_xaxes(range=[0, 210], row=3, col=1)
figure.update_yaxes(ticklabelposition="outside", side="left",
                 title=dict(text="Count #", standoff=5, font_size=14), row=2, col=1)
figure.update_traces(connectgaps=False, selector=dict(type="Scatter3d"))
figure.update_layout(
    updatemenus=[
        dict(
            buttons=histogram_layout_buttons,
            direction="right",
            pad={"r": 0, "t": 5},
            showactive=True,
            x=0,
            xanchor="left",
            y=-0.06,
            yanchor="bottom"
        ),
    ],
    font=dict(
        family="Arial, Bahnschrift",
        size=12,
       
    ),
    margin=dict(
        l=5,
        r=5,
        b=5,
        t=5,
        pad=0
    ),
    legend=dict(
        groupclick="toggleitem",

    ),
    barmode='overlay',
    
    scene=dict(
        aspectmode='data',
        xaxis=dict(nticks=10, backgroundcolor=background_color, ),
        yaxis=dict(nticks=10, backgroundcolor=background_color, ),
        # zaxis=dict(nticks=5, backgroundcolor=background_color, ),
    ),
    plot_bgcolor=background_color,
    # hovermode='x unified'

)

# Sate path to store .html file
figure.write_html(os.path.join('/Users/himanishah/Desktop/VCCF_Computations/Intestine_64_data/html_vccf', f"Region_{region_index}.html"))
# Sate path to store .png file
figure.write_image(os.path.join('/Users/himanishah/Desktop/VCCF_Computations/Intestine_64_data/images_vccf', f"Region_{region_index}.png"))

# export as static image
# pio.write_image(figure, os.path.join('/Users/himanishah/Desktop/VCCF_Computations/Intestine_64_data/images_vccf', f"Region_{region_index}.png"))