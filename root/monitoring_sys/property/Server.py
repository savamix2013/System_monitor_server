import random
from datetime import datetime
from root.monitoring_sys.property.metric_func.CPUMetric import CPUMetric
from root.monitoring_sys.property.metric_func.DiskMetric import DiskMetric
from root.monitoring_sys.property.metric_func.MemoryMetric import MemoryMetric
from root.monitoring_sys.property.metric_func.NetworkMetric import NetworkMetric

class Server:
    def __init__(self, server_ID, name, IP_address, server_type, operating_system):
        self.server_ID = server_ID
        self.name = name
        self.IP_address = IP_address
        self.server_type = server_type
        self.operating_system = operating_system
        self.cpu_metric = None
        self.memory_metric = None
        self.disk_metric = None
        self.network_metric = None

    def generate_metrics(self):
        self.cpu_metric = CPUMetric(random.uniform(0, 100), random.randint(1, 16), self.name)
        self.memory_metric = MemoryMetric(random.uniform(0, 100), self.name)
        self.disk_metric = DiskMetric(random.uniform(0, 100), "C", 500)
        self.network_metric = NetworkMetric(random.uniform(0, 100), "eth0", 1000)

    def display_monitoring(self):
        print(f"Моніторинг сервера {self.name} ({self.server_type}):")
        print(self.cpu_metric.get_value())
        print(self.memory_metric.get_value())
        print(self.disk_metric.get_value())
        print(self.network_metric.get_value())
        print("------------------------------")

    def generate_report(self):
        print(f"Сервер {self.name}:")
        print(f"  CPU: {self.cpu_metric.value}%")
        print(f"  Memory: {self.memory_metric.value}%")
        print(f"  Disk: {self.disk_metric.value}%")
        print(f"  Network: {self.network_metric.value}%")
        print("------------------------------")
