# -*- coding = utf-8 -*-

"""
定义一个函数, 返回字符串, 使用装饰器实现对这个字符串添加后缀.txt

"""


def str_suffixes(fn):
    def inner():
        change_str = fn()
        change_str = change_str+'.txt'
        return change_str
    return inner

@str_suffixes
def string():
    """返回字符串"""
    return 'Hello Python!'


# 打印函数返回值
print(string())
