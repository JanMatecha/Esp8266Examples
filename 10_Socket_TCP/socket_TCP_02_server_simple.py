'''
https://www.binarytides.com/python-socket-programming-tutorial/
prvni priklad
'''

import socket
import sys

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 8888  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print('Socket bind complete')

s.listen(10)
print('Socket now listening')


# now keep talking with the client
# TODO na PC to nefunguje
# po pripojeni telnetem: telnet localhost 5000
# se pomoci recev precte jen jedno pismenko, pak probehne zbytek smycky
# az k accept a uz se to nepripoji
# trochu jsem to upravil oproti prikladu
# asi to bude telnetem, ktery to posila po pismenku


while 1:
    print("zacatek")
    # wait to accept a connection - blocking call
    conn, addr = s.accept()
    # display client information
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    while 1:
        print("recv")
        data = conn.recv(1024)
        print(data)
        reply = 'OK...' + data.decode('utf-8')
        print(reply)
        print("tady")
        if not data:
            print("not data")

            break
        print("reply")
        conn.sendall(reply.encode('utf-8'))
        print("reply")
        if data.decode('utf-8')=="e":
            print("Konec")
            break

conn.close()
print("conn close")
s.close()

