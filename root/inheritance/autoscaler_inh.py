from root.property.Server import Server
from root.property.MonitoringSystem import MonitoringSystem

system = MonitoringSystem()

server1 = Server(1, "Server-A", "10.0.0.1", "web", "Linux")
server2 = Server(2, "Server-B", "10.0.0.2", "db", "Linux")

system.add_server(server1)
system.add_server(server2)

system.run_monitoring_cycle()
