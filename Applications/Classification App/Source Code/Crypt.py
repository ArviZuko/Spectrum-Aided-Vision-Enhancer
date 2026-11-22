from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from hashlib import sha256
import os

input_file = r'C:\Users\Arvind\Downloads\best.pt'
output_file = 'best.pt.encrypted'
password = '12345678' 
key = sha256(password.encode()).digest()
with open(input_file, 'rb') as f:
    plaintext = f.read()
pad_len = 16 - len(plaintext) % 16
plaintext += bytes([pad_len]) * pad_len
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(plaintext)
with open(output_file, 'wb') as f:
    f.write(iv + ciphertext)
print("Encryption complete. Output:", output_file)