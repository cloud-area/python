# -*- coding = utf-8 -*-

"""


"""
import time
import multiprocessing

def coding():
    for i in range(20):
        print(f'正在编写第{i}行代码')
        time.sleep(0.2)


def music():
    for i in range(20):
        print(f'正在听第{i}首歌曲')
        time.sleep(0.2)


if __name__ == '__main__':
    t1 = time.time()
    # 创建子进程
    p1 = multiprocessing.Process(target=coding)
    p2 = multiprocessing.Process(target=music)

    # 启动子进程
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    t2 = time.time()
    print('%fs' % (t2 - t1))
