import json
from credential_server import CredentialServer
from credential_service import load_servers, load_actual_servers, load_old_servers
from svn_client import SvnClient

if __name__ == "__main__":
    servers = load_servers("credentials.json")
    atual_server = load_actual_servers("credentials.json")
    antigo_server = load_old_servers("credentials.json")

    print("All Servers:")
    for s in servers:
        print(s)

    print("\nAtual Server:")
    print(atual_server)

    print("\nAntigo Server:")
    print(antigo_server)
   
    svn_client = SvnClient(
        server=atual_server.server,
        username=atual_server.login,
        password=atual_server.senha
    )
    print("\nSvn Info:")
    print(svn_client.info())
    svn_client.cat("new/hmenu.mkp")

    

    
