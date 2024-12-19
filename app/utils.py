import os
from pathlib import Path


class Paths:
    parent_dir = Path(os.getcwd())

    def create_image_directory(self, name):
        file_path = self.parent_dir / Path(name)
        if not file_path.exists():
            Path.mkdir(self.parent_dir / Path(name))
        return file_path

    @staticmethod
    def model_save_directory(name) -> Path:
        file_path = Paths.parent_dir / name.upper()
        if not file_path.exists():
            Path.mkdir(file_path)
        return file_path

    def create_directory_in_parents(self, dir):
        folder_path = self.parent_dir / dir
        if not folder_path.exists():
            Path.mkdir(folder_path)
        return folder_path
