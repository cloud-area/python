# -*- coding = utf-8 -*-

"""
线程之间共享全局变量

"""
import threading
import time

# 定义全局变量
my_list = []

def write_data():
    """
    写入数据的任务
    :return:
    """
    for i in range(3):
        print("add:", i)
        my_list.append(i)

    print("write:", my_list)


def read_data():
    """
    读取数据的任务
    :return:
    """
    print("read:", my_list)


if __name__ == '__main__':
    # 创建子线程
    write_data = threading.Thread(target=write_data)
    read_data = threading.Thread(target=read_data)

    # 启动线程
    write_data.start()

    time.sleep(1)
    read_data.start()