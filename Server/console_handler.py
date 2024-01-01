# console_handler.py
from Server.Exceptions import InvalidClientId
from colorama import Fore, Style
import importlib
import threading


def handle_console(clients):
    command_finished = threading.Event()
    while True:
        command = input(Fore.CYAN + "Enter command: " + Style.RESET_ALL)

        if command == 'LIST':
            for i in range(30):
                print("-", end="")
            print()
            for i, conn in enumerate(clients):
                print(f"{i}: {conn.getpeername()}")
            for i in range(30):
                print("-", end="")
            print()
            continue

        # anything below this line requires an ID and uses handle_commands()
        try:
            cmd, id = command.split()
            id = int(id)
            if id >= len(clients) or id < 0:
                raise InvalidClientId(id)
        except ValueError:
            print(Fore.RED + "Invalid command: {}".format(command) + Style.RESET_ALL)
            continue
        except InvalidClientId as e:
            print(Fore.RED + "Client does not exist: {}".format(e.id) + Style.RESET_ALL)
            continue

        handle_commands(clients[id], command, id, clients, command_finished)
        command_finished.wait()
        command_finished.clear()


def handle_commands(conn, command, id, clients, command_finished):
    cmd = command.split()[0]
    args = command.split()[1:]
    try:
        command_module = importlib.import_module(f'commands.{cmd.lower()}')
        if command_module.requires_id and args:
            id = int(args.pop(0))
            if id >= len(clients) or id < 0:
                raise InvalidClientId(id)
            command_module.execute(conn, args, clients, id)
        else:
            command_module.execute(conn, args, clients)
    except ImportError:
        print(Fore.RED + f"Invalid command: {cmd}" + Style.RESET_ALL)
    finally:
        command_finished.set()