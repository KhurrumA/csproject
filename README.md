# Secure File Storage System

**Secure File Storage System** is a desktop-based Python application that allows users to upload and retrieve encrypted files with proper authentication and access control.  
The system features role-based permissions (Admin/User), AES encryption, and secure login functionality — all wrapped in a clean Tkinter GUI.

---

## Features

- Secure login using hashed passwords (bcrypt)
- Role-based access control (Admin/User)
- Upload and encrypt files (AES-256)
- Decrypt and download only accessible files
- View all or personal files based on user role
- Includes unit tests for authentication, encryption, and RBAC
- Simple GUI using Tkinter


---

## Installation & Setup

1. Clone the repo or download the project.
2. Install required libraries:
```bash
pip install bcrypt cryptography
```
3. Create the database:
```bash
python DB.py
```
4. (Optional) Run `test_login.py` to create sample users:
```bash
python test_login.py
```
5. Launch the app:
```bash
python app.py
```

---

## Tests

You can test each component manually:

- `test_auth.py` → Tests login
- `test_encryp.py` → Tests encryption & decryption
- `test_rbac.py` → Verifies file access permissions

---

## Default Test Users

Run `test_login.py` to register:

```bash
Username: admin       Password: adminpass     Role: admin
Username: user1       Password: user1pass     Role: user
```

---

## Author

**Khurrum Arif**  
 [KhurrumArif02@gmail.com](mailto:KhurrumArif02@gmail.com)  
 [LinkedIn](https://www.linkedin.com/in/khurrum-arif-uol) | [GitHub](https://github.com/KhurrumA)

---
