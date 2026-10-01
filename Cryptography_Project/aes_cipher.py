from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

# ==========================================
# AES-256 FILE ENCRYPTION AND DECRYPTION
# ==========================================

# Generate a 256-bit AES key
key = AESGCM.generate_key(bit_length=256)
aes = AESGCM(key)

# Generate a random 12-byte nonce
nonce = os.urandom(12)

# File paths
input_file = "test_files/message.txt"
encrypted_file = "test_files/message_encrypted.bin"
decrypted_file = "test_files/message_decrypted.txt"

# ==========================================
# ENCRYPTION
# ==========================================

# Read original file
with open(input_file, "rb") as file:
    plaintext = file.read()

# Encrypt file content
ciphertext = aes.encrypt(nonce, plaintext, None)

# Save encrypted data
with open(encrypted_file, "wb") as file:
    file.write(ciphertext)

print("AES-256 FILE ENCRYPTION")
print("-----------------------")
print("Original file :", input_file)
print("AES Key       :", key.hex())
print("Nonce         :", nonce.hex())
print("Encrypted file:", encrypted_file)
print("Encryption successful.")

# ==========================================
# DECRYPTION
# ==========================================

# Read encrypted file
with open(encrypted_file, "rb") as file:
    encrypted_data = file.read()

# Decrypt
decrypted_data = aes.decrypt(nonce, encrypted_data, None)

# Save decrypted data
with open(decrypted_file, "wb") as file:
    file.write(decrypted_data)

print("\nAES-256 FILE DECRYPTION")
print("-----------------------")
print("Encrypted file:", encrypted_file)
print("Decrypted file:", decrypted_file)
print("Decryption successful.")

# ==========================================
# CORRECTNESS TEST
# ==========================================

if plaintext == decrypted_data:
    print("\nSUCCESS: Decrypted file matches the original file.")
else:
    print("\nFAILED: Decrypted file does not match the original file.")