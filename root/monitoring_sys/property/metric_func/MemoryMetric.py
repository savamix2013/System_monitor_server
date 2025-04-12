from datetime import datetime
from root.monitoring_sys.property.metric_func.Metric import Metric

class MemoryMetric(Metric):
    def __init__(self, value, server_name):
        super().__init__("Memory", value)
        self.server = server_name
        self.timestamp = datetime.now()

    def get_value(self):
        return f"Server: {self.server} | Memory Usage: {self.value}%, Timestamp: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
