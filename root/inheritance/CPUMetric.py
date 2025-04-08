from property.Metric import Metric
from datetime import datetime

class CPUMetric(Metric):
    def __init__(self, value, cores):
        super().__init__("CPU", value)
        self.cores = cores

    def get_value(self):
        return f"CPU Usage: {self.value}%, Cores: {self.cores}"
    
    def set_value(self, value):
        self.value = value
        self.timestamp = datetime.now()

    