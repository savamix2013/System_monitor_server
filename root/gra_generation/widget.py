import pandas as pd
import seaborn as sns
from datetime import datetime
import matplotlib.pyplot as plt

class Widget:
    def __init__(self, widget_type, data_source, display_settings=None):
        self.widget_type = widget_type
        self.data_source = data_source
        self.display_settings = display_settings or {}

    def update_data(self, new_data):
        self.data_source = new_data

    def display(self):
        times = [datetime.strptime(entry['metrics'][self.widget_type.lower()]['timestamp'], "%Y-%m-%d %H:%M:%S") for entry in self.data_source]
        values = [entry['metrics'][self.widget_type.lower()]['usage'] for entry in self.data_source]
        return times, values

def create_widgets(data):

    time_stamps = []
    cpu_values = []
    memory_values = []
    disk_values = []
    network_values = []
    server_names = []
    
    colors = {
        "CPU": "green",
        "Memory": "blue",
        "Disk": "red",
        "Network": "purple"
    }

    for timestamp, servers in data.items():
        for server in servers:
            server_name = server['server_name']
            server_names.append(server_name)

            cpu_widget = Widget(widget_type="CPU", data_source=[server])
            times, values = cpu_widget.display()
            time_stamps.append(times[0])
            cpu_values.append(values[0])

            memory_widget = Widget(widget_type="Memory", data_source=[server])
            times, values = memory_widget.display()
            memory_values.append(values[0])

            disk_widget = Widget(widget_type="Disk", data_source=[server])
            times, values = disk_widget.display()
            disk_values.append(values[0])

            network_widget = Widget(widget_type="Network", data_source=[server])
            times, values = network_widget.display()
            network_values.append(values[0])

    df = pd.DataFrame({
        'Timestamp': time_stamps,
        'Server': server_names,
        'CPU': cpu_values,
        'Memory': memory_values,
        'Disk': disk_values,
        'Network': network_values
    })

    df_melted = pd.melt(df, id_vars=['Timestamp', 'Server'], value_vars=['CPU', 'Memory', 'Disk', 'Network'],
                        var_name='Metric', value_name='Usage')

    sns.set(style="whitegrid")
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x="Timestamp", y="Usage", hue="Metric", data=df_melted, palette=colors)

    plt.title("Server Metrics Over Time")
    plt.xlabel("Time")
    plt.ylabel("Usage (%)")
    plt.xticks(rotation=45)
    plt.legend(title="Metric")
    plt.tight_layout()
    plt.show()
