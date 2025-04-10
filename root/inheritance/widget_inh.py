from root.property.Widget import Widget

cpu_widget = Widget(
    widget_type="CPU",
    data_source="CPUMetric",
    display_settings={"color": "green", "size": "large"}
)

cpu_widget.update_data()
cpu_widget.display_widget()

memory_widget = Widget(
    widget_type="Memory",
    data_source="MemoryMetric",
    display_settings={"color": "blue", "size": "medium"}
)

memory_widget.update_data()
memory_widget.display_widget()