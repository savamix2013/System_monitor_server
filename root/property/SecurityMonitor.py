class SecurityMonitor:
    def __init__(self):
        self.threats = []

    def analyze_logs(self, entry):
        print("Analyzing logs for security threats...")
        for log in entry:
            if "unauthorized access" in log:
                self.threats.append(entry)
                print(f"Threat detected: {log}")
    
    def detect_anomalies(self, network_data):
        for entry in network_data:
            if entry.get("traffic") and entry.get("traffic") > 1000:
                message = f" Аномальний трафік з сервера {entry.get('server')}: {entry['traffic']} пакетів"
                self.threats.append(message)
                print(message)

    def notify_threats(self):
        if not self.threats:
            print("No security threats detected.")
            return

        print("Security threats detected:") 
        for threat in self.threats:
            print(f"- {threat}")
        self.threats.clear()
