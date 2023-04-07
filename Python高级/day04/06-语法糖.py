# 发表评论前,要先登录
# 1.定义装饰器:装饰器名称就是外部函数名
# 2.1 嵌套
def outer(fn):
    # 2.2 引用
    def inner():
        # 2.4 额外功能
        print('请先登录...')
        fn()
    # 2.3 返回
    return inner

# 2.定义原有函数
@outer
def comment():
    print('发表评论')

# 3.调用
comment()