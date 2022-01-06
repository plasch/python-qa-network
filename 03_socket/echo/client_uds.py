import socket

srv_addr = './unix_socket'

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
    print(f'connecting to {srv_addr}')
    s.connect(srv_addr)

    sent_msg = 'Test message'
    print(f'sending "{sent_msg}"')
    s.send(sent_msg.encode('utf-8'))

    recv_msg = s.recv(1024).decode('utf-8')
    print(f'received "{recv_msg}"')
