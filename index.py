import subprocess
import webbrowser

URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'


def main():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe', URL])


if __name__ == "__main__":
    main()
