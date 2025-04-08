from inheritance.CPUMetric import CPUMetric

class AutoScaler:
    def __init__(self, cpu_threshold=75, memory_threshold=75):
        self.cpu_threshold = cpu_threshold
        self.memory_threshold = memory_threshold
        
    def analiz_load(self, metrics):
        recomendations = []
        for metric in metrics:
            server_name = metric.get('server_name')
            cpu = metric.get('cpu')
            memory = metric.get('memory')

            if cpu is None or memory is None:
                continue

            if cpu > self.cpu_threshold or memory > self.memory_threshold:
                recomendations.append((server_name, "Upgrade"))
            elif cpu < 30 and memory < 40:
                recomendations.append((server_name, "Downgrade"))
            else:
                recomendations.append((server_name, "OK"))

        cpu_usages = [m.value for m in metrics if isinstance(m, CPUMetric)]
        avg_cpu = sum(cpu_usages) / len(cpu_usages) if cpu_usages else 0
        print(f"Average CPU usage: {avg_cpu:.2f}%")

        if avg_cpu > 80:
            return "scale_up"
        
        elif avg_cpu < 20:
            return "scale_down"
        else:
            return "stable"


    def optimize_resources(self, servers, recomendation):
        for server in servers:
            for name, action in recomendation:
                if action == "Upgrade":
                    server.config = "Upgraded"
                elif action == "Downgrade":
                    server.config = "Downgraded"
                else:
                    print(f"Server {server.name} is OK, no action needed.")
    
    
