# -*- coding = utf-8 -*-

"""
将字符串“AI人工智能进阶班”转换为二进制bytes类型的结果
将二进制bytes数据 b"AI python"转换为字符串str类型的结果

"""
str_1 = 'AI人工智能进阶班'
print(str_1)
new_str = str_1.encode(encoding='utf-8')
print(new_str)

str_2 = b"AI python"
print(type(str_2))
new_str2 = str_2.decode(encoding='utf-8')
print(type(new_str2))
print(new_str2)