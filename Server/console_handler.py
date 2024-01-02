# console_handler.py
from Server.Exceptions import InvalidClientId
from colorama import Fore, Style
import importlib
import threading

inactive = threading.Event()  # Define command_finished here


def handle_console(clients):
    inactive.set()
    while True:
        if inactive.is_set():
            command = input("Enter command: " + Style.RESET_ALL)
        else:
            inactive.wait()
            inactive.clear()
            continue

        handle_commands(command, clients)
        # inactive.wait()
        # inactive.set()


def handle_commands(command, clients):
    cmd = command.split(' ')[0]
    args = command.split(' ')[1:]
    try:
        command_module = importlib.import_module(f'commands.{cmd.lower()}')
        if command_module.requires_id and args:
            id = int(args[0])
            if id >= len(clients) or id < 0:
                raise InvalidClientId(id)

            command_module.execute(clients[id], args, clients, id)
        elif command_module.requires_id and not args:
            print(Fore.RED + "Command requires arguments: " + cmd + Style.RESET_ALL)
        else:
            command_module.execute(args, clients)
        inactive.set()
    except ImportError:
        print(Fore.RED + f"Invalid command: {cmd}" + Style.RESET_ALL)
    except InvalidClientId as e:
        print(Fore.RED + f"Invalid Client ID: {e.id}" + Style.RESET_ALL)
    finally:
        inactive.set()
