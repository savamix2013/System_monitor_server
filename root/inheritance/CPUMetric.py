from root.property.Metric import Metric
from datetime import datetime

class CPUMetric(Metric):
    def __init__(self, value, cores, server_name, timestamp=None):
        super().__init__("CPU", value)
        self.cores = cores
        self.server = server_name
        self.timestamp = timestamp or datetime.now()

    def get_value(self):
        return f"Server: {self.server} | CPU Usage: {self.value}%, Cores: {self.cores}, Timestamp: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

    def set_value(self, value):
        self.value = value
        self.timestamp = datetime.now()
