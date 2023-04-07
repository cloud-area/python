# 1.定义函数
def func():
    print('这是一个函数')

# 2.查看函数的作用
# func()
# 2.1 函数名
print(func)
# 2.2 调用函数
func()
# 2.3 函数名可以像其他一样赋值
func2 = func
print(func2)
# 2.4 变量执行函数
func2()