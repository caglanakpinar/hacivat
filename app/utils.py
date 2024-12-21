import os
from pathlib import Path


class Paths:
    parent_dir = Path(os.getcwd())
    data_path = parent_dir / "data"
    if not data_path.exists():
        data_path.mkdir()

    def remove_files_in_data(self):
        self.data_path.rmdir()
        self.data_path.mkdir()
