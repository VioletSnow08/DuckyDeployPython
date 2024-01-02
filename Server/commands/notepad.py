# commands/notepad.py
from colorama import Fore, Style

requires_id = True
argumentError = "Invalid arguments. Usage: notepad <client_id> <text>"


def execute(conn, args, clients, id):
    if len(args) < 2:
        print(Fore.RED + argumentError + Style.RESET_ALL)
        return
    msg = 'NOTEPAD ' + args[1:]
    clients[id].sendall(bytes(msg, 'utf-8'))
    print("Displaying text using notepad on client:", id)
