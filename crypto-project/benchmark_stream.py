import os
import time
from stream_cipher import SimplifiedRC4


def create_dummy_file(filename, size_in_bytes):
    with open(filename, "wb") as f:
        f.write(os.urandom(size_in_bytes))


def benchmark_stream_cipher(filename, key):
    with open(filename, "rb") as f:
        data = f.read()

    # Encryption
    cipher_enc = SimplifiedRC4(key)

    start_time = time.perf_counter()
    ciphertext = cipher_enc.encrypt_decrypt(data)
    enc_time = (time.perf_counter() - start_time) * 1000

    # Decryption
    cipher_dec = SimplifiedRC4(key)

    start_time = time.perf_counter()
    decrypted = cipher_dec.encrypt_decrypt(ciphertext)
    dec_time = (time.perf_counter() - start_time) * 1000

    # Verify
    assert data == decrypted

    # Throughput
    size_mb = len(data) / (1024 * 1024)

    enc_throughput = size_mb / (enc_time / 1000)
    dec_throughput = size_mb / (dec_time / 1000)

    print(f"File: {filename}")
    print(f"Size: {len(data) / 1024:.1f} KB")
    print(f"Encryption: {enc_time:.3f} ms")
    print(f"Decryption: {dec_time:.3f} ms")
    print(f"Encryption Throughput: {enc_throughput:.3f} MB/s")
    print(f"Decryption Throughput: {dec_throughput:.3f} MB/s")
    print()


if __name__ == "__main__":

    key = b"KunciUjian123"

    files = {
        "file_1kb.bin": 1024,
        "file_100kb.bin": 100 * 1024,
        "file_1mb.bin": 1024 * 1024
    }

    print("=== STREAM CIPHER PERFORMANCE TEST ===")
    print()

    for filename, size in files.items():
        create_dummy_file(filename, size)
        benchmark_stream_cipher(filename, key)