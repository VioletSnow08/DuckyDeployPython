
requires_id = True
expectedNumArgs = 2
argumentError = "Usage: exec <client_id> <command>"
def execute(conn, id, args, clients):
    print("Executing command...")
    conn.sendall(args[1].encode())