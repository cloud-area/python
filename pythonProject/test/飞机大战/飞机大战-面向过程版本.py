import pygame
# 从我们的pygame中 导入所有的事件变量
# 可以直接使用这里的变量
from pygame.locals import *
import time
hero_x = 150
hero_y = 600

# 存放子弹
hero_bullet = []

enemy_x = 150
enemy_path = "right"
a = pygame.image.load("feiji/enemy0_down1.png")
b = pygame.image.load("feiji/enemy0_down2.png")
c = pygame.image.load("feiji/enemy0_down3.png")
d = pygame.image.load("feiji/enemy0_down4.png")
enemy_blowup = [a,b,c,d]
enemy_num = 0
enemy_life = "活着"

def hero_plane(screen,hero,bullet):
    global hero_x,hero_y
    """英雄飞机的相关操作"""
    # 给窗体加英雄飞机
    screen.blit(hero, (hero_x, hero_y))
    # 第一次循环:(150,600) 第二次循环(150,595)
    # hero_y -= 10
    # 获取键盘按键 按键盘就是一个事件
    # 获取所有的事件
    for event in pygame.event.get():
        # 判断一下事件的类型
        # pygame中有对应的数值代表了对应的时间
        if event.type == QUIT:
            # 游戏结束
            exit()
        # 按一次键盘的事件 (按下去)
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                hero_x += 10
            elif event.key == K_LEFT:
                hero_x -= 10
            elif event.key == K_UP:
                hero_y -= 10
            elif event.key == K_DOWN:
                hero_y += 10
            elif event.key == K_SPACE:
                print("发射子弹")
                # 每一次按空格 就像列表里添加一个字典(子弹)
                hero_bullet.append({"x":hero_x+40,"y":hero_y - 20})
                # screen.blit(bullet,(hero_x + 40,hero_y - 20))

    # 从弹夹里拿子弹 让子弹不断的向上走
    for i in hero_bullet:
        # hero_bullet  ==> [{"x":hero_x+40,"y":hero_y - 20},{},{}]
        # i ==> {"x":hero_x+40,"y":hero_y - 20}
        screen.blit(bullet, (i["x"], i["y"]))
        # screen.blit(bullet, (i["x"], i["y"]))
        i["y"] -= 10

def enemy_plane(screen,enemy):
    global enemy_x
    global enemy_path
    global enemy_num
    global enemy_life

    # 挡子弹碰到敌人飞机的时候 飞机就爆炸了
    # 敌人飞机的(x,y) 子弹的(x,y) 相等了 子弹碰到了飞机
    for i in hero_bullet:
    # hero_bullet  ==> [{"x":hero_x+40,"y":hero_y - 20},{},{}]
    # i ==> {"x":hero_x+40,"y":hero_y - 20}
        if i["x"] == enemy_x+20 and i["y"] == 10:
            enemy_life = "死了"

    if enemy_life == "活着":
        # 把敌人飞机贴到屏幕上
        screen.blit(enemy,(enemy_x+20,10))
        # 设置敌人飞机的方向
        if enemy_x >= 350:
            enemy_path = "left"
        elif enemy_x <= -20:
            enemy_path = "right"

        # 判断敌人飞机的方向
        if enemy_path == "right":
            enemy_x += 10
        elif enemy_path == "left":
            enemy_x -= 10
    elif enemy_life == "死了":
        # 让敌人飞机爆炸
        if enemy_num <= 3:
            screen.blit(enemy_blowup[enemy_num],(enemy_x+20,10))
            enemy_num += 1

def main():
    # 1 搭建游戏窗体
    # display : 展示
    # image : 加载图片
    # 参数1: ()元组 宽 高
    screen = pygame.display.set_mode((400,800),0,32)
    # 加载背景图片
    background = pygame.image.load("feiji/background.png")
    # 加载英雄图片
    hero = pygame.image.load("feiji/hero1.png")
    # 子弹图片
    bullet = pygame.image.load("feiji/bullet1.png")
    # 敌人飞机
    enemy = pygame.image.load("feiji/enemy0.png")

    while True:
        # 循环贴图
        # 给窗体加背景
        # 参数1 要粘贴的图片
        # 参数2 图片的粘贴位置==>元组(x,y)
        screen.blit(background,(0,0))
        # 给窗体加英雄飞机
        hero_plane(screen,hero,bullet)
        # 给窗体加敌人飞机
        enemy_plane(screen,enemy)
        # 展示数据的更新
        pygame.display.update()
        # 让我们的程序这里休息0.1
        time.sleep(0.1)

main()