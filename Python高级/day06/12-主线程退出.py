# -*- coding = utf-8 -*-

"""
主线程会等待所有子线程执行结束再结束


"""
import threading
import time

def work():
    """
    工作函数，执行2s
    :return:
    """
    for i in range(10):
        print("working...")
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子线程
    work_thread = threading.Thread(target=work)
    # 启动线程
    work_thread.start()

    time.sleep(1)
    print("主线程执行完毕")