# -*- coding = utf-8 -*-

"""
通过TCP客户端发送消息：欢迎来传智教育，真牛!
通过TCP服务器端接收消息，并打印出来

"""
import socket

if __name__ == '__main__':
    # 1.创建服务端套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定IP地址和端口号
    ip = '127.0.0.1'
    port = 8888
    tcp_server_socket.bind((ip, port))

    # 3.设置监听
    tcp_server_socket.listen(5)
    print('正在监听中...')


    # 4.等待接受客户端的连接请求
    conn_socket, client_ad = tcp_server_socket.accept()
    print(f'客户端地址: {client_ad}')

    # 5.发送数据或接收数据
    recv_data = conn_socket.recv(1024)
    print(f'接收到客户端发送的数据{recv_data.decode(encoding="UTF-8")}')
    send_str = '数据已收到'
    send_data = send_str.encode(encoding='UTF-8')
    conn_socket.send(send_data)

    # 7.关闭套接字
    tcp_server_socket.close()