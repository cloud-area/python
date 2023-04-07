# 1.定义父类
class Traffic(object):
    # 定义公共方法
    def start(self):
        pass
    def stop(self):
        pass


# 2.定义子类:car和plane
class Car(Traffic):
    def __init__(self,kind):
        self.kind = kind

    def start(self):
        print(f'{self.kind}启动了')

    def stop(self):
        print(f'{self.kind}停止了')


class Plane(Traffic):
    def __init__(self, kind):
        self.kind = kind

    def start(self):
        print(f'{self.kind}起飞了')

    def stop(self):
        print(f'{self.kind}降落了')


# 3.定义老师类
class Teacher(object):
    def __init__(self,name):
        self.name = name

    def start_traffic(self,traffic):
        print(f'{self.name}要出发了')
        traffic.start()

    def stop_traffic(self,traffic):
        print(f'{self.name}到目的地了')
        traffic.stop()


# 4.实例化
teacher = Teacher('姚老师')
car = Car('小汽车')
teacher.start_traffic(car)
teacher.stop_traffic(car)

plane = Plane('空客')
teacher.start_traffic(plane)
teacher.stop_traffic(plane)