import sqlite3
PAGES_DB="pages.sqlite"

def create_table():
    conn = sqlite3.connect(PAGES_DB)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contPages (
            url TEXT PRIMARY KEY,
            cont INTEGER
        )
    ''')

def clean_table():
    conn = sqlite3.connect(PAGES_DB)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM contPages')

    conn.commit()
    conn.close()


def print_table():
    cont = 0
    conn = sqlite3.connect(PAGES_DB)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM contPages ORDER BY cont DESC')
    resultados = cursor.fetchall()

    for linha in resultados:
        print(cont, linha)
        cont +=1

    conn.close()



def table_to_array():
    conn = sqlite3.connect(PAGES_DB)
    cursor = conn.cursor()

    cursor.execute('SELECT url FROM contPages ORDER BY cont DESC')
    resultados = cursor.fetchall()
    array_resultados = []

    for linha in resultados:
        array_resultados.append(list(linha))

    conn.close()
    return array_resultados

create_table()