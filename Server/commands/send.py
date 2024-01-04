# commands/send.py
from colorama import Fore, Style

requires_id = True
expectedNumArgs = 1
argumentError = "Usage: send <client id>"
from Server.console_handler import command_busy
def execute(conn, id, args, clients):
    msg = input(Fore.CYAN + "Enter message: " + Style.RESET_ALL)
    clients[id].sendall(msg.encode())
    print(Fore.BLUE + "Sent message to client:" + Style.RESET_ALL, id)
    # command_busy.clear()  # Clear the event here

