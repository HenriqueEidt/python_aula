#Importando as bibliotecas
from warnings import resetwarnings
import numpy as np
import pandas_datareader as web
import pandas as pd
import statsmodels.api as  sm

#Criando os intervalos de tempo que serão utilizados

antes_inicio_mariana = '09-04-2015'
antes_fim_mariana = '11-04-2015'

dps_inicio_mariana = '11-05-2015'
dps_fim_mariana = '01-07-2016'

antes_inicio_brumadinho ='11-22-2018'
antes_fim_brumandinho = '01-24-2019'

dps_inicio_brumadinho = '01-24-2019'
dps_fim_brumandinho = '03-27-2019'

ativos = ['^BVSP', 'VALE3.sa']

#Criando a função que executa uma reg da taxa de retorno do ativo em função da taxa de retorno
#do Ibov, em um determinado intervalo de tempo

def retorno_vale(data_inicio,data_fim):
    df = web.DataReader(['^BVSP','VALE3.sa'],'yahoo',start=data_inicio,end=data_fim)
    df = df[df["Volume"]>0]
    df = df['Close']

    df = df.dropna()

    for i in ativos:
        df.insert(loc = ativos.index(i), column = 'ln{}'.format(i), value = np.log(df[i]/df[i].shift()))

    df = df.iloc[1:]

    ibov = sm.add_constant(df['ln^BVSP'])

    for i in ativos:
        mod = sm.OLS(endog=df['ln{}'.format(i)],exog= ibov)
        res = mod.fit()
        print(res.summary())

    df.to_csv('preço_vale.csv')

#retorno_vale(dps_inicio_brumadinho,dps_fim_brumandinho)




#Criando a função que executa uma reg do volume de negociação do ativo em função do volume de 
#negociação do Ibov, em um determinado intervalo de tempo

def volume_vale(data_inicio,data_fim):
    df = web.DataReader(['^BVSP','VALE3.sa'],'yahoo',start=data_inicio,end=data_fim)

    df = df[df["Volume"]>0]
    df = df['Volume']

    df = df.dropna()


    for i in ativos:
        df.insert(loc = ativos.index(i), column = 'ln{}'.format(i), value = np.log(df[i]))

    df = df.iloc[1:]

    ibov = sm.add_constant(df['ln^BVSP'])

    for i in ativos:
        mod = sm.OLS(endog=df['ln{}'.format(i)],exog= ibov)
        res = mod.fit()
        print(res.summary())

    df.to_csv('volume_vale.csv')

volume_vale(dps_inicio_brumadinho,dps_fim_brumandinho)
