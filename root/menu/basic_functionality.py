import os
from root.monitoring_sys.property.Server import Server
from root.monitoring_sys.property.DataStorage import DataStorage

def basic_functionality():
    os.system('cls')
    print("Запуск системи моніторингу серверів...")

    server1 = Server(server_ID=1, name="Server-A", IP_address="192.168.1.10", server_type="web", operating_system="Linux")
    server2 = Server(server_ID=2, name="Server-B", IP_address="192.168.1.11", server_type="db", operating_system="Windows")
    
    servers = [server1, server2]

    data_storage = DataStorage("In-Memory", {}, file_path="root/data/data_history.json")

    for server in servers:
        server.generate_metrics()  
        server.display_monitoring()  

        data_storage.save_data(
            server.name,
            server.server_type,
            {
                "usage": server.cpu_metric.value,
                "cores": server.cpu_metric.cores,
                "timestamp": server.cpu_metric.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            },
            {
                "usage": server.memory_metric.value,
                "timestamp": server.memory_metric.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            },
            {
                "usage": server.disk_metric.value,
                "disk_name": server.disk_metric.disk_name,
                "total_space": server.disk_metric.total_space,
                "timestamp": server.disk_metric.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            },
            {
                "usage": server.network_metric.value,
                "interface": server.network_metric.interface,
                "bandwidth": server.network_metric.bandwidth,
                "timestamp": server.network_metric.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            }
        )

    print("Збережені дані:")
    print(data_storage.get_data())

    input("Натисніть Enter, щоб повернутися в меню.")
    from main import main
    main()