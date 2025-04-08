import json

class DataStorage:
    def __init__(self, storage_type, connection_settings):
        self.storage_type = storage_type
        self.connection_settings = connection_settings
        self.data_store = []
        print(f"DataStorage initialized with type: {self.storage_type}")

    def save_data(self, data):
        self.data_store.append(data)
        print(f"Data saved: {data}")

    def get_data(self):
        print("Data retrieved:")
        return self.data_store

    def clear_old_data(self, limit = 10):
        if len(self.data_store) > limit:
            old_count = len(self.data_store) - limit
            self.data_store = self.data_store[-limit:]
            print(f"Очищено {old_count} старих записів.")
        else:
            print("Даних для очищення немає.")

    def save_to_file(self, filename="metrics_history.json"):
        with open(filename, 'w') as file:
            json.dump(self.data_store, file)
        print(f"Дані збережено у файл {filename}")

    def load_from_file(self, filename="metrics_history.json"):
        try:
            with open(filename, "r") as f:
                self.data_history = json.load(f)
        except FileNotFoundError:
            self.data_history = []

    def filter_data(self, server_name=None, metric_type=None):
        result = self.data_store
        if server_name:
            result = [m for m in result if m.get("server") == server_name]
        if metric_type:
            result = [m for m in result if m.get("type") == metric_type]
        return result
    