from datetime import datetime

class Alert:
    def __init__(self, alert_type, level, severity, message, timestamp=None):
        self.alert_type = alert_type
        self.level = level
        self.severity = severity
        self.message = message
        self.timestamp = timestamp or datetime.now()

    def create_alert(self, level, message, severity="Critical", timestamp=None):
        # Створюємо новий алерт з переданим severity
        alert = Alert(alert_type="Автоматичне", level=level, severity=severity, message=message, timestamp=timestamp)
        return alert  # Повертаємо створений алерт

    def send_alert(self):
        # Placeholder for sending alert logic (e.g., email, SMS, etc.)
        print(f"Sending alert: {self.create_alert(self.level, self.message, self.severity, self.timestamp)}")

    def send(self):
        print(f"[{self.level}] {self.alert_type} Alert at {self.timestamp}: {self.message}")
