import socket

server = socket.socket()

server.bind(('127.0.0.1',8001))
server.listen(2)
while 1:
    conn , addr = server.accept()

    from_browser_msg = conn.recv(1024).decode('utf8')
    print(from_browser_msg)

    conn.send(b'Http/1.1  200 ok \r\n\r\n')

    with open(r'E:\PYXUEXI\OBPY1\020_前端\a02_html基础\a03_form_input.html',mode='rb') as f:
        date = f.read()
    conn.send(date)
    # conn.send(b'<h1>hello world</h1>')
    conn.close()

server.close()