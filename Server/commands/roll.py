# commands/kill.py
from colorama import Fore, Style

requires_id = True

from Server.console_handler import inactive


def execute(conn, args, clients, id):
    inactive.clear()
    clients[id].sendall(b'ROLL')
    print("Rickrolling client:", id)
    inactive.set()  # set the event here
