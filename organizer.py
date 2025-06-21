import os
import shutil
from datetime import datetime


# STEP 1: Define the folder to organize
folder_to_organize = input("Enter folder path to organize (or press Enter to use Downloads): ").strip()

# Use default Downloads if no input
if not folder_to_organize:
    folder_to_organize = os.path.join(os.path.expanduser("~"), "Downloads")

print(f"Organizing folder: {folder_to_organize}")
log_file = os.path.join(folder_to_organize, "organizer_log.txt")
with open(log_file, "a") as log:
    log.write(f"\n=== Run on {datetime.now()} ===\n")


# STEP 2: Create a dictionary to map file types
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Spreadsheets': ['.xls', '.xlsx', '.csv'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Archives': ['.zip', '.rar', '.7z'],
    'Code': ['.py', '.cpp', '.js', '.html'],
    'Others': []
}

# STEP 3: Create destination folders if needed and move files
for filename in os.listdir(folder_to_organize):
    file_path = os.path.join(folder_to_organize, filename)

    # Skip if it's a folder
    if os.path.isdir(file_path):
        continue

    # Get the file extension
    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    # Find the category
    moved = False
    for folder_name, extensions in file_types.items():
        if ext in extensions:
            destination_folder = os.path.join(folder_to_organize, folder_name)
            os.makedirs(destination_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(destination_folder, filename))

            
            
            moved = True
            break

    # If extension doesn't match any category, move to "Others"
    if not moved:
        destination_folder = os.path.join(folder_to_organize, 'Others')
        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(destination_folder, filename))

           # ✅ Logging here
        with open(log_file, "a") as log:
            log.write(f"Moved: {filename} -> {destination_folder}\n")


print("✅ Done! Files have been organized.")
