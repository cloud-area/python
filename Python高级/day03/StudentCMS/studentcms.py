# -*- coding = utf-8 -*-
import time
import menu as m
from student import Student
import student_id as std_id


class Studentcms:
    """定义系统类"""

    def __init__(self):
        """初始化"""
        # 创建对象
        # 对象名 = 类名([参数列表])
        self.student_lists = []

    def add_student(self):
        """
        添加学生信息
        :return: None
        """
        while True:
            # 获取姓名和电话
            name = input("请输入要添加的姓名:")
            mobile = input("请输入要添加的联系方式:")

            # 重复录入检查
            for student in self.student_lists:
                # 如果有重复学生，则跳出循环
                if (student.name == name) and (student.mobile == mobile):
                    print("此学员已添加！")
                    print("")
                    break
            else:
                # 继续添加个人信息
                age = input("请输入要添加的年龄:")
                gender = input("请输入要添加的性别:")
                des = input("请输入要添加的描述信息:")

                # 生成学号
                stu_id = std_id.student_id()
                # 转换为对象
                student = Student(name, age, gender, stu_id, mobile, des)

                # 添加到属性中
                self.student_lists.append(student)
                print("=========学生信息已添加成功!!===========")
                return

    def update_student(self):
        """
        修改学生信息
        :return: None
        """
        # 获取要修改学生的学号
        change_id = input("请输入要修改信息的学员学号:")

        # 查找是否有该学生
        for student in self.student_lists:
            # 如果有该学生
            if student.std_id == change_id:
                # 获取学生信息,进行修改
                student.name = input("请输入修改后的学员姓名:")
                student.age = input("情输入修改后的学员年龄:")
                student.mobile = input("情输入修改后的学员电话:")
                student.des = input("情输入修改后的学员描述:")
                print("修改完毕!!!")
                return
        else:
            # 如果没有
            print("查无此人！")

    def del_student(self):
        """
        删除学生信息
        :return:
        """
        # 获取要删除学生的学号
        del_id = input("请输入要删除的学员学号:")
        for student in self.student_lists:
            # 如果找到该学员
            if student.std_id == del_id:
                # 将学员信息从列表中删除
                self.student_lists.remove(student)
                print(f'已删除学员的信息!')
                return

        # 如果没有找到
        else:
            print("未找到该学员信息!!!")

    def search_student(self):
        """
        查询学生信息
        :return:
        """
        # 获取要查找学生的学号
        search_id = input("请输入要查找学员的学号:")

        for student in self.student_lists:
            # 如果有该学员
            if student.std_id == search_id:
                print("{:<5s}{:<4s}{:<4s}{:<14s}{:<13s}{:<11s}".format("姓名", "年龄", "性别", "学号", "电话",
                                                                       "个人描述"))
                print("{:<5s}{:<5s}{:<4s}{:<15s}{:<15s}{:<11s}".format(student.name, student.age, student.gender,
                                                                       student.std_id, student.mobile, student.des))

                return
        else:
            print("抱歉，未找到该学员...")

    def show_all_student(self):
        """
        显示所有学员信息
        :return: None
        """
        print("{:<5s}{:<4s}{:<4s}{:<14s}{:<13s}{:<11s}".format("姓名", "年龄", "性别", "学号", "电话", "个人描述"))
        for student in self.student_lists:
            print("{:<5s}{:<5s}{:<4s}{:<15s}{:<15s}{:<11s}".format(student.name, student.age, student.gender,
                                                                   student.std_id, student.mobile, student.des))

    def load_data(self):
        # 打开文件 获取数据
        try:
            f = open('student.data', 'r', encoding="UTF-8")
        except FileNotFoundError:
            # 如果找不到文件，则创建文件
            f = open('student.data', 'w', encoding="UTF-8")
        # 获取数据(文件中的数据默认是字符串类型的)
        file_data = f.read()
        f.close()

        # 判断一下文件总的数据是否为空
        if len(file_data) == 0:
            # 为空则创建一个空列表
            file_data = '[]'

        # 数据类相的转化 字符串==>列表嵌套字典
        file_data = eval(file_data)
        # 把数据加载到student_lists
        self.student_lists = [Student(i["name"], i["age"], i["gender"], i["std_id"], i["mobile"], i["des"]) for i in
                              file_data]
        f.close()

    def save_data(self):
        f = open("student.data", "w", encoding="UTF-8")
        # 文件只能存储字符串
        f.write(str([student.__dict__ for student in self.student_lists]))
        f.close()

    def start(self):
        """
        启动系统
        :return:
        """
        # 加载数据
        self.load_data()

        # 显示版本
        print("=" * 37)
        print("|\t\t欢迎使用学员管理系统 V2.0\t\t|")
        print('=' * 37)

        # 模拟启动
        print("正在玩命加载中,请稍后", end='')
        # 用户等待
        time.sleep(0.2)
        print('.', end='')
        time.sleep(0.3)
        print('.', end='')
        time.sleep(0.4)
        print('.')
        time.sleep(0.5)

        # 显示界面
        m.menu()

        # 2.循环
        while True:
            # 2.1 用户输入
            while True:
                num = input("请输入操作序号: ")
                if num.isdigit():
                    option = int(num)
                    break
                else:
                    print("您输入的操作有误，请重新输入")
                    print("")

            # 2.2 判断
            if option == 1:
                #  添加学生
                print("--------添加学生---------")
                self.add_student()
            elif option == 2:
                # 删除学生
                print("--------删除学生---------")
                self.del_student()
            elif option == 3:
                # 修改学生
                print("--------修改学生---------")
                self.update_student()
            elif option == 4:
                # 查询学生
                print("-------查询学生信息-------")
                self.search_student()
            elif option == 5:
                # 显示所有学生
                print("-------显示所有学生-------")
                self.show_all_student()
            elif option == 0:
                # 退出前 保存数据
                self.save_data()

                # 退出确认
                out_str = input("您是否确认退出(Y/N): ")
                if out_str.lower() == 'y':
                    print('已退出系统\n感谢您的(测试)使用!!!')
                    return
                else:
                    continue

            else:
                print("新功能敬请期待...")

            print("")

# 测试功能
# if __name__ == '__main__':
#     stu = Studentcms()
#     stu.start()

# stu = Studentcms()
# print(stu.student_lists)
# stu.show_all_student()
# stu.add_student()
# stu.update_student()
# stu.search_student()

# print(stu.student_lists)
