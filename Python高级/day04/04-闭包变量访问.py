# 1.函数嵌套:内外部函数(outer,inner)
# 2.有引用:内部函数引用外部函数的变量
# 3.有返回:外部函数要返回内部函数名
# 4.nonlocal声明后可以使用内部函数修改外部函数的变量
def outer():
    a = 1
    def inner():
        nonlocal a
        a=a+1
        print(f'a的取值{a}')
    return inner

f =outer()
f()
f()