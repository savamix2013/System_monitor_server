import time
from root.monitoring_sys.property.Server import Server
from root.monitoring_sys.property.AutoScaler import AutoScaler
from root.monitoring_sys.property.DataStorage import DataStorage
from root.monitoring_sys.property.AlertManager import AlertManager
from root.monitoring_sys.property.metric_func.CPUMetric import CPUMetric
from root.monitoring_sys.property.SecurityMonitor import SecurityMonitor
from root.monitoring_sys.property.CloudIntegration import CloudIntegration
from root.monitoring_sys.property.TicketIntegration import TicketIntegration
from root.monitoring_sys.property.metric_func.MemoryMetric import MemoryMetric

class MonitoringSystem:
    def __init__(self):
        self.servers = []
        self.data_storage = DataStorage(storage_type="In-Memory", connection_settings={})
        self.alert_manager = AlertManager(alert_rules={
            "CPU > 80": "Critical",
            "Memory < 20": "Warning"
        })
        self.auto_scaler = AutoScaler()
        self.security_monitor = SecurityMonitor()
        self.cloud_integration = CloudIntegration()
        self.configurations = {
            "database": {"interval": 5, "alerts": {"CPU > 70": "Critical"}},
            "web": {"interval": 10, "alerts": {"Memory < 30": "Warning"}},
            "file": {"interval": 15, "alerts": {"Disk > 90": "Critical"}}
        }
        self.ticket_integration = TicketIntegration(system_type="Jira", api_url="https://jira.example.com", auth_token="your_token", project_key="PROJ")
        self.ticket_integration.create_ticket(  # Исправлено: ticket_integration вместо ticket_system
            issue_title="Server Down",
            issue_description="The server is not responding.",
            severity="Critical"
        )

    def add_server(self, server: Server):
        self.servers.append(server)
        self.data_collector.add_server(server)
        print(f"Server {server.name} added to monitoring system.")

        config = self.configurations.get(server.server_type, {})
        if config:
            self.data_collector.set_interval(server.server_type, config["interval"])
            self.alert_manager.alert_rules.update(config["alerts"])
            print(f"Configuration for {server.server_type} server applied.")
        else:
            print(f"No specific configuration found for {server.server_type} server.")
        print(f"Server {server.name} with IP {server.IP_address} added to monitoring system.")

    def configure_monitoring(self, interval):
        self.data_collector.interval = interval
        print(f"Monitoring interval set to {interval} seconds.")

    def generate_report(self, metrics):
        print("Звіт по серверах:")
        for entry in metrics:
            if isinstance(entry, CPUMetric):
                print(f"- Сервер: {entry.server}, CPU: {entry.value}%, Cores: {entry.cores}")
            elif isinstance(entry, MemoryMetric):
                print(f"- Сервер: {entry.server}, Memory: {entry.value}%")
        else:
            print("Не знайдено відповідних даних для звіту.")

    def run_monitoring_cycle(self):
        print("Starting monitoring cycle...")
        collected_data = self.data_collector.collect_data()
        for metric in collected_data:
            self.data_storage.save_data(metric)

        self.alert_manager.check_alert_conditions(collected_data)
        self.alert_manager.send_alerts()

        recommendations = self.auto_scaler.analiz_load(collected_data)
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

            recommendations = self.auto_scaler.analyze_load(collected_data)
            self.auto_scaler.optimize_resources(self.servers, recommendations)

            self.security_monitor.detect_anomalies(collected_data)
            self.security_monitor.notify_threats()

            time.sleep(interval_seconds)

        print("Real-time monitoring completed.")