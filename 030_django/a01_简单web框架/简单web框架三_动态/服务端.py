import socket
from threading import Thread
import time
server = socket.socket()
ip_port = ('127.0.0.1', 8001)
server.bind(ip_port)
server.listen()


def html1(conn):

    data_tag = str(time.time())
    print(data_tag)
    with open(r'OBPY1\030_django\a01_简单web框架\简单web框架三_动态\test.html',
              mode='r',
              encoding='utf-8') as f:
        data = f.read()
    # 字符串替换 实现动态
    data = data.replace('$xxoo$', data_tag)
    data = data.encode('utf-8')
    conn.send(data)
    conn.close()


def css1(conn):
    with open(r'OBPY1\030_django\a01_简单web框架\简单web框架三_动态\test.css',
              mode='rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()


def js1(conn):
    with open(r'OBPY1\030_django\a01_简单web框架\简单web框架三_动态\test.js',
              mode='rb') as f:
        data = f.read()
    print(data)
    conn.send(data)
    conn.close()


urlpatterns = [('/', html1), ('/test.css', css1), ('/test.js', js1)]

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
            t = Thread(target=i[1], args=(conn, ))
            t.start()
