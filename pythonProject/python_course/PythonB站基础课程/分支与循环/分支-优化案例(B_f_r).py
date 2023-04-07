# Python 3.10

# - 输入
# 	- 身高
personHeight = input("请输入身高（m）:")
personHeight = float(personHeight)
if not (0 < personHeight < 3):
    print("身高数据有误！")
    exit()
# 	- 体重
personWeight = input("请输入体重（kg）:")
personWeight = float(personWeight)
if not (0 < personWeight < 300):
    print("体重数据有误！")
    exit()
# 	- 年龄
personAge = input("请输入年龄:")
personAge = int(personAge)
if not (0 < personAge < 150):
    print("年龄数据有误！")
    exit()
# 	- 性别
personSex = input("请输入性别（男:1 女:0）:")
personSex = int(personSex)
if not (personSex == 0 or personSex == 1):
    print("性别数据有误！")
    exit()
"""
# 容错处理：数据有效性的验证
if not(0 < personHeight < 3 and 0 < personWeight < 300 and 0 < personAge < 150 and (personSex == 1 or personSex == 0)):
    # 退出程序
    print("数据不满足需求")
    exit()
"""

# - 处理数据
# 	- 计算体脂率
# BMI = 体重(kg) / (身高 * 身高)(米)
# 体脂率 = 1.2 * BMI + 0.23 * 年龄 - 5.4 - 10.8 * 性别(男: 1   女: 0)
BMI = personWeight / (personHeight * personHeight)
TZL = 1.2 * BMI + 0.23 * personAge - 5.4 - 10.8 * personSex
TZL /= 100

# 	- 判定体脂率，是否在正常的标准范围之内
# 正常成年人的体脂率分别是男性15%~18%和女性25%~28%
# TZL  MIN  MAX

# 区分男女
if personSex == 1:
    # 判断男性标准的代码
    result = 0.15 < TZL < 0.18
    minNum = 0.15
    maxNum = 0.18
elif personSex == 0:
    # 判断女性标准的代码
    result: bool = 0.25 < TZL < 0.28
    minNum = 0.25
    maxNum = 0.28

# minNum = 0.15 + 0.10 * (1 - personSex)
# maxNum = 0.18 + 0.10 * (1 - personSex)
#
# result = (minNum < TZL < maxNum)

# - 输出：告诉用户，是否正常
print("你的体脂率是：%.2f%%" % (TZL * 100))
print("你的体脂率，是否符合标准", bool)

# 问好
if personSex == 1:
    WenHao = "先生你好,"
elif personSex == 0:
    WenHao = "女士你好,"

# 提示部分
if bool:
    notice = "恭喜你，身体非常健康，请继续保持"
else:
    # 偏胖的条件
    if TZL > maxNum:
        notice = "请注意，您的身体偏胖"
    # 偏瘦的条件
    else:
        notice = "请注意，您的身体偏瘦"

print(WenHao, notice)
