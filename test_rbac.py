from modules.rbac import check_access

# Check if 'admin' can access any file
print(check_access('admin', 1))  # Should return True
