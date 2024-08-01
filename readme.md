# Encryption/Decryption Tool

This is a Python-based encryption and decryption tool with a graphical user interface (GUI). The tool allows users to encrypt and decrypt text files using a symmetric key encryption algorithm. The GUI is built with `tkinter` and supports basic file operations.

## Features

- Generate encryption keys
- Encrypt and decrypt text files
- GUI with buttons for copy and reset operations

## Requirements

- Python 3.x
- PyCryptodome
- tkinter (usually included with Python)
- PyInstaller (for creating executables)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
2. Create and activate a virtual environment:
    ```
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
3. Install Dependencies:
    ```
    pip install -r requirements.txt
4. Generate a Key:
    Run the keygen.py script to generate and save a new encryption key:
    ```
    python keygen.py
5. Run the GUI:
    ```
    python encryption_gui.py

## Usage
### Key Generation
+ Run keygen.py to generate a new key. The key will be saved as secret.key in the project directory.
+ Encrypting and Decrypting Files
### Use the GUI to:
- Encrypt: Enter the text to be encrypted, and click the "Encrypt" button. The encrypted text will be displayed.
- Decrypt: Enter the encrypted text, and click the "Decrypt" button. The decrypted text will be displayed.
- Copy Functionality :You can copy the encrypted or decrypted text to the clipboard using the "Copy" button in the GUI.