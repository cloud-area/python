# -*- coding = utf-8 -*-

"""


"""
import threading
import time

def work():
    """
    工作函数，执行2s
    :return:
    """
    for i in range(10):
        print('working...')
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子线程
    # 方式1 参数方式设置守护主线程
    # work_thread = threading.Thread(target=work, daemon=True)
    # work_thread.start()
    # time.sleep(1)
    # print("主线程执行完毕")

    # 方式2 调用setDaemon函数
    work_thread = threading.Thread(target=work)
    work_thread.setDaemon(True)
    work_thread.start()
    time.sleep(1)
    print("主程序执行完毕")