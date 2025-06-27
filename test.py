import os
import pandas as pd
import sqlalchemy as db
import requests

STOCK_DATA_API_KEY = os.environ.get('STOCK_DATA_API_KEY')
url = 'https://api.stockdata.org/v1/data/quote'
params = {'api_token':STOCK_DATA_API_KEY, 'symbols':'AAPL,GOOG,AMZN'}
r = requests.get(url, params=params)
data = r.json()['data']
params['symbols'] = 'TSLA,V,SPY'
r = requests.get(url, params=params)
data += r.json()['data']
params['symbols'] = 'MSFT,NVDA,JPM'
r = requests.get(url, params=params)
data += r.json()['data']
df = pd.DataFrame.from_dict(data)
engine = db.create_engine('sqlite:///stocks.db')
df.to_sql('symbols', con=engine, if_exists='replace', index=False)
with engine.connect() as c:
  query_results = c.execute(db.text('SELECT * FROM symbols;')).fetchall()
  print(pd.DataFrame(query_results))
