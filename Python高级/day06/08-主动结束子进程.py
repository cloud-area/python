# -*- coding = utf-8 -*-

"""


"""
import multiprocessing
import time


# 1.定义任务
def work():
    for i in range(10):
        print(f'第{i}次工作中...')
        time.sleep(0.2)


# 2.创建进程
if __name__ == '__main__':
    p = multiprocessing.Process(target=work)

    p.start()
    time.sleep(1)

    # 手动结束子进程
    p.terminate() # 这种方式不会清理资源，僵尸进程

    print('主进程执行完成！')