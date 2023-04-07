# -*- coding = utf-8 -*-

"""
函数binary_search接受一个有序数组和一个元素。
如果指定的元素包含在数组中，这个函数将返回其位置。
你将跟踪要在其中查找的数组部分——开始时整个数组。

"""


def binary_search(list_1, item):
    """
    二分法查找有序数组元素
    :param list_1: 有序数组
    :param item: 查找的元素
    :return: 元素位置
    """
    # low和high用于跟踪要在其中查找的列表部分
    low = 0
    high = len(list_1) - 1

    # 只要范围没有缩小到只包含一个元素
    while low <= high:
        mid = (low + high)  # 就查找中间的元素
        guess = list_1[mid]

        # 找到了元素
        if guess == item:
            return mid

        # 猜的数字打了
        elif guess > item:
            high = mid - 1

        # 猜的数字小了
        else:
            low = mid + 1

    # 若没有指定的元素
    return None


# 测试一下
# 给定一个有序数组
my_list = [1, 3, 5, 7, 9]

# 打印元素3
print(binary_search(my_list, 3))

# 打印元素-1(不在此数组中)
print(binary_search(my_list, -1))
