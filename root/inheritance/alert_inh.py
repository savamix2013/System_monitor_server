from root.property.Alert import Alert

alert = Alert("Disk", "Disk usage is high", 80, 90, 95, 100)
print(alert.create_alert())
alert.send_alert()