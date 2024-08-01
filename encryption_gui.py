import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import font
from cryptography.fernet import Fernet

# Load the key
def load_key():
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        print("Error: 'secret.key' file not found.")
        messagebox.showerror("Error", "Key file not found. Please generate a key.")
        exit()

key = load_key()
fernet = Fernet(key)

# Function to handle encryption
def encrypt_text():
    plaintext = entry_text.get("1.0", tk.END).strip().encode()
    try:
        encrypted_text = fernet.encrypt(plaintext).decode()
        entry_result.delete("1.0", tk.END)
        entry_result.insert(tk.END, encrypted_text)
    except Exception as e:
        print(f"Encryption Exception: {e}")  # Print the error to the console
        messagebox.showerror("Error", f"Encryption failed: {e}")

# Function to handle decryption
def decrypt_text():
    encrypted_text = entry_text.get("1.0", tk.END).strip().encode()
    try:
        decrypted_text = fernet.decrypt(encrypted_text).decode()
        entry_result.delete("1.0", tk.END)
        entry_result.insert(tk.END, decrypted_text)
    except Exception as e:
        print(f"Decryption Exception: {e}")  # Print the error to the console
        messagebox.showerror("Error", f"Decryption failed: {e}")

# Function to copy text to clipboard
def copy_to_clipboard():
    text = entry_result.get("1.0", tk.END).strip()
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(text)  # Append the text to the clipboard
    messagebox.showinfo("Info", "Text copied to clipboard!")

# Button hover effect
def on_enter(e):
    e.widget['background'] = '#0056b3'  # Darker blue
    e.widget['foreground'] = '#000000'  # Black text

def on_leave(e):
    e.widget['background'] = '#007bff'  # Original blue
    e.widget['foreground'] = '#000000'  # Black text

# Create the main window
root = tk.Tk()
root.title("Encryption/Decryption Tool")
root.geometry("600x500")  # Set a larger size for the window
root.configure(bg='#343a40')  # Dark grey background color

# Define custom fonts and colors
header_font = font.Font(family="Arial", size=14, weight="bold")
button_font = font.Font(family="Arial", size=12, weight="bold")
bg_color = '#495057'  # Lighter grey for frames
button_color = '#007bff'  # Blue button color
text_color = '#f8f9fa'  # Light grey text color
button_text_color = '#000000'  # Black text color

# Create and place widgets in frames
frame_input = tk.Frame(root, padx=20, pady=20, bg=bg_color)
frame_input.pack(fill=tk.X)

frame_buttons = tk.Frame(root, padx=20, pady=10, bg=bg_color)
frame_buttons.pack()

frame_result = tk.Frame(root, padx=20, pady=20, bg=bg_color)
frame_result.pack(fill=tk.BOTH, expand=True)

tk.Label(frame_input, text="Enter Text (Plain or Encrypted):", font=header_font, bg=bg_color, fg=text_color).pack(anchor='w')
entry_text = scrolledtext.ScrolledText(frame_input, height=6, width=70, wrap=tk.WORD, font=("Arial", 12), bg='#6c757d', fg=text_color)
entry_text.pack(padx=5, pady=5)

# Create buttons with hover effects
button_encrypt = tk.Button(frame_buttons, text="Encrypt", command=encrypt_text, font=button_font, bg=button_color, fg=button_text_color, padx=10, pady=5, relief=tk.RAISED, bd=2)
button_encrypt.pack(side=tk.LEFT, padx=10)
button_encrypt.bind("<Enter>", on_enter)
button_encrypt.bind("<Leave>", on_leave)

button_decrypt = tk.Button(frame_buttons, text="Decrypt", command=decrypt_text, font=button_font, bg=button_color, fg=button_text_color, padx=10, pady=5, relief=tk.RAISED, bd=2)
button_decrypt.pack(side=tk.LEFT, padx=10)
button_decrypt.bind("<Enter>", on_enter)
button_decrypt.bind("<Leave>", on_leave)

button_copy = tk.Button(frame_buttons, text="Copy", command=copy_to_clipboard, font=button_font, bg=button_color, fg=button_text_color, padx=10, pady=5, relief=tk.RAISED, bd=2)
button_copy.pack(side=tk.LEFT, padx=10)
button_copy.bind("<Enter>", on_enter)
button_copy.bind("<Leave>", on_leave)

tk.Label(frame_result, text="Result:", font=header_font, bg=bg_color, fg=text_color).pack(anchor='w')
entry_result = scrolledtext.ScrolledText(frame_result, height=12, width=70, wrap=tk.WORD, font=("Arial", 12), bg='#6c757d', fg=text_color)
entry_result.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()
