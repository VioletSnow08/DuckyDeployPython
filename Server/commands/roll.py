# commands/kill.py
from colorama import Fore, Style

requires_id = True
expectedNumArgs = 1
argumentError = "Usage: roll <client id>"

def execute(conn, id, args, clients):
    clients[id].sendall(b'ROLL')
    print("Rickrolling client:", id)
