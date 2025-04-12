class Alert:
    def __init__(self, severity, message, timestamp, metric_type, warning_threshold, critical_threshold, urgent_threshold, recommendation_threshold):
        self.severity = severity
        self.message = message
        self.timestamp = timestamp
        self.metric_type = metric_type
        self.warning_threshold = warning_threshold
        self.critical_threshold = critical_threshold
        self.urgent_threshold = urgent_threshold
        self.recommendation_threshold = recommendation_threshold


    def create_alert(self):
        if self.metric_type == "CPU" and self.warning_threshold < 80:
            return "Warning"
        if self.metric_type == "Memory" and self.critical_threshold < 20:
            return "Critical"
        return "Unknown"

    def send_alert(self):
        print(f"Sending alert for {self.metric_type} with message: {self.message}, severity: {self.severity}")
