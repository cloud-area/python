import time

# def a():
#     print('1')
#     def b():
#         print('2')
#     return b
#
#
# a
# print(a)
# a()
# print(a())
print('1')
time.sleep(2)

def a():
    def b():
        pass
        return 1
    return b
print()

time.sleep(2)
a()
print(a())
