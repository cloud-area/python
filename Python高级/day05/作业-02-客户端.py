# -*- coding = utf-8 -*-

"""
通过TCP客户端发送消息：欢迎来传智教育，真牛!
通过TCP服务器端接收消息，并打印出来

"""
import socket

# 1.创建套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.向服务端发送请求
ip = '127.0.0.1'
port = 8888
client_socket.connect((ip, port))

# 3.发送和接收数据
str_1 = '欢迎来传智教育，真牛!'

client_socket.send(str_1.encode(encoding='UTF-8'))
recv_data = client_socket.recv(1024)
print(recv_data.decode(encoding='UTF-8'))

# 4.关闭套接字
client_socket.close()
