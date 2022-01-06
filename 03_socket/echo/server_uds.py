import os
import socket

srv_addr = './unix_socket'

# Make sure the socket does not already exist
try:
    os.unlink(srv_addr)
except OSError:
    if os.path.exists(srv_addr):
        raise

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
    print(f'starting on {srv_addr}, pid: {os.getpid()}')

    s.bind(srv_addr)
    s.listen(1)

    while True:
        print('waiting for a connection')
        conn, raddr = s.accept()

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
