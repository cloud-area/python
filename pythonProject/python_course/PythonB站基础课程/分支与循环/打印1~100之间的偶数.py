"""
打印1~100之间的偶数

"""
# 1-100这样的集合
# 函数 -> range
for num in range(1, 101):
    # 怎样去判定偶数
    if num % 2 == 0:
        print(num)
