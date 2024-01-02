# commands/send.py
from colorama import Fore, Style

requires_id = True

from Server.console_handler import command_busy
def execute(conn, args, clients, id):
    msg = input(Fore.CYAN + "Enter message: " + Style.RESET_ALL)
    clients[id].sendall(msg.encode())
    print(Fore.BLUE + "Sent message to client:" + Style.RESET_ALL, id)
    # command_busy.clear()  # Clear the event here

