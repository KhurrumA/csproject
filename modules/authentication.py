import sqlite3
import bcrypt

def register_user(username, password, role):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    con = sqlite3.connect('database/file_storage.db')
    cursor = con.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", 
                       (username, hashed, role))
        con.commit()
        print(f"User {username} registered successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    con.close()

def authenticate_user(username, password):
    con = sqlite3.connect('database/file_storage.db')
    cursor = con.cursor()

    cursor.execute("SELECT password, role FROM users WHERE username=?", (username,))
    result = cursor.fetchone()

    con.close()
    if result and bcrypt.checkpw(password.encode(), result[0]):
        return True, result[1]
    return False, None
