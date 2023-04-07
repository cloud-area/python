# -*- coding = utf-8 -*-

"""


"""
import threading
import time

def coding(name, num):
    for i in range(num):
        print(f'{name}正在编写第{i}行代码')
        time.sleep(0.2)


def music(name, num):
    for i in range(num):
        print(f'{name}正在听第{i}首歌曲')
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子线程
    coding_thread = threading.Thread(target=coding,args=('小明',3))
    music_thread = threading.Thread(target=music,kwargs={'num':3,'name':'小红'})

    # 启动子线程执行任务
    coding_thread.start()
    music_thread.start()