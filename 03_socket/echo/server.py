import os
import socket

from lib.helpers import get_open_port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    srv_addr = ('', get_open_port())
    print(f'starting on {srv_addr}, pid: {os.getpid()}')

    s.bind(srv_addr)
    s.listen(1)

    while True:
        print('waiting for a connection')
        conn, raddr = s.accept()
        print(s)
        print(conn)

        print('connection from', raddr)
        while True:
            data = conn.recv(1024)
            text = data.decode('utf-8')
            print(f'received {repr(text)}')
            if text:
                print('sending data back to the client')
                conn.send(data)
            else:
                print(f'no data from {raddr}')
                break
        conn.close()
