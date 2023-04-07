# 存储学生信息的列表
student_info = []


def show_menu():
    """
    这里是菜单 供用户选择
    :return: None
    """
    print('-' * 20)
    print('欢迎登录学员管理系统')
    print('1: 添加学员')
    print('2: 删除学员')
    print('3: 修改学员信息')
    print('4: 查询学员信息')
    print('5: 显示所有学员信息')
    print('6: 退出系统')
    print('-' * 20)


def show_all_info():
    """
    显示所有的学生的信息
    :return: None
    """
    print("姓名\t年龄\t电话")
    # i ==> {"name": "老王", "age": 18, "tel": 110}
    for i in student_info:
        print(f'{i["name"]}\t{i["age"]}\t{i["tel"]}')


def add_student_info():
    """
    添加学生的信息
    :return:
    """
    # 如果全局变量是一个可变数据类型 不声明global 也是可以修改的
    # 如果全局变量是一个不可变数据类型 不声明global 是不可以修改的
    # 不管是不是可变类型 只要在函数中修改全局变量 都应该声明全局变量global
    global student_info
    # 获取要添加的学生信息
    add_tel = int(input("请输入要添加的人的电话:"))
    # 查看要添加的人的电话是否有重复的
    # i ==> {"name": "老王", "age": 18, "tel": 110}
    for i in student_info:
        if i["tel"] == add_tel:
            print("此人已存在!!!")
            return
    else:
        # 如果能够执行else证明 没有人的电话和add_tel重复
        add_name = input("请输入要添加的人的姓名:")
        add_age = int(input("请输入要添加的人的年龄:"))
        # 定义一个字典用来存储要添加的学生的信息
        add_dict = {"name": add_name, "age": add_age, "tel": add_tel}
        # 信息添加到字典中
        # 把字典添加到列表中
        student_info.append(add_dict)
        print("添加完毕!!!")


def del_student_info():
    """
    删除指定的学生信息
    :return: None
    """
    global student_info
    # 获取要删除的学生信息
    del_tel = int(input("请输入要删除的人的电话:"))
    # 查找一下有没有要是删除的人
    # i ==> {"name": "老王", "age": 18, "tel": 110}
    for i in student_info:
        if i["tel"] == del_tel:
            # 如果if语句成立 证明要删除的人是存在
            student_info.remove(i)
            print("删除完毕!!!")
            return
    else:
        # 如果执行else证明 要删除的人不存在的
        print("查无此人!!!")


def change_student_info():
    """
    修改学生信息的
    :return: None
    """
    global student_info
    # 获取要修改的人的电话
    change_tel = int(input('请输入要修改信息的人的电话:'))
    # 查找一下有没有这个人
    for i in student_info:
        # i ==> {"name": "老王", "age": 18, "tel": 110}
        if i["tel"] == change_tel:
            # 如果if语句成立 证明要修改的人存在
            change_name = input("请输入修改后的人的姓名:")
            change_age = int(input("情输入修改后的人的年龄:"))
            change_tel = int(input("情输入修改后的人的电话:"))
            # 修改信息了
            i["name"] = change_name
            i["age"] = change_age
            i["tel"] = change_tel
            print("修改完毕!!!")
            return
    else:
        # 如果执行这里的else 证明要修改的人不存在
        print('查无此人!!!')


def search_student_info():
    """
    查找学生信息
    :return:
    """
    # 获取要查找的人的电话
    search_tel = int(input("请输入要查找的人的电话:"))

    for i in student_info:
        if i["tel"] == search_tel:
            print(f"姓名:{i['name']} 年龄:{i['age']} 电话:{i['tel']}")
            return
    else:
        print("查无此人!!!")


def load_data():
    """数据加载"""
    global student_info

    # 打开文件 获取数据
    f = open("./data.txt", "r", encoding="utf8")
    # 获取数据(文件中的数据默认是字符串类型的)
    file_data = f.read()
    f.close()
    # 判断一下文件总的数据是否为空
    if len(file_data) > 0:
        # 如果执行if语句 证明文件中是有数据的
        # 数据类相的转化 字符串==>列表嵌套字典
        file_data = eval(file_data)
        # 把数据加载到student_info
        # file_data ==> [{"name": "老王", "age": 18, "tel": 110}, {"name": "老李", "age": 18, "tel": 120}]
        student_info = file_data
    else:
        # 如果执行else 证明文件中没有数据
        return


def save_data():
    """存储数据"""
    f = open("data.txt", "w", encoding="utf8")
    # 文件只能存储字符串
    f.write(str(student_info))
    f.close()


def main():
    """
    作为一个程序的总流程
    :return: None
    """

    # 加载数据
    load_data()

    while True:
        # 展示菜单
        show_menu()
        # 获取用户选项
        num = input('请输入您的选项:')
        # 判断用户选项
        if num == "1":
            add_student_info()
        elif num == "2":
            del_student_info()
        elif num == "3":
            change_student_info()
        elif num == "4":
            search_student_info()
        elif num == "5":
            show_all_info()
        elif num == "6":
            # 退出前 保存数据
            save_data()
            print("谢谢使用!!!")
            return
        else:
            print("选项错误!!!")

        input("按回车继续执行")


if __name__ == '__main__':
    # show_menu()
    # 程序的入口
    main()
