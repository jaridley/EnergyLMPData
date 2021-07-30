import pandas as pd_lmp
from sqlalchemy import create_engine
from settings import congifsettings

connection = congifsettings()['alchemy_engine']
db_conn = create_engine(connection)

trade_date = '7/25/2021'
lmp_data = pd_lmp.read_csv('https://docs.misoenergy.org/marketreports/20210725_da_exante_lmp.csv', skiprows=4)
lmp_data.insert(3, 'Date', trade_date)
data = lmp_data.head()
data.to_sql(db_conn, name='da_exante_lmp', if_exists='append', index=False)

# print(lmp_data.columns.values)
# print(lmp_data.dtypes)
# print(lmp_data.head())

