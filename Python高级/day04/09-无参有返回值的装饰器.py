# 1.装饰器
def outer(fn):
    def inner():
        print('正在努力计算中...')
        result=fn()
        return result
    return inner


# 2.原有函数:无参有返回值
@outer
def get_sum():
    sum = 10 + 20
    return sum

# 3.调用
sum = get_sum()
print(sum)
