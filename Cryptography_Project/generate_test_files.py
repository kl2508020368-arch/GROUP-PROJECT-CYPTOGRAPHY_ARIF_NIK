import os

# Create folder if it does not exist
os.makedirs("test_files", exist_ok=True)

# Required test file sizes in bytes
files = {
    "1KB.txt": 1024,
    "100KB.txt": 100 * 1024,
    "1MB.txt": 1024 * 1024
}

for filename, size in files.items():

    filepath = os.path.join("test_files", filename)

    with open(filepath, "wb") as file:
        file.write(b"A" * size)

    actual_size = os.path.getsize(filepath)

    print(f"{filename} created successfully")
    print(f"Size: {actual_size} bytes")
    print()