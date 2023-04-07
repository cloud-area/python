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
class Tudi(Heima):
    # 1.1 属性
    def __init__(self):
        self.kofu = '[独创技术]'

    # 1.2 方法
    def make_cake(self):
        print(f'使用{self.kofu}摊煎饼')

    # 1.4 使用黑马技术
    def heima_make_cake(self):
        super().__init__()
        super().make_cake()


# 3.实例化
xiaoming = Tudi()
# print(xiaoming.kofu)
# xiaoming.make_cake()
# xiaoming.master_make_cake()
xiaoming.heima_make_cake()

