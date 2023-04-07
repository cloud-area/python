# -*- coding = utf-8 -*-

"""
随着排序的进行，每次需要检查的元素数在逐渐减少，最后一次需要检查的元素都只有一个。
既然如此，运行时间怎么还是O(n2)呢？
第一次需要检查n个元素，但随后检查的元素数依次为 n-1, n–2, …, 2和 1。平均每次检查的元素数为 1/2×n，因此运行时间为(n×1/2×n)。

"""
def find_smallest(arr):
    """
    找出数组中最小元素
    :param arr: 数组
    :return: 元素索引
    """
    # 存储最小的值
    smallest = arr[0]
    # 存储最小元素的索引
    smallest_index = 0
    # for循环依次比较
    for i in range(1, len(arr)):
        # 找出比其他元素都小的元素
        if arr[i] < smallest:
            # 最小值
            smallest = arr[i]
            # 最小元素索引
            smallest_index = i
    # 返回最小元素的索引
    return smallest_index

def selection_sort(arr):
    """
    选择排序算法
    :param arr:数组
    :return: 排序好的数组
    """
    # 建立一个新的数组用于存储元素
    new_arr = []
    # 依次将查找到的值放入到新数组中
    for i in range(len(arr)):
        # 将元素按照从小到大依次放入
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    # 返回顺序数组
    return new_arr

# 测试一下
# 定义一个无序数组
list_1= [5,3,6,2,10]

# 排序输出
print(selection_sort(list_1))