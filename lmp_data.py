import pandas as pd_lmp
from sqlalchemy import create_engine
from settings import configsettings

connection = configsettings()['alchemy_engine']
db_table = configsettings()['table']
db_conn = create_engine(connection)


trade_date = '7/25/2021'
lmp_data = pd_lmp.read_csv('https://docs.misoenergy.org/marketreports/20210725_da_exante_lmp.csv', skiprows=4)
lmp_data.insert(3, 'Date', trade_date)
lmp_data.columns = lmp_data.columns.str.lower()
lmp_data.rename(columns=configsettings()['rename_columns'], inplace=True)

data = lmp_data.head()
try:
    data.to_sql(db_table, db_conn, if_exists='append', index=False)
    print('Data was imported')
except Exception as db_error:
    print(db_error)

# print(lmp_data.columns)
# print(lmp_data.dtypes)
# print(data)

