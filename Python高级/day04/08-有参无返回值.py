# 1.装饰器
# 1.1 有嵌套
def outer(fn):
    def inner(a, b):
        # 1.4 增加额外功能
        print('正在努力计算中....')
        # 1.2 有引用:并且添加了参数
        fn(a, b)

    # 1.3 有返回
    return inner


# 2.原有函数
@outer
def get_sum(x, y):
    sum = x + y
    print(f'两数之和{sum}')


# 3.调用
get_sum(10, 20)
