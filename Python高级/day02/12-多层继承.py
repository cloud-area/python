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
class Tudi(Heima, Master):
    # 1.1 属性
    def __init__(self):
        self.kofu = '[独创技术]'

    # 1.2 方法
    def make_cake(self):
        self.__init__()
        print(f'使用{self.kofu}摊煎饼')

    # 1.3 使用老师傅的技术
    def master_make_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    # 1.4 使用黑马技术
    def heima_make_cake(self):
        Heima.__init__(self)
        Heima.make_cake(self)


# 4.创建徒孙类
class Tusun(Tudi):
    pass


xiaoxiaoming = Tusun()
print(xiaoxiaoming.kofu)
xiaoxiaoming.make_cake()
xiaoxiaoming.heima_make_cake()
xiaoxiaoming.master_make_cake()