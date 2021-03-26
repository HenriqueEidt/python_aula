from numpy.core.defchararray import index
import pandas as pd
import pandas_datareader as web
import numpy as np
import statsmodels.api as sm
from statsmodels.regression.linear_model import OLS

ativos = ['^BVSP','JBSS3.sa','BRFS3.sa','MRFG3.sa','BEEF3.sa']

fase_1_start = '02-7-2017'
fase_1_end = '03-18-2021'

fase_2_start = '04-21-2017'
fase_2_end = '05-31-2017'

fase_3_start = '03-25-2018'
fase_3_end = '05-05-2018'

def preço_primeira_parte():
    df = web.DataReader(ativos,'yahoo',start=fase_1_start,end=fase_1_end)
    df = df['Adj Close']
    
    for i in ativos:
        df.insert(loc = ativos.index(i),column='ln{}'.format(i),value = np.log(df[i]/df[i].shift()))
        df = df.iloc[1:]

        ibov = sm.add_constant(df['ln^BVSP'])
        mod = sm.OLS(endog=df['ln{}'.format(i)],exog= ibov)
        res = mod.fit()
        print(res.summary())


def volum_primeira_parte():
    df = web.DataReader(ativos,'yahoo',start='02-7-2017',end='03-18-2017')
    df = df['Volume']
    
    for i in ativos:
        df.insert(loc = ativos.index(i),column='ln_vol{}'.format(i),value = np.log(df[i]/df[i].shift()))
        df = df.iloc[1:]

        ibov = sm.add_constant(df['ln_vol^BVSP'])
        mod = sm.OLS(endog=df['ln_vol{}'.format(i)],exog= ibov)
        res = mod.fit()
        print(res.summary())
    print(df)

volum_primeira_parte()

