#  File Organizer – Python Automation Project

This is a Python-based automation script that organizes files in a selected folder by sorting them into categorized subfolders (e.g., Images, Videos, Documents, etc.). It helps keep your directories clean and structured automatically.

---

##Features

- Automatically scans a folder and sorts files into categorized subfolders
- Supports common file types: images, videos, documents, executables, etc.
- Easy to configure and expand with more file types
- Simple graphical interface using `tkinter`
- Packaged as a standalone desktop app with `PyInstaller`

---

## How It Works

1. The user selects a target folder using a file dialog GUI.
2. The script scans that folder (and optionally its subfolders).
3. Based on file extensions, files are moved into categorized folders like:
   - `Images/`
   - `Videos/`
   - `Documents/`
   - `Music/`
   - `Archives/`
   - `Others/`

---

##  Technologies Used

- **Python 3**
- `tkinter` (for GUI)
- `os`, `shutil`, `pathlib` (for file and folder operations)
- `PyInstaller` (for packaging as a desktop app)

---

##  How to Run the Script

### Option 1 – Run from Python directly:
```bash
python organizer_gui.py



