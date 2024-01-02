# commands/kill.py
from colorama import Fore, Style

requires_id = False

def execute(args, clients):
    # create list of current clients with ID
    for client in clients:
        print(Fore.BLUE + "Client ID: " + Style.RESET_ALL + "(" + str(clients.index(client)) + ",", client.getpeername()[0] + ")" )
