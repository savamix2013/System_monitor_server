from root.monitoring_sys.property.metric_func.CPUMetric import CPUMetric
from root.monitoring_sys.property.metric_func.MemoryMetric import MemoryMetric

class AutoScaler:
    def __init__(self, cpu_threshold=75, memory_threshold=75):
        self.cpu_threshold = cpu_threshold
        self.memory_threshold = memory_threshold
        
    def analiz_load(self, metrics):
        recommendations = []
        for metric in metrics:
            if hasattr(metric, 'server'):
                server_name = metric.server
            else:
                continue

            cpu = metric.value if isinstance(metric, CPUMetric) else None
            memory = metric.value if isinstance(metric, MemoryMetric) else None

            if cpu is None and memory is None:
                continue

            if cpu is not None and cpu > self.cpu_threshold:
                recommendations.append((server_name, "Upgrade"))
            elif memory is not None and memory > self.memory_threshold:
                recommendations.append((server_name, "Upgrade"))
            elif cpu is not None and cpu < 30 and memory is not None and memory < 40:
                recommendations.append((server_name, "Downgrade"))
            else:
                recommendations.append((server_name, "OK"))

        cpu_usages = [m.value for m in metrics if isinstance(m, CPUMetric) and m.value is not None]
        avg_cpu = sum(cpu_usages) / len(cpu_usages) if cpu_usages else 0
        print(f"Average CPU usage: {avg_cpu:.2f}%")

        if avg_cpu > 80:
            return "scale_up"
        
        elif avg_cpu < 20:
            return "scale_down"
        else:
            return "stable"

    def optimize_resources(self, servers, recommendations): 
        for server in servers:
            for recommendation in recommendations:
                if len(recommendation) == 2: 
                    name, action = recommendation
                    if action == "Upgrade":
                        server.config = "Upgraded"
                    elif action == "Downgrade":
                        server.config = "Downgraded"
                    else:
                        print(f"Server {server.name} is OK, no action needed.")
                else:
                    print(f"Invalid recommendation format: {recommendation}")