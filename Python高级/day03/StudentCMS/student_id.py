# -*- coding = utf-8 -*-
import time


def student_id():
    """
    利用时间戳，生成学生学号
    :return:
    """
    # 获取时间戳
    i = int(time.time())

    # 获取时间戳后5位，作为唯一值
    only_num = str("%05d" % (i - (i // 100000) * 100000))
    time_tuple = time.localtime(time.time())

    # 年作为前4位
    year= str(time_tuple[0])

    # 月作为5、6位
    month = str("%02d" % int(time_tuple[1]))
    std_id = year + month + only_num

    # 返回学号
    return std_id


# 功能测试
# print(student_id())
