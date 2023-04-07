# 1.定义装饰器
def outer(fn, flag):
    def inner(a, b):
        if flag == "+":
            print('正在进行加法计算....')
        elif flag == "-":
            print('正在进行减法计算....')
        result = fn(a, b)
        return result

    return inner


# 2.定义原有函数
@outer('+')
def add(x, y):
    sum = x + y
    return sum


# 3.调用
result = add(10, 20)
print(result)
