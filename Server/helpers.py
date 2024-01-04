from colorama import Fore, Style


def checkArgs(args, expectedNumArgs):
    if len(args) != expectedNumArgs:
        return False
    return True