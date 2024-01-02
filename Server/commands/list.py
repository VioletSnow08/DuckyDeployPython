# commands/list.py

import socket
from rich.console import Console
from rich.table import Table

requires_id = False


def execute(args, clients):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")

    table.add_column("ID")
    table.add_column("Hostname")
    table.add_column("Port")
    table.add_column("IP")

    for client in clients:
        id = str(clients.index(client))
        ip = client.getpeername()[0]
        port = str(client.getpeername()[1])
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = "Unknown"
        table.add_row(id, hostname, port, ip)

    console.print(table)
