import socket
from lib.helpers import get_open_port

with socket.socket() as s:
    s.bind(('', get_open_port()))
    print(s)
    s.listen(1)
