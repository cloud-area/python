# -*- coding = utf-8 -*-

"""
TCP开发流程

TCP服务器端

客户端



"""
import socket

if __name__ == '__main__':
    # 1.创建服务端套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 8.端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,True)

    # 2.绑定IP地址和端口号
    ip = '127.0.0.1'
    port = 8888
    tcp_server_socket.bind((ip, port))

    # 3.设置监听
    tcp_server_socket.listen(128)
    print('正在监听中...')

    count = 0
    while count<100:
        # 4.等待接受客户端的连接请求
        conn_socket, client_ad = tcp_server_socket.accept()
        print(f'客户端地址: {client_ad}')

        # 5.发送数据或接收数据
        recv_data = conn_socket.recv(8388608)
        print(f'接收到客户端发送的数据{recv_data.decode(encoding="UTF-8")}')
        send_str = '数据已收到'
        send_data = send_str.encode(encoding='UTF-8')
        conn_socket.send(send_data)
        count += 1

        # 7.关闭套接字
        # tcp_server_socket.close()


