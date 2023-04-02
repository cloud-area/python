# 学生信息系统管理类
from student import Student
import time

# 1.定义类
class StudentCMS(object):

    # 1.1 属性
    def __init__(self):
        self.student_list = []

    # 1.2 方法
    # 1.2.1 显示界面
    @staticmethod
    def show_info():
        print("*"*40)
        print('本学员管理系统V2.0完成一下操作:')
        print('\t1.添加学员')
        print('\t2.修改学员')
        print('\t3.删除学员')
        print('\t4.查询某个学员')
        print('\t5.显示所有学员')
        print('\t6.保存学员')
        print('\t0.退出系统')
        print("*"*40)

    # 加载文件中的学员信息
    def load_data(self):
        # 1.打开文件
        try:
            student_read=open('data/student.data','r',encoding='utf-8')
        except:
            student_read = open('data/student.data', 'w', encoding='utf-8')
        # 2.读取数据,进行转换,添加到list
        data = student_read.read()
        if len(data)== 0:
            data = '[]'
        # print(data)
        data_list=eval(data)
        #print(data_list)
        self.student_list=[Student(student_dict['name'],student_dict['age'],student_dict['gender'],student_dict['mobile'],student_dict['des']) for student_dict in data_list]
        # 3.关闭文件
        student_read.close()


    # 添加学员
    def add_student(self):
        # 1.创建学生对象
        name = input('请输入学生姓名:')
        gender = input('请输入学生性别:')
        age = int(input('请输入学生年龄:'))
        mobile = input('请输入学生联系方法:')
        des = input('请输入学生备注信息:')
        student =Student(name,age,gender,mobile,des)
        # print(student)
        # 2.添加到list
        self.student_list.append(student)
        # print(self.student_list)

    # 修改学员信息
    def update_student(self):
        # 1.输入学员名称
        update_name =input('请输入要修改的学员姓名:')
        # 2.查找学员,进行修改
        for student in self.student_list:
            if student.name == update_name:
                student.age = input('请输入学员年龄:')
                student.gender = input('请输入学员的性别:')
                student.mobile = input('请输入学员手机号:')
                student.des = input('请输入学员备注信息:')
                break
        else:
            print('查无此人')

    # 删除学员
    def del_student(self):
        # 1.输入要删除的学员
        del_name = input('请输入要删除的学员姓名:')
        # 2.查找学员,找到就删除
        for student in self.student_list:
            if student.name == del_name:
                self.student_list.remove(student)
                break
        else:
            print('查无此人')

    # 查询某个学员
    def search_student(self):
        # 1.输入要查询的学员姓名
        search_name =input('请输入要查询的学员姓名:')
        # 2.查找学员
        for student in self.student_list:
            if student.name == search_name:
                print(student)
                break
        else:
            print('查无此人')

    # 显示所有学员信息
    def show_all_student(self):
        # 1.遍历列表
        print('\t姓名\t性别\t年龄\t电话\t备注')
        for student in self.student_list:
            # 2.输出每个学员信息
            # print(student)
            print(f'\t{student.name}\t{student.gender}\t{student.age}\t{student.mobile}\t{student.des}')
    # 保存学员信息
    def save_student(self):
        # 1.打开文件
        student_write =open('data/student.data','w',encoding='utf-8')
        # 2.写入数据
        list =str([student.__dict__ for student in self.student_list])
        student_write.write(list)
        # 3.close
        student_write.close()


    # 循环的实现
    def start(self):
        # 1.用户等待
        time.sleep(1)
        # # 供测试使用,最后应该删除
        # s1 = Student('小红',16,'女',10087,'高中生')
        # self.student_list.append(s1)
        # s2 = Student('小灰', 16, '男', 10077, '高中生')
        # self.student_list.append(s2)
        # s3 = Student('小明', 16, '男', 10088, '高中生')
        # self.student_list.append(s3)
        self.load_data()
        # 2.循环
        while True:
            # 2.1 显示界面
            StudentCMS.show_info()
            # 2.2 用户输入
            num = int(input('请输入要执行的任务对应序号:'))
            # 2.3 判断:增加容错性
            if num == 1:
                print('请添加学员:')
                self.add_student()
            elif num == 2:
                print('请修改学员:')
                self.update_student()
            elif num == 3:
                print('请删除学员:')
                self.del_student()
            elif num == 4:
                print('请查询学员')
                self.search_student()
            elif num == 5:
                print('请查询所有学员')
                self.show_all_student()
            elif num == 6:
                print('请保存学员')
                self.save_student()
            elif num == 0:
                str = input('你是否要退出系统(Y/N):')
                if str.lower() == "y":
                    print('退出系统,再见')
                    break

            else:
                print('请输入0-6之间的序号,新的功能敬请期待')



# 2.测试功能
if __name__ == '__main__':
    # StudentCMS.show_info()
    stu = StudentCMS()
    stu.start()
