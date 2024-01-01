# server.py

import socket
import threading
from client_handler import handle_client
from console_handler import handle_console
from colorama import Fore, Style

HOST = '127.0.0.1'
PORT = 1234

clients = []


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(Fore.GREEN + "Listening on port {}...".format(PORT) + Fore.RESET)
        threading.Thread(target=handle_console, args=(clients,), daemon=True).start()

        while True:  # search for clients
            conn, addr = s.accept()
            clients.append(conn)
            threading.Thread(target=handle_client, args=(conn, addr, clients), daemon=True).start()


if __name__ == "__main__":
    main()
