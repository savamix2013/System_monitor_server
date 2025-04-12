from root.property.AlertManager import AlertManager

rules = {
    "CPU > 80": "Critical",
    "Memory < 20": "Warning",
}

manager = AlertManager(alert_rules=rules)

metrics = [
    {"type": "CPU", "value": 85},
    {"type": "Memory", "value": 15},
    {"type": "Disk", "value": 50},
]

manager.check_alert_conditions(metrics)
manager.send_alerts()