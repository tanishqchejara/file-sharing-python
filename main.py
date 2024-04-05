# Import necessary modules
import tkinter as tk
from tkinter import messagebox
import tkinter.filedialog as fd
import shutil
import os
from cryptography.fernet import Fernet

# Define a global encryption key
encryption_key = None

# Create main application window
app = tk.Tk()
app.title("File Sharing App")

# User credentials
user_credentials = {
    "user1": "password1",
    "user2": "password2"
}


# Generate a secure encryption key
def generate_key():
    return Fernet.generate_key()

# Encrypt file with the given key
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)
    with open(file_path, 'wb') as f:
        f.write(encrypted_data)

# Decrypt file with the given key
def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(file_path, 'wb') as f:
        f.write(decrypted_data)


# Function to handle login button click
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username in user_credentials and user_credentials[username] == password:
        messagebox.showinfo("Login", "Login successful!")
        populate_file_list()
        # Placeholder for further actions after successful login
    else:
        messagebox.showerror("Login Error", "Invalid username or password")

# Function to populate file listbox with available files
def populate_file_list():
    # Clear existing items in the listbox
    file_listbox.delete(0, tk.END)
    # Get list of files in the "uploads" folder
    files = os.listdir("uploads")
    # Add files to the listbox
    for file in files:
        file_listbox.insert(tk.END, file)

# Function to handle file upload button click
def upload():
    # Ask user to select a file for upload
    file_path = fd.askopenfilename()
    if file_path:
        # Placeholder for uploading logic
        # For now, let's just copy the file to a destination folder
        destination_folder = "uploads"
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        shutil.copy(file_path, destination_folder)
        messagebox.showinfo("Upload", "File uploaded successfully!")
        populate_file_list()

# Function to handle file download button click
def download():
    # Placeholder for downloading logic
    # For now, let's just show a message box with the selected file path
    selected_file = file_listbox.get(tk.ACTIVE)
    if selected_file:
        # messagebox.showinfo("Download", f"Selected file: {selected_file}")
        source_path = os.path.join("uploads", selected_file)
        destination_folder = "download"
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        destination_path = os.path.join("download", selected_file)  # Destination folder: "download"
        shutil.copy(source_path, destination_path)
        messagebox.showinfo("Download", f"File '{selected_file}' downloaded successfully to 'download' folder.")
   
# Function to handle file deletion
def delete():
    selected_file = file_listbox.get(tk.ACTIVE)
    if selected_file:
        confirmation = messagebox.askyesno("Delete", f"Are you sure you want to delete {selected_file}?")
        if confirmation:
            file_path = os.path.join("uploads", selected_file)
            os.remove(file_path)
            messagebox.showinfo("Delete", f"{selected_file} has been deleted.")
            populate_file_list()

# Create and place widgets in the window
label_username = tk.Label(app, text="Username:")
label_username.grid(row=0, column=0, padx=5, pady=5)

entry_username = tk.Entry(app)
entry_username.grid(row=0, column=1, padx=5, pady=5)

label_password = tk.Label(app, text="Password:")
label_password.grid(row=1, column=0, padx=5, pady=5)

entry_password = tk.Entry(app, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5)

login_button = tk.Button(app, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

upload_button = tk.Button(app, text="Upload", command=upload)
upload_button.grid(row=3, column=0, padx=5, pady=5, sticky="we")

download_button = tk.Button(app, text="Download", command=download)
download_button.grid(row=3, column=1, padx=5, pady=5, sticky="we")

# Listbox to display uploaded files
file_listbox = tk.Listbox(app)
file_listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# Button to delete selected file
delete_button = tk.Button(app, text="Delete", command=delete)
delete_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Run the application
app.mainloop()
