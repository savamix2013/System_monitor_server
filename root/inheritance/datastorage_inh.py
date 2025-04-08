from property.DataStorage import DataStorage

storage = DataStorage(storage_type="In-Memory", connection_settings={"host": "localhost", "port": 5432})

storage.save_data({"server": "Server 1", "cpu": 45})
storage.save_data({"server": "Server 2", "cpu": 67})
storage.save_data({"server": "Server 1", "cpu": 52})

all_data = storage.get_data()
print(all_data)

storage.clear_old_data(limit=1)
print(all_data)