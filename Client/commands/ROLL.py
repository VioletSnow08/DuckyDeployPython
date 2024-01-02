import subprocess
from colorama import Style, Fore

from Client.client import send_shell_results
from Client.commands.CHROME import open_chrome

rickroll_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


def execute(s, args):
    open_chrome(rickroll_URL)
    print("Server sent rickroll.")
