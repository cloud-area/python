# 1.定义装饰器
def outer(fn):
    def inner(*args,**kwargs):
        print('正在努力计算中....')
        result = fn(*args,**kwargs)
        return result
    return inner


# 2.定义原有函数
@outer
def get_sum(*args, **kwargs):
    sum = 0
    for arg in args:
        sum += arg
    for value in kwargs.values():
        sum += value
    return sum


# 3.调用
result = get_sum(1, 2, 3, 4, a=1, b=2, c=3)
print(result)
