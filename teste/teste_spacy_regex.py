# Pelo terminal, fiz instalação da spacy e download do pt_core_news_lg

import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import seaborn as sns
#import spacy
#nlp = spacy.load("pt_core_news_lg")
with open('/home/skywalker/repositorios/discursoambientalbrasil/discursos/cop10.txt', 'r') as cop10:
   df10 = pd.read_csv(cop10, sep="\n", header=None)
   print(df10.head(10))
