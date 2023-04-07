# import turtle as t
# import time

# turtle.pen()
# turtle.mainloop()  # 画面保持

"""
绘制正方形

turtle.setup(800, 400)  # 调整画板大小
turtle.up()  # 提起笔
turtle.goto(-50, 50)  # 调整画板起始点
turtle.down()  # 放下笔
turtle.color("red")  # 画笔颜色
turtle.speed(1)  # 控制绘画速度

# 画图过程
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
# 保持画面
turtle.mainloop()
"""

# t.color("red", "yellow")
# t.speed(1)
# t.begin_fill()
# for _ in range(25):
#     t.forward(200)
#     t.left(165)
#
# t.end_fill()
# time.sleep(5)

from turtle import *

def tree(branch_len, tut):
    if branch_len > 5:
        tut.forward(branch_len)
        tut.right(20)
        tree(branch_len - 15, tut)
        tut.left(40)
        tree(branch_len - 10, tut)
        tut.right(20)
        tut.backward(branch_len)


t = Turtle()
TurtleScreen = t.getscreen()  # 获取屏幕
t.speed()
# t.hideturtle()  # 隐藏箭头
t.left(90)  # 掉转绘制方向朝上
t.up()  # 画笔离开
t.backward(300)  # 将画笔移动到屏幕下方
t.down()  # 画笔落下
t.color("green")  # 调整画笔颜色
tree(110, t)  # 调用绘制函数
TurtleScreen.exitonclick()  # 点击关闭屏幕
