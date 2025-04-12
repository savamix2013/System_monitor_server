from datetime import datetime
from root.monitoring_sys.property.Alert import Alert
from root.monitoring_sys.property.metric_func.CPUMetric import CPUMetric
from root.monitoring_sys.property.metric_func.MemoryMetric import MemoryMetric

class AlertManager:
    def __init__(self, alert_rules: dict):
        self.alert_rules = alert_rules
        self.active_alerts = []

    def check_alerts(self, metrics):
        for metric in metrics:
            for rule, level in self.alert_rules.items():
                if self._evaluate_rule(rule, metric):
                    message = f"Перевищено поріг для {metric.type}: {metric.value}"
                    self.create_alert(level, message)

    def _evaluate_rule(self, rule, metric):
        try:
            metric_type, operator, threshold = rule.split()
            if metric.type != metric_type:
                return False
            
            threshold = float(threshold)
            if operator == ">" and metric.value > threshold:
                return True
            if operator == "<" and metric.value < threshold:
                return True
            if operator == "==" and metric.value == threshold:
                return True
        except Exception as e:
            print(f"Error evaluating rule: {e}")
            return False

    def create_alert(self, message, timestamp=None, metric_type="Unknown", warning_threshold=70, critical_threshold=90, urgent_threshold=95, recommendation_threshold=50):
        timestamp = timestamp or datetime.now() 
        
        alert = Alert(severity="Critical", 
                    message=message, 
                    timestamp=timestamp,
                    metric_type=metric_type,
                    warning_threshold=warning_threshold,
                    critical_threshold=critical_threshold,
                    urgent_threshold=urgent_threshold,
                    recommendation_threshold=recommendation_threshold)
        
        self.active_alerts.append(alert)
        print(f"Створено сповіщення: {message}")

    def send_alerts(self):
        print("Відправка сповіщень:")
        for alert in self.active_alerts:
            alert.send_alert()
        print("Усі сповіщення відправлено.")
        self.active_alerts.clear()

    def check_alert_conditions(self, metrics):
        for metric in metrics:
            if isinstance(metric, CPUMetric) and metric.value > 80:
                self.create_alert(
                    f"High CPU: {metric.value}%", 
                    metric.timestamp,
                    metric_type="CPU", 
                    warning_threshold=75,
                    critical_threshold=85,
                    urgent_threshold=90,
                    recommendation_threshold=70
                )

            elif isinstance(metric, MemoryMetric) and metric.value < 20:
                self.create_alert(
                    f"Low Memory: {metric.value}%", 
                    metric.timestamp,
                    metric_type="Memory",
                    warning_threshold=30,
                    critical_threshold=20,
                    urgent_threshold=10,
                    recommendation_threshold=40
                )
