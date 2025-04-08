from root.property.Widget import Widget
from root.property.Dashboard import Dashboard
from root.property.MonitoringSystem import MonitoringSystem
from root.property.Server import Server

cpu_data = [
    {"timestamp": 1, "value": 45},
    {"timestamp": 2, "value": 56},
    {"timestamp": 3, "value": 73},
]

cpu_widget = Widget("CPU Usage", data_source=cpu_data)
dashboard = Dashboard("Main System Dashboard")
dashboard.add_widget(cpu_widget)

dashboard.refresh_all()  # Показує графік


# filtered = storage.filter_data(server_name="Server-A", metric_type="CPU")
# print(filtered)



