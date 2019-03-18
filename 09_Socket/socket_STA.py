import socket
# Adresa druheho Wemosu, kde bezi smycka

APIP='192.168.1.10'
addr = socket.getaddrinfo(APIP, 8888)[0][-1]

# vytvoreni socketu
s = socket.socket()
# pripojeni
s.connect(addr)
# odeslani
s.send("ABCDE\r\n".encode('utf-8'))
# pozor na konci musi byt \r\n\r\n - zatim nevim proc
s.send("WERTY\r\n\r\n".encode('utf-8'))
# obdrzeni odpovedi
# while True:
#     data = s.recv(100)
#     if data:
#         print(str(data, 'utf8'), end='')
#     else:
#         break
#
# # zavreni socketu
#
s.close()

