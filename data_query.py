from db_connect import db_connect
import pandas as pd


def data_query():
    query = '''SELECT * from da_exante_lmp
    where node='AEC'
    '''
    lmp_df = pd.read_sql(query, db_connect())
    print(lmp_df)


data_query()
