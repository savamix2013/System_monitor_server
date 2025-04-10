class TicketIntegration:
    def __init__(self, system_type="Jira", api_url="", auth_token="", project_key=""):
        self.system_type = system_type
        self.api_url = api_url
        self.auth_token = auth_token
        self.project_key = project_key

    def create_ticket(self, issue_title, issue_description, severity="Medium"):
        print(f"Creating ticket in {self.system_type}: [{severity}] {issue_title} - {issue_description}")

    def update_ticket(self, ticket_id, new_status):
        print(f"Updating ticket {ticket_id} in {self.system_type} to status: {new_status}")

    def close_ticket(self, ticket_id):
        print(f"Closing ticket {ticket_id} in {self.system_type}")