"""
循环练习

"""

# print("6\n" * 10)

# while 条件
"""
注意：循环需要考虑好结束！
1.修改条件
2.打断循环，break
"""

# num = 0
# condition = True
# while condition:
#     print("adc")
#     num += 1
#     print(num)
#     if num == 10:
#         condition = False

num = 0
while num < 10:
    num += 1
    num1 = 0
    while num < 10:
        num1 += 1
        print("num:%d  num1:%d" % (num, num1))
        if num1 == 10:
            break
else:
    print("最后的num:", num)
    print("整个循环完毕")
