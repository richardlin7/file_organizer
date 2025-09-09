import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".tar", ".gz"],
}

def organize_files(folder_path):
    """Organize files in the given folder into subfolders by type."""
    folder = Path(folder_path)

    # Create subfolders
    for folder_name in FILE_TYPES:
        (folder / folder_name).mkdir(exist_ok=True)

    # Move files
    moved_files = 0
    for file in folder.iterdir():
        if file.is_file():
            for folder_name, extensions in FILE_TYPES.items():
                if file.suffix.lower() in extensions:
                    shutil.move(str(file), str(folder / folder_name / file.name))
                    moved_files += 1
                    break

    return moved_files

def browse_folder():
    """Open folder picker and organize files."""
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        count = organize_files(folder_selected)
        messagebox.showinfo("Done", f"Organized {count} files in:\n{folder_selected}")

# GUI Setup
root = tk.Tk()
root.title("Python File Organizer")
root.geometry("400x200")

label = tk.Label(root, text="Select a folder to organize:", font=("Arial", 12))
label.pack(pady=20)

browse_button = tk.Button(root, text="Browse Folder", command=browse_folder, font=("Arial", 12))
browse_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=root.quit, font=("Arial", 12))
quit_button.pack(pady=10)

root.mainloop()