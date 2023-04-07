# 尝试定义一个工程师类，同时使用`__init__()`初始化岗位名称、薪资金额等属性，
# 工作内容是每天码代码，同时使用`__str__()`展示对象所拥有的所有信息。

# 1.定义类
class Engineer:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def coding(self):
        print('每天都在写代码....')

    def __str__(self):
        return f'{self.name}的薪资是{self.salary}'


# 2.创建对象
en = Engineer('算法工程师', 1000000)
en.coding()
print(en)
