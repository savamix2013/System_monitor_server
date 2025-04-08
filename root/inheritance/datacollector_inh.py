from property.DataCollector import DataCollector
import time


data_collector = DataCollector(servers=["Server1", "Server2"], collection_interval=5)
data_collector.start_collection()

time.sleep(15)  # Simulate some time passing for data collection

data_collector.stop_collection()
data_collector.process_data()

