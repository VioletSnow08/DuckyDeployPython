from Client.helpers import send_shell_results, open_chrome

rickroll_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


def execute(conn, args):
    open_chrome(rickroll_URL)
    print("Server sent rickroll.")
