import csv
from datetime import datetime as dt

from .db_access import get_db_connection


def write_to_db(file_content: str):
    conn, cursor = None, None

    try:
        conn, cursor = get_db_connection()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dados (
                cpf character varying(20) NOT NULL,
                cnpj character varying(20) NOT NULL,
                data date NOT NULL
            );
        ''')

        query = 'INSERT INTO dados(cpf, cnpj, data) VALUES '

        query_values = []
        values = []

        lines = csv.reader(file_content)
        headers = next(lines)
        print('headers', headers)

        for line in lines:
            print('line', line)
            query_values.append('(%s, %s, %s)')
            cpf = line[0].replace('.', '').replace('-', '')
            cnpj = line[1].replace('.', '').replace('-', '').replace('/', '')
            date = (dt.strptime(line[2], '%d/%m/%Y')).strftime('%Y-%m-%d')

            values += [cpf, cnpj, date]

        query += ', '.join(query_values)

        cursor.execute(query, values)

        conn.commit()
    except Exception as e:
        str_e = str(e)
        print("# write_to_db ERROR: ", str_e)
        return False
    finally:
        cursor.close()
        conn.close()

    return True
