"""
做一个简单的加法计算器，让用户输入两个数值，输出对应的和
要求：
    用户如果不退出这个程序，则输出完毕之后，继续让用户使用
    如果中间用户输入的数据有误，则给出错误提示，并从头开始，让用户数据数值

"""

# # 1.获取用户输入的两个数值
# num1 = float(input("请输入第一个数值: "))
# num2 = float(input("请输入第二个数值: "))
# # 2.计算两个数值的和
# result = num1 + num2
#
# # 3.输出数值
# print("你计算的结果是: ", result)


while True:
    # 1.获取用户输入的两个数值
    num1 = float(input("请输入第一个数值: "))
    num2 = float(input("请输入第二个数值: "))

    # 输入值大于100则异常
    if num1 > 100 or num2 > 100:
        print("您输入的数据有误！请重新输入")
        continue
    # 2.计算两个数值的和
    result = num1 + num2

    # 3.输出数值
    print("你计算的结果是: ", result)

    isQ = input("是否想要退出(q: 退出，其他: 不退出，继续)")
    if isQ == 'q':
        break
