import subprocess
from colorama import Style, Fore

from Client.client import send_shell_results

chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'


def open_chrome(url):
    subprocess.call([chrome_path, url])


def execute(s, args):
    print("Opening Chrome tab: " + args[1])
    open_chrome(args[1])
