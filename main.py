from root.property.MonitoringSystem import MonitoringSystem
from root.property.Server import Server

def main():
    print("Запуск системи моніторингу серверів...")

    # Ініціалізація системи
    system = MonitoringSystem()

    # Створення та додавання серверів
    server1 = Server(server_ID=1, name="Server-A", IP_address="192.168.1.10", server_type="web", operating_system="Linux")
    server2 = Server(server_ID=2, name="Server-B", IP_address="192.168.1.11", server_type="db", operating_system="Windows")
    system.add_server(server1)
    system.add_server(server2)

    # Налаштування моніторингу
    system.configure_monitoring(interval=10)

    # Симуляція одного циклу моніторингу
    system.run_monitoring_cycle()

    # Генерація звіту
    system.generate_report(system.data_collector.collect_data())

    # Аналіз безпеки
    sample_logs = [
        "User admin failed login",
        "Unauthorized access attempt from IP 192.168.1.100",
        "Normal operation log"
    ]
    network_samples = [
        {"server": "Server-A", "traffic": 1200},
        {"server": "Server-B", "traffic": 400}
    ]
    system.security_monitor.analyze_logs(sample_logs)
    system.security_monitor.detect_anomalies(network_samples)
    system.security_monitor.notify_threats()

    # Візуалізація даних (за потреби окремий модуль)
    # system.visualizer.display_dashboard()

if __name__ == "__main__":
    main()
