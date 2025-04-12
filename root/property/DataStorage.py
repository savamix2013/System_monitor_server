import json
from datetime import datetime

class DataStorage:
    def __init__(self, storage_type, connection_settings, file_path="root/data/data_history.json"):
        self.storage_type = storage_type
        self.connection_settings = connection_settings
        self.data_store = {}
        self.file_path = file_path
        print(f"DataStorage initialized with type: {self.storage_type}")

    def save_data(self, server_name, server_type, cpu, memory, disk, network):
        saved_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        server_data = {
            "server_name": server_name,
            "server_type": server_type,
            "metrics": {
                "cpu": {
                    "usage": cpu["usage"],
                    "cores": cpu["cores"],
                    "timestamp": cpu["timestamp"]
                },
                "memory": {
                    "usage": memory["usage"],
                    "timestamp": memory["timestamp"]
                },
                "disk": {
                    "usage": disk["usage"],
                    "disk_name": disk["disk_name"],
                    "total_space": disk["total_space"],
                    "timestamp": disk["timestamp"]
                },
                "network": {
                    "usage": network["usage"],
                    "interface": network["interface"],
                    "bandwidth": network["bandwidth"],
                    "timestamp": network["timestamp"]
                }
            }
        }

        if saved_at not in self.data_store:
            self.data_store[saved_at] = []

        self.data_store[saved_at].append(server_data)
        print(f"Data saved for {server_name} at {saved_at}")
        self._save_to_file()

    def get_data(self):
        print("Data retrieved:")
        return self.data_store

    def _save_to_file(self):
        try:
            try:
                with open(self.file_path, 'r') as file:
                    existing_data = json.load(file)
            except FileNotFoundError:
                existing_data = {}

            existing_data.update(self.data_store)

            with open(self.file_path, 'w') as file:
                json.dump(existing_data, file, indent=4)
                print(f"Дані збережено в файл {self.file_path}")
        except Exception as e:
            print(f"Помилка при збереженні даних у файл: {e}")

    def load_from_file(self):
        try:
            with open(self.file_path, 'r') as file:
                self.data_store = json.load(file)
                print(f"Дані завантажено з файлу {self.file_path}")
        except Exception as e:
            print(f"Помилка при завантаженні даних з файлу: {e}")