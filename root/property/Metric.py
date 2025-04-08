from abc import ABC, abstractmethod
from datetime import datetime

class Metric(ABC):
    def __init__(self, metric_type, value):
        self.metric_type = metric_type
        self.value = value
        self.timestamp = datetime.now()

    @abstractmethod
    def get_value(self):
        """Метод для отримання значення метрики"""
        pass

    @abstractmethod
    def set_value(self, value):
        """Метод для встановлення значення метрики"""
        pass

