import pandas_datareader as wb
import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style



#Pega automaticamente todos os dados das ações e índices do yahoo finance para as datas em questão
df = wb.DataReader(['^BVSP','CYRE3.SA','EZTC3.SA','JHSF3.SA','TRIS3.SA','ITSA3.SA','DIRR3.SA','EVEN3.SA'],'yahoo',start = '01/01/2019', end = '12/31/2019')

#df passa a ser apenas os valoes Close, desconsiderando os demais
df = df['Close']

#Insere colunas de log-retorno para todas as ações
df.insert(loc=1, column = 'lnIBOV', value =  np.log(df['^BVSP']/df['^BVSP'].shift()))
df.insert(loc=3, column = 'lnCYRE3', value =  np.log(df['CYRE3.SA']/df['CYRE3.SA'].shift()))
df.insert(loc=5, column = 'lnEZTC3', value =  np.log(df['EZTC3.SA']/df['EZTC3.SA'].shift()))
df.insert(loc=7, column = 'lnJHSF3', value =  np.log(df['JHSF3.SA']/df['JHSF3.SA'].shift()))
df.insert(loc=9, column = 'lnTRIS3', value =  np.log(df['TRIS3.SA']/df['TRIS3.SA'].shift()))
df.insert(loc=11, column = 'lnITSA3', value =  np.log(df['ITSA3.SA']/df['ITSA3.SA'].shift()))
df.insert(loc=13, column = 'lnDIRR3', value =  np.log(df['DIRR3.SA']/df['DIRR3.SA'].shift()))
df.insert(loc=13, column = 'lnEVEN3', value =  np.log(df['EVEN3.SA']/df['EVEN3.SA'].shift()))


#Coloca o df em um csv, é necessário pois os log retornos geram valores 'NAN' na primeira linha, o que quebra o código a seguir
df.to_csv('trabalho.csv')

#Lê o arquivo csv pulando a primeira linha que contêm os valores 'NAN'
df = pd.read_csv('trabalho.csv',skiprows=[1])


ibov = sm.add_constant(df['lnIBOV'])
print(df)

#Define o modelo endog=y, exog=x
mod = sm.OLS(endog=df['lnITSA3'],exog= ibov)

#Roda o modelo
res = mod.fit()

#Printa os resultados
print(res.summary())


#CYRE3
mod_cyre3 = sm.OLS(endog=df['lnCYRE3'],exog= ibov)
res_cyre3 = mod_cyre3.fit()
print(res_cyre3.summary())

#EZTC3
mod_eztc3 = sm.OLS(endog=df['lnEZTC3'],exog= ibov)
res_eztc3 = mod_eztc3.fit()
print(res_eztc3.summary())

#JHSF3
mod_jhsf3 = sm.OLS(endog=df['lnJHSF3'],exog= ibov)
res_jhsf3 = mod_jhsf3.fit()
print(res_jhsf3.summary())

#TRIS3
mod_tris3 = sm.OLS(endog=df['lnTRIS3'],exog= ibov)
res_tris3 = mod_tris3.fit()
print(res_tris3.summary())

#DIRR3
mod_dirr3 = sm.OLS(endog=df['lnDIRR3'],exog= ibov)
res_dirr3 = mod_dirr3.fit()
print(res_dirr3.summary())

mod_even3 = sm.OLS(endog=df['lnEVEN3'],exog= ibov)
res_even3 = mod_even3.fit()
print(res_even3.summary())

#teqwe = res_cyre3.params


lista = res_cyre3,res_dirr3,res_even3,res_eztc3,res_jhsf3,res_tris3
teste = []
for i in lista:
    teste.append(i.params.iloc[0])
print(teste)






#Gera um df apenas de log retornos
returns = ['lnCYRE3','lnEZTC3','lnJHSF3','lnTRIS3','lnITSA3','lnDIRR3','lnEVEN3']

df_resid = pd.DataFrame(df['Date'])
for i in returns:
    df_resid[i] = df[i]
df_resid.set_index('Date',inplace=True)

#Converte as datas do formato string(padrão do pandas) para datetime. Sem esse procedimento o gráfico fica problemático
dates = df_resid.index.tolist()
dates = [pd.to_datetime(d) for d in dates]

#Estilos
style.use('seaborn')

#O restante é apenas configuração do gráfico
fig,axs = plt.subplots()

axs.scatter(x=dates,y=df_resid['lnEVEN3'],color='cornflowerblue',s=20)
axs.axhline(0,color='black')
axs.set_xlabel('Tempo')
axs.set_ylabel('Resíduos')
axs.set_title('EVEN3')


fig.suptitle("Resíduos em função do tempo", size=20)
fig.autofmt_xdate()

plt.show()
