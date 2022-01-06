import socket

with socket.socket() as s:
    s.connect(('', 5000))
    print(s)
