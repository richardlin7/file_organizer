import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            ext = filename.split('.')[-1]
            folder = os.path.join(directory, ext.upper() + '_Files')
            os.makedirs(folder, exist_ok=True)
            shutil.move(os.path.join(directory, filename), os.path.join(folder, filename))

if __name__ == "__main__":
    print("Please input the target directory path where files need to be organized: ")
    path = input().strip()
    target_dir = (path)  # Change to your target directory
    organize_files(target_dir)
    print(f"Files in '{target_dir}' have been organized by file type.")