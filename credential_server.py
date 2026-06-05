from dataclasses import dataclass

@dataclass
class CredentialServer:
    name: str
    server: str
    login: str
    senha: str