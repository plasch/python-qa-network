import socket

with socket.socket() as s:
    s.connect(('', 5000))
    text = 'Hello, OTUS!'
    print(f'Sending message\n"{text}"')
    sent_bytes = s.send(text.encode('utf-8'))
    print(f'{sent_bytes} bytes sent')
