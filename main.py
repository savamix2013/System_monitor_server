import os
from root.property.Server import Server
from root.property.DataStorage import DataStorage
from root.gra_generation.widget import create_widgets
from root.gra_generation.data_loader import DataLoader

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
    main()


def data_visualisation():
    os.system('cls')
    print("Візуалізація даних...\n")
    
    data_loader = DataLoader("root/data/data_history.json")
    data_loader.load_from_file()

    create_widgets(data_loader.data_store)

    input("Натисніть Enter, щоб повернутися в меню.")
    main()

def main():
    os.system('cls')
    print("МЕНЮ СИСТЕМИ МОНІТОРИНГУ СЕРВЕРІВ:\n")
    print("1 - Провести моніторинг серверів")
    print("2 - Візуалізація даних")
    print("3 - Вийти з програми")

    while True:
        choice = input("Ваш вибір: ")
        if choice == "1":
            basic_functionality()
        elif choice == "2":
            data_visualisation()
        elif choice == "3":
            print("Вихід з програми.")
            exit()
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()