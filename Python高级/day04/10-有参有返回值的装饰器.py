# 1.定义装饰器
def outer(fn):
    def inner(a,b):
        print('正在计算中....')
        result =fn(a,b)
        return result
    return inner


# 2.原有函数
@outer
def get_sum(x,y):
    sum =x+y
    return sum


# 3.调用
result =get_sum(10,20)
print(result)
