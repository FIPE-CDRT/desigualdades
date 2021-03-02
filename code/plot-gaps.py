# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 09:03:14 2021

@author: Lucas
"""

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import json

wage_gaps = pd.read_csv('tmp/wage_gaps.csv')

with open('input/sp_simple3.geojson', encoding='utf-8') as response:    
    mapa_mun_sp = json.load(response)

nomes = pd.read_csv('input/sp_hard2.csv', encoding='utf-8')

wage_gaps = wage_gaps.merge(nomes, left_on='Mun', right_on='code')
wage_gaps.loc[wage_gaps.p_valor_negros > 0.10, 'gap_negros'] = 0
wage_gaps.loc[wage_gaps.p_valor_mulheres > 0.10, 'gap_mulheres'] = 0

wage_gaps = wage_gaps.round({'gap_negros': 4, 'gap_mulheres': 4})

std_racial = np.std(wage_gaps['gap_negros'])
std_genero = np.std(wage_gaps['gap_mulheres'])

conditions = [
    (wage_gaps["gap_negros"].gt(0)),
    (wage_gaps["gap_negros"].le(0) & wage_gaps["gap_negros"].gt(0-0.25*std_racial)),
    (wage_gaps["gap_negros"].le(0-0.25*std_racial) & wage_gaps["gap_negros"].gt(0-0.5*std_racial)),
    (wage_gaps["gap_negros"].le(0-0.5*std_racial) & wage_gaps["gap_negros"].gt(0-1*std_racial)),
    (wage_gaps["gap_negros"].le(0-1*std_racial) & wage_gaps["gap_negros"].gt(0-2*std_racial)),
    (wage_gaps["gap_negros"].le(0-2*std_racial)),
]
choices = ["-", "Equitativos", "Balanceados", "Em Transição", "Desiguais",
           "Vulneráveis"]

wage_gaps["Categorias - Racial"] = np.select(conditions, choices)
wage_gaps.loc[wage_gaps['name']=='Lourdes', 'Categorias - Racial'] = '-'


conditions = [
    (wage_gaps["gap_mulheres"].gt(0)),
    (wage_gaps["gap_mulheres"].le(0) & wage_gaps["gap_mulheres"].gt(0-0.25*std_genero)),
    (wage_gaps["gap_mulheres"].le(0-0.25*std_genero) & wage_gaps["gap_mulheres"].gt(0-0.5*std_genero)),
    (wage_gaps["gap_mulheres"].le(0-0.5*std_genero) & wage_gaps["gap_mulheres"].gt(0-1*std_genero)),
    (wage_gaps["gap_mulheres"].le(0-1*std_genero) & wage_gaps["gap_mulheres"].gt(0-2*std_genero)),
    (wage_gaps["gap_mulheres"].le(0-2*std_genero)),
]
choices = ["-", "Equitativos", "Balanceados", "Em Transição", "Desiguais",
           "Vulneráveis"]

wage_gaps["Categorias - Gênero"] = np.select(conditions, choices)


gaps_racial = (wage_gaps[['name', 'gap_negros']])
gaps_racial1 = gaps_racial.sort_values('name')
gaps_racial2 = gaps_racial.sort_values('gap_negros')

gaps_genero = (wage_gaps[['name', 'gap_mulheres']])
gaps_genero1 = gaps_genero.sort_values('name')
gaps_genero2 = gaps_genero.sort_values('gap_mulheres')


# -----------------------------------------------------------------------------

# Tabelas - 
fig = make_subplots(
    rows=1, cols=2,
    shared_xaxes=False,
    column_widths=[0.5, 0.5],
    vertical_spacing=0.05,
    specs=[[{"type": "table"}, {"type": "table"}]]
)


fig.add_trace(go.Table(header=dict(values=["Município", "Gap Salarial"],
                       font=dict(size=10),
                       align="left"),
                       cells=dict(values=[gaps_racial1[k].tolist() for k in gaps_racial1.columns[0:]],
                                  align="left")),
              row=1, col=1)


fig.add_trace(go.Table(header=dict(values=["Município", "Gap Salarial"],
                       font=dict(size=10),
                       align="left"),
                       cells=dict(values=[gaps_racial2[k].tolist() for k in gaps_racial2.columns[0:]],
                                  align="left")),
              row=1, col=2)


fig.write_html("output/gap_racial_tabs.html",
               include_plotlyjs="cdn")


fig = px.choropleth(wage_gaps,
                    geojson=mapa_mun_sp,
                    featureidkey="properties.CD_GEOCMU",
                    locations='Mun',
                    hover_name='name',
                    color='Categorias - Racial',
                    category_orders={"Categorias - Racial": ["Equitativos",
                                                             "Balanceados",
                                                             "Em Transição",
                                                             "Desiguais",
                                                             "Vulneráveis"]
                                     },
                    color_discrete_map={'-': 'grey',
                                        'Equitativos': 'rgb(110, 169, 179)',
                                        'Balanceados': 'rgb(207, 226, 230)',
                                        'Em Transição': 'rgb(255, 218, 103)',
                                        'Desiguais': 'rgb(255, 136, 51)',
                                        'Vulneráveis': 'rgb(127, 30, 8)'})

fig.update_layout(
    title_text='<b>Gap Salarial entre Negros e Brancos</b>',
    title_x=0.5,
    annotations=[
        go.layout.Annotation(x=0.5,
                             y=-0.1,
                             text=("Diferença no log(salário/h) entre negros e brancos controlando por idade,"
                             "ocupação, setor e sexo. <br> Cálculos a partir dos microdados da RAIS 2019. <br>"
                             "Coeficientes não significativos a 10% foram considerados zero."),                   
                             showarrow=False,
                             xref='paper',
                             yref='paper',
                             xanchor='center',
                             yanchor='auto',
                             xshift=0,
                             yshift=0)
        ]
    )

fig.update_geos(fitbounds='locations',
                visible=False)

fig.write_html("output/gap_racial_map.html",
               include_plotlyjs="cdn")



#------------------------------------------------------------------------------


# Create figure
fig = make_subplots(
    rows=1, cols=2,
    shared_xaxes=False,
    column_widths=[0.5, 0.5],
    vertical_spacing=0.05,
    specs=[[{"type": "table"}, {"type": "table"}]]
)


# Add tabela aqui

fig.add_trace(go.Table(header=dict(values=["Município", "Gap Salarial"],
                       font=dict(size=10),
                       align="left"),
                       cells=dict(values=[gaps_genero1[k].tolist() for k in gaps_genero1.columns[0:]],
                                  align="left")),
              row=1, col=1)


fig.add_trace(go.Table(header=dict(values=["Município", "Gap Salarial"],
                       font=dict(size=10),
                       align="left"),
                       cells=dict(values=[gaps_genero2[k].tolist() for k in gaps_genero2.columns[0:]],
                                  align="left")),
              row=1, col=2)

fig.write_html("output/gap_genero_tabs.html",
               include_plotlyjs="cdn")


fig = px.choropleth(wage_gaps,
                    geojson=mapa_mun_sp,
                    featureidkey="properties.CD_GEOCMU",
                    locations='Mun',
                    hover_name='name',
                    color='Categorias - Gênero',
                    category_orders={"Categorias - Gênero": ["Equitativos",
                                                             "Balanceados",
                                                             "Em Transição",
                                                             "Desiguais",
                                                             "Vulneráveis"]
                                     },
                    color_discrete_map={'-': 'grey',
                                        'Equitativos': 'rgb(110, 169, 179)',
                                        'Balanceados': 'rgb(207, 226, 230)',
                                        'Em Transição': 'rgb(255, 218, 103)',
                                        'Desiguais': 'rgb(255, 136, 51)',
                                        'Vulneráveis': 'rgb(127, 30, 8)'})


fig.update_layout(
    title_text='<b>Gap Salarial entre Mulheres e Homens</b>',
    title_x=0.5,
    annotations=[
        go.layout.Annotation(x=0.5,
                             y=-0.1,
                             text=("Diferença no log(salário/h) entre mulheres e homens controlando por idade,"
                             "ocupação, setor e raça. <br> Cálculos a partir dos microdados da RAIS 2019. <br>"
                             "Coeficientes não significativos a 10% foram considerados zero."),                   
                             showarrow=False,
                             xref='paper',
                             yref='paper',
                             xanchor='center',
                             yanchor='auto',
                             xshift=0,
                             yshift=0)
        ]
    )


fig.update_geos(fitbounds='locations',
                visible=False)

fig.write_html("output/gap_genero_map.html",
               include_plotlyjs="cdn")
