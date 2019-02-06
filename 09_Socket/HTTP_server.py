import socket
import time
html = """<!DOCTYPE html>
<html>
    <head> <title>ESP8266 Pins</title> </head>
    <body> <h1>ESP8266 Pins</h1>
        <p> </p>
    </body>
</html>
"""
# <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]


s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    print("cl_file", cl_file)
    while True:
        line = cl_file.readline()
        print("line",line)
        if not line or line == b'\r\n':
            break

    # rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
    # response = html % '\n'.join(rows)
    # response = html % "ABC"
    print("tady")
    cl.send(html.encode('utf-8'))
    # cl.send("HTTP/1.0 200 OK\r\n\r\n<h1>Hallo Michael, how are you?</h1>\r\n".encode('utf-8'))
    print("tady2")
    time.sleep(1)
    print("tady3")
    cl.close()

cl, addr = s.accept()
print('client connected from', addr)
cl_file = cl.makefile('rwb', 0)
print("cl_file", cl_file)
while True:
    line = cl_file.readline()
    print("line",line)
    if not line or line == b'\r\n':
        break

# rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
# response = html % '\n'.join(rows)
# response = html % "ABC"
print("tady")
cl.send(html.encode('utf-8'))
# cl.send("HTTP/1.0 200 OK\r\n\r\n<h1>Hallo Michael, how are you?</h1>\r\n".encode('utf-8'))
print("tady2")
time.sleep(1)
print("tady3")
cl.close()