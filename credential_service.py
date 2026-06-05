import json
from credential_server import CredentialServer

def load_servers(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [CredentialServer(**item) for item in data]

def load_actual_servers(path):
    servers = load_servers(path)
    return next((s for s in servers if s.name == "atual"), None)

def load_old_servers(path):
    servers = load_servers(path)
    return next((s for s in servers if s.name == "antigo"), None)
