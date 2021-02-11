
library(PNADcIBGE)
library(convey)
library(survey)
library(tidyverse)

#===============================================================================

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
setwd('..')

ano = 2020
trimestre = 3


#===============================================================================

ano_inicio = ano - 4
anos_completos = (ano_inicio + 1):(ano -1)

gini_data <- data.frame(matrix(ncol = 4, nrow = 0))   
  colnames(gini_data) <- c('Ano', 'Trimestre', 'UF', 'Gini')
  

  
for (t in 1:trimestre) {
  
  
  pnadc = get_pnadc(year = ano,
                    quarter = t,
                    vars = c('Ano','Trimestre', 'UF', 'VD4019'))
  
  pnadc <- convey_prep(pnadc)
  
  gini_estados <- svyby(~VD4019, by = ~UF, pnadc, svygini, na.rm  =  TRUE)
  gini_br <- svygini(~VD4019, pnadc, na.rm  =  TRUE)
  
  gini_br <- gini_br %>% 
    data.frame(stringsAsFactors = FALSE) %>%
    mutate(UF = 'Brasil') %>%
    rename(se = VD4019) %>%
    rename(VD4019 = gini)
  
  gini_estados <- rbind(gini_estados, gini_br)
  rm(gini_br)
  
    rownames(gini_estados) <- NULL
  
  gini_estados <- gini_estados %>%
                  dplyr::select(UF, VD4019) %>%
                  dplyr::rename(Gini = VD4019) %>%
                  dplyr::mutate(Ano = ano,
                                Trimestre = t) %>%
                  dplyr::relocate(Ano, Trimestre, UF, Gini)
  
  gini_data <- rbind(gini_data, gini_estados)
  
    
}


  
  
for (year in anos_completos) {
    
    for (t in 1:4) {
      
      pnadc = get_pnadc(year = year,
                        quarter = t,
                        vars = c('Ano','Trimestre', 'UF', 'VD4019'))
      
      pnadc <- convey_prep(pnadc)
      
      gini_estados <- svyby(~VD4019, by = ~UF, pnadc, svygini, na.rm  =  TRUE)
      gini_br <- svygini(~VD4019, pnadc, na.rm  =  TRUE)
      
      gini_br <- gini_br %>% 
        data.frame(stringsAsFactors = FALSE) %>%
        mutate(UF = 'Brasil') %>%
        rename(se = VD4019) %>%
        rename(VD4019 = gini)
      
      gini_estados <- rbind(gini_estados, gini_br)
      rm(gini_br)
      
      rownames(gini_estados) <- NULL
      
      gini_estados <- gini_estados %>%
        dplyr::select(UF, VD4019) %>%
        dplyr::rename(Gini = VD4019) %>%
        dplyr::mutate(Ano = year,
                      Trimestre = t) %>%
        dplyr::relocate(Ano, Trimestre, UF, Gini)
      
      gini_data <- rbind(gini_data, gini_estados)
      
      
    }
    
}
  
  
  
for (t in trimestre:4) {
  
  
  pnadc = get_pnadc(year = ano_inicio,
                    quarter = t,
                    vars = c('Ano','Trimestre', 'UF', 'VD4019'))
  
  pnadc <- convey_prep(pnadc)
  
  gini_estados <- svyby(~VD4019, by = ~UF, pnadc, svygini, na.rm  =  TRUE)
  gini_br <- svygini(~VD4019, pnadc, na.rm  =  TRUE)
  
  gini_br <- gini_br %>% 
    data.frame(stringsAsFactors = FALSE) %>%
    mutate(UF = 'Brasil') %>%
    rename(se = VD4019) %>%
    rename(VD4019 = gini)
  
  gini_estados <- rbind(gini_estados, gini_br)
  rm(gini_br)
  
    rownames(gini_estados) <- NULL
  
  gini_estados <- gini_estados %>%
                  dplyr::select(UF, VD4019) %>%
                  dplyr::rename(Gini = VD4019) %>%
                  dplyr::mutate(Ano = ano_inicio,
                                Trimestre = t) %>%
                  dplyr::relocate(Ano, Trimestre, UF, Gini)
  
  gini_data <- rbind(gini_data, gini_estados)
  
  
}


  
serie_gini <- gini_data %>%
              tidyr::pivot_wider(names_from = UF,
                                 values_from = Gini) %>%
              dplyr::arrange(Ano, Trimestre) %>%
              dplyr::mutate(Ano_Tri = paste0(Ano, 'T', Trimestre)) %>%
              dplyr::select(-Ano, -Trimestre) %>%
              dplyr::relocate(Ano_Tri)


names(serie_gini) <- str_replace_all(names(serie_gini), c(" " = "." , "," = "" ))  

write_csv(serie_gini, 'tmp/serie_gini.csv')