# AES File Encryption/Decryption Project Documentation

## Project Overview

This project implements a file encryption and decryption tool using the Advanced Encryption Standard (AES) algorithm. It provides a user-friendly web interface built with Streamlit, allowing users to securely encrypt and decrypt various file types including TXT, PDF, and DOCX.

## Project Structure

```
aes-file-encryption-tool/
│
├── app.py
├── config.py
├── encryption_utils.py
├── file_utils.py
├── requirements.txt
├── README.md
│
├── encrypted_files/
└── decrypted_files/
```

### File Descriptions

1. `app.py`: The main Streamlit application file that handles the user interface and orchestrates the encryption/decryption process.

2. `config.py`: Contains configuration settings for the project, including directory paths and chunk size for file processing.

3. `encryption_utils.py`: Implements the core encryption and decryption functions using the AES algorithm.

4. `file_utils.py`: Provides utility functions for file handling, including reading files in chunks and writing encrypted/decrypted data.

5. `requirements.txt`: Lists all the Python dependencies required for the project.

6. `README.md`: Provides an overview of the project, installation instructions, and usage guidelines.

7. `encrypted_files/`: Directory where encrypted files are stored.

8. `decrypted_files/`: Directory where decrypted files are stored.

## Functionality

### Encryption Process

1. The user uploads a file through the Streamlit interface.
2. The file is read in chunks (defined in `config.py`).
3. Each chunk is encrypted using AES encryption (implemented in `encryption_utils.py`).
4. The encrypted chunks are written to a new file in the `encrypted_files/` directory.

### Decryption Process

1. The user uploads an encrypted file through the Streamlit interface.
2. The encrypted file is read in chunks.
3. Each chunk is decrypted using the AES decryption function.
4. The decrypted chunks are written to a new file in the `decrypted_files/` directory.

## Key Components

### AES Encryption (encryption_utils.py)

- Uses the PyCryptodome library for AES implementation.
- Implements `encrypt_chunk()` and `decrypt_chunk()` functions.
- Utilizes AES in CBC (Cipher Block Chaining) mode for enhanced security.

### File Handling (file_utils.py)

- Implements `split_file()` function to read files in chunks.
- Provides `encrypt_file()` and `decrypt_file()` functions to process entire files.

### User Interface (app.py)

- Built with Streamlit for an intuitive web-based interface.
- Allows users to choose between encryption and decryption.
- Handles file uploads and provides download buttons for processed files.

## Security Considerations

- The encryption key must be 32 bytes long (or 64 hexadecimal characters).
- Users are responsible for securely storing and managing their encryption keys.
- The tool processes files locally, enhancing security by avoiding data transmission over networks.

## Future Enhancements

1. Implement key derivation from passwords for easier key management.
2. Add support for more file types.
3. Implement progress bars for large file processing.
4. Add option for customizing encryption parameters (e.g., key size, mode of operation).

## Usage Guidelines

1. Start the application by running `streamlit run app.py`.
2. Use the web interface to upload a file and enter an encryption key.
3. Choose between encryption and decryption.
4. Process the file and download the result.

## Maintenance and Updates

- Regularly update dependencies to ensure security and compatibility.
- Monitor for any reported issues or vulnerabilities in the used libraries.
- Periodically review and update the codebase to follow best practices and improve performance.

This documentation provides an overview of the project structure, functionality, and key components. It serves as a guide for understanding the project's architecture and can be helpful for future maintenance or enhancements.
