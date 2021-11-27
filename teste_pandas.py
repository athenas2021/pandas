import pandas as pd
import numpy as np
import os


file = f'{os.path.dirname(os.path.realpath(__file__))}\\bovespa_teste_tudo.csv'

# Ler csv
df = pd.read_csv(file, delimiter=',')

# Filtragem ações Itau e preço de abertura >= 28
filtro_itau = (df['sigla_acao'] == 'ITUB4')
df_itau = df[ filtro_itau & (df['preco_abertura'] >= 28)]

# Loc
print(df_itau.loc[:,'data_pregao'])

# iLoc
print(df_itau.iloc[:,2:5])
