import socket

server = socket.socket()
ip_port = ('127.0.0.1', 8001)
server.bind(ip_port)
server.listen()

while 1:
    conn, addr = server.accept()
    from_client_msg = conn.recv(1024)
    request_msg = from_client_msg.decode('utf-8')
    path = request_msg.split('\r\n')[0].split(' ')[1]
    print(path)
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n')


    with open(r'OBPY1\030_django\a01_简单web框架\简单web框架一\test.html', mode='rb') as f:
        data = f.read()
    # print(data)
    conn.send(data)
    conn.close()