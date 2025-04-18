from root.monitoring_sys.property.metric_func.CPUMetric import CPUMetric
from root.monitoring_sys.property.metric_func.DiskMetric import DiskMetric
from root.monitoring_sys.property.metric_func.MemoryMetric import MemoryMetric
from root.monitoring_sys.property.metric_func.NetworkMetric import NetworkMetric

cpu_metric = CPUMetric(35, 8)
print(cpu_metric.get_value())

memory_metric = MemoryMetric(70, 16)
print(memory_metric.get_value())

disk_metric = DiskMetric(50, "C", 500)
print(disk_metric.get_value())

network_metric = NetworkMetric(100, "eth0", 1000)
print(network_metric.get_value())

