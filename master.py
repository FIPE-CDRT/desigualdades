# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 10:22:54 2021

@author: Lucas
"""

import os

# Mude aqui para o diretório onde se encontra este script
os.chdir('C:/Users/Lucas/Desktop/desigualdades/')

# Mude aqui para o diretório onde encontra o R (como abaixo)
os.environ['R_HOME'] = 'C:/Program Files/R/R-4.0.1/'

import rpy2.robjects as robjects  # tem que vir depois da definição do path do R
r = robjects.r

os.mkdir('tmp/')
os.mkdir('output/')

# =============================================================================


# Índice de Equilíbrio Racial e de Gênero
exec(open("./code/indices-equilibrio.py").read())
exec(open("./code/mapa-ie-genero.py", encoding="utf-8").read())
exec(open("./code/mapa-ie-racial.py", encoding="utf-8").read())


# Série do Índice de Gini por estado [demora +/- 1h e não roda na SDE]
r['source']('./code/gini.R')
exec(open("./code/plot-gini.py", encoding="utf-8").read())


# Gaps salariais de raça e gênero (OBS.: só rode se RAM > 32GB) [rodei no servidor,
# por isso vou deixar comentado]
# r['source']('code/regs-municipais.R')
# exec(open("./code/plot-gaps.py", encoding = "utf-8").read())
