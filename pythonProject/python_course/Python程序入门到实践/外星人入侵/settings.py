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
