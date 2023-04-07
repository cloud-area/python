# 1.定义装饰器
# 1.1 登录的装饰器
def login(fn):
    def inner():
        print('请登录用户...')
        fn()
        # print('活体检测')

    return inner
# 1.2 验证的装饰器
def check(fn):
    def inner():
        print('请输入验证码...')
        fn()
    return inner
# 2.原有函数
@login
@check
def comment():
    print('发表评论...')
# 3.调用
comment()
