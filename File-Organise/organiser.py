from pathlib import Path
import shutil
import sys

cat = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".webm"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Installers": [".exe", ".msi", ".dmg", ".deb", ".pkg"],
    "Code": [".py", ".html", ".css", ".js", ".json", ".cpp"]
}

"""
so in this program we'll organise given folders inside the pc
"""

name=input("Enter Exact Path Of The Folder You Need To Organise: ")

path=Path(name)
if not path.exists():
    sys.exit("Path Does Not Exits")
if path.is_file():
    sys.exit("Path Redirects to a File Not Folder")

folder=path
for i in folder.iterdir():
    if not i.is_file():
        pass
    else:
        for name,suffix in cat.items():
            if i.suffix.lower() in suffix:
                dest=folder/name
                dest.mkdir(exist_ok=True)
                shutil.move(i, dest)
                break
        

