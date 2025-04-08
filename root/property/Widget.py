import matplotlib.pyplot as plt


class Widget:
    def __init__(self, widget_type, data_source, display_settings=None):
        self.widget_type = widget_type
        self.data_source = data_source
        self.display_settings = display_settings or {}

    def update_data(self, new_data):
        self.data_source = new_data
        # Placeholder for data update logic
        print(f"Updating data for {self.widget_type} widget from {self.data_source}.")

    def display(self):
        times = [entry['timestamp'] for entry in self.data_source]
        values = [entry['value'] for entry in self.data_source]

        plt.figure(figsize=(6, 3))
        plt.plot(times, values, label=self.widget_type, color="green")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.title(f"{self.widget_type}")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()



    
