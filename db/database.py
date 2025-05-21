import sqlite3

DB_NAME = 'data.db'

def connect():
    conn = sqlite3.connect(DB_NAME)
    return conn

def init_db():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

