# commands/kill.py
from colorama import Fore, Style

requires_id = True

from Server.console_handler import command_finished

def execute(conn, args, clients, id):
    clients[id].sendall(b'ROLL')
    print("Rickrolling client:", id)
    command_finished.clear()  # Clear the event here
