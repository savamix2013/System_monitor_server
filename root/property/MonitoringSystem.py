from Server import Server
from DataCollector import DataCollector
from DataStorage import DataStorage
from AlertManager import AlertManager
from AutoScaler import AutoScaler
from SecurityMonitor import SecurityMonitor
from CloudIntegration import CloudIntegration
import time

class MonitoringSystem:
    def __init__(self):
        self.servers = []
        self.data_collector = DataCollector([], interval = 10)
        self.data_storage = DataStorage(storage_type="In-Memory", connection_settings={})
        self.alert_manager = AlertManager(alert_rules={
            "CPU > 80": "Critical",
            "Memory < 20": "Warning"
        })
        self.auto_scaler = AutoScaler()
        self.security_monitor = SecurityMonitor()
        self.cloud_integration = CloudIntegration()

    def add_server(self, server: Server):
        self.servers.append(server)
        self.data_collector.add_server(server)
        print(f"Server {server.name} added to monitoring system.")

    def configure_monitoring(self, interval):
        self.data_collector.interval = interval
        print(f"Monitoring interval set to {interval} seconds.")

    def generate_report(self):
        print("Generating report...")
        data = self.data_storage.get_data()
        if not data:
            print("No data available for report generation.")
            return
    
        print(f"🔍 Всього записів: {len(data)}")
        for entry in data:
            print(f"- Сервер: {entry.get('server')}, CPU: {entry.get('cpu')}%, Memory: {entry.get('memory')}%")

    def run_monitoring_cycle(self):
        print("Starting monitoring cycle...")
        collected_data = self.data_collector.collect_data()
        for metric in collected_data:
            self.data_storage.save_data(metric)

        self.alert_manager.check_alert_conditions(collected_data)
        self.alert_manager.send_alerts()

        recommendations = self.auto_scaler.analyze_load(collected_data)
        self.auto_scaler.optimize_resources(self.servers, recommendations)

    
        sample_logs = [
            "User admin failed login",
            "Unauthorized access attempt from IP 192.168.1.100",
            "Normal operation log"
        ]

        self.security_monitor.analyze_logs(sample_logs)

        network_samples = [
            {"server": "Server-A", "traffic": 1200},
            {"server": "Server-B", "traffic": 400}
        ]
        self.security_monitor.detect_anomalies(network_samples)

        self.security_monitor.notify_threats()

    def discover_and_add_cloud_servers(self, provider_name):
        cloud_servers = self.cloud_integration.discover_servers(provider_name)
        for s in cloud_servers:
            server = Server(
                server_id=s["name"],
                name=s["name"],
                IP_address=s["IP_address"],
                server_type=s["Cloud"],
                operating_system=s["Linux"],
            )
            self.add_server(server)

    def start_realtime_monitoring(self, duration_seconds=60, interval_seconds=5):
        print(f"Starting real-time monitoring for {duration_seconds} seconds...")
        start_time = time.time()

        while time.time() - start_time < duration_seconds:
            print(f"\n Цикл моніторингу: {time.strftime('%H:%M:%S')}")

            collected_data = self.data_collector.collect_data()

            for metric in collected_data:
                self.data_storage.save_data(metric)

            self.alert_manager.check_alert_conditions(collected_data)
            self.alert_manager.send_alerts()

            recomendations = self.auto_scaler.analyze_load(collected_data)
            self.auto_scaler.optimize_resources(self.servers, recomendations)

            self.security_monitor.detect_anomalies(collected_data)
            self.security_monitor.notify_threats()

            time.sleep(interval_seconds)

        print("Real-time monitoring completed.")

        