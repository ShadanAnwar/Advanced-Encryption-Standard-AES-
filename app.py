import streamlit as st
import binascii
import os
from file_utils import encrypt_file, decrypt_file
from config import ENCRYPTED_DIR, DECRYPTED_DIR

def main():
    st.set_page_config(page_title="AES", page_icon="🔒")
    st.title("AES Encryption App")

    action = st.radio("Choose action:", ("Encrypt", "Decrypt"))
    uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "docx"])
    key = st.text_input("Enter encryption key (32 bytes or 64 hexadecimal characters):", type="password")

    if uploaded_file is not None and key:
        try:
            key_bytes = binascii.unhexlify(key.strip())
            if len(key_bytes) != 32:
                st.error("Key must be 32 bytes (64 hexadecimal characters) long.")
                return
        except binascii.Error:
            if len(key.encode()) != 32:
                st.error("Key must be 32 bytes long.")
                return
            key_bytes = key.encode()

        try:
            if action == "Encrypt":
                if st.button("Encrypt File"):
                    with st.spinner("Encrypting..."):
                        output_file = encrypt_file(uploaded_file, key_bytes)
                        
                        if os.path.exists(output_file):
                            with open(output_file, "rb") as f:
                                st.download_button(
                                    label="Download Encrypted File",
                                    data=f,
                                    file_name=os.path.basename(output_file),
                                    mime="application/octet-stream"
                                )
                            st.success(f"File encrypted successfully! Saved in {ENCRYPTED_DIR}")
                        else:
                            st.error("Encryption failed. Output file not created.")

            elif action == "Decrypt":
                if st.button("Decrypt File"):
                    with st.spinner("Decrypting..."):
                        output_file = decrypt_file(uploaded_file, key_bytes)
                        
                        if os.path.exists(output_file):
                            with open(output_file, "rb") as f:
                                st.download_button(
                                    label="Download Decrypted File",
                                    data=f,
                                    file_name=os.path.basename(output_file),
                                    mime="application/octet-stream"
                                )
                            st.success(f"File decrypted successfully! Saved in {DECRYPTED_DIR}")
                        else:
                            st.error("Decryption failed. Output file not created.")

        except Exception as e:
            if "Invalid base64-encoded string" in str(e):
                st.error("Decryption failed. The file may be corrupted or not properly encrypted. Please ensure you're using the correct key and a valid encrypted file.")
            else:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
