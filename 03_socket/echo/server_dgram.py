import os
import socket

from lib.helpers import get_open_port

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    srv_addr = ('', get_open_port())
    print(f'starting on {srv_addr}, pid: {os.getpid()}')

    s.bind(srv_addr)

    while True:
        data, raddr = s.recvfrom(1024)
        print(f'received {len(data)} bytes from {raddr}')
        decoded = data.decode('utf-8')
        print(f'received message: "{decoded}"')

        if data:
            sent = s.sendto(data, raddr)
            print(f'sent {sent} bytes back to {raddr}')
