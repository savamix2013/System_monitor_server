class CloudIntergration:
    def __init__(self):
        self.providers = {
            "AWS": [],
            "Azure": [],
            "Google Cloud": [],
        }

    def discover_servers(self, provider_name):
        print(f"Discovering servers in {provider_name}...")

        dummy_servers = [
            {"name": "Server1", "status": "running"},
            {"name": "Server2", "status": "stopped"},
            {"name": "Server3", "status": "running"},
        ]
        self.providers[provider_name].extend(dummy_servers)
        print(f"Discovered servers in {provider_name}: {dummy_servers}")
        return dummy_servers
    
    def get_all_servers(self):
        all_severs = []
        for provider, servers in self.providers.items():
            all_severs.extend(servers)
        return all_severs
    
    