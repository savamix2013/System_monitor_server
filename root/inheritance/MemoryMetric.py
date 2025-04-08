from property.Metric import Metric
from datetime import datetime

def __init__(self, value, total_memory):
    super().__init__("Memory", value)
    self.total_memory = total_memory

def get_value(self):
    return f"Memory Usage: {self.value}%, Total Memory: {self.total_memory} GB"

def set_value(self, value):
    self.value = value
    self.timestamp = datetime.now()