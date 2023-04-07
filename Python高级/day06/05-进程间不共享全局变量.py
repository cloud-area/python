# -*- coding = utf-8 -*-

"""


"""
import multiprocessing
import time

my_list = []


# 1. 定义任务
def write_data():
    global my_list
    for i in range(5):
        my_list.append(i)
        print(f'添加数字{i}')
        time.sleep(0.1)
    print(f'写之后的数据{my_list}')


def read_data():
    global my_list
    print(f'读取结果:{my_list}')


# 2.创建进程
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=write_data)
    p2 = multiprocessing.Process(target=read_data)
    p1.start()
    time.sleep(1)
    p2.start()
    p1.join()
    p2.join()
