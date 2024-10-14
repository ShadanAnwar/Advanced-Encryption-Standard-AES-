import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENCRYPTED_DIR = os.path.join(BASE_DIR, 'encrypted_files')
DECRYPTED_DIR = os.path.join(BASE_DIR, 'decrypted_files')

# Ensure directories exist
os.makedirs(ENCRYPTED_DIR, exist_ok=True)
os.makedirs(DECRYPTED_DIR, exist_ok=True)

CHUNK_SIZE = 1024

