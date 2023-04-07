# -*- coding = utf-8 -*-

"""
定义一个可以计算多个数据和多个字典value值之和的函数，并调用。

"""


def print_info(func):
    """
    打印信息装饰器
    :param func:引用原有函数
    :return: 内部函数地址
    """

    def inner(*args,**kwargs):
        """
        原有函数
        :param args:
        :return: None
        """
        print("正在努力计算中...")
        res = func(*args,**kwargs)
        return res
    return inner

@print_info
def get_sum(*args, **kwargs):
    """
    求和
    :param args:
    :param kwargs:
    :return: 和
    """
    sum_num = 0
    for arg in args:
        sum_num += arg
    for value in kwargs.values():
        sum_num += value

    return sum_num


result = get_sum(1, 2, 3, 4, a=1, b=2, c=3)
print(result)
