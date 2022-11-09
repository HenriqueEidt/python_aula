import pandas as pd
from datetime import datetime

url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.11426/dados?formato=json&dataInicial=01/01/2000&dataFinal=01/0{}/{}'.format(datetime.today().month-1,datetime.today().year)
df = pd.read_json(url)
print(df)
