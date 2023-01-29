import os
import psycopg2
from psycopg2.extras import DictCursor


AWS_DB_USER = os.environ['AWS_DB_USER']
AWS_DB_PASSOWRD = os.environ['AWS_DB_PASSOWRD']
AWS_DB_HOST = os.environ['AWS_DB_HOST']
AWS_DB_PORT = os.environ['AWS_DB_PORT']
AWS_DB_NAME = os.environ['AWS_DB_NAME']


def get_db_connection(cf=None):
    conn = psycopg2.connect(user=AWS_DB_USER, password=AWS_DB_PASSOWRD,
                            host=AWS_DB_HOST, port=AWS_DB_PORT,
                            database=AWS_DB_NAME)

    return conn, conn.cursor(cursor_factory=DictCursor) \
        if cf == 'dict_cursor' else conn.cursor()
