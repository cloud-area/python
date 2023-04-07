# -*- coding = utf-8 -*-

"""
定义一个闭包，用于求解方程的y与x值的变化，例如 y = ax + b。

"""


def outer(a_1, b_1):
    """
    先获取 a 和 b 的值
    利用闭包保存 a 和 b 的值
    :param a_1: a的值
    :param b_1: b的值
    :return:
    """
    print(f'a:{a_1}  b:{b_1}')

    def inner(x_1):
        """
        获取 x 值，计算出 y = ax + b
        :param x_1: x
        :return: y
        """
        y = a * x + b
        print(f'x={x_1} 时 y= {y}')

    return inner


print("计算 y = ax + b  (x值不为数字则退出！)")
a = int(input("请先输入a的值: "))
b = int(input("请再输入b的值: "))
fun = outer(a, b)
while True:
    try:
        x = int(input("x的值: "))
        fun(x)
    except ValueError:
        break
