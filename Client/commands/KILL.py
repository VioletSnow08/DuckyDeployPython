import subprocess
from colorama import Style, Fore

from Client.client import send_shell_results


def execute(s, args):
    print("Server sent KILL command. Exiting...")
    exit(0)