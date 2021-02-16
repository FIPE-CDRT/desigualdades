Este repositório contém todos os códigos e arquivos necessários para produzir as visualizações do relatório de desigualdades.

O projeto foi implementado utilizando `Python 3.8.5`e `R 4.0.1`, mas espera-se que funcione em versões posteriores.

É necessário instalar os seguintes pacotes, executando os códigos abaixo:
- Python: <br>
  ```python
  pip install pnadc plotly r2py
  ```
- R: <br>
  ```R
  install.packages("tidyverse", "PNADcIBGE", "convey", "fixest", "this.path")
  ```
Para replicar todos os resultados, basta mudar os diretórios de trabalho e o caminho para o R como indicado no arquivo `master.py` e executá-lo.

