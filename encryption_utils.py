from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def encrypt_chunk(chunk, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(chunk, AES.block_size))
    return base64.b64encode(iv + encrypted).decode('utf-8')

def decrypt_chunk(encrypted_chunk, key):
    try:
        encrypted_data = base64.b64decode(encrypted_chunk)
        iv = encrypted_data[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(encrypted_data[AES.block_size:]), AES.block_size)
    except (ValueError, TypeError) as e:
        raise ValueError(f"Decryption error: {str(e)}. The file may be corrupted or not properly encrypted.")