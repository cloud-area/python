# 1.定义师傅类
class Master(object):
    # 1.1 属性
    def __init__(self):
        self.kofu = '[传统方法]'

    # 1.2 方法
    def make_cake(self):
        print(f'使用{self.kofu}摊煎饼')


# 2.定义黑马类
class Heima(object):
    # 1.1 属性
    def __init__(self):
        self.kofu = '[AI方法]'

    # 1.2 方法
    def make_cake(self):
        print(f'使用{self.kofu}摊煎饼')


# 3.定义徒弟类
class Tudi(Heima,Master):
    pass


# 3.实例化
xiaoming = Tudi()
print(xiaoming.kofo)
xiaoming.make_cake()


print(Tudi.__mro__)
print(Tudi.mro())