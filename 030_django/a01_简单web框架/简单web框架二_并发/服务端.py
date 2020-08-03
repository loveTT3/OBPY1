import socket
from threading import Thread

server = socket.socket()
ip_port = ('127.0.0.1', 8001)
server.bind(ip_port)
server.listen()


def html1(conn):
    with open(r'OBPY1\030_django\a01_简单web框架\简单web框架二_并发\test.html',
            mode='rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()

def css1(conn):
    with open(r'OBPY1\030_django\a01_简单web框架\简单web框架二_并发\test.css',
            mode='rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()

def js1(conn):
    with open(r'OBPY1\030_django\a01_简单web框架\简单web框架二_并发\test.js',mode='rb') as f:
        data = f.read()
    print(data)
    conn.send(data)
    conn.close()

urlpatterns = [
    ('/',html1),
    ('/test.css',css1),
    ('/test.js',js1)
]

while 1:
    conn, addr = server.accept()
    from_client_msg = conn.recv(1024)
    request_msg = from_client_msg.decode('utf-8')
    path = request_msg.split('\r\n')[0].split(' ')[1]
    print(path)
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n')

    for i in urlpatterns:
        if path == i[0]:
            # i[1](conn)
            t = Thread(target=i[1],args=(conn,))
            t.start()
