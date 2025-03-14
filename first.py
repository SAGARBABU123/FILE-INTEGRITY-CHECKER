import hashlib
import tkinter as tk
from tkinter import messagebox

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found. Please check the path and try again.")
        return None

def get_file_hash():
    file_path = entry.get()
    hash_value = calculate_hash(file_path)
    if hash_value:
        messagebox.showinfo("SHA-256 Hash", f"Hash:\n{hash_value}")

# GUI setup
root = tk.Tk()
root.title("File Integrity Checker")

label = tk.Label(root, text="Enter the file path:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

button = tk.Button(root, text="Generate Hash", command=get_file_hash)
button.pack()

root.mainloop()
# C:\Users\Sagar Babu\OneDrive\Desktop\cotech.txt\first.py 