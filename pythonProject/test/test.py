def binary_search(list_1, item):
    """
    二分法查找有序数组元素
    :param list_1:
    :param item:
    :return:
    """
    # low和high用于跟踪要在其中查找的列表部分
    low = 0
    high = len(list_1)-1

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