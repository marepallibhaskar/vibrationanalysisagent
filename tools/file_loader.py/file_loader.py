import pandas as pd
import os

class FileLoader:
    def __init__(self):
        pass

    def run(self, file_path):
        ext = os.path.splitext(file_path)[-1].lower()
        if ext == ".csv":
            return pd.read_csv(file_path)
        elif ext in [".xls", ".xlsx"]:
            return pd.read_excel(file_path)
        elif ext == ".json":
            return pd.read_json(file_path)
        else:
            raise ValueError(f"Unsupported format: {ext}")
