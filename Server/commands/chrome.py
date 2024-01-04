# commands/chrome.py
from colorama import Fore, Style

from Server.Exceptions import InvalidArguments

requires_id = True
expectedNumArgs = 2
argumentError = "Usage: chrome <client_id> <url>"


def execute(conn, id, args, clients):
    if len(args) < 2:
        print(Fore.RED + argumentError + Style.RESET_ALL)
        return
    msg = 'CHROME ' + args[1]
    clients[id].sendall(bytes(msg, 'utf-8'))
    print("Opening Chrome tab on client:", id)
