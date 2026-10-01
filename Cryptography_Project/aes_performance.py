from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import time
import statistics

# ==========================================
# AES-256 PERFORMANCE TEST
# ==========================================

key = AESGCM.generate_key(bit_length=256)
aes = AESGCM(key)

test_files = [
    "test_files/1KB.txt",
    "test_files/100KB.txt",
    "test_files/1MB.txt"
]

RUNS = 100

print("AES-256 PERFORMANCE TEST")
print("=" * 65)
print(f"Number of runs per file: {RUNS}")

for filepath in test_files:

    with open(filepath, "rb") as file:
        plaintext = file.read()

    encryption_times = []
    decryption_times = []

    correctness = True

    for _ in range(RUNS):

        nonce = os.urandom(12)

        # Encryption
        start = time.perf_counter()
        ciphertext = aes.encrypt(nonce, plaintext, None)
        end = time.perf_counter()

        encryption_times.append(end - start)

        # Decryption
        start = time.perf_counter()
        decrypted_data = aes.decrypt(nonce, ciphertext, None)
        end = time.perf_counter()

        decryption_times.append(end - start)

        if decrypted_data != plaintext:
            correctness = False

    # Calculate average
    avg_encryption = statistics.mean(encryption_times)
    avg_decryption = statistics.mean(decryption_times)

    filename = os.path.basename(filepath)

    print(f"\nFile: {filename}")
    print(f"Size: {len(plaintext)} bytes")
    print(f"Average Encryption Time: {avg_encryption:.9f} seconds")
    print(f"Average Decryption Time: {avg_decryption:.9f} seconds")
    print(f"Correctness: {'PASS' if correctness else 'FAIL'}")

print("\n" + "=" * 65)
print("Performance testing completed.")