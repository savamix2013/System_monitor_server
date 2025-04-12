class Dashboard:
    def __init__(self, name):
        self.name = name
        self.widgets = []

    def add_widget(self, widget):
        self.widgets.append(widget)
        print(f"Widget '{widget}' added to dashboard '{self.name}'.")

    def remove_widget(self, widget):
        if widget in self.widgets:
            self.widgets.remove(widget)
            print(f"Widget '{widget}' removed from dashboard '{self.name}'.")
        else:
            print(f"Widget '{widget}' not found in dashboard '{self.name}'.")

    def update_widget(self):
        for widget in self.widgets:
            widget.update()
            print(f"Widget '{widget}' updated.")

    def refresh_all(self):
        for widget in self.widgets:
            widget.display()