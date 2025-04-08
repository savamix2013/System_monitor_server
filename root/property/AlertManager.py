from datetime import datetime
from Alert import Alert 
from inheritance.CPUMetric import CPUMetric
from inheritance.MemoryMetric import MemoryMetric

class AlertManager:
    def __init__(self, alert_rules: dict):
        self.alert_rules = alert_rules
        self.alerts = []

    def check_alerts(self, metrics):
        for metric in metrics:
            for rule, level in self.alert_rules.items():
                if self._evaluate_rule(rule, metric):
                    message = f"Перевищено поріг для {metric['type']}: {metric['value']}"
                    self.create_alert(level, message)

    def _evaluate_rule(self, rule, metric):
        try:
            metric_type, operator, threshold = rule.split()
            if metric['type'] != metric_type:
                return False
            
            if operator == ">" and metric['value'] > float(threshold):
                return True
            if operator == "<" and metric['value'] < float(threshold):
                return True
            if operator == "==" and metric['value'] >= float(threshold):
                return True
        except Exception as e:
            print(f"Error evaluating rule: {e}")
            return False
        
    def create_alert(self, alert_type, level, message, timestamp):
        timestamp = datetime.now()
        alert = Alert(alert_type="Автоматичне", level=level, message=message, timestamp=timestamp)
        self.active_alerts.append(alert)
        print(f"Створено сповіщення: {message} (Рівень: {level})")

    def send_alerts(self):
        print("Відправка сповіщень:")
        for alert in self.active_alerts:
            alert.send_alert()
        print("Усі сповіщення відправлено.")
        self.active_alerts.clear()

    def check_alert_conditions(self, metrics):
        for metric in metrics:
            if isinstance(metric, CPUMetric) and metric.value > 80:
                self.create_alert("CPU", "Critical", f"High CPU: {metric.value}%", metric.timestamp)

            elif isinstance(metric, MemoryMetric) and metric.value < 20:
                self.create_alert("Memory", "Warning", f"Low Memory: {metric.value}%", metric.timestamp)

    