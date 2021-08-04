import sys
import psycopg2
from settings import configsettings


def db_connect():
    try:
        print(f'Connecting to database')
        conn = psycopg2.connect(
            user=configsettings()['user'],
            password=configsettings()['password'],
            host=configsettings()['host'],
            database=configsettings()['database']
        )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print('Connection successful')
    return conn
