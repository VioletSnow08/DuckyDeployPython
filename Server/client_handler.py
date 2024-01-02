# client_handler.py

import socket
from colorama import Fore, Style
from console_handler import inactive


def handle_client(conn, addr, clients):
    # with conn:  # while connected to client
    print("\n" + Fore.BLUE + "Connected by" + Style.RESET_ALL, addr)
    # while True:  # while connected to client, listen for requests
    #     try:
    #         data = conn.recv(1024)
    #         if not data:
    #             print(Fore.YELLOW + "Connection closed by" + Style.RESET_ALL, addr)
    #             if conn in clients:
    #                 clients.remove(conn)
    #             break
    #
    #         if command_finished.is_set():  # if command_finished is true(AKA no command is being executed) print received data
    #             print(Fore.BLUE + "Received data: {}".format(data.decode('utf-8')) + Style.RESET_ALL)
    #
    #             # Insert your logic here to handle the received data
    #             # You may want to check the content of the received data and perform actions accordingly
    #
    #     except socket.error as e:
    #         print(Fore.RED + "Connection error with {}: {}".format(addr, e) + Style.RESET_ALL)
    #         if conn in clients:
    #             clients.remove(conn)
    #         break
