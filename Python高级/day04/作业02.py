# -*- coding = utf-8 -*-

"""
创建一个闭包，实现统计函数执行的次数功能。有如下调用闭包函数的代码：
f = func_count()
f()
f()
f()

执行结果如下：
    > hello world
    > 执行了1次
    > hello world
    > 执行了2次
    > hello world
    > 执行了3次
请完善 func_count 函数的实现。
"""


def func_count():
    """利用闭包实现输出"""
    # 增加一个计数器
    count = 0

    def inner():
        """输出"""
        nonlocal count
        count += 1
        print("hello world")
        print(f'执行了{count}次')

    return inner

f = func_count()
f()
f()
f()
