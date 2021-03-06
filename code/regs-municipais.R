#===============================================================================
#     Microdados da RAIS s�o muito pesados, deve rodar s� em pc com RAM >= 32gb
#===============================================================================


library(tidyverse)
library(fixest)
library(plotly)


rais_sp_2019 <- read_csv2(file = 'd:/Users/lucas.dias/Downloads/RAIS_VINC_PUB_SP.txt',
                          locale(encoding = "LATIN1"),
                          col_names = TRUE,
                          col_types = NULL) %>%
                dplyr::select(`CBO Ocupa��o 2002`, `CNAE 2.0 Classe`,
                              `V�nculo Ativo 31/12`, `Qtd Hora Contr`,
                              `Idade`, `Munic�pio`, `Ra�a Cor`,
                              `Vl Remun Dezembro Nom`, `Sexo Trabalhador`)
                dplyr::filter(`V�nculo Ativo 31/12` == 1)


raismun_2019 <- rais_sp_2019 %>%
    dplyr::filter(`V�nculo Ativo 31/12` == 1 &
                  as.numeric(sub(",", ".", `Vl Remun Dezembro Nom`, fixed = TRUE)) != 0 &
                  `Qtd Hora Contr` != 0 &
                  `Ra�a Cor` != "09" & `Ra�a Cor` != "99" &
                  `CBO Ocupa��o 2002` != -1) %>%
    dplyr::select(`CBO Ocupa��o 2002`, `CNAE 2.0 Classe`, `V�nculo Ativo 31/12`,
                  `Qtd Hora Contr`,`Idade`, `Munic�pio`, `Ra�a Cor`,
                  `Vl Remun Dezembro Nom`, `Sexo Trabalhador`) %>%
    dplyr::mutate(negro = ifelse(`Ra�a Cor` == '04' | `Ra�a Cor` == '08', 1, 0),
                  mulher = ifelse(`Sexo Trabalhador` == '02', 1, 0),
                  cbo = floor(`CBO Ocupa��o 2002`/100),
                  setor = as.numeric(`CNAE 2.0 Classe`),
                  idade = `Idade`,
                  idade2 = (`Idade`)^2,
                  wage = log(as.numeric(sub(",", ".", `Vl Remun Dezembro Nom`, fixed = TRUE))/`Qtd Hora Contr`)
                 )

wage_gaps <- data.frame()


for (mun in unique(raismun_2019$Munic�pio)) {
  
  rais_mun <- raismun_2019 %>%
    dplyr::filter(`Munic�pio` == mun)
  
  modelo <- feols(wage ~ negro + mulher + idade + idade2 | cbo + setor, rais_mun)
  
  tabela <- as.data.frame(modelo[['coeftable']])
  
  wage_gaps[paste0(mun), 'gap_negros'] <- tabela['negro', 'Estimate']
  wage_gaps[paste0(mun), 'p_valor_negros'] <- tabela['negro', 'Pr(>|t|)']
  wage_gaps[paste0(mun), 'gap_mulheres'] <- tabela['mulher', 'Estimate']
  wage_gaps[paste0(mun), 'p_valor_mulheres'] <- tabela['mulher', 'Pr(>|t|)']
  
}


wage_gaps$Mun <- rownames(wage_gaps)

is.num <- sapply(wage_gaps, is.numeric)
wage_gaps[is.num] <- lapply(wage_gaps[is.num], round, 8)


p_valor <- 0.10


wage_gaps <- wage_gaps %>% 
  dplyr::mutate(gap_negros = replace(gap_negros, p_valor_negros > p_valor, 0),
                gap_mulheres = replace(gap_mulheres, p_valor_mulheres > p_valor, 0))


write_csv(wage_gaps, 'tmp/wage_gaps.csv')
