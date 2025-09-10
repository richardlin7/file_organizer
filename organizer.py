import shutil
from pathlib import Path

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