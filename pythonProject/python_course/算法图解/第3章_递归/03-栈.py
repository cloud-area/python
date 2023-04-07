# -*- coding = utf-8 -*-

"""
递归函数调用栈

"""


def fact(x):
    """
    计算阶乘
    :param x:阶乘数字
    :return:
    """
    if x == 1:
        # 如果最后减小到1，则返回1参与计算
        return 1
    else:
        # 返回计算的递归逆序数乘积
        return x * fact(x - 1)

print(fact(5))


