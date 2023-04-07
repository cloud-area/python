# Python 3.10

# - 输入
# 	- 身高
personHeight = input("请输入身高（m）:")
personHeight = float(personHeight)
# 	- 体重
personWeight = input("请输入体重（kg）:")
personWeight = float(personWeight)
# 	- 年龄
personAge = input("请输入年龄:")
personAge = int(personAge)
# 	- 性别
personSex = input("请输入性别（男:1 女:0）:")
personSex = int(personSex)


# - 处理数据
# 	- 计算体脂率
# BMI = 体重(kg) / (身高 * 身高)(米)
# 体脂率 = 1.2 * BMI + 0.23 * 年龄 - 5.4 - 10.8 * 性别(男: 1   女: 0)
BMI = personWeight / (personHeight * personHeight)
TZL = 1.2 * BMI + 0.23 * personAge - 5.4 - 10.8 * personSex

# 	- 判定体脂率，是否在正常的标准范围之内
# 正常成年人的体脂率分别是男性15%~18%和女性25%~28%
# TZL  MIN  MAX
minNum = 15 + 10 * (1 - personSex)
maxNum = 18 + 10 * (1 - personSex)

result = (minNum < TZL < maxNum)

# - 输出：告诉用户，是否正常
print("你的体脂率是：%.3f%%" % TZL)
print("你的体脂率，是否符合标准", result)
