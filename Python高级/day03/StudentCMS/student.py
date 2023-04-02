# -*- coding = utf-8 -*-
class Student(object):
    """定义学生类"""

    def __init__(self, name, age, gender, std_id, mobile, des):
        """定义学生属性"""
        self.name = name
        self.age = age
        self.gender = gender
        self.std_id = std_id
        self.mobile = mobile
        self.des = des
        self.add_dict = {"name": self.name, "age": self.age, "gender": self.gender, "std_id": self.std_id,
                         "mobile": self.mobile, "des": self.des}

    def __str__(self):
        return f'{self.add_dict}'


# 测试功能
# if __name__ == '__main__':
#     student = Student('小红', "16", '女', '202304158886', '10086', '高中生')
#     print(student.add_dict)
