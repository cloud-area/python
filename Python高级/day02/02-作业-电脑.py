# 定义一个电脑类，并给电脑添加品牌、价格等属性，同时电脑能用于编程、看视频。

# 1.定义类
class Computer:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def coding(self):
        print('编写代码')

    def video(self):
        print('看视频')

    def show(self):
        print(self.brand)
        print(self.price)
# 2.创建对象
com = Computer('华为',8000)
com.show()
com.coding()
com.video()