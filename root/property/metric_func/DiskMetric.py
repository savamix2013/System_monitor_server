from datetime import datetime
from root.property.metric_func.Metric import Metric

class DiskMetric(Metric):
    def __init__(self, value, disk_name, total_space, server_name=None, timestamp=None):
        super().__init__("Disk", value)
        self.value = value
        self.disk_name = disk_name
        self.total_space = total_space
        self.server_name = server_name
        self.timestamp = timestamp or datetime.now()

    def get_value(self):
        return f"Disk Usage: {self.value}%, Disk Name: {self.disk_name}, Total Space: {self.total_space} GB, Timestamp: {self.timestamp}"