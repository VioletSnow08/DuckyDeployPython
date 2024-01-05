# console_handler.py

from colorama import Fore, Style

import threading

from Server.command_handler import handle_commands

command_busy = threading.Event()  # Define command_finished here


def handle_console(clients):
    while True:
        command = input("Enter command: " + Style.RESET_ALL)
        handle_commands(command, clients)


# console_handler.py
