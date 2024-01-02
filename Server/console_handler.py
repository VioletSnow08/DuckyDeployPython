# console_handler.py
from Server.Exceptions import InvalidClientId, InvalidArguments
from colorama import Fore, Style
import importlib
import threading

command_busy = threading.Event()  # Define command_finished here


def handle_console(clients):
    command_busy.clear()
    while True:
        if not command_busy.is_set():
            command = input("Enter command: " + Style.RESET_ALL)
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
            # check if ID is within range
            if id >= len(clients) or id < 0:
                raise InvalidClientId(id)
            else:
                command_busy.set()
                command_module.execute(clients[id], args, clients, id)
        elif command_module.requires_id and not args:
            raise InvalidArguments(command_module.argumentError)
        elif not command_module.requires_id:
            command_busy.set()
            command_module.execute(args, clients)
    except ImportError:
        print(Fore.RED + f"Invalid command: {cmd}" + Style.RESET_ALL)
    except InvalidClientId as e:
        print(Fore.RED + f"Invalid Client ID: {e.id}" + Style.RESET_ALL)
    except InvalidArguments as e:
        print(Fore.RED + e.argumentError + Style.RESET_ALL)

    finally:
        command_busy.clear()
