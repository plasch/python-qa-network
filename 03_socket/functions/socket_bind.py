import socket
from lib.helpers import get_open_port

with socket.socket() as s:
    print(s)

    HOST = ''  # Symbolic name meaning all available interfaces
    PORT = get_open_port()
    s.bind((HOST, PORT))
    print(s)
