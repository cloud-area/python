"""《外星人入侵》
在游戏中，玩家控制着一艘最初出现在屏幕底部中央的飞船

"""

import pygame
import sys
from time import sleep
import pygame.font
# import game_functions as gf
from pygame.sprite import Group,Sprite



class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        """
        初始化外星人并设置其起始位置
        :param ai_settings:
        :param screen:
        """
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blit_me(self):
        """
        在指定位置绘制外星人
        :return:
        """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        向左或向右移动外星人
        :return:
        """
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """
        如果外星人位于屏幕边缘，就返回True
        :return:
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        """
        在飞船所处的位置创建一个子弹对象
        :param ai_settings:
        :param screen:
        :param ship:
        """
        super().__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储小数表示子弹的位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """
        向上移动子弹
        :return:
        """
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """
        在屏幕上绘制子弹
        :return:
        """
        pygame.draw.rect(self.screen, self.color, self.rect)


class GameStats:
    """
    跟踪游戏的统计信息
    """

    def __init__(self, ai_settings):
        """
        初始化统计信息
        :param ai_settings:
        """
        self.level = 1
        self.score = 0
        self.ships_left = None
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏刚启动时处于非活动状态
        self.game_active = False

        # 在任何情况下都不应重置最高得分
        # self.high_score = 0

    def reset_stats(self):
        """
        初始化在游戏运行期间可能变化的统计信息
        :return:
        """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1


class Scoreboard:
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """
        初始化显示得分涉及的属性
        :param ai_settings:
        :param screen:
        :param stats:
        """
        self.ships = None
        self.level_rect = None
        self.high_score_rect = None
        self.high_score_image = None
        self.score_rect = None
        self.score_image = None
        self.level_image = None
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('None', 48)

        # # 准备包含最高得分和当前得分的图像
        self.prep_score()
        # self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上显示飞船和得分"""
        self.screen.blit(self.score_image, self.score_rect)
        # self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # 绘制飞船
        self.ships.draw(self.screen)

    # def prep_high_score(self):
    #     """将最高得分转换为渲染的图像"""
    #     high_score = int(round(self.stats.high_score, -1))
    #     high_score_str = "Maximum score"+"{:,}".format(high_score)
    #     self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
    #
    #     # 将最高得分放在屏幕顶部中央
    #     self.high_score_rect = self.high_score_image.get_rect()
    #     self.high_score_rect.centerx = self.screen_rect.centerx
    #     self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.level_image = self.font.render("level: " + str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """显示还余下多少艘飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

class Settings:
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.alien_points = None
        self.fleet_direction = None
        self.bullet_width = None
        self.alien_speed_factor = None
        self.bullet_speed_factor = None
        self.ship_speed_factor = None
        self.screen_width = 800
        self.screen_height = 1000
        self.bg_color = (0, 0, 0)

        # 飞船的设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_height = 15
        self.bullet_color = 255, 255, 255
        self.bullets_allowed = 3

        # 外星人设置
        self.fleet_drop_speed = 10

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.5

        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        初始化随游戏进行而变化的设置
        :return:
        """
        self.ship_speed_factor = 0.2
        self.bullet_speed_factor = 0.6
        self.alien_speed_factor = 0.02
        self.bullet_width = 6

        # fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 1

        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """
        提高速度设置和外星人点数
        :param self:
        :return:
        """
        self.ship_speed_factor *= 1.1
        self.bullet_speed_factor *= 1.25
        self.bullet_width *= 1.5
        self.alien_speed_factor *= 3
        self.fleet_drop_speed *= 2

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)


class Button:
    def __init__(self, screen, msg):
        """初始化按钮的属性"""
        self.msg_image_rect = None
        self.msg_image = None
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('None', 48)

        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """
        初始化飞船并设置其初始位置
        :param ai_settings:
        :param screen: 指定飞船绘制到什么地方
        """
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """
        根据移动标志调整飞船位置
        :return:
        """
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center
        self.rect.centery = self.center_y

    def blit_me(self):
        """
        在指定位置绘制飞船
        :return:
        """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """
        让飞船在屏幕上据中
        :return:
        """
        self.center = self.screen_rect.centerx


"""
按键响应类函数
"""


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """
    响应按键
    :param event:
    :param ai_settings:
    :param screen:
    :param ship:
    :param bullets:
    :return:
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并将其加入到编组bullet中
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """
    响应松开按键
    :param event:
    :param ship:
    :return:
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """
    响应按键和鼠标事件
    :param aliens:
    :param play_button:
    :param sb:
    :param stats:
    :param ai_settings:
    :param screen:
    :param ship:
    :param bullets:
    :return:
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """
    在玩家单击Play按钮时开始新游戏
    :param bullets:
    :param aliens:
    :param ship:
    :param sb:
    :param screen:
    :param ai_settings:
    :param stats:
    :param play_button:
    :param mouse_x:
    :param mouse_y:
    :return:
    """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌图像
        sb.prep_score()
        # sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


"""
子弹类函数
"""


def fire_bullet(ai_settings, screen, ship, bullets):
    """
    如果还没有到达限制，就发射一颗子弹
    :param ship:
    :param ai_settings:
    :param screen:
    :param bullets:
    :return:
    """
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    更新子弹的位置，并删除已消失的子弹
    :param sb:
    :param stats:
    :param ai_settings:
    :param screen:
    :param ship:
    :param aliens:
    :param bullets:
    :return:
    """
    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    响应子弹和外星人的碰撞
    :param sb:
    :param stats:
    :param ai_settings:
    :param screen:
    :param ship:
    :param aliens:
    :param bullets:
    :return:
    """
    # 检查是否有子弹击中了外星人
    # 如果是这样，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        # check_high_score(stats, sb)

    if len(aliens) == 0:
        # 如果整群外星人都被消灭，就提高一个等级
        bullets.empty()
        ai_settings.increase_speed()

        # 提高等级
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


"""
外星人类函数
"""


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """
    创建一个外星人并将其放在当前行
    :param row_number:
    :param ai_settings:
    :param screen:
    :param aliens:
    :param alien_number:
    :return:
    """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """
    创建外星人群
    :param ship:
    :param ai_settings:
    :param screen:
    :param aliens:
    :return:
    """
    # 创建一个外星人，并计算每行可容纳多少个外星人
    alien = Alien(ai_settings, screen)
    numbers_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(numbers_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """
    计算每行可容纳多少个外星人(外星人行数)
    :param ai_settings:
    :param alien_width:
    :return:
    """
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (4 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """
    计算屏幕可容纳多少行外星人(外星人列数)
    :param ai_settings:
    :param ship_height:
    :param alien_height:
    :return:
    """
    available_space_y = (ai_settings.screen_height - (5 * alien_height) - ship_height)
    numbers_rows = int(available_space_y / (3 * alien_height))
    return numbers_rows


def check_fleet_edges(ai_settings, aliens):
    """
    有外星人到达边缘时采取相应的措施
    :param ai_settings:
    :param aliens:
    :return:
    """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """
    将整群外星人下移，并改变它们的方向
    :param ai_settings:
    :param aliens:
    :return:
    """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    检查是否有外星人位于屏幕边缘，并更新整群外星人的位置
    :param sb:
    :param ai_settings:
    :param stats:
    :param screen:
    :param ship:
    :param bullets:
    :param aliens:
    :return:
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    响应被外星人撞到的飞船
    :param sb:
    :param ai_settings:
    :param stats:
    :param screen:
    :param ship:
    :param aliens:
    :param bullets:
    :return:
    """
    if stats.ships_left > 0:
        # 将ship_left减1
        stats.ships_left -= 1

        # 更新记分牌
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停一会儿
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    检查是否有外星人到达了屏幕底端
    :param sb:
    :param ai_settings:
    :param stats:
    :param screen:
    :param ship:
    :param aliens:
    :param bullets:
    :return:
    """
    screen_ret = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_ret.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break


"""
画面类函数
"""


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """
    更新屏幕上的图像，并切换到新屏幕
    :param play_button:
    :param sb:
    :param stats:
    :param aliens:
    :param ai_settings:
    :param screen:
    :param ship:
    :param bullets:
    :return:
    """
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blit_me()
    aliens.draw(screen)

    # 显示得分
    sb.show_score()

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


# def check_high_score(stats, sb):
#     """检查是否诞生了新的最高得分"""
#     if stats.score > stats.high_score:
#         stats.high_score = stats.score
#         sb.prep_high_score()



def run_game():
    """
    运行游戏
    :return:None
    """
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(screen, "Play")

    # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船,一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
