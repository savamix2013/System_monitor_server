import time
from threading import Thread
from root.inheritance.CPUMetric import CPUMetric
from root.inheritance.MemoryMetric import MemoryMetric
from root.inheritance.DiskMetric import DiskMetric
from root.inheritance.NetworkMetric import NetworkMetric
import random

class DataCollector:
    def __init__(self, servers, interval=10):
        self.servers = servers
        self.interval = interval
        self.custom_intervals = {}
        self.collecting = False
        self.collected_data = []

    def set_interval(self, server_type, interval):
        self.custom_intervals[server_type] = interval
        print(f"⏱ Інтервал для серверів типу '{server_type}' встановлено: {interval} секунд.")

    def start_collection(self):
        if not self.collecting:
            self.collecting = True
            print("📊 Запуск збору метрик...")
            self.collection_thread = Thread(target=self._collect_data_loop)
            self.collection_thread.start()
        else:
            print("⚠️ Збір метрик вже виконується.")

    def stop_collection(self):
        if self.collecting:
            self.collecting = False
            self.collection_thread.join()
            print("🛑 Збір метрик зупинено.")
        else:
            print("ℹ️ Збір метрик не активний.")

    def _collect_data_loop(self):
        while self.collecting:
            metrics = self.collect_data()
            self.collected_data.extend(metrics)
            print(f"✅ Зібрано {len(metrics)} метрик.")
            time.sleep(self.interval)

    def collect_data(self):
        if not self.servers:
            print("ℹ️ Немає серверів для моніторингу.")
            return []

        metrics = []
        timestamp = time.time()

        for server in self.servers:
            cpu = random.randint(0, 100)
            mem = random.randint(0, 100)
            disk = random.randint(0, 100)
            net = random.randint(0, 2000)

            # Використовуємо кастомний інтервал, якщо він встановлений
            interval = self.custom_intervals.get(server.server_type, self.interval)
            
            metrics.append(CPUMetric(cpu, timestamp, server.name))
            metrics.append(MemoryMetric(mem, timestamp, server.name))
            metrics.append(DiskMetric(disk, timestamp, server.name))
            metrics.append(NetworkMetric(net, timestamp, server.name))

        return metrics

    def process_data(self):
        if not self.collected_data:
            print("ℹ️ Немає даних для обробки.")
        else:
            print("🔄 Обробка зібраних метрик...")
            for data in self.collected_data:
                print(f"  📌 {data}")
            self.collected_data.clear()
            print("✅ Обробка завершена.")

    def add_server(self, server):
        self.servers.append(server)
        print(f"➕ Сервер {server.name} додано до моніторингу.")

