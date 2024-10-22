from modules.encryption import encrypt_file, decrypt_file
import os

key = os.urandom(32)  
encrypted = encrypt_file('test.txt', key)

with open('test_encrypted.bin', 'wb') as f:
    f.write(encrypted)

decrypted = decrypt_file(encrypted, key)
with open('test_decrypted.txt', 'wb') as f:
    f.write(decrypted)
