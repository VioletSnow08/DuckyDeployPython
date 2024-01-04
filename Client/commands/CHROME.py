import subprocess

from Client.helpers import open_chrome


def execute(conn, args):
    print("Opening Chrome tab: " + args[1])
    open_chrome(args[1])
