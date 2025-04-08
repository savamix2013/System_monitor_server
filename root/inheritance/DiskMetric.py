from property.Metric import Metric
from datetime import datetime

class Diskmetric(Metric):
    def __init__(self, value, disk_name, total_space):
        super().__init__("Disk", value)
        self.disk_name = disk_name
        self.total_space = total_space

    def get_value(self):
        return f"Disk Usage: {self.value}%, Disk Name: {self.disk_name}, Total Space: {self.total_space} GB"
    
    def set_value(self, value):
        self.value = value
        self.timestamp = datetime.now()
