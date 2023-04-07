# -*- coding = utf-8 -*-

"""


"""
import time
import threading


def coding():
    for i in range(20):
        print(f'正在编写第{i}行代码')
        time.sleep(0.2)


def music():
    for i in range(20):
        print(f'正在听第{i}首歌曲')
        time.sleep(0.2)


if __name__ == '__main__':
    t_start = time.time()
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=music)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    t_stop = time.time()
    print(t_stop-t_start)