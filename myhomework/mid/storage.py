import sqlite3

conn = sqlite3.connect('url.db')


def create_table():
    cursor = conn.cursor()
    table_sql = """
    create table url(
      id INTEGER PRIMARY KEY autoincrement NOT NULL ,
      short_url text NOT NULL,
      long_url text NOT NULL
    )
    """
    cursor.execute(table_sql)
    conn.commit()      

    table_sql = """
    create table url_index(
      id INTEGER PRIMARY KEY autoincrement NOT NULL,
      useless INTEGER
    )
    """
    cursor.execute(table_sql)
    conn.commit()      
    cursor.close()
