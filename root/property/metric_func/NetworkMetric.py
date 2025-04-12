from datetime import datetime
from root.property.metric_func.Metric import Metric

class NetworkMetric(Metric):
    def __init__(self, value, interface, bandwidth, server_name=None, disk_name=None, timestamp=None):
        super().__init__("Network", value)
        self.interface = interface
        self.bandwidth = bandwidth
        self.disk_name = disk_name
        self.server_name = server_name
        self.timestamp = timestamp or datetime.now()

    def get_value(self):
        return f"Network Usage: {self.value}%, Interface: {self.interface}, Bandwidth: {self.bandwidth} MbpsDisk Name: {self.disk_name}, Timestamp: {self.timestamp}"