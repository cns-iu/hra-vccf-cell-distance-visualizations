from turtle import bgcolor
import pandas as pd
import numpy as np
import math
import plotly.express as px
import os
from plotly.graph_objs import *

region_index = 12

df_Region_1 = pd.read_csv('/Users/himanishah/Desktop/VCCF_Computations/Intestine_64_data/Region_12.csv')
df_Region_1 = df_Region_1[['x', 'y', 'Cell Type']]
micro_per_pixel = 0.866
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
    # line_z = [None] * (len(df) * 2)

   

    line_x[::2] = df[f"X{key}"]
    line_y[::2] = df[f"Y{key}"]
    # line_z[::2] = df[f"n{key}z"]
    line_x[1::2] = df["x"]
    line_y[1::2] = df["y"]
    # line_z[1::2] = df["nz"]

    l_data = dict()
    l_data["x"] = line_x
    l_data["y"] = line_y
    # l_data["z"] = line_z
    # v_color = ['red'] * len(vessel_x_list)
    # v_data["color"] = v_color
    l_df = pd.DataFrame(l_data)
    l_gap = (l_df.iloc[1::2]
             .assign(x=np.nan, y=np.nan)
             .rename(lambda x: x + .5))
    l_df_one = pd.concat([l_df, l_gap], sort=False).sort_index().reset_index(drop=True)
    l_df_one.loc[l_df_one.isnull().any(axis=1), :] = np.nan
    return l_df_one


df_Region_1_immmune_one = generate_one_line_df(new_line_df, key='V')

color_c = []
color_c = px.colors.qualitative.Plotly

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
# 'Smooth muscle': {
#         'legend': "Smooth muscle",
#         'full': "Smooth muscle",
#         'short': "Smooth muscle",
#         'group': "stromal",
#         'color': '#AA0DFE',
#         'marker': 'diamond-open',
#         'size': 10,
#         'histogram_location': [3, 1],
#     },

# 'Lymphatic': {
#         'legend': "Lymphatic",
#         'full': "Lymphatic",
#         'short': "Lymphatic",
#         'group': "stromal",
#         'color': '#AA0DFE',
#         'marker': 'diamond-open',
#         'size': 10,
#         'histogram_location': [3, 1],
#     },

# 'Stroma': {
#         'legend': "Stroma",
#         'full': "Stroma",
#         'short': "Stroma",
#         'group': "stromal",
#         'color': '#AA0DFE',
#         'marker': 'diamond-open',
#         'size': 10,
#         'histogram_location': [3, 1],
#     },

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

cell_dict = {
    'NK': {
        'legend': "NK",
        'full': "NK",
        'short': "NK",
        'group': "Immune Cells",
        'color': '#AA0DFE',
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
    # '#862A16', '#A777F1', '#620042', '#1616A7', '#DA60CA', '#6C4516', '#0D2A63', '#AF0038'
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
        'color': "coral",
        'marker': 'diamond',
        'size': 5,
        'histogram_location': [0, 0],
    }
 
}

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff

def generate_nuclei_scatter(df, ct, visible=True, show_legend=True, legend_group=""):
    return go.Scatter(x=df[df['Cell Type'] == ct]["x"],
                        y=df[df['Cell Type'] == ct]["y"],
                        # z=df[df['type'] == ct]["nz"],
                        mode="markers",
                        name=cell_dict[cell_type]['legend'],
                        showlegend=show_legend,
                        # legendgroup=legend_group,
                        # legendgrouptitle_text=legend_group,
                        marker=dict(
                            # size=df[df['Cell Type'] == ct]["size"],
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
                            # size=df["size"],
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
                        # z=df["z"],
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
nuclei_type_list = ['NK', 'M1 Macrophage', 'CD8+ T', 'DC', 'M2 Macrophage', 'B', 'Neutrophil', 'Plasma', 'CD4+ T cell', 'CD7+ Immune']

for cell_type in set(nuclei_type_list):
    if cell_type in immune_cell_types:
        traces_n.append(generate_nuclei_scatter(df_Region_1_immmune, cell_type,
                                                legend_group=cell_dict[cell_type]['group']))
trace_v = generate_other_scatter(df_Region_1_immmune, key='V', name=cell_dict['Endothelial']['legend'], symbol_name='Endothelial', visible=True,
                                 legend_group="Endothelial")

traces_vessel_line = generate_line(df_Region_1_immmune_one, name=f"Distance-{cell_dict['Endothelial']['legend']}",
                                   color=cell_dict['Endothelial']['color'], visible=True, legend_group="Link")

traces_n.extend([trace_v, traces_vessel_line])
main_fig_count = len(traces_n)






# image_hyperlink = f'https://raw.githubusercontent.com/hubmapconsortium/vccf-visualization-release/main/vheimages/S002_VHE_region_0{region_index:02d}.jpg'
main_subtitle = f'<br><sup>Region {region_index} </sup>'
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

        if cell_type in immune_cell_types:
            data = df_Region_1_immmune[df_Region_1_immmune['Cell Type'] == cell_type]["MinDistance"]
            print(cell_type, data.size)
            if data.size > 5:
                hist_data.append(data)
                hist_names.append(cell_type)
            fig2 = ff.create_distplot(hist_data, hist_names, histnorm='probability')  # , curve_type='normal')


    for i in range(len(hist_data)):
            
            # fig.add_trace(go.Histogram(x=fig2['data'][i]['x'],xbins=bin_dict,opacity=0.5,
            #                            marker_color=color_dict[hist_names[i]], showlegend=False,
            #                            ), row=2, col=col)
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

# figure.show()


           
            
    
# Invisble scale for keep space instant
invisible_scale = go.Scatter3d(
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
# # Create and add slider
# steps = []
# z_count = 2
# for i in range(z_count + 1):
#     title = f"{str(i)}" if i != 0 else "All"
#     step = dict(
#         label=title,
#         method="update",
#         args=[{"visible": [False] * len(figure.data),
#                "showlegend": [False] * len(figure.data)},
#               {"title": ""}],  # layout attribute
#     )
#     for f in range(main_fig_count):
#         step["args"][0]["visible"][i * main_fig_count + f] = True  # Toggle i'th trace to "visible"
#         step["args"][0]["showlegend"][i * main_fig_count + f] = True
#     rest = len(figure.data) - (z_count + 1) * main_fig_count
#     for h in range(1, rest + 1):
#         step["args"][0]["visible"][-h] = True
#     steps.append(step)
# layer_select_buttons = steps

# sliders = [dict(
#     active=0,
#     currentvalue={"prefix": "Slide: "},
#     pad={"t": 0, "b": 0},
#     steps=steps,
#     yanchor='top', y=1,
#     xanchor='right', x=1,
#     lenmode='fraction', len=0.25
# )]

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

# fig.add_annotation(dict(text="Slide:", showarrow=False,
#                         x=1, y=0.88, xref="paper", yref="paper", xanchor='right', yanchor='top', ))
figure.update_yaxes(rangemode='tozero', tickfont=dict(size=12), row=2)
figure.update_yaxes(rangemode='tozero', tickfont=dict(size=10), row=3)
figure.update_xaxes(rangemode='tozero', tickfont=dict(size=12), row=2)
figure.update_xaxes(rangemode='tozero', tickfont=dict(size=12), row=3)
figure.update_xaxes(ticklabelposition="outside", side="bottom",
                 title=dict(text="Distance (μm)", standoff=5, font_size=14), row=3, )
# fig.update_xaxes(range=[0, np.percentile(nuclei_vessel_distance_list, 99)], row=3, col=1)
figure.update_xaxes(range=[0, 210], row=3, col=1)
# fig.update_xaxes(range=[0, np.percentile(nuclei_skin_distance_list, 98)], row=3, col=2)
# fig.update_yaxes(ticklabelposition="inside", side="right", row=3, )
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

        # dict(
        #     buttons=layer_select_buttons,
        #     direction="down",
        #     pad={"r": 0, "t": 5},
        #     showactive=True,
        #     x=1,
        #     xanchor="right",
        #     y=0.85,
        #     yanchor="top"
        # ),
    ],
    font=dict(
        family="Arial, Bahnschrift",
        size=12,
        # color="RebeccaPurple"
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
        # yanchor="top",
        # y=0.95,
        # xanchor="left",
        # x=0
    ),
    barmode='overlay',
    # sliders=sliders,
    scene=dict(
        aspectmode='data',
        xaxis=dict(nticks=10, backgroundcolor=background_color, ),
        yaxis=dict(nticks=10, backgroundcolor=background_color, ),
        zaxis=dict(nticks=5, backgroundcolor=background_color, ),
    ),
    plot_bgcolor=background_color,
    # xaxis=dict(tickangle=30),
    # yaxis=dict(tickangle=30)
)


figure.write_html(os.path.join('/Users/himanishah/Desktop/VCCF_Computations/Intestine_64_data/', f"region_{region_index}.html"))