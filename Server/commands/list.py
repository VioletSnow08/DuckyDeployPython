# commands/kill.py
from colorama import Fore, Style

requires_id = False
from Server.console_handler import inactive

def execute(args, clients):
    inactive.clear()
    # create list of current clients with ID
    for client in clients:
        print(Fore.BLUE + "Client ID: {}".format(clients.index(client)) + Style.RESET_ALL)
    inactive.set()  # set the event here
