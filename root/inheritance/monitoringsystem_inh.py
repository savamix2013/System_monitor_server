from root.property.Server import Server
from root.property.MonitoringSystem import MonitoringSystem

system = MonitoringSystem()

server1 = Server(1, "Server-1", "192.168.0.1", "web", "Linux")
server2 = Server(2, "Server-2", "192.168.0.2", "db", "Windows")

system.add_server(server1)
system.add_server(server2)
system.configure_monitoring(5)
system.run_monitoring_cycle()
system.generate_report()

monitor = MonitoringSystem()
monitor.add_server(Server("s1", "MainServer", "192.168.0.10", "Physical", "Linux"))
monitor.discover_and_add_cloud_servers("AWS")
monitor.start_realtime_monitoring(duration_seconds=30, interval_seconds=5)

