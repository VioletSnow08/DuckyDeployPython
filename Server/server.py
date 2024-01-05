# server.py

import socket
import threading
import time

from client_handler import handle_client
from console_handler import handle_console
from colorama import Fore, Style
from Server.helpers import debugPrint

# get local IP address
HOST = (socket.gethostbyname_ex(socket.gethostname())[2][-1])
PORT = 5616

clients = []


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(Fore.GREEN + "Listening on IP: {}, port {}...".format(HOST, PORT) + Fore.RESET)
        try:
            debugPrint("Console handler started.")
            threading.Thread(target=handle_console, args=(clients,), daemon=True).start()
        except Exception as e:
            debugPrint("Error starting console handler: {}".format(e))

        # TODO: add a way to package commands in pyinstaller
        # TODO: add a way to confirm a command was executed successfully
        while True:  # search for clients
            conn, addr = s.accept()
            clients.append(conn)
            debugPrint("Client connected from: {}".format(addr))
            threading.Thread(target=handle_client, args=(conn, addr, clients ), daemon=True).start()
            debugPrint(f"Client handler started on ID: {len(clients) - 1}")


if __name__ == "__main__":
    main()
