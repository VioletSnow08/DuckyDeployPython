# commands/notepad.py
from colorama import Fore, Style

requires_id = True
expectedNumArgs = 2
argumentError = "Usage: notepad <client_id> <text>"


def execute(conn, id, args, clients):

    msg = 'NOTEPAD ' + str(args[1:])
    clients[id].sendall(bytes(msg, 'utf-8'))
    print("Displaying text using notepad on client:", id)
