# commands/kill.py
from colorama import Fore, Style

requires_id = True
argumentError = "Invalid arguments. Usage: roll <client id>"
from Server.console_handler import command_busy

def execute(conn, args, clients, id):
    # command_busy.set()
    clients[id].sendall(b'ROLL')
    print("Rickrolling client:", id)
    # command_busy.clear()  # set the event here
