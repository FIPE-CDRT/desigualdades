# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 08:47:47 2021

@author: Lucas
"""

import os
import plotly.graph_objects as go
import pandas as pd
import json

os.chdir('C:/Users/Lucas/Desktop/pnadc-reports')

serie_gini = pd.read_csv('tmp/serie_gini.csv')


color1 = 'rgb(64, 64, 64)'
width1 = 4
size1 = 8

color2 = 'rgb(192, 192, 192)'
width2 = 2
size2 = 4

fig = go.Figure()

# Add traces

fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['São.Paulo'],
                    mode = 'lines+markers',
                    name = 'SP', 
                    line = dict(color=color1, width = width1),
                    marker = dict(color = color1, size = size1))
              )

fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Acre'],
                    mode='lines+markers',
                    name='AC',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Alagoas'],
                    mode='lines+markers',
                    name='AL',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Amapá'],
                    mode='lines+markers',
                    name='AM',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Amazonas'],
                    mode='lines+markers',
                    name='AM',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Bahia'],
                    mode='lines+markers',
                    name='BA',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Ceará'],
                    mode='lines+markers',
                    name='CE',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Distrito.Federal'],
                    mode='lines+markers',
                    name='DF',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Espírito.Santo'],
                    mode='lines+markers',
                    name='ES',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Goiás'],
                    mode='lines+markers',
                    name='GO',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Maranhão'],
                    mode='lines+markers',
                    name='MA',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Mato.Grosso'],
                    mode='lines+markers',
                    name='MT',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Mato.Grosso.do.Sul'],
                    mode='lines+markers',
                    name='MS',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Minas.Gerais'],
                    mode='lines+markers',
                    name='MG',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Pará'],
                    mode='lines+markers',
                    name='PA',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Paraíba'],
                    mode='lines+markers',
                    name='PB',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Paraná'],
                    mode='lines+markers',
                    name='PR',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Pernambuco'],
                    mode='lines+markers',
                    name='PE',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Piauí'],
                    mode='lines+markers',
                    name='PI',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Rio.de.Janeiro'],
                    mode='lines+markers',
                    name='RJ',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Rio.Grande.do.Norte'],
                    mode='lines+markers',
                    name='RN',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Rio.Grande.do.Sul'],
                    mode='lines+markers',
                    name='RS',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Rondônia'],
                    mode='lines+markers',
                    name='RO',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Roraima'],
                    mode='lines+markers',
                    name='RR',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Santa.Catarina'],
                    mode='lines+markers',
                    name='SC',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Sergipe'],
                    mode='lines+markers',
                    name='SE',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )
fig.add_trace(go.Scatter(x = serie_gini['Ano_Tri'], y = serie_gini['Tocantins'],
                    mode='lines+markers',
                    name='TO',
                    visible='legendonly',
                    line = dict(color = color2, width = width2),
                    marker = dict(color = color2, size = size2))
              )


fig.update_layout(
    title_text = 'Evolução da Desigualdade de Renda',
    xaxis_title = " ",
    yaxis_title = "Índice de Gini",
    annotations=[
        go.layout.Annotation(x = 0.5,
                             y = -0.15,
                             text = ('Desigualdade de renda do trabalho medida com dados das '
                                     'PNADs Contínuas Trimestrais.'
                                     'Clique nas siglas da legenda para plotar mais estados. <br>'
                                     'Gini = 1: concentração absoluta na distribuição de renda.<br>'
                                     'Gini = 0: igualdade absoluta na distribuição de renda.'),                   
                             showarrow = False, xref='paper', yref='paper', 
                             xanchor='center',
                             yanchor='auto',
                             xshift=0,
                             yshift=0
        )]
)



fig.write_html("tmp/gini.html",
               include_plotlyjs="cdn")

