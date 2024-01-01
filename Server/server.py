# server.py

import socket
import threading
from client_handler import handle_client
from console_handler import handle_console
from colorama import Fore, Style

# get local IP address
HOST = (socket.gethostbyname_ex(socket.gethostname())[2][-1])
PORT = 5616

clients = []


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(Fore.GREEN + "Listening on IP: {}, port {}...".format(HOST, PORT) + Fore.RESET)
        threading.Thread(target=handle_console, args=(clients,), daemon=True).start()

        while True:  # search for clients
            conn, addr = s.accept()
            clients.append(conn)
            threading.Thread(target=handle_client, args=(conn, addr, clients ), daemon=True).start()


if __name__ == "__main__":
    main()
