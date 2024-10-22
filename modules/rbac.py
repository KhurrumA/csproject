import sqlite3

def check_access(user_role, file_id):
    if user_role == "admin":
        return True

    con = sqlite3.connect('database/file_storage.db')
    cursor = con.cursor()

    cursor.execute("SELECT owner FROM files WHERE id=?", (file_id,))
    file_owner = cursor.fetchone()

    con.close()

    if file_owner is None:
        print(f"No file found with id: {file_id}")
        return False

    file_owner = file_owner[0] 

    if user_role == file_owner:
        return True
    else:
        return False
