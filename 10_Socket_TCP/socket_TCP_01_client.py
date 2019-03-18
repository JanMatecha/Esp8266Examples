'''
https://www.binarytides.com/python-socket-programming-tutorial/
prvni priklad - upraveny pro micropython
'''

import socket  # for sockets
import sys  # for exit
import errno

# TODO potreba predelat pro micropython
try:
    # create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
    sys.exit()

print('Socket Created')

host = 'www.google.com'
port = 80

try:
    # remote_ip = socket.gethostbyname(host)
    addr = socket.getaddrinfo(host, 80)[0][-1]
# except socket.gaierror:
except OSError as msg:
    # could not resolve
    # print(msg)
    # print(msg.args[0])
    # errno.errorcode[msg.args[0]]
    print('Hostname could not be resolved. Exiting')
    sys.exit()

print('Ip address of ' + host + ' is ' + addr[0])

# Connect to remote server
s.connect(addr)

print('Socket Connected to ' + host + ' on ip ' + addr[0])

# Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"

# TODO potreba predelat pro micropython
try:
    # Set the whole string
    s.sendall(message.encode('utf-8'))
except socket.error:
    # Send failed
    print('Send failed')
    sys.exit()

print('Message send successfully')

# Now receive data
reply = s.recv(4096)

print(reply.decode('ascii'))

s.close()
