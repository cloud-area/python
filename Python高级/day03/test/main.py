# 项目入口:只负责程序的进入,业务相关的各个功能都不要在这里实现
from studentcms import StudentCMS

# 程序入口:
if __name__ == '__main__':
    studentCMS = StudentCMS()
    studentCMS.start()