from datetime import date, datetime
from os import sep
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style



#A série 11426 começa em janeiro de 2001 por isso não pode ser baixada e calculada automaticamete como as outras
#Cria-se uma lista de integers com o código de cada série
series_cod = [433,4466,11427,16121,16122,27838,27839]

#Cria-se um dataframe completamente vazio
series_df = pd.DataFrame()

#Metas de inflação por ano
metas_inflação = [8,6,4,3.5,3.25,3.75,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.25,4,3.75,3.50,3.25]
limite_superior = [10,8,6,5.5,5.25,6.25,7,6.5,6.5,6.5,6.5,6.5,6.5,6.5,6.5,6.5,6.5,6.5,6,6,5.75,5.5]
limite_inferior = [6,4,2,1.5,1.25,1.25,2,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,3,3,2.75,2.5]

#O loop abaixo inicialmente lê em forma de loop cada uma das séries na lista series_cod, além disso ele pega automaticamente o último dado disponível
#O loop também calcula o índice e faz o acumulado em 12 meses
for i in series_cod:
    url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json&dataInicial=01/01/2000&dataFinal=01/0{}/{}'.format(i,datetime.today().month-1,datetime.today().year)
    df = pd.read_json(url)
    series_df['data'] = df['data']
    series_df[str(i)] = df['valor']
    series_df['índice - {}'.format(i)] = 1 + series_df[str(i)]/100
    series_df['acumulado - {}'.format(i)] = series_df['índice - {}'.format(i)].rolling(12).apply(np.prod,raw=True)
    series_df['acumulado - {}'.format(i)] = (series_df['acumulado - {}'.format(i)]-1)*100 

#Como a série 11426 começa em 01/01/2001 essa série é adicionada manualmente, é adicionado valores NaN para o ano 2000 dessa série
url_11426 = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.11426/dados?formato=json&dataInicial=01/01/2000&dataFinal=01/0{}/{}'.format(datetime.today().month-1,datetime.today().year)
df_11426 = pd.read_json(url_11426)
lista_11426 = []
for i in range(0,12):
    lista_11426.append(np.NaN)
lista_11426 = lista_11426 + df_11426['valor'].tolist()

series_df['11426'] = lista_11426
series_df['índice - 11426'] = 1 + series_df['11426']/100
series_df['acumulado - 11426'] = series_df['índice - 11426'].rolling(12).apply(np.prod,raw=True)
series_df['acumulado - 11426'] = (series_df['acumulado - 11426']-1)*100


#Adiciona as metas de inflação, fiz um loop para repetir cada valor 12 vezes e adionar no df
metas_inflação_mensal = []
limite_superior_mensal = []
limite_inferior_mensal = []

for i,k,p in zip(metas_inflação,limite_superior,limite_inferior):
    for j in range (0,12):
        metas_inflação_mensal.append(i)
        limite_superior_mensal.append(k)
        limite_inferior_mensal.append(p)

series_df['Metas inflação'] = pd.Series(metas_inflação_mensal)
series_df['Limite superior'] = pd.Series(limite_superior_mensal)
series_df['Limite inferior'] = pd.Series(limite_inferior_mensal)

#Cria uma série com as datas em um formato reconhecido pelo pandas/matplotlib, o formato padrão do site do bcb nada mais é que uma string representando uma data
series_df['Datas formatadas'] = pd.to_datetime(series_df['data'],dayfirst=True)

#Coloca as datas formatadas como o índice do dataframe, isso serve para facilitar o plot
series_df = series_df.set_index('Datas formatadas')
#print(series_df)


#Usa um estilo mais bonito para o gráfico
style.use('seaborn')

#Gráfico e algumas configurações
fig,ax = plt.subplots()
ax.plot(series_df[['acumulado - 433','acumulado - 11427','acumulado - 16121']])
ax.legend(('IPCA acumulado 12 meses','Sem monitorados e alimentos no domicílio - EX0','Núcleo por exclusão – EX1'))
fig.autofmt_xdate()
#plt.title('IPCA acumulado em 12 meses com as metas e limite superior e inferior')
fig.text(x=0.55,y=0.1,s='fonte: SGS - Sistema Gerenciador de Séries Temporais')
plt.grid(True)
#fig.savefig('ipca',dpi=600)
plt.show()


