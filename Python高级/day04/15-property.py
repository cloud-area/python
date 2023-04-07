# 定义一个类
class Person(object):
    def __init__(self):
        self.__money = 2000

    # def get_money(self):
    #     return self.__money
    #
    # def set_money(self):
    #     self.__money = 5000
    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self,m):
        if m < 100:
            print('这是不可能的')
        else:
            self.__money = m


# 在类外获取
p = Person()
print(p.money)
p.money = 5000
print(p.money)
