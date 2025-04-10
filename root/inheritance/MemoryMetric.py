from root.property.Metric import Metric
from datetime import datetime

class MemoryMetric(Metric):
    def __init__(self, value, server_name, timestamp=None):
        super().__init__("Memory", value)
        self.server = server_name
        self.timestamp = timestamp or datetime.now()

    def get_value(self):
        return f"Server: {self.server} | Memory Usage: {self.value}%, Timestamp: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

    def set_value(self, value):
        self.value = value
        self.timestamp = datetime.now()
