# -*- coding = utf-8 -*-

"""


"""
import time
import multiprocessing


def coding(name, num):
    for i in range(num):
        print(f'{name}在编写第{i}行代码。')
        time.sleep(0.2)


def music(name, num):
    for i in range(num):
        print(f'{name}在听第{i}首歌曲, 听了第{i}首歌曲。')
        time.sleep(0.2)


if __name__ == '__main__':
    t1 = time.time()
    # 创建子进程
    # p1 = multiprocessing.Process(target=coding,args=('小明', 10))
    # p2 = multiprocessing.Process(target=music,args=('lina', 12))
    p1 = multiprocessing.Process(target=coding, kwargs={'name':'小明','num':8})
    p2 = multiprocessing.Process(target=music, kwargs={'num':11, 'name':'lina'})
    # 启动子进程
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    t2 = time.time()
    time_1 = t2 - t1
    print('%fs' % time_1)

    p3 = multiprocessing.Process(target=coding, kwargs={'name': '小明', 'num': 100})
    p4 = multiprocessing.Process(target=music, kwargs={'num': 100, 'name': 'lina'})
    # 顺序执行子进程
    p3.start()
    p3.join()
    p4.start()
    p4.join()

    t3 = time.time()
    time_2 = t3 - t2
    print('%fs' % time_2)

    print(f'{time_1}s,{time_2}s')