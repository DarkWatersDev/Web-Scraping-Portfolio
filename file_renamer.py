import os
import shutil

# 🔹 CONFIGURATION: Customize these values
FOLDER_PATH = "C:/Users/YourUsername/Documents/FilesToOrganize"  # Change this to your folder path
PREFIX = "Project_"  # Prefix to add to all files
SUFFIX = "_Final"  # Suffix to add to all files
SORT_BY_TYPE = True  # Set to False if you don’t want to sort files

# 🔹 Create sorted folders if sorting is enabled
if SORT_BY_TYPE:
    file_types = set([f.split('.')[-1] for f in os.listdir(FOLDER_PATH) if "." in f])
    for file_type in file_types:
        os.makedirs(os.path.join(FOLDER_PATH, file_type), exist_ok=True)

# 🔹 Rename & Sort Files
for filename in os.listdir(FOLDER_PATH):
    if "." in filename:  # Ignore folders
        name, ext = os.path.splitext(filename)
        new_name = f"{PREFIX}{name}{SUFFIX}{ext}"  # Apply prefix & suffix
        old_path = os.path.join(FOLDER_PATH, filename)
        new_path = os.path.join(FOLDER_PATH, new_name)
        os.rename(old_path, new_path)

        # Move file to its respective folder if sorting is enabled
        if SORT_BY_TYPE:
            shutil.move(new_path, os.path.join(FOLDER_PATH, ext[1:], new_name))

print("✅ Files renamed and organized successfully!")
