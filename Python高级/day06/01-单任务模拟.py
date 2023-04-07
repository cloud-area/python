# -*- coding = utf-8 -*-

"""


"""
import time


def coding():
    for i in range(10):
        print(f'正在编写第{i}行代码')
        time.sleep(0.2)


def music():
    for i in range(10):
        print(f'正在听第{i}首歌曲')
        time.sleep(0.2)


if __name__ == '__main__':
    t1 = time.time()
    coding()
    music()
    t2 = time.time()
    print('%.02fs' % (t2 - t1))
