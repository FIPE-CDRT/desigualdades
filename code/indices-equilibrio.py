# -*- coding: utf-8 -*-

# Preambulo (mude o diretório se necessário) ==================================

import pandas as pd
import numpy as np
import pnadc

# =============================================================================


# Download e build da PNAD ====================================================

pnad_raw = pnadc.get(quarter=4, year=2020)

# =============================================================================


# Cálculo dos IEs =============================================================

pnadc = (pnad_raw
         .filter(items=['V2007', 'V2010', 'V4010', 'VD4010', 'VD4016', 'VD4002', 'V1028', 'UF'])
         .assign(cod=np.floor(pnad_raw['V4010']/1000),
                 setor=pnad_raw['VD4010'],
                 mulher=(pnad_raw['V2007'] == 2).astype(int),
                 negro=(pnad_raw['V2010'].isin([2, 4])).astype(int),
                 salario=pnad_raw['VD4016'],
                 count=1,
                 peso=pnad_raw['V1028'])
         .query('salario==salario'))              # NaN são diferentes entre si

# proporções a nível setor-ocupação

pnadc['salario'] = pnadc['salario']*pnadc['peso']   # para ponderar para a massa salarial

wm = lambda x: np.average(x, weights=pnadc.loc[x.index, 'peso'])

b_ocup_setor = (pnadc
                .query('VD4002==1')               # ocupação só existe para empregados
                .groupby(['UF', 'setor', 'cod'])
                .agg(b_mulher=('mulher', wm),
                     b_negro=('negro', wm),
                     massa_salarial=('salario', 'sum'))
                .reset_index()
                )


p_refs = (pnadc
          .query('VD4002==1 | VD4002==2')        # PEA é a minha pop de referencia
          .groupby(['UF'])
          .agg(p_mulher=('mulher', wm),
               p_negro=('negro', wm))
          .reset_index()
          )


indice_estado = (b_ocup_setor
                 .merge(right=p_refs,
                        how='inner',
                        on=['UF'])
                 .reset_index()
                 )


# calculo os IEs já multiplicando pela massa salarial para depois agregar e somar tudo
indice_estado['ie_racial_pre'] = (((indice_estado['b_negro'] - indice_estado['p_negro'])/indice_estado['p_negro'])*((indice_estado['p_negro'])/(1-indice_estado['p_negro']))**(indice_estado['b_negro']))*indice_estado['massa_salarial']
indice_estado['ie_genero_pre'] = (((indice_estado['b_mulher'] - indice_estado['p_mulher'])/indice_estado['p_mulher'])*((indice_estado['p_mulher'])/(1-indice_estado['p_mulher']))**(indice_estado['b_mulher']))*indice_estado['massa_salarial']

indice_estado = indice_estado.filter(['UF', 'setor', 'ie_racial_pre', 'ie_genero_pre', 'massa_salarial'])

indice_estado = indice_estado.groupby(['UF', 'setor']).sum().reset_index()

indice_estado = indice_estado[indice_estado['setor'] != 12]

indice_estado['ie_racial'] = indice_estado['ie_racial_pre']/indice_estado['massa_salarial']
indice_estado['ie_genero'] = indice_estado['ie_genero_pre']/indice_estado['massa_salarial']

# =============================================================================


# DFs separados para cada índice ==============================================

ie_genero = (indice_estado.pivot(index='UF',
                                 columns='setor',
                                 values='ie_genero')
                          .reset_index()
             )

ie_racial = (indice_estado.pivot(index='UF',
                                 columns='setor',
                                 values='ie_racial')
                          .reset_index()
             )


siglas = pd.read_csv('input/siglas-estados.csv')    # para dar merge no GeoJSON

ie_genero = ie_genero.merge(right=siglas,
                            how='inner',
                            left_on='UF',
                            right_on='COD')

ie_genero = ie_genero.rename(columns={1.0: 'um',
                                      2.0: 'dois',
                                      3.0: 'tres',
                                      4.0: 'quatro',
                                      5.0: 'cinco',
                                      6.0: 'seis',
                                      7.0: 'sete',
                                      8.0: 'oito',
                                      9.0: 'nove',
                                      10.0: 'dez',
                                      11.0: 'onze',
                                      'NOME': 'nome'})

ie_genero['SIGLA'] = ie_genero['SIGLA'].astype(str)


ie_racial = ie_racial.merge(right=siglas,
                            how='inner',
                            left_on='UF',
                            right_on='COD')

ie_racial = ie_racial.rename(columns={1.0: 'um',
                                      2.0: 'dois',
                                      3.0: 'tres',
                                      4.0: 'quatro',
                                      5.0: 'cinco',
                                      6.0: 'seis',
                                      7.0: 'sete',
                                      8.0: 'oito',
                                      9.0: 'nove',
                                      10.0: 'dez',
                                      11.0: 'onze',
                                      'NOME': 'nome'})

ie_racial['SIGLA'] = ie_racial['SIGLA'].astype(str)

del [p_refs, indice_estado, pnadc, b_ocup_setor, siglas, pnad_raw]
