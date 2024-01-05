import subprocess
import pyautogui
import time

notepad_path = "C:\\Windows\\System32\\notepad.exe"
def execute(conn, args):
    print("Server sent NOTEPAD command. Displaying text...")
    subprocess.call([notepad_path])
    time.sleep(2)
    text = str(args[1:])
    pyautogui.typewrite(text)