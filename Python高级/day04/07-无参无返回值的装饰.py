# 1.定义装饰器
# 1.1 有嵌套
def outer(fn):
    # 1.2 有引用
    def inner():
        # 1.4 有额外功能
        print('正在努力计算中...')
        fn()

    # 1.3 有返回
    return inner


# 2.原有函数(无参无返回值)
@outer
def get_sum():
    a = 10
    b = 20
    print(f'求和结果为{a + b}')

# 3.调用
get_sum()
