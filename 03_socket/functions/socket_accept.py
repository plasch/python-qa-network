import socket

with socket.socket() as s:
    s.bind(('', 5000))
    s.listen(1)
    print(s)

    conn, addr = s.accept()
    print(conn)
    print(addr)
