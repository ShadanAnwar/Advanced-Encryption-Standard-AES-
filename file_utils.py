import os
from config import CHUNK_SIZE, ENCRYPTED_DIR, DECRYPTED_DIR
from encryption_utils import encrypt_chunk, decrypt_chunk
import streamlit as st

def split_file(file):
    while True:
        chunk = file.read(CHUNK_SIZE)
        if not chunk:
            break
        yield chunk

def encrypt_file(input_file, key):
    file_name = os.path.basename(input_file.name)
    output_file = os.path.join(ENCRYPTED_DIR, f"encrypted_{file_name}")
    os.makedirs(ENCRYPTED_DIR, exist_ok=True)  # Ensure the directory exists
    with open(output_file, 'w') as outfile:
        for chunk in split_file(input_file):
            encrypted_chunk = encrypt_chunk(chunk, key)
            outfile.write(encrypted_chunk + '\n')
    return output_file

def decrypt_file(input_file, key):
    file_name = os.path.basename(input_file.name)
    output_file = os.path.join(DECRYPTED_DIR, file_name.replace("encrypted_", "decrypted_"))
    os.makedirs(DECRYPTED_DIR, exist_ok=True)  # Ensure the directory exists
    with open(output_file, 'wb') as outfile:
        content = input_file.getvalue().decode().split('\n')
        for line in content:
            if line:  # Skip empty lines
                try:
                    decrypted_chunk = decrypt_chunk(line.strip(), key)
                    outfile.write(decrypted_chunk)
                except ValueError as e:
                    raise ValueError(f"Error decrypting file: {str(e)}")
    return output_file