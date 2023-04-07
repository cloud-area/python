# -*- coding = utf-8 -*-

"""
re模块提取分组数据

"""
import re


# def str_search(list_str):
#     """
#     |匹配左右任意一个表达式
#     :param list_str:
#     :return:
#     """
#     for i in range(len(list_str)):
#         str_1 = list_str[i]
#         match_str = re.match('apple|pear', str_1)
#         if match_str:
#             result = match_str.group()
#             print(f"匹配成功的结果: {result}")
#
#         else:
#             print("未匹配成功")
#
#
# list_1 = ['apple', 'banana', 'orange', 'pear']
# str_search(list_1)


# def qq_search(list_qq):
#     """
#     (ab)将括号中字符作为一个分组
#     :param list_qq:
#     :return:
#     """
#     match_qq = re.match('([a-z]{2})(\W)([0-9]{5,10})', list_qq)
#     if match_qq:
#         result_1 = match_qq.group(1)
#         result_2 = match_qq.group(2)
#         result_3 = match_qq.group(3)
#         print(f"匹配成功的结果: {result_1}")
#         # print(type(result_1))
#         print(f"匹配成功的结果: {result_2}")
#         # print(type(result_2))
#         print(f"匹配成功的结果: {result_3}")
#     else:
#         print("未匹配成功！")


# str_1 = "qq:908725367"
# qq_search(str_1)


def html_search(str_html):
    """
    \num引用分组num匹配到的字符串
    :param str_html:
    :return:
    """
    match_html = re.match('<([a-z]{4})><([a-z,0-9]{2})>([a-z]{3}).([a-z]{3,20}).([a-z]{2,5})<(/\\2)><(/\\1)>',str_html)
    if match_html:
        result_1 = match_html.group(1)
        result_2 = match_html.group(2)
        result_3 = match_html.group(3)
        result_4 = match_html.group(4)
        result_5 = match_html.group(5)
        result_6 = match_html.group(6)
        result_7 = match_html.group(7)
        print(f"匹配成功的结果: {result_1}")
        print(f"匹配成功的结果: {result_2}")
        print(f"匹配成功的结果: {result_3}")
        print(f"匹配成功的结果: {result_4}")
        print(f"匹配成功的结果: {result_5}")
        print(f"匹配成功的结果: {result_6}")
        print(f"匹配成功的结果: {result_7}")
    print('\n')

    match_html_2 = re.match('<([a-z]{4})><([a-z0-9]{2})>(.*)<(/\\2)><(/\\1)>', str_html)
    if match_html_2:
        result_1 = match_html_2.group(1)
        result_2 = match_html_2.group(2)
        result_3 = match_html_2.group(3)
        result_4 = match_html_2.group(4)
        result_5 = match_html_2.group(5)
        print(f"匹配成功的结果: {result_1}")
        print(f"匹配成功的结果: {result_2}")
        print(f"匹配成功的结果: {result_3}")
        print(f"匹配成功的结果: {result_4}")
        print(f"匹配成功的结果: {result_5}")

str_2 = '<html><h1>www.itcast.cn</h1></html>'
html_search(str_2)
print("-"*20)
str_3 = '<html><h2>www.baidu.cn</h2></html>'
html_search(str_3)