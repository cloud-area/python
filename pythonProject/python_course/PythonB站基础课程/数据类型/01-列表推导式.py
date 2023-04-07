"""
[表达式 for 变量 in 列表]

"""

nums = [1, 2, 3, 4, 5]
resultList = [num ** 2 for num in nums]
resultList1 = [1 for num in nums]
print(resultList)
print(resultList1)

resultList2 = [num ** 2 for num in nums if num % 2 != 0]
print(resultList2)
