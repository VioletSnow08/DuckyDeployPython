# commands/advlist.py

import socket
from rich.console import Console
from rich.table import Table

requires_id = False
expectedNumArgs = 0

def execute(args, clients):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")

    table.add_column("ID")
    table.add_column("Hostname")
    table.add_column("Port")
    table.add_column("IP")
    table.add_column("OS")
    table.add_column("User")

    for client in clients:
        id = str(clients.index(client))
        ip = client.getpeername()[0]
        port = str(client.getpeername()[1])
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = "Unknown"

        # Send commands to get OS and user information
        client.sendall(b'EXEC ver')
        # Receive the results
        results = client.recv(1024).decode('utf-8').split('\n')
        os_info = results[1]

        client.sendall(b'EXEC whoami')
        # Receive the results
        results = client.recv(1024).decode('utf-8').split('\n')
        user = results[0]

        table.add_row(id, hostname, port, ip, os_info, user)

    console.print(table)