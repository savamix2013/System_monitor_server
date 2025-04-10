from root.property.MonitoringSystem import MonitoringSystem

ms = MonitoringSystem()
ms.discover_and_add_cloud_servers("AWS")
ms.discover_and_add_cloud_servers("Google Cloud")
ms.run_monitoring_cycle()
