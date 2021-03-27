import numpy as np
import pandas_datareader as web
import pandas as pd
import statsmodels.api as  sm




antes_inicio_1 = '01-16-2017'
antes_fim_1 = '03-16-2017'

dps_inicio_1 = '03-17-2017'
dps_fim_1 = '05-18-2017'




antes_inicio_2 = '03-28-2017'
antes_fim_2 = '05-30-2017'

dps_inicio_2 = '06-01-2017'
dps_fim_2 = '07-30-2017'




antes_inicio_3 = '05-30-2018'
antes_fim_3 = '07-31-2018'

dps_inicio_3 = '08-02-2018'
dps_fim_3 = '10-03-2018'




ativos=['^BVSP','BRFS3.sa','MRFG3.sa','JBSS3.sa','BEEF3.sa']

def estudo_retorno(data_inicio,data_fim):
    df = web.DataReader(['^BVSP','BRFS3.sa','MRFG3.sa','JBSS3.sa','BEEF3.sa'],'yahoo',start=data_inicio,end=data_fim)
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
        print(sm.stats.stattools.durbin_watson(res.resid))


    df.to_csv('preços.csv')


#estudo_retorno(dps_inicio_1,dps_fim_1)













def estudo_volume(data_inicio,data_fim):
    df = web.DataReader(['^BVSP','BRFS3.sa','MRFG3.sa','JBSS3.sa','BEEF3.sa'],'yahoo',start=data_inicio,end=data_fim)
    
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

    df.to_csv('volume.csv')

estudo_volume(data_inicio = dps_inicio_3, data_fim = dps_fim_3)
