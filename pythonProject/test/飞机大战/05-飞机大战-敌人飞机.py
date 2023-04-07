import pygame
import time
from pygame.locals import *

hero_x = 150
hero_y = 600
# 子弹夹
my_bullet = []

enemy_x = 130
enemy_path = "right"

def hero_plane(screen, hero, bullet):
    global hero_x
    global hero_y
    global my_bullet
    # 显示英雄飞机
    screen.blit(hero,(hero_x, hero_y))
    # 事件捕获 捕获事件放在一个列表中
    for event in pygame.event.get():
        # 关闭游戏了
        if event.type == QUIT:
            # 直接退出游戏
            exit()
        # 键盘按键
        elif event.type == KEYDOWN:
            # 右方向键
            if event.key == K_RIGHT:
                hero_x += 10
            elif event.key == K_LEFT:
                hero_x -= 10
            elif event.key == K_DOWN:
                hero_y += 10
            elif event.key == K_UP:
                hero_y -= 10
            elif event.key == K_SPACE:
                print("发射子弹")
                my_bullet.append({"x":hero_x+40,"y":hero_y-20})
    for i in my_bullet:
        # i ==> {"x":hero_x+40,"y":hero_y-20}
        screen.blit(bullet,(i["x"], i["y"]))
        screen.blit(bullet, (i["x"]+ 20, i["y"]))
        screen.blit(bullet, (i["x"] - 20, i["y"]))
        # 子弹就可以自己向上跑了
        i["y"] -= 50

def enemy_plane(screen, enemy):
    global enemy_x
    global enemy_path

    screen.blit(enemy,(enemy_x,10))

    if enemy_x >= 250:
        enemy_path = "left"
    elif enemy_x <= 0:
        enemy_path = "right"

    if enemy_path == "right":
        enemy_x += 10
    elif enemy_path == "left":
        enemy_x -= 10

def main():
    """流程控制函数"""
    # 1 创建一个游戏窗口
    # display方法: 展示相关的都会用到这个方法
    # 参数1:元组(长,高)像素
    # 参数2:没有特殊功能
    # 参数3:像素深度
    screen = pygame.display.set_mode((400, 800),0,32)
    # 加载背景图片 image
    background = pygame.image.load("feiji/background.png")
    # 加载英雄飞机图片
    hero = pygame.image.load("feiji/hero1.png")
    # 加载英雄子弹的图片
    bullet = pygame.image.load("feiji/plane.png")
    # 加载敌人飞机图片
    enemy = pygame.image.load("feiji/enemy2.png")

    while True:
        # 把这个图片添加到窗口上
        # blit 剪切,粘贴
        screen.blit(background,(0,0))

        # 显示英雄飞机
        hero_plane(screen,hero,bullet)

        # 显示敌人飞机
        enemy_plane(screen,enemy)

        # 数据更新
        pygame.display.update()

        # 阻塞10秒钟
        time.sleep(0.1)


    # 2 向窗口贴背景

    # 3 英雄飞机

    # 4 敌人飞机


main()
