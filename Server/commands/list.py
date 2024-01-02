# commands/kill.py
from colorama import Fore, Style

requires_id = False
from Server.console_handler import command_busy

def execute(args, clients):
    # create list of current clients with ID
    for client in clients:
        print(Fore.BLUE + "Client ID: {}".format(clients.index(client)) + Style.RESET_ALL)
