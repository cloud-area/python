# age = int(input("年龄输入："))
# if age < 0:
#     print("年龄输入错误！")
# else:
#     if age >= 18:
#         print("你已经成年")
#     else:
#         print("赶紧回家吃饭")
"""
根据分数区间，打印对应的级别
100~90: 优秀
90~80: 良好
60~80: 及格
0~60: 不及格
"""
score = int(input("请输入成绩(0~100)："))

# if score >= 90 and score <= 100:
#     print("优秀")
# else:
#     if score >= 80 and score < 60:
#         print("良好")
#     else:
#         if score >= 60 and score < 80:
#             print("及格")
#         else:
#             if score >= 0 and score < 60:
#                 print("不及格")

# 链表判断
# if 90 <= score <= 100:
#     print("优秀")
# if 80 <= score < 90:
#     print("良好")
# if 60 <= score < 80:
#     print("及格")
# if 0 <= score < 60:
#     print("不及格")

# if 90 <= score <= 100:  # 可阅读性比较差
#     print("优秀")
# else:
#     if 80 <= score:
#         print("良好")
#     else:
#         if 60 <= score:
#             print("及格")
#         else:
#             print("不及格")

if 90 <= score <= 100:
    print("优秀")
elif 80 <= score < 90:
    print("良好")
elif 60 <= score < 80:
    print("及格")
elif 0 <= score < 60:
    print("不及格")
else:
    print("成绩输入有误！")


