# commands/kill.py
from colorama import Fore, Style

requires_id = True
argumentError = "Usage: roll <client id>"

def execute(conn, args, clients, id):
    clients[id].sendall(b'ROLL')
    print("Rickrolling client:", id)
