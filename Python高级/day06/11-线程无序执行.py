# -*- coding = utf-8 -*-

"""
线程间是无序执行的

"""
import threading
import time

def get_info():
    time.sleep(0.2)
    thr = threading.current_thread()
    print(thr)

if __name__ == '__main__':
    for i in range(10):
        sub_thread = threading.Thread(target=get_info)
        sub_thread.start()