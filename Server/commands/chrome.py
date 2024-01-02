# commands/chrome.py
from colorama import Fore, Style

from Server.Exceptions import InvalidArguments

requires_id = True
argumentError = "Invalid arguments. Usage: chrome <client_id> <url>"


def execute(conn, args, clients, id):
    if len(args) < 2:
        print(Fore.RED + argumentError + Style.RESET_ALL)
        return
    msg = 'CHROME ' + args[1]
    clients[id].sendall(bytes(msg, 'utf-8'))
    print("Opening Chrome tab on client:", id)
