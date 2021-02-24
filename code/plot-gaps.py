# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 09:03:14 2021

@author: Lucas
"""

import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import json

wage_gaps = pd.read_csv('tmp/wage_gaps.csv')

with open('input/sp_simple3.geojson', encoding='utf-8') as response:    
    mapa_mun_sp = json.load(response)

nomes = pd.read_csv('input/sp_hard2.csv', encoding = 'utf-8')

wage_gaps = wage_gaps.merge(nomes, left_on='Mun', right_on='code' )
wage_gaps.loc[wage_gaps.p_valor_negros > 0.10, 'gap_negros'] = 0
wage_gaps.loc[wage_gaps.p_valor_mulheres > 0.10, 'gap_mulheres'] = 0

wage_gaps = wage_gaps.round({'gap_negros': 4, 'gap_mulheres': 4})

gaps_racial = (wage_gaps[['name', 'gap_negros']])
gaps_racial1 = gaps_racial.sort_values('name')
gaps_racial2 = gaps_racial.sort_values('gap_negros')

gaps_genero = (wage_gaps[['name', 'gap_mulheres']])
gaps_genero1 = gaps_genero.sort_values('name')
gaps_genero2 = gaps_genero.sort_values('gap_mulheres')

# -----------------------------------------------------------------------------

# Create figure
fig = make_subplots(
    rows=2, cols=2,
    shared_xaxes=False,
    column_widths=[0.25, 0.75],
    vertical_spacing=0.05,
    specs=[[{"type": "table"}, {"type": "choropleth", "rowspan": 2}],
           [{"type": "table"}, None]]
)

fig.add_trace(go.Choropleth(geojson = mapa_mun_sp,
                            featureidkey = "properties.CD_GEOCMU",
                            locations = wage_gaps['Mun'],
                            z = wage_gaps['gap_negros'],
                            text = wage_gaps['name'],
                            colorscale = "Viridis",
                            colorbar_title = "Diferença salarial <br> (negros - brancos)",
                            marker_line_color = 'white',
                            marker_line_width = 0.8),
              row=1, col=2)


# Add tabela aqui

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
                  row=2, col=1)


fig.update_layout(
    title_text = 'Gap Salarial entre Negros e Brancos',
    annotations = [
        go.layout.Annotation(x = 0.5,
                             y = -0.1,
                             text = ("Diferença no log(salário/h) entre negros e brancos controlando por idade,"
                             "ocupação, setor e sexo. <br> Cálculos a partir dos microdados da RAIS 2019. <br>"
                             'Valores < 0 indicam salários menores para negros quando comparados a brancos.'
                             "Coeficientes não significativos a 10% foram considerados zero."),                   
                             showarrow = False, xref='paper', yref='paper', 
                             xanchor='center',
                             yanchor='auto',
                             xshift=0,
                             yshift=0
        )]    
)

fig.update_geos(fitbounds='locations',
                visible=False)

fig.write_html("tmp/gap_racial.html",
               include_plotlyjs="cdn")


#------------------------------------------------------------------------------


# Create figure
fig = make_subplots(
    rows=2, cols=2,
    shared_xaxes=False,
    column_widths=[0.25, 0.75],
    vertical_spacing=0.05,
    specs=[[{"type": "table"}, {"type": "choropleth", "rowspan": 2}],
           [{"type": "table"}, None]]
)


fig.add_trace(go.Choropleth(geojson = mapa_mun_sp,
                            featureidkey = "properties.CD_GEOCMU",
                            locations = wage_gaps['Mun'],
                            z = wage_gaps['gap_mulheres'],
                            text = wage_gaps['name'],
                            colorscale = "Viridis",
                            colorbar_title = "Diferença salarial <br> (mulheres - homens)",
                            marker_line_color = 'white',
                            marker_line_width = 0.8),
              row=1, col=2)

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
                  row=2, col=1)


fig.update_layout(
    title_text = 'Gap Salarial entre Mulheres e Homens',
    annotations = [
        go.layout.Annotation(x = 0.5,
                             y = -0.1,
                             text = ("Diferença no log(salário/h) entre mulheres e homens controlando por idade,"
                             "ocupação, setor e raça. <br> Cálculos a partir dos microdados da RAIS 2019. <br>"
                             'Valores < 0 indicam salários menores para mulheres quando comparadas aos homens.'
                             "Coeficientes não significativos a 10% foram considerados zero."),                   
                             showarrow = False, xref='paper', yref='paper', 
                             xanchor='center',
                             yanchor='auto',
                             xshift=0,
                             yshift=0
        )]    
)

fig.update_geos(fitbounds='locations',
                visible=False)

fig.write_html("tmp/gap_genero.html",
               include_plotlyjs="cdn")
