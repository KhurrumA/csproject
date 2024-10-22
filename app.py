import tkinter as tk
from tkinter import messagebox, filedialog
from modules.authentication import authenticate_user
from modules.rbac import check_access
from modules.encryption import encrypt_file, decrypt_file
import sqlite3
import os

root = tk.Tk()
root.title("Secure File Storage System")
root.geometry("400x300")

current_user = None
current_role = None

def login():
    global current_user, current_role
    username = username_entry.get()
    password = password_entry.get()

    success, role = authenticate_user(username, password)
    if success:
        current_user = username
        current_role = role
        messagebox.showinfo("Login Success", f"Logged in as {username} ({role})")
        open_main_menu()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_login_screen():
    for widget in root.winfo_children():
        widget.destroy()

    global username_entry, password_entry

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    login_button = tk.Button(root, text="Login", command=login)
    login_button.pack()

def open_main_menu():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text=f"Welcome {current_user}!").pack()

    if current_role == "admin":
        tk.Button(root, text="Upload File", command=upload_file).pack()
        tk.Button(root, text="View All Files", command=view_files).pack()
    else:
        tk.Button(root, text="Upload File", command=upload_file).pack()
        tk.Button(root, text="View My Files", command=view_files).pack()

    tk.Button(root, text="Logout", command=logout).pack()

def upload_file():
    file_path = filedialog.askopenfilename(title="Select a file to upload")
    if not file_path:
        return

    aes_key = os.urandom(32)  
    encrypted_data = encrypt_file(file_path, aes_key)

    encrypted_filename = os.path.basename(file_path) + ".enc"
    with open(f"uploads/{encrypted_filename}", 'wb') as f:
        f.write(encrypted_data)

    con = sqlite3.connect('database/file_storage.db')
    cursor = con.cursor()
    cursor.execute("INSERT INTO files (filename, owner, aes_key) VALUES (?, ?, ?)", 
                   (encrypted_filename, current_user, aes_key))
    con.commit()
    con.close()

    messagebox.showinfo("Success", f"File '{encrypted_filename}' uploaded and encrypted successfully!")

def view_files():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Your Files:").pack()

    con = sqlite3.connect('database/file_storage.db')
    cursor = con.cursor()

    if current_role == "admin":
        cursor.execute("SELECT id, filename FROM files")
    else:
        cursor.execute("SELECT id, filename FROM files WHERE owner=?", (current_user,))

    files = cursor.fetchall()
    con.close()

    for file_id, filename in files:
        tk.Button(root, text=filename, command=lambda f=file_id: download_file(f)).pack()

    tk.Button(root, text="Back", command=open_main_menu).pack()

def download_file(file_id):
    con = sqlite3.connect('database/file_storage.db')
    cursor = con.cursor()

    cursor.execute("SELECT filename, aes_key, owner FROM files WHERE id=?", (file_id,))
    file_info = cursor.fetchone()
    con.close()

    if not file_info:
        messagebox.showerror("Error", "File not found.")
        return

    filename, aes_key, owner = file_info

    if not check_access(current_user, file_id):
        messagebox.showerror("Access Denied", "You do not have permission to access this file.")
        return

    with open(f"uploads/{filename}", 'rb') as f:
        encrypted_data = f.read()

    decrypted_data = decrypt_file(encrypted_data, aes_key)

    save_path = filedialog.asksaveasfilename(defaultextension=".txt", title="Save decrypted file as")
    if save_path:
        with open(save_path, 'wb') as f:
            f.write(decrypted_data)

        messagebox.showinfo("Success", "File decrypted and saved successfully!")

def logout():
    global current_user, current_role
    current_user = None
    current_role = None
    open_login_screen()

open_login_screen()
root.mainloop()
