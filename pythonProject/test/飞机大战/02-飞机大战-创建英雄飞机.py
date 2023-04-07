import pygame
import time

def hero_plane(screen, hero):
    # 显示英雄飞机
    screen.blit(hero,(150,600))


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

    # 加载飞机图片
    hero = pygame.image.load("feiji/hero1.png")

    # 把这个图片添加到窗口上
    # blit 剪切,粘贴
    screen.blit(background,(0,0))

    # 显示英雄飞机
    hero_plane(screen,hero)

    # 数据更新
    pygame.display.update()

    # mac需要这只一下
    pygame.event.get()

    # 阻塞10秒钟
    time.sleep(10)


    # 2 向窗口贴背景

    # 3 英雄飞机

    # 4 敌人飞机


main()
