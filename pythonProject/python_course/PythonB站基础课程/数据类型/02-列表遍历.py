"""列表的遍历操作

"""
# 方法1
# 根据元素进行遍历
# for item in list:
# print(item)

values = ["a", "b", "c", "d"]
# 添加一个计数器
currentIndex = 0
for i in values:
    print(i)
    print(values.index(i, currentIndex))
    currentIndex += 1
