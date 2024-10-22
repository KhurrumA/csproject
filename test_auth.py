from modules.authentication import authenticate_user

success, role = authenticate_user('admin', 'adminpass')
if success:
    print(f"Login successful. Role: {role}")
else:
    print("Login failed.")
