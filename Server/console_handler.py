# console_handler.py
from Server.Exceptions import InvalidClientId, InvalidArguments
from colorama import Fore, Style
import importlib
import threading

command_busy = threading.Event()  # Define command_finished here


def handle_console(clients):
    while True:
        command = input("Enter command: " + Style.RESET_ALL)
        handle_commands(command, clients)


# console_handler.py
def handle_commands(command, clients):
    cmd = command.split(' ')[0]
    args = command.split(' ')[1:]

    try:
        command_module = importlib.import_module(f'commands.{cmd.lower()}')
        if command_module.requires_id and args:
            id = int(args[0])
            # check if ID is within range
            if id >= len(clients) or id < 0:
                raise InvalidClientId(id)
            else:
                command_thread = threading.Thread(target=command_module.execute, args=(clients[id], args, clients, id))
                command_thread.start()
                command_thread.join()  # Wait for the command thread to finish
        elif command_module.requires_id and not args:
            raise InvalidArguments(command_module.argumentError)
        elif not command_module.requires_id:
            command_thread = threading.Thread(target=command_module.execute, args=(args, clients))
            command_thread.start()
            command_thread.join()  # Wait for the command thread to finish
    except ImportError:
        print(Fore.RED + f"Invalid command:" + Style.RESET_ALL + f" {cmd}")
    except InvalidClientId as e:
        print(Fore.RED + f"Invalid Client ID: {e.id}" + Style.RESET_ALL)
    except InvalidArguments as e:
        print(Fore.RED + e.argumentError + Style.RESET_ALL)