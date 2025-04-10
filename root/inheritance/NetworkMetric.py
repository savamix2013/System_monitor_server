from root.property.Metric import Metric
from datetime import datetime

class NetworkMetric(Metric):
    def __init__(self, value, interface, bandwidth):
        super().__init__("Network", value)
        self.interface = interface
        self.bandwidth = bandwidth

    def get_value(self):
        return f"Network Usage: {self.value}%, Interface: {self.interface}, Bandwidth: {self.bandwidth} Mbps"
    
    def set_value(self, new_value):
        self.value = new_value
        self.timestamp = datetime.now()