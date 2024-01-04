import subprocess

chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

def send_shell_results(s, results):
    try:
        data_to_send = results.encode("utf-8")
        # Send data in chunks
        for i in range(0, len(data_to_send), 1024):
            s.sendall(data_to_send[i:i + 1024]) # Send 1024 bytes at a time
        print("Sent results.")
    except BrokenPipeError:
        print("Connection closed by server.")
        return
def open_chrome(url):
    subprocess.call([chrome_path, url])