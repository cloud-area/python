# -*- coding = utf-8 -*-

"""
使用互斥锁保证线程间的数据安全
    互斥锁：多个线程一起去抢，抢到锁的线程先执行，没有抢到锁的线程进行等待，
    等锁使用完释放后，其它等待的线程再去抢这个锁。

"""

import threading

# 1.定义全局变量
g_num = 0

# 2.创建互斥锁
mutex = threading.Lock()

def sum_num1():
    """
    两个函数实现加法
    :return:
    """
    global g_num

    # 上锁
    mutex.acquire()

    for i in range(1000000):
        g_num += 1

    # 解锁
    mutex.release()
    print("g_num1:", g_num)


def sum_num2():
    """
    两个函数实现加法
    :return:
    """
    global g_num

    # 上锁
    mutex.acquire()

    for i in range(1000000):
        g_num += 1

    # 解锁
    mutex.release()
    print("g_num2:", g_num)




if __name__ == '__main__':
    # 创建子线程
    sum1_thread = threading.Thread(target=sum_num1)
    sum2_thread = threading.Thread(target=sum_num2)

    # 启动线程
    sum1_thread.start()
    sum2_thread.start()