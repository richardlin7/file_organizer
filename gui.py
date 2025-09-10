import tkinter as tk
from tkinter import filedialog, messagebox
from organizer import organize_files

def browse_folder():
    """Open folder picker and organize files."""
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        count = organize_files(folder_selected)
        messagebox.showinfo("Done", f"Organized {count} files in:\n{folder_selected}")

def run_gui():
    root = tk.Tk()
    root.title("Python File Organizer")
    root.geometry("600x400")

    label = tk.Label(root, text="Select a folder to organize:", font=("System", 12))
    label.pack(pady=20)

    browse_button = tk.Button(root, text="Browse Folder", command=browse_folder, font=("System", 12))
    browse_button.pack(pady=10)

    quit_button = tk.Button(root, text="Quit", command=root.quit, font=("System", 12))
    quit_button.pack(pady=10)

    root.mainloop()