# -*- coding = utf-8 -*-

"""
re 模块匹配多个字符

"""
import re

""" *匹配前一个字符出现0次或者无限次，即可有可无"""
match_obj1 = re.match('[a-z]*','it_cast')
match_obj1_1 = re.match('[a-z]*','0it_cast')
# 获取结果
if match_obj1:
    result = match_obj1.group()
    print(result)
else:
    print("未匹配成功！")
if match_obj1_1:
    result = match_obj1_1.group()
    print(result)
else:
    print("未匹配成功！")


""" +匹配前一个字符出现1次或者无限次，即至少有1次"""
# match_obj2 = re.match('[a-z]+','it_cast')
# match_obj2_1 = re.match('[a-z]+','0it_cast')
# # 获取结果
# if match_obj2:
#     result = match_obj2.group()
#     print(result)
# else:
#     print("未匹配成功！")
# # 获取结果
# if match_obj2_1:
#     result = match_obj2_1.group()
#     print(result)
# else:
#     print("未匹配成功！")

""" ?匹配前一个字符出现1次或者0次，即要么有1次，要么没有"""
# match_obj3 = re.match('[it]?','iit_is_cast_it)')
# match_obj3_1 = re.match('[it]?','0is_cast')
# # 获取结果
# if match_obj3:
#     result = match_obj3.group()
#     print(result)
# else:
#     print("未匹配成功！")
# # 获取结果
# if match_obj3_1:
#     result = match_obj3_1.group()
#     print(result)
# else:
#     print("未匹配成功！")


""" {m}匹配前一个字符出现m次"""
# match_obj4 = re.match('[\w]{5}','iit_is_cast_it)')
# match_obj4_1 = re.match('[\w]{2}','0is')
# # 获取结果
# if match_obj4:
#     result = match_obj4.group()
#     print(result)
# else:
#     print("未匹配成功！")
# # 获取结果
# if match_obj4_1:
#     result = match_obj4_1.group()
#     print(result)
# else:
#     print("未匹配成功！")


""" {m,n}匹配前一个字符出现从m到n次"""
# match_obj5 = re.match('\w{2,5}','iit_is_cast_it)')
# match_obj5_1 = re.match('\w{2,5}','0is')
# # 获取结果
# if match_obj5:
#     result = match_obj5.group()
#     print(result)
# else:
#     print("未匹配成功！")
# # 获取结果
# if match_obj5_1:
#     result = match_obj5_1.group()
#     print(result)
# else:
#     print("未匹配成功！")