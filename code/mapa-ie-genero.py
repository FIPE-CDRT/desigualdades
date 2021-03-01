# -*- coding: utf-8 -*-
# Preciso de do input fundamental aqui, que é o df com os ie_genero

import plotly.graph_objects as go
import pandas as pd
import json

# GeoJSON do mapa dos estados

with open('input/GEOBR.geojson', encoding='utf-8') as response:
    mapa_estados = json.load(response)


# Create figure
fig = go.Figure()

for sector in ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze']:

    fig.add_trace(go.Choropleth(geojson=mapa_estados,
                                featureidkey="properties.name",
                                locations=ie_genero['nome'],
                                z=ie_genero[sector].astype(float),
                                colorscale="Viridis",
                                colorbar_title="IEG",
                                marker_line_color='white',
                                marker_line_width=0.8,
                                zmin=-1,
                                zmax=1))

# Add dropdowns
fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        x=0.3,
        xanchor='left',
        y=1.2,
        yanchor='top',
        buttons=list(
            [dict(label='Agricultura, pecuária, produção florestal, pesca e aquicultura',
                  method='update',
                  args=[{'visible': [True, False, False, False, False, False, False, False, False, False, False]},
                        {'showlegend': True}]),
             dict(label='Indústria geral',
                  method='update',
                  args=[{'visible': [False, True, False, False, False, False, False, False, False, False, False]},
                        {'showlegend': True}]),
             dict(label='Construção',
                  method='update',
                  args=[{'visible': [False, False, True, False, False, False, False, False, False, False, False]},
                        {'showlegend': True}]),
             dict(label='Comércio, reparação de veí­culos automotores e motocicletas',
                  method='update',
                  args=[{'visible': [False, False, False, True, False, False, False, False, False, False, False]},
                        {'showlegend': True}]),
             dict(label='Transporte, armazenagem e correios ',
                  method='update',
                  args=[{'visible': [False, False, False, False, True, False, False, False, False, False, False]},
                        {'showlegend': True}]),
             dict(label='Alojamento e alimentação ',
                  method='update',
                  args=[{'visible': [False, False, False, False, False, True, False, False, False, False, False]},
                        {'showlegend': True}]),
             dict(label='Informação, comunicação e atividades financeiras, imobiliárias, profissionais e administrativas',
                  method='update',
                  args=[{'visible': [False, False, False, False, False, False, True, False, False, False, False]},
                        {'showlegend': True}]),
             dict(label='Administração pública, defesa e seguridade social',
                  method='update',
                  args=[{'visible': [False, False, False, False, False, False, False, True, False, False, False]},
                        {'showlegend': True}]),
             dict(label='Educação, saúde humana e serviços sociais',
                  method='update',
                  args=[{'visible': [False, False, False, False, False, False, False, False, True, False, False]},
                        {'showlegend': True}]),
             dict(label='Outros Serviços',
                  method='update',
                  args=[{'visible': [False, False, False, False, False, False, False, False, False, True, False]},
                        {'showlegend': True}]),
             dict(label='Serviços domésticos',
                  method='update',
                  args=[{'visible': [False, False, False, False, False, False, False, False, False, False, True]},
                        {'showlegend': True}]),
             ])
        )
    ])

fig.update_layout(
    title_text='<b>Índice de Equilíbrio de Gênero</b> <br>'
               'IEG = 1: homens excluídos. <br>'
               'IEG = -1: mulheres excluídas.',
    annotations=[
        go.layout.Annotation(x=0.5,
                             y=-0.1,
                             text=('Nota: IEG calculado baseado em '
                                   '<a href="https://www.insper.edu.br/wp-content/uploads/2020/12/IER_Firpo_Franca_Cavalcanti_.pdf">Firpo, França e Rodrigues (2020)</a> '
                                   'com dados do 3T da PNADC de 2020.'),
                             showarrow=False,
                             xref='paper',
                             yref='paper',
                             xanchor='center',
                             yanchor='auto',
                             xshift=0,
                             yshift=0)]
)

fig.update_geos(fitbounds='locations',
                visible=False)

fig.write_html("output/ie_genero.html",
               include_plotlyjs="cdn")
