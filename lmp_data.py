import pandas as pd_lmp
from sqlalchemy import create_engine
from settings import congifsettings

connection = congifsettings()['alchemy_engine']
db_table = congifsettings()['table']
db_conn = create_engine(connection)

rename_columns = {
    'he 1': 'he_1',
    'he 2': 'he_2',
    'he 3': 'he_3',
    'he 4': 'he_4',
    'he 5': 'he_5',
    'he 6': 'he_6',
    'he 7': 'he_7',
    'he 8': 'he_8',
    'he 9': 'he_9',
    'he 10': 'he_10',
    'he 11': 'he_11',
    'he 12': 'he_12',
    'he 13': 'he_13',
    'he 14': 'he_14',
    'he 15': 'he_15',
    'he 16': 'he_16',
    'he 17': 'he_17',
    'he 18': 'he_18',
    'he 19': 'he_19',
    'he 20': 'he_20',
    'he 21': 'he_21',
    'he 22': 'he_22',
    'he 23': 'he_23',
    'he 24': 'he_24',
}

trade_date = '7/25/2021'
lmp_data = pd_lmp.read_csv('https://docs.misoenergy.org/marketreports/20210725_da_exante_lmp.csv', skiprows=4)
lmp_data.insert(3, 'Date', trade_date)
lmp_data.columns = lmp_data.columns.str.lower()
lmp_data.rename(columns=rename_columns, inplace=True)

data = lmp_data.head()

try:
    data.to_sql(db_table, db_conn, if_exists='append', index=False)
    print('Data was imported')
except Exception as db_error:
    print(db_error)

# print(lmp_data.columns)
# print(lmp_data.dtypes)
# print(data)

