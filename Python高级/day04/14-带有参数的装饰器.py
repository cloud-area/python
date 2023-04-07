# 1.装饰器
def logging(flag):
    def outer(fn):
        def inner(a, b):
            # 额外功能
            if flag == "+":
                print('正在进行加法计算...')
            elif flag == '-':
                print('正在进行减法运算....')
            z = fn(a, b)
            return z

        return inner

    return outer


# 2.原有函数
@logging('+')
def add(a, b):
    sum = a + b
    return sum


@logging('-')
def reduce(a, b):
    res = a - b
    return res


# 3.调用
result1 = add(10, 20)
print(result1)
result2 = reduce(20, 10)
print(result2)
