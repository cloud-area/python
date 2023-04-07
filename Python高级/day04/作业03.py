# -*- coding = utf-8 -*-

"""
请使用装饰器方式来统计输出100000句"黑马程序员YYDS"的执行时间

"""
# 导入包
import time


# 装饰器
def execution_time(fn):
    """统计执行时间装饰器"""

    def inner():
        # 获取运行前时间
        t1 = int(time.time() * 1000)

        # 运行原函数
        fn()

        # 输出运行结束时间
        t2 = int(time.time() * 1000)
        print("\n运行时间: %dms" % (t2 - t1))

    return inner


@execution_time
def print_str():
    """
    输出100000次“黑马程序员YYDS”
    :return:
    """
    # 计数器
    count = 0
    # 循环输出函数
    while count < 100000:
        print("黑马程序员YYDS")
        count += 1


# 调用输出函数
print_str()
