# -*- coding = utf-8 -*-

"""
守护进程目的是:
    主进程退出子进程销毁

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
    # 子进程设置为守护进程
    p.daemon = True

    p.start()
    time.sleep(1.2)

    print('主进程执行完成！')
