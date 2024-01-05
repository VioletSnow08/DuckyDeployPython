from Server.Exceptions import InvalidClientId, InvalidArguments
from colorama import Fore, Style
import importlib
import threading
from Server.helpers import debugPrint as debugPrint
from Server.helpers import checkArgs as checkArgs
from Server.helpers import validateID as validateID


def handle_commands(command, clients):
    cmd = command.split(' ')[0]
    args = command.split(' ')[1:]
    command_module = None
    try:
        debugPrint(f"Checking if command '{cmd}' exists.")
        command_module = importlib.import_module(f'commands.{cmd.lower()}')
        debugPrint(f"Command {cmd} exists.") # if it doesn't exist, it would throw an error and skip this line
        if command_module.requires_id and args and validateID(args, clients):
            if not checkArgs(args, command_module.expectedNumArgs): raise InvalidArguments(command_module.argumentError)

            startIDCommand(command_module, clients[int(args[0])], int(args[0]), args, clients)

        elif command_module.requires_id and not args:
            debugPrint(f"Command {command_module} requires an ID, but none was provided.")
            raise InvalidArguments(command_module.argumentError)

        elif not command_module.requires_id:
            if not checkArgs(args, command_module.expectedNumArgs): raise debugPrint() and InvalidArguments(command_module.argumentError)

            startIDlessCommand(command_module, args, clients)


    except ImportError as e:
        print(Fore.RED + f"Failed to import command module 'commands.{cmd.lower()}': " + Style.RESET_ALL + f"{e}")
    except InvalidClientId as e:
        print(Fore.RED + f"Invalid Client ID: {e.id}" + Style.RESET_ALL)
    except InvalidArguments as e:
        print(Fore.RED + "Invalid Arguments.", Style.RESET_ALL + e.argumentError)


def startIDCommand(command_module, conn, id, args, clients):
    debugPrint(f"Starting command thread for {command_module} with args {args} on client {id}")
    command_thread = threading.Thread(target=command_module.execute, args=(conn, id, args, clients,))
    command_thread.start()
    command_thread.join()  # Wait for the command thread to finish


def startIDlessCommand(command_module, args, clients):
    debugPrint(f"Starting command thread for {command_module} with args {args}")
    command_thread = threading.Thread(target=command_module.execute, args=(args, clients,))
    command_thread.start()
    command_thread.join()  # Wait for the command thread to finish
