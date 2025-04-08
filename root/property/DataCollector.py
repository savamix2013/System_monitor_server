import time
from threading import Thread
from inheritance.CPUMetric import CPUMetric
from inheritance.MemoryMetric import MemoryMetric
from inheritance.DiskMetric import DiskMetric
from inheritance.NetworkMetric import NetworkMetric
import random

class DataCollector:
    def __init__(self, servers, collection_interval):
        self.servers = servers
        self.collection_interval = collection_interval
        self.collecting = False
        self.collected_data = []

    def start_collection(self):
        if not self.collecting:
            self.collecting = True
            self.collected_data = []
            print("Starting data collection...")
            self.collection_thread = Thread(target=self.collect_data)
            self.collection_thread.start()
        else:
            print("Data collection is already running.")

    def stop_collection(self):
        if self.collecting:
            self.collecting = False
            self.collection_thread.join()
            print("Data collection stopped.")
        else:
            print("Data collection is not running.")

    def collect_data(self):
        while self.collecting:
            for server in self.servers:
                data = self.get_server_data(server)
                self.collected_data.append(data)
                print(f"Collected data from {server}: {data}")
            time.sleep(self.collection_interval)

    def process_data(self):
        if not self.collected_data:
            print("No data to process.")
        else:
            print("Processing collected data...")
            # Placeholder for data processing logic
            for data in self.collected_data:
                print(f"Processing data: {data}")
            self.collected_data.clear()
            print("Data processing complete.")

    def add_server(self, server):
        self.servers.append(server)

    def collect_data(self):
        metrics = []
        timestamp = time.time()

        for server in self.servers:
            cpu = random.randint(0, 100)
            mem = random.randint(0, 100)
            disk = random.randint(0, 100)
            net = random.randint(0, 2000)

            metrics.append(CPUMetric(cpu, timestamp, server.name))
            metrics.append(MemoryMetric(mem, timestamp, server.name))
            metrics.append(DiskMetric(disk, timestamp, server.name))
            metrics.append(NetworkMetric(net, timestamp, server.name))

        print(f"✅ Зібрано {len(metrics)} метрик для {len(self.servers)} сервер(ів).")
        return metrics


