class Server:
    def __init__(self, server_ID, name, IP_address, server_type, operating_system):
        self.server_ID = server_ID
        self.name = name
        self.IP_address = IP_address
        self.server_type = server_type
        self.operating_system = operating_system
        
def get_status(self):
    """Метод для отримання статусу сервера"""
    # Тут можна реалізувати логіку для отримання статусу сервера
    return f"Server {self.name} is running."

def update_configuration(self, new_type=None, new_os=None):
    """Метод для оновлення конфігурації сервера"""
    if new_type:
        self.server_type = new_type
    if new_os:
        self.operating_system = new_os
    return f"Server {self.name} configuration updated."



