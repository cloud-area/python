# # 关键字
# import keyword
# print(keyword.kwlist)

# # 变量
# a = 6
# b = 7
# c, d = 2, 2
# print(a, b, c, d)
#
# # 数据类型查看
# result = type("6")
# print(result)
# num = 10
# print(type(num))

# # 类型转换
# num = "6"
# # print(type(int(num)))
# print(4 + int(num))
# print(str(4) + num)
#
# score = input("请输入一个数字")
# print(type(score))
# print(score)
# print(int(score) + 6)

# # 运算符
# # 加法运算法
# print(1 + 2)
# print("1" + "2")
# print([1, 2] + [3, 4])
#
# # 减法运算符
# print(4 - 12)
#
# # 乘法运算符
# print(2 * 3)
#
# # 幂运算符
# print(2 ** 11)
#
# # 除法运算符
# print(5 / 2)
#
# # 整除运算符
# print(5 // 2)
# print(5.2 // 2)  # 5.2 / 2 = 2.6
#
# # 求模运算符（求余运算）
# print(5 % 2)
#

# a = 10
# b = 10
# print(id(a), id(b))  # 地址相同
# print(a is b)

# c = [1]
# d = [1]
# print(id(c), id(d))  # 地址不同
# print(a == b)  # 值相同
# print(c is d)

# # 链式比较运算符
# num = 4
# print(3 < num < 20)  # num > 3 && num < 20

# content = input("请输入内容：")  # 类型为str
# result = eval(content)  # 类型转换
# print(type(result))  # 类型为int
# print(result)

# # 输出格式化
# name = "sz"
# age = 18
# print("我的名字是%s, 年龄是%d" % (name, age))

# %[(name)][flags][width][.precision]typecode  #[]：可以省略
# (name):表示根据指定的名称（key），查找对应的值，格式化到字符串当中
# mathScore = 109
# englishScore = 58
# # print("数学分数是%d，英语分数是%d" % (mathScore, englishScore))
# print("数学分数是%(ms)d，英语分数是%(es)d" % ({"es": englishScore, "ms": mathScore}))
# # width：表示，占用的宽度
# print("%10d" % mathScore)
# # flags 对齐：- 表示左对齐；'空格' 表示左侧填充一个空格
# print("%-10d" % englishScore)
hours = 4
minutes = 5
seconds = 18
# 04:05:18
print("%02d:%02d:%02d" % (hours, minutes, seconds))