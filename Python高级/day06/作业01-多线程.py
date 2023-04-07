# -*- coding = utf-8 -*-

"""
请使用多任务形式完成：一边编程、一边听音乐、一边跟同事聊天。要求如下：

a.使用多进程完成；
b.使用多线程完成；
c.分别观察与对比多进程、多线程的执行效果。

"""
# 导入模块包
import time
import threading

# 定义任务
def coding():
    """
    编程任务
    :return:
    """
    for i in range(2):
        print("正在疯狂敲代码")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")

def listen():
    """
    听音乐任务
    :return:
    """
    time.sleep(0.5)
    for i in range(3):
        print("享受HiFi音乐")
        time.sleep(0.5)
        print(".")
        time.sleep(1)
        print(".")

def talking():
    """
    同事对话任务
    :return:
    """
    time.sleep(1)
    for i in range(2):
        print("和同事交流摸鱼心得")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")


if __name__ == '__main__':
    # 初始计时器
    t1 = time.time()

    # 创建进程
    coding_thread = threading.Thread(target=coding)
    listen_thread = threading.Thread(target=listen)
    talking_thread = threading.Thread(target=talking)

    # 启动任务
    coding_thread.start()
    listen_thread.start()
    talking_thread.start()

    # 添加阻塞
    coding_thread.join()
    listen_thread.join()
    talking_thread.join()

    # 任务结束
    print("结束快乐的摸鱼下班！！！")

    # 输出计时器
    t2 = time.time()
    time_step = t2-t1

    print("运行时间: %.02fs" % time_step)