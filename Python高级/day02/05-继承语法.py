# 1.定义父类
class Father(object):
    def __init__(self):
        self.gender = 'man'

    def walk(self):
        print('爱好散步行走')


# 2.定义子类
class Son(Father):
    pass


# 3.实例化,验证继承结果
son = Son()
print(son.gender)
son.walk()
