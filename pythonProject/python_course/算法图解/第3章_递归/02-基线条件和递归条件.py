# -*- coding = utf-8 -*-

"""
由于递归函数调用自己，因此编写这样的函数时很容易出错，进而导致无限循环

"""


# 递归输出逆序数
# def count_down(i):
#     print(i)
#     count_down(i-1)
#
# print(count_down(3))


# 给count_down添加基线条件
def count_down(i):
    print(i)
    if i <= 0:  # 基线条件
        return
    else:  # 递归条件
        count_down(i - 1)


count_down(3)
