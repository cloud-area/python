# -*- coding = utf-8 -*-

"""
正则表达式 re
匹配字符串首个字符

"""
import re

""".匹配任意单个字符"""
# match_obj = re.match('it..', 'it_cast')
# # 获取结果
# if match_obj:
#     result = match_obj.group()
#     print(result)
# else:
#     print("未匹配成功！")


"""[]匹配其中列举的字符"""
# match_obj1 = re.match('[it]', 'it_cast')
# # 获取结果
# if match_obj1:
#     result = match_obj1.group()
#     print(result)
# else:
#     print("未匹配成功！")


"""[^]匹配除了指定字符以外的所有字符"""
# match_obj2 = re.match('[^a-z]','Abase')
# # 获取结果
# if match_obj2:
#     result = match_obj2.group()
#     print(result)
# else:
#     print("未匹配成功！")


"""\d匹配数字，即0-9"""
# match_obj3 = re.match('\d','23_cat')
# # 获取结果
# if match_obj3:
#     result = match_obj3.group()
#     print(result)
# else:
#     print("未匹配成功！")


"""\D匹配非数字，即不是数字"""
# match_obj4 = re.match('\D','it_2_cat')
# # 获取结果
# if match_obj4:
#     result = match_obj4.group()
#     print(result)
# else:
#     print("未匹配成功！")


"""\s匹配空白，即空格，tab键"""
# match_obj5 = re.match('\s','    it_cat')
# # 获取结果
# if match_obj5:
#     result = match_obj5.group()
#     print(result+'找到')
# else:
#     print("未匹配成功！")


"""\S匹配非空白"""
# match_obj6 = re.match('\S','it cat')
# # 获取结果
# if match_obj6:
#     result = match_obj6.group()
#     print(result)
# else:
#     print("未匹配成功！")


"""\w匹配非特殊字符，即a-z，A-Z，0-9，_，汉字"""
# match_obj7 = re.match('\w','北京今日15℃')
# # 获取结果
# if match_obj7:
#     result = match_obj7.group()
#     print(result)
# else:
#     print("未匹配成功！")


"""\W匹配特殊字符，即非字母，非数字，非汉字"""
match_obj8 = re.match('\W','&北京今日15℃')
# 获取结果
if match_obj8:
    result = match_obj8.group()
    print(result)
else:
    print("未匹配成功！")

