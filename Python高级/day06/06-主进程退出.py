# -*- coding = utf-8 -*-

"""
主进程要等待子进程结束之后再退出

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
    print('主进程执行完成！')