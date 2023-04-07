# -*- coding = utf-8 -*-

"""


"""

import socket
import test

# count = 0
# while count<2:
# 1.创建套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.向服务端发送请求
ip = '192.168.36.88'
port = 5647
client_socket.connect((ip,port))


# 3.发送和接收数据
# str_2 = test.ascill_art("smile.png")
str_3 = test.ascill_art("png03.png")

# client_socket.send(str_2.encode(encoding='UTF-8'))
client_socket.send(str_3.encode(encoding='UTF-8'))
recv_data = client_socket.recv(1024)
print(recv_data.decode(encoding='UTF-8'))
# count += 1
# 4.关闭套接字
client_socket.close()