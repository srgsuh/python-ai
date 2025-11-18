import os
import cv2
from os.path import join

def empty_folder(folder: str) -> None:
    """Recursively remove all files from the specified folder and its subdirectories."""
    for dirpath, _, filenames in os.walk(folder):
            for filename in filenames:
                os.remove(join(dirpath, filename))

def empty_folders(*folders: str) -> None:
    """Recursively remove all files from the specified folders and their subdirectories."""
    for folder in folders:
        empty_folder(folder)

def write_text(file_path: str, text: str) -> None:
    with open(file_path, 'w') as f:
        f.write(text)

def write_image(file_path: str, img: cv2.typing.MatLike) -> None:
    cv2.imwrite(file_path, img)