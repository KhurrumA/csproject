import sqlite3

def create_db():
    con = sqlite3.connect('database/file_storage.db')
    cursor = con.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        owner TEXT,
        aes_key BLOB
    )
    ''')

    con.commit()
    con.close()

if __name__ == "__main__":
    create_db()
