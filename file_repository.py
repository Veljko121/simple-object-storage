from config import FILES_DIR
from flask import send_from_directory
import os

class FileRepository:

    def __init__(self):
        self.files_dir = os.path.expanduser(FILES_DIR)
        if not os.path.exists(self.files_dir):
            os.makedirs(self.files_dir)

    def get(self, filename: str):
        return send_from_directory(self.files_dir, filename)
    
    def save(self, file, path):
        if path is None:
            path = file.filename
        file_path = os.path.join(self.files_dir, path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        file.save(file_path)