class SecurityMonitor:
    def __init__(self):
        self.threats = []

    def analyze_logs(self, logs):
        print("Analyzing logs for security threats...")
        for log in logs:
            if "unauthorized access" in log:
                self.threats_logs.append(log)
                print(f"Threat detected: {log}")
    
    def detect_anomalies(self, network_data):
        for entry in network_data:
            if entry.get("traffic") and entry.get("traffic") > 1000:
                message = f" Аномальний трафік з сервера {entry.get('server')}: {entry['traffic']} пакетів"
                self.threats_log.append(entry)
                print(message)

    def notify_threats(self):
        if not self.threats_log:
            print("No security threats detected.")
            return

        print("Security threats detected:") 
        for threat in self.threats_log:
            print(f"- {threat}")
        self.threats_log.clear()

           