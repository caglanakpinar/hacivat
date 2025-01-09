import os
from pathlib import Path
import shutil


class Paths:
    parent_dir = Path(os.getcwd())
    data_path = parent_dir / "data"
    if not data_path.exists():
        data_path.mkdir()

    def remove_files_in_data(self):
        shutil.rmtree(self.data_path)
        self.data_path.mkdir()
