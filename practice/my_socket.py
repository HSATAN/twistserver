# _*_ coding:utf8 _*_

import socket

sock = socket.socket()

sock.connect(('www.myenger.com', 80))
sock.send("GET /search HTTP/1.1\r\nContent-Type: text/html;"
          " charset=UTF-8\r\nAccept-Encoding:gzip, deflate,"
          " sdch\t\nHost:www.myenger.com\r\n\r\n")
data = sock.recv(1024)
print(data)