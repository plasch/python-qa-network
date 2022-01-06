import socket
import sys

PORT = None

try:
    PORT = int(sys.argv[1])
except IndexError:
    print("Pass a port for connection")
    exit(1)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    srv_addr = ('', PORT)

    sent_msg = 'Test message'
    print(f'sending "{sent_msg}"')
    sent = s.sendto(sent_msg.encode('utf-8'), srv_addr)
    print(f'sent {sent} bytes to {srv_addr}')

    print('waiting to receive')
    data, server = s.recvfrom(1024)
    decoded = data.decode('utf-8')
    print(f'received message: "{decoded}"')
