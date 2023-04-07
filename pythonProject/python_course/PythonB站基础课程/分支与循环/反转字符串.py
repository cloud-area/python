"""
反转字符串
原字符串: "爱我中华"
反转后: "华中我爱"

"""

notice = "爱我中华"
result = ""

for c in notice:
    result = c + result
    # print(c)
print(result)
