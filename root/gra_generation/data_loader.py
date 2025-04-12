import json

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data_store = {}

    def load_from_file(self):
        try:
            with open(self.file_path, 'r') as file:
                self.data_store = json.load(file)
                print(f"Дані завантажено з файлу {self.file_path}")
        except Exception as e:
            print(f"Помилка при завантаженні даних з файлу: {e}")
