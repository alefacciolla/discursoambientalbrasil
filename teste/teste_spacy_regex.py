# Pelo terminal, fiz instalação da spacy e download do pt_core_news_lg

import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import seaborn as sns
import spacy 
nlp = spacy.load("pt_core_news_lg")
with open('/home/skywalker/repositorios/discursoambientalbrasil/discursos/cop8_abertura.txt', 'r') as cop8:
   #file_text = cop8.read()
   df1 = pd.read_csv(cop8, sep="\n", header=None)
   print(df1)
