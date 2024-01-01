import subprocess
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
                    data = s.recv(1024)
                    if not data:
                        break
                    elif data == b'KILL':
                        print("Connection closed by server.")
                        exit(0)
                    print("Received data: {}".format(data))
        except socket.error as e:  # if server connection fails
            print("Connection error: {}".format(e))


if __name__ == "__main__":
    main()
