import socket

# specify family and type
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print(s)
s.close()
print(s)

# default family and type
s = socket.socket()
print(s)
s.close()
print(s)
