from colorama import Fore, Style

from Server.Exceptions import InvalidClientId

DEBUG = True


def checkArgs(args, expectedNumArgs):
    debugPrint("Checking args: {} against expected: {}".format(args, expectedNumArgs))
    if len(args) != expectedNumArgs:
        debugPrint("Invalid number of arguments.")
        return False
    debugPrint("Valid number of arguments.")
    return True


def validateID(args, clients):
    debugPrint("Validating ID: {}".format(args[0]))
    try:
        id = int(args[0])
    except ValueError:
        debugPrint("No ID provided.")
        raise InvalidClientId(args[0])
    # check if ID is within range
    if id >= len(clients) or id < 0:
        debugPrint("Invalid ID: {}".format(id))
        raise InvalidClientId(id)
    return id


def debugPrint(msg):
    if DEBUG:
        print(Fore.YELLOW + "[DEBUG] " + Style.RESET_ALL + msg)
