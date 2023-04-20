
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


unique_images= ['10_31742_1_2' , '20_31789_14_2' , '16_31772_4_5' , '6_31730_10_11'
 , '8_31736_12_17' , '6_31731_15_8' , '6_31727_8_9' , '20_31791_18_13'
 , '8_31736_12_19' , '8_31738_6_17' , '6_31729_10_1' , '10_31740_16_6'
 , '18_31785_5_15' , '10_31744_1_3' , '6_31732_11_10' , '16_31768_17_2'
 , '16_31763_20_10' , '14_31759_20_6' , '16_31768_3_6' , '20_31797_6_9'
 , '16_31771_14_14' , '8_31735_12_8' , '20_31794_6_6' , '18_31783_14_8'
 , '8_31736_12_15' , '14_31758_20_4' , '6_31727_15_3' , '6_31731_11_5'
 , '6_31725_8_3' , '6_31731_11_2' , '16_31772_4_7' , '6_31726_8_5' , '20_31793_6_2'
 , '8_31734_12_4' , '10_31741_1_1' , '8_31734_12_3' , '14_31758_20_5'
 , '16_31773_4_10' , '10_31745_16_9' , '6_31730_10_12' , '18_31783_14_9'
 , '6_31729_10_2' , '18_31783_14_7' , '6_31729_10_5' , '16_31773_4_8'
 , '6_31727_8_12' , '16_31765_19_1' , '8_31735_12_11' , '16_31774_14_13'
 , '8_31736_16_5' , '16_31762_20_9' , '14_31756_20_2' , '16_31767_17_1'
 , '8_31735_12_10' , '20_31792_18_14' , '14_31759_16_18' , '16_31767_3_3'
 , '20_31790_18_12' , '16_31767_3_4' , '14_31755_18_1' , '16_31762_20_8'
 , '8_31736_16_3' , '6_31725_15_2' , '8_31737_12_20' , '8_31736_16_4'
 , '6_31733_11_16' , '16_31774_4_12' , '6_31728_15_4' , '14_31757_20_3'
 , '18_31782_5_6' , '12_31748_1_8' , '8_31737_12_22' , '18_31779_5_4'
 , '10_31743_16_7' , '8_31735_12_12' , '20_31788_5_17' , '20_31793_13_9'
 , '12_31750_1_10' , '6_31725_15_1' , '10_31743_16_8' , '8_31737_12_23'
 , '12_31754_1_14' , '8_31735_12_14' , '12_31749_1_9' , '20_31793_13_8'
 , '12_31750_1_11' , '8_31735_12_13' , '16_31765_3_1' , '20_31788_5_18'
 , '20_31797_13_3' , '20_31787_14_4' , '20_31787_14_3' , '6_31732_11_9'
 , '6_31733_15_10' , '16_31770_14_15' , '10_31739_6_13' , '10_31739_6_14'
 , '16_31769_18_11' , '12_31751_1_12' , '18_31783_5_8' , '20_31791_13_13'
 , '6_31733_15_11' , '18_31782_5_7' , '6_31728_15_5' , '16_31775_5_1'
 , '6_31733_11_17' , '20_31791_13_12' , '18_31783_5_9' , '10_31739_6_15'
 , '14_31760_16_19' , '16_31770_4_1' , '6_31729_10_4' , '16_31773_4_9'
 , '12_31749_16_11' , '6_31729_10_3' , '8_31734_16_2' , '12_31750_16_12'
 , '16_31772_4_4' , '6_31731_11_6' , '6_31726_8_8' , '6_31727_8_10'
 , '6_31730_18_15' , '6_31726_8_6' , '20_31793_6_1' , '6_31731_11_8'
 , '6_31731_15_7' , '16_31770_4_2' , '8_31736_12_18' , '8_31734_16_1'
 , '6_31730_10_10' , '8_31736_12_16' , '20_31795_13_4' , '6_31726_8_7'
 , '14_31758_16_17' , '6_31727_8_11' , '8_31734_12_1' , '16_31771_4_3'
 , '16_31765_20_11' , '6_31731_11_7' , '20_31789_5_20' , '16_31770_14_16'
 , '18_31783_14_11' , '16_31774_4_11' , '6_31730_10_9' , '6_31733_11_15'
 , '18_31783_5_10' , '6_31730_10_7' , '8_31737_6_18' , '18_31784_14_6'
 , '18_31780_5_5' , '20_31791_13_11' , '20_31786_14_5' , '18_31783_14_10'
 , '20_31789_5_19' , '14_31761_20_7' , '8_31734_11_18' , '20_31793_13_10'
 , '6_31728_15_6' , '18_31783_5_11' , '6_31730_10_6' , '6_31733_15_12'
 , '6_31732_15_9' , '6_31733_11_14' , '6_31733_11_13' , '6_31730_10_8'
 , '8_31734_12_2' , '20_31793_6_3' , '6_31726_8_4' , '8_31734_12_5'
 , '20_31789_14_1' , '16_31772_4_6' , '6_31725_8_2' , '6_31731_11_4'
 , '20_31798_13_1' , '20_31794_13_7' , '16_31762_16_21' , '6_31728_9_2'
 , '16_31768_3_5' , '10_31745_16_10' , '18_31776_14_12' , '6_31728_9_3'
 , '10_31745_1_6' , '20_31794_13_6' , '20_31794_6_4' , '10_31747_1_7'
 , '6_31729_9_4' , '10_31740_6_12' , '6_31732_11_12' , '12_31754_16_13'
 , '10_31745_1_4' , '12_31754_16_14' , '8_31735_12_6' , '12_31754_18_2'
 , '18_31776_5_2' , '20_31795_6_7' , '18_31785_5_14' , '10_31740_6_11'
 , '6_31732_11_11' , '18_31785_5_13' , '8_31735_12_7' , '10_31745_1_5'
 , '12_31754_16_15' , '20_31787_5_16' , '20_31790_13_14' , '8_31735_12_9'
 , '14_31761_16_20' , '16_31769_3_7' , '6_31730_11_1' , '16_31766_3_2']


image_index = sys.argv[1]

path = r'/u/shahhi/vccf_computations_data/Placenta_209_data/Image_' + str(image_index) + '.csv'
df_point = pd.read_csv(path)

df_Region_1 = df_point[['centroid0', 'centroid1', 'lineage']]

df_Region_1 .rename(columns={'centroid0': 'x', 'centroid1': 'y', 'lineage': 'Cell Type' }, inplace=True)
micro_per_pixel = 0.391
scale =  micro_per_pixel
df_Region_1['x'] =  scale * df_Region_1['x']
df_Region_1['y'] =  scale * df_Region_1['y']
df_Region_1_vessel = df_Region_1.loc[df_Region_1['Cell Type'] == 'Endothelial']
df_Region_1_immmune = df_Region_1.loc[df_Region_1['Cell Type'] != 'Endothelial']

x_list = []
y_list = []
xv_list = []
yv_list = []
new_x = []
new_y = []
new_dist = []

x_list = df_Region_1_immmune['x'].values.tolist()
y_list = df_Region_1_immmune['y'].values.tolist()
xv_list = df_Region_1_vessel['x'].values.tolist()
yv_list = df_Region_1_vessel['y'].values.tolist()

print(len(x_list))
print(len(y_list))
print(len(xv_list))
print(len(yv_list))

for i in range(len(x_list)):
    min_dist = 1000
    has_near = False
    for j in range(len(xv_list)):
        if abs(x_list[i] - xv_list[j]) < min_dist and abs(y_list[i] - yv_list[j]) < min_dist:
            dist = math.sqrt((x_list[i] - xv_list[j]) ** 2 + (y_list[i] - yv_list[j]) ** 2 )
            if dist < min_dist:
                has_near = True
                min_dist = dist
                temp_x = xv_list[j]
                temp_y = yv_list[j]
    new_x.append(temp_x)
    new_y.append(temp_y)
    if has_near == False:
        new_dist.append(-1)
    else:
        new_dist.append(min_dist)

x_min, x_max = min(x_list), max(x_list)
y_min, y_max = min(y_list), max(y_list)

margin_index = 0.05
x_margin = (x_max - x_min) * margin_index
y_margin = (y_max - y_min) * margin_index



df_Region_1_immmune['XV'] = new_x
df_Region_1_immmune['YV'] = new_y
df_Region_1_immmune['MinDistance'] = new_dist

new_line_df = df_Region_1_immmune.loc[df_Region_1_immmune['MinDistance'] > 0 ]

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

color_c = []
color_c = px.colors.qualitative.Alphabet


cell_dict = {
    'Mac2a': {
        'legend': "Mac2a",
        'full': "Mac2a",
        'short': "Mac2a",
        'group': "Immune Cells",
        'color': color_c[10],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'other': {
        'legend': "other",
        'full': "other",
        'short': "other",
        'group': "Other cells",
        'color': color_c[9],
        'marker': 'triangle-up',
        'size': 10,
        'histogram_location': [3, 1],
    },
  
    'NK1': {
        'legend': "NK1",
        'full': "NK1",
        'short': "NK1",
        'group': "Immune Cells",
        'color': color_c[8],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'Fibroblasts': {
        'legend': "Fibroblasts",
        'full': "Fibroblasts",
        'short': "Fibroblasts",
        'group': "Structural",
        'color': color_c[7],
        'marker': 'cross',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'NKT': {
        'legend': "NKT",
        'full': "NKT",
        'short': "NKT",
        'group': "Immune Cells",
        'color': color_c[6],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'Myofibroblasts': {
        'legend': "Myofibroblasts",
        'full': "Myofibroblasts",
        'short': "Myofibroblasts",
        'group': "Structural",
        'color': color_c[5],
        'marker': 'cross',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'Mac1a': {
        'legend': "Mac1a",
        'full': "Mac1a",
        'short': "Mac1a",
        'group': "Immune Cells",
        'color': color_c[4],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'EVT1a': {
        'legend': "EVT1a",
        'full': "EVT1a",
        'short': "EVT1a",
        'group': "Fetal",
        'color': color_c[3],
        'marker': 'diamond-open',
        'size': 10,
        'histogram_location': [3, 1],
    },

  
    'Mac1b': {
        'legend': "Mac1b",
        'full': "Mac1b",
        'short': "Mac1b",
        'group': "Immune Cells",
        'color': color_c[2],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'CD8T': {
        'legend': "CD8T",
        'full': "CD8T",
        'short': "CD8T",
        'group': "Immune Cells",
        'color': color_c[1],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'EVT1b': {
        'legend': "EVT1b",
        'full': "EVT1b",
        'short': "EVT1b",
        'group': "Fetal",
        'color': color_c[11],
        'marker': 'diamond-open',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'Mac2c': {
        'legend': "Mac2c",
        'full': "Mac2c",
        'short': "Mac2c",
        'group': "Immune Cells",
        'color': color_c[12],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'NK2': {
        'legend': "NK2",
        'full': "NK2",
        'short': "NK2",
        'group': "Immune Cells",
        'color': color_c[13],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'NK3': {
        'legend': "NK3",
        'full': "NK3",
        'short': "NK3",
        'group': "Immune Cells",
        'color': color_c[14],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'NK4': {
        'legend': "NK4",
        'full': "NK4",
        'short': "NK4",
        'group': "Immune Cells",
        'color': color_c[15],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },

      # Mac2a', 'other', 'NK1', 'Fibroblasts', 'NKT', 'Endothelial',
      #  'Myofibroblasts', 'Mac1a', 'EVT1a', 'Mac1b', 'CD8T', 'EVT1b',
      #  'Mac2c', 'NK2', 'muscle', 'NK3', 'EVT2', 'Mac2b', 'Fibroblasts',
      #  'Glandular', 'CD4T', 'EVT1c', 'Placental_Mac', 'NK4', 'Mast',
      #  'Treg'

      # ['Mac2a', 'other', 'NK1', 'Fibroblasts', 'NKT', 'Endothelial',
      #  'Myofibroblasts', 'Mac1a', 'EVT1a', 'Mac1b', 'CD8T', 'EVT1b',
      #  'Mac2c', 'NK2', 'muscle', 'NK3', 'EVT2', 'Mac2b', 'DC',
      #  'Glandular', 'CD4T', 'EVT1c', 'Placental_Mac', 'NK4', 'Mast',
      #  'Treg']
    'muscle': {
        'legend': "muscle",
        'full': "muscle",
        'short': "muscle",
        'group': "Immune Cells",
        'color': color_c[16],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'EVT2': {
        'legend': "EVT2",
        'full': "EVT2",
        'short': "EVT2",
        'group': "Fetal",
        'color': color_c[17],
        'marker': 'diamond-open',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'Mac2b': {
        'legend': "Mac2b",
        'full': "Mac2b",
        'short': "Mac2b",
        'group': "Immune Cells",
        'color': color_c[18],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'DC': {
        'legend': "DC",
        'full': "DC",
        'short': "DC",
        'group': "Immune Cells",
        'color': color_c[19],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },
    'Glandular': {
        'legend': "Glandular",
        'full': "Glandular",
        'short': "Glandular",
        'group': "Structural",
        'color': color_c[20],
        'marker': 'cross',
        'size': 10,
        'histogram_location': [3, 1],
    },

    'CD4T': {
        'legend': "CD4T",
        'full': "CD4T",
        'short': "CD4T",
        'group': "Immune Cells",
        'color': color_c[21],
        'marker': 'circle',
        'size': 10,
        'histogram_location': [3, 1],
    },

    'EVT1c': {
        'legend': "EVT1c",
        'full': "EVT1c",
        'short': "EVT1c",
        'group': "Fetal",
        'color': color_c[22],
        'marker': 'diamond-open',
        'size': 10,
        'histogram_location': [3, 1],
    },

    'Placental_Mac': {
        'legend': "Placental_Mac",
        'full': "Placental_Mac",
        'short': "Placental_Mac",
        'group': "Fetal",
        'color': color_c[23],
        'marker': 'diamond-open',
        'size': 10,
        'histogram_location': [3, 1],
    },

    'Mast': {
        'legend': "Mast",
        'full': "Mast",
        'short': "Mast",
        'group': "Immune Cells",
        'color': color_c[24],
        'marker': 'circle',
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
  
  'Treg': {
        'legend': "Treg",
        'full': "Treg",
        'short': "Treg",
        'group': 'Immune Cells',
        'color': color_c[25],
        'marker': 'circle',
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

# region_index = 1

def generate_nuclei_scatter(df, ct, visible=True, show_legend=True, legend_group=""):
    return go.Scatter(x=df[df['Cell Type'] == ct]["x"],
                        y=df[df['Cell Type'] == ct]["y"],
                        
                        mode="markers",
                        name=cell_dict[cell_type]['legend'],
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
                        mode="markers",
                        name=name,
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
                        
                        mode="lines",
                        name=name,
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
nuclei_type_list = df_Region_1[df_Region_1['Cell Type'] != 'Endothelial']['Cell Type'].unique()

for cell_type in set(immune_cell_types):
    
    traces_n.append(generate_nuclei_scatter(df_Region_1_immmune, cell_type,
                                            legend_group=cell_dict[cell_type]['group']))
trace_v = generate_other_scatter(df_Region_1_immmune, key='V', name=cell_dict['Endothelial']['legend'], symbol_name='Endothelial', visible=True,
                                 legend_group="Endothelial")

traces_vessel_line = generate_line(df_Region_1_immmune_one, name=f"Distance-{cell_dict['Endothelial']['legend']}",
                                   color=cell_dict['Endothelial']['color'], visible=True, legend_group="Link")

traces_n.extend([trace_v, traces_vessel_line])
main_fig_count = len(traces_n)






# image_hyperlink = f'https://raw.githubusercontent.com/hubmapconsortium/vccf-visualization-release/main/vheimages/S002_VHE_region_0{image_index:02d}.jpg'
main_subtitle = f'<br><sup>Image {image_index} </sup>'
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




figure.update_layout(
    scene=dict(
        aspectmode='data',
    ),
)



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
        zaxis=dict(nticks=5, backgroundcolor=background_color, ),
    ),
    plot_bgcolor=background_color,

)

figure.write_html(os.path.join('/u/shahhi/vccf_computations_data/html_vccf', f"Image_{image_index}.html"))