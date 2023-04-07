# -*- coding = utf-8 -*-

"""
一种优雅的解决方法。
盒子套盒子找钥匙

"""

"""
方法一:
1.创建一个要查找的盒子堆
2.从盒子堆取出一个盒子，在里面找
3.如果找出的是盒子，就将其加入盒子堆中，以便以后再查找
4.如果找到钥匙，则大功告成！
5.回到第二步
"""
# 伪代码复现
# def look_for_key(main_box):
#     pile = main_box.make_a_pile_to_look_through()
#     while pile != None:
#         box = pile.grab_a_box()
#         for item in box:
#             if item.is_a_box():
#                 pile.append(item)
#             elif item.is_a_key():
#                 print("found the key")

"""
方法二:
1.检查盒子中的每样东西
2.如果是盒子，就回到第一步
3.如果是钥匙，就大功告成！
"""
# 伪代码复现
# def look_for_key(box):
#     for item in box:
#         if item.is_a_box():
#             look_for_key(item)  # 递归
#         elif item.is_a_key():
#             print("found the key!")