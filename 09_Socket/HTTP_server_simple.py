import socket

html = """<!DOCTYPE html>
<html>
    <head> <title>WEMOS</title> </head>
    <body> <h1> Vase zarizeni</h1>
        <p> IP: %s </p>
        <p> zarizeni a prohlizec: %s </p>
    </body>
</html>
\r\n\r\n
"""


addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]


s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)
zarizeni = ""

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    # pokud IP adresa nezacina 192.168 rovnou ukonci socket
    if addr[0].startswith("192.168"):
        cl_file = cl.makefile('rwb', 0)
        print("cl_file", cl_file)
        # cl.send(html.encode('utf-8'))
        while True:
            print("cl_file.readline()")
            line = cl_file.readline()
            print("line", line)
            if line.startswith("User-Agent:"):
                zarizeni = line.decode('utf-8')
                print ("zarizeni: ", zarizeni)
            if not line or line == b'\r\n':
                break
        cl.send(html.encode('utf-8') % (addr[0], zarizeni))
    cl.close()



