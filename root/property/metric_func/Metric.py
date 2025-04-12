class Metric:
    def __init__(self, metric_type, value):
        self.metric_type = metric_type
        self.value = value

    def get_value(self):
        return self.value