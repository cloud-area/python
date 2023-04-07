class Master(object):
    # 1.1 属性
    def __init__(self):
        self.kofu = '[传统方法]'

    # 1.2 方法
    def make_cake(self):
        print(f'使用{self.kofu}摊煎饼')

# 创建对象
m = Master()
# 对象名.方法名
# m.make_cake()

# 类名.方法名(对象名)
Master.make_cake(m)