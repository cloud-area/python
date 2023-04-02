# -*- coding = utf-8 -*-

"""
函数嵌套: 内外部函数  (outer, inner)
有引用: 内部函数引用外部函数的变量
有返回: 外部函数要返回内部函数名

"""
# 案例1
# 函数嵌套
# def outer(num1):
#     def inner(num2):
#         # 有引用
#         sum_num = num2+num1
#         print(f'两数之和是{sum_num}')
#
#     # 有返回
#     return inner
#
#
# # 调用闭包
# func = outer(5)
# func(20)
#
#
# func = outer(6)
# func(7)

"""
案例2 打印不同分割线
"""


def line_config(content, length):
    """

    :param content: 输入内容
    :param length: 线长度
    :return:
    """

    def line():
        print("-" * (length // 2) + content + "-" * (length // 2))

    return line


# line_config("闭包",40)

line1 = line_config("闭包", 40)
line1()
line1()

line2 = line_config("xxx", 20)
line2()
line2()