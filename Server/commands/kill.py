# commands/kill.py
from colorama import Fore, Style

requires_id = True
argumentError = "Usage: kill <client id>"


def execute(conn, args, clients, id):
    clients[id].sendall(b'KILL')
    print(Fore.YELLOW + "Killing client:" + Style.RESET_ALL, id)

    clients[id].close()
    clients.pop(id)
