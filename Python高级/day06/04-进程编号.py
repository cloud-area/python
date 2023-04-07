# -*- coding = utf-8 -*-

"""
方法一:
import os
# 获取当前进程编号
pid = os.getpid()
print(pid)

方法二:
import multiprocessing
pid = multiprocessing.current_process().pid
print(pid)

"""
import time
import multiprocessing
import os


def coding(name, num):
    for i in range(num):
        print(f'{name}在编写第{i}行代码。')
        time.sleep(0.2)
    print(f'coding进程编号: {os.getpid()}')
    print(f'coding父进程编号: {os.getppid()}')


def music(name, num):
    for i in range(num):
        print(f'{name}在听第{i}首歌曲, 听了第{i}首歌曲。')
        time.sleep(0.2)
    print(f'music进程编号: {os.getpid()}')
    print(f'music父进程编号: {os.getppid()}')


if __name__ == '__main__':
    t1 = time.time()
    # 创建子进程
    # p1 = multiprocessing.Process(target=coding,args=('小明', 10))
    # p2 = multiprocessing.Process(target=music,args=('lina', 12))
    p1 = multiprocessing.Process(target=coding, kwargs={'name': '小明', 'num': 8})
    p2 = multiprocessing.Process(target=music, kwargs={'num': 11, 'name': 'lina'})
    # 启动子进程
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    t2 = time.time()
    time_1 = t2 - t1
    print('%.02fs' % time_1)

    os.kill(os.getpid(),9)