# client_handler.py

import socket
from colorama import Fore, Style


def handle_client(conn, addr, clients):
    with conn:  # while connected to client
        print("\n" + Fore.BLUE + "Connected by" + Style.RESET_ALL, addr)
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    print(Fore.YELLOW + "Connection closed by" + Style.RESET_ALL, addr)
                    if conn in clients:
                        clients.remove(conn)
                    break
                print(Fore.BLUE + "Received data: {}".format(data) + Style.RESET_ALL)
                conn.sendall(data)
            except socket.error as e:
                print(Fore.RED + "Connection error with {}: {}".format(addr, e) + Style.RESET_ALL)
                if conn in clients:
                    clients.remove(conn)
                break