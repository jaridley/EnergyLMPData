import sys

import psycopg2

db_param = {
    'host': '34.69.172.133',
    'database': 'miso-dalmp',
    'user': 'postgres',
    'password': 'Bakusaiga#01'
}


def db_connect(db_param):
    conn = None
    try:
        print(f'Connecting to database')
        conn = psycopg2.connect(**db_param)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print('Connection successful')
    return conn


db_connect(db_param)
