# commands/kill.py
from colorama import Fore, Style

requires_id = True

from Server.console_handler import command_busy


def execute(conn, args, clients, id):
    clients[id].sendall(b'KILL')
    clients[id].close()
    clients.pop(id)
    print(Fore.BLUE + "Killing client:" + Style.RESET_ALL, id)
    # command_busy.clear()  # Clear the event here
