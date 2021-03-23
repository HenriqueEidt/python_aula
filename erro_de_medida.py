import numpy as np
from numpy.core.defchararray import count, mod
from pandas.core.frame import DataFrame
import statsmodels.api as sm
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import statistics

#tes

B1 = []
B2 = []
for i in range(0,1000):

    u = np.random.normal(loc=0,scale=1,size = 100)
    w = np.random.normal(loc=0,scale=1,size = 100)
    X = np.random.normal(loc=0,scale=1,size = 100) + 10
    Y = 5+5*X+u
    Xe = X + w

    Xe = sm.add_constant(Xe)
    mod = sm.OLS(endog = Y,exog = Xe)
    res = mod.fit()
    B1.append(res.params[0])
    B2.append(res.params[1])

print('--------------------Estat desc para reg simples com erro de medida em X2---------------')
print('B1')
print(statistics.mean(B1))
print(statistics.stdev(B1))
print(min(B1))
print(max(B1))

print('B2')
print(statistics.mean(B2))
print(statistics.stdev(B2))
print(min(B2))
print(max(B2))
print('---------------------------------------------------------------------------------------')

fig = px.histogram(B1)
#fig.show()

fig = px.histogram(B2)
#fig.show()






#Agora aumentando a variancia de X e e diminuindo a variancia do w


B1 = []
B2 = []
for i in range(0,1000):

    u = np.random.normal(loc=0,scale=1,size = 100)
    w = (np.random.normal(loc=0,scale=1,size = 100))/2
    X = (np.random.normal(loc=0,scale=1,size = 100) + 10) *5
    Y = 5+5*X+u
    Xe = X + w

    Xe = sm.add_constant(Xe)
    mod = sm.OLS(endog = Y,exog = Xe)
    res = mod.fit()
    B1.append(res.params[0])
    B2.append(res.params[1])

fig = px.histogram(B1)
#fig.show()

fig = px.histogram(B2)
#fig.show()

print('--------------------Estat desc para reg simples com erro de medida em X2 com variancia ajeitadas---------------')
print('B1')
print(statistics.mean(B1))
print(statistics.stdev(B1))
print(min(B1))
print(max(B1))

print('B2')
print(statistics.mean(B2))
print(statistics.stdev(B2))
print(min(B2))
print(max(B2))
print('---------------------------------------------------------------------------------------')









#Cotexto de regressão multipla SEM CORRELAÇÃO ENTRE X3 E X2

B1 = []
B2 = []
B3 = []
for i in range(0,1000):

    u = np.random.normal(loc=0,scale=1,size = 100)
    w = np.random.normal(loc=0,scale=1,size = 100)
    X2 = (np.random.normal(loc=0,scale=1,size = 100) + 10)
    X3 = (np.random.normal(loc=0,scale=1,size = 100) + 20)
    X2e = X2 + w

    Y = 5 + 5*X2 + 5*X3 + u

    #cria um df que recebe as duas litas, x2e e x3, essas são as variaveis independentes
    df = pd.DataFrame(list(zip(X2e,X3)))
    df.columns = ['X2e','X3']

    #cria uma var Xcodigo para adicionar a constante, acho que da pra fazer usando o df direto
    Xcodigo = df[['X2e','X3']]
    Xcodigo = sm.add_constant(Xcodigo)

    mod = sm.OLS(endog = Y,exog = Xcodigo)
    res = mod.fit()

    B1.append(res.params[0])
    B2.append(res.params[1])
    B3.append(res.params[2])


fig = px.histogram(B1)
#fig.show()

fig = px.histogram(B2)
#fig.show()

fig = px.histogram(B3)
#fig.show()


print('--------------------REG MULTIPLA SEM CORRELAÇÃO ENTRE X2 E X3---------------')
print('B1')
print(statistics.mean(B1))
print(statistics.stdev(B1))
print(min(B1))
print(max(B1))
print('B2')
print(statistics.mean(B2))
print(statistics.stdev(B2))
print(min(B2))
print(max(B2))
print('---------------------------------------------------------------------------------------')









#Cotexto de regressão multipla COM CORRELAÇÃO ENTRE X3 E X2

B1 = []
B2 = []
B3 = []
for i in range(0,1000):

    u = np.random.normal(loc=0,scale=1,size = 100)
    w = np.random.normal(loc=0,scale=1,size = 100)
    X2 = (np.random.normal(loc=0,scale=1,size = 100) + 10)
    X3 = ((np.random.normal(loc=0,scale=1,size = 100) + 20)+0.6*X2)
    X2e = X2 + w

    Y = 5 + 5*X2 + 5*X3 + u

    #cria um df que recebe as duas litas, x2e e x3, essas são as variaveis independentes
    df = pd.DataFrame(list(zip(X2e,X3)))
    df.columns = ['X2e','X3']

    #cria uma var Xcodigo para adicionar a constante, acho que da pra fazer usando o df direto
    Xcodigo = df[['X2e','X3']]
    Xcodigo = sm.add_constant(Xcodigo)

    mod = sm.OLS(endog = Y,exog = Xcodigo)
    res = mod.fit()

    B1.append(res.params[0])
    B2.append(res.params[1])
    B3.append(res.params[2])


fig = px.histogram(B1)
#fig.show()

fig = px.histogram(B2)
#fig.show()

fig = px.histogram(B3)
#fig.show()

print('--------------------REG MULTIPLA COM CORRELAÇÃO ENTRE X2 E X3---------------')
print('B1')
print(statistics.mean(B1))
print(statistics.stdev(B1))
print(min(B1))
print(max(B1))

print('B2')
print(statistics.mean(B2))
print(statistics.stdev(B2))
print(min(B2))
print(max(B2))
print('---------------------------------------------------------------------------------------')

print('B3')
print(statistics.mean(B3))
print(statistics.stdev(B3))
print(min(B3))
print(max(B3))
print('---------------------------------------------------------------------------------------')








#Cotexto de regressão multipla COM CORRELAÇÃO ENTRE X3 E X2

B1 = []
B2 = []
B3 = []
for i in range(0,1000):

    u = np.random.normal(loc=0,scale=1,size = 100)
    w = np.random.normal(loc=0,scale=1,size = 100)
    X2 = (np.random.normal(loc=0,scale=1,size = 100) + 10)
    X3 = ((np.random.normal(loc=0,scale=1,size = 100) + 20)+0.6*X2)
    X2e = X2 + w

    Y = 5 + 5*X2 + 5*X3 + u

    #cria um df que recebe as duas litas, x2e e x3, essas são as variaveis independentes
    df = pd.DataFrame(list(zip(X2e,X3)))
    df.columns = ['X2e','X3']

    #cria uma var Xcodigo para adicionar a constante, acho que da pra fazer usando o df direto
    Xcodigo = df[['X2e','X3']]
    Xcodigo = sm.add_constant(Xcodigo)

    mod = sm.OLS(endog = Y,exog = Xcodigo)
    res = mod.fit()

    B1.append(res.params[0])
    B2.append(res.params[1])
    B3.append(res.params[2])


fig = px.histogram(B1)
#fig.show()

fig = px.histogram(B2)
#fig.show()

fig = px.histogram(B3)
#fig.show()

print('--------------------REG MULTIPLA COM CORRELAÇÃO ENTRE X2 E X3---------------')
print('B1')
print(statistics.mean(B1))
print(statistics.stdev(B1))
print(min(B1))
print(max(B1))

print('B2')
print(statistics.mean(B2))
print(statistics.stdev(B2))
print(min(B2))
print(max(B2))
print('---------------------------------------------------------------------------------------')

print('B3')
print(statistics.mean(B3))
print(statistics.stdev(B3))
print(min(B3))
print(max(B3))
print('---------------------------------------------------------------------------------------')










#REG COM SOBESPECIFICAÇÃO

B1 = []
B2 = []
for i in range(0,1000):

    u = np.random.normal(loc=0,scale=1,size = 100)
    X2 = (np.random.normal(loc=0,scale=1,size = 100) + 10)
    X3 = (np.random.normal(loc=0,scale=1,size = 100) + 20)

    Y = 5 + 5*X2 + 5*X3 + u

    X2 = sm.add_constant(X2)

    mod = sm.OLS(endog = Y,exog = X2)
    res = mod.fit()

    B1.append(res.params[0])
    B2.append(res.params[1])


fig = px.histogram(B1)
#fig.show()

fig = px.histogram(B2)
#fig.show()


print('--------------------REG MULTIPLA COM SOBESPECIFICAÇÃO---------------')
print('B1')
print(statistics.mean(B1))
print(statistics.stdev(B1))
print(min(B1))
print(max(B1))

print('B2')
print(statistics.mean(B2))
print(statistics.stdev(B2))
print(min(B2))
print(max(B2))
print('---------------------------------------------------------------------------------------')