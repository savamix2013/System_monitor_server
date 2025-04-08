from datetime import datetime

class Alert:
    def __init__(self, alter_type, level, severity, message, timestamp):
        self.alert_type = alter_type
        self.severity = severity
        self.message = message
        self.timestamp = datetime.now()
        self.level = level
        self.timestamp = timestamp

    def create_alert(self):
        return {
            "alert_type": self.alert_type,
            "severity": self.severity,
            "message": self.message,
            "timestamp": self.timestamp
        }
    
    def send_alert(self):
        # Placeholder for sending alert logic (e.g., email, SMS, etc.)
        print(f"Sending alert: {self.create_alert()}")

    def send(self):
        print(f"[{self.level}] {self.alert_type} Alert at {self.timestamp}: {self.message}")

        