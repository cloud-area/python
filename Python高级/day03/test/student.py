# 学生类

# 1.定义类
class Student(object):
    # 1.1 定义属性
    def __init__(self, name, age, gender, mobile, des):
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile = mobile
        self.des = des

    # 1.2 输出信息设置
    def __str__(self):
        return f'{self.name}的年龄是{self.age},性别{self.gender},手机号{self.mobile},备注{self.des}'


# 2.测试功能
if __name__ == '__main__':
    s1 = Student('小红', 23, '女', 10086, '程序媛')
    print(s1.age)
    print(s1.__dict__)
