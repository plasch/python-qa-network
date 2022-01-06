import socket

with socket.socket() as s:
    # https://hea-www.harvard.edu/~fine/Tech/addrinuse.html
    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind(('', 5000))
    s.listen(1)

    conn, addr = s.accept()
    recv_bytes = conn.recv(1024)
    text = recv_bytes.decode('utf-8')
    print(f'Message received\n"{recv_bytes}"')

    # https://developer.mozilla.org/ru/docs/Web/HTTP/Messages
    # http://httpbin.org/#/HTTP_Methods
    body = '<h1>Hello from OTUS!</h1>\r\n'
    status_line = 'HTTP/1.1 200 OK'
    headers = '\r\n'.join([
        status_line,
        f'Content-Length: {len(body)}',
        'Content-Type: text/html'
    ])
    resp = '\r\n\r\n'.join([
        headers,
        body
    ])
    sent_bytes = conn.send(resp.encode('utf-8'))
    print(f'{sent_bytes} bytes sent')
    conn.close()
