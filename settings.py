class Settings:
    #存储游戏《外星人入侵》中所有设置的类
    def __init__(self):
        #初始化游戏设置
        #屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=("black")
        #飞船的设置
        self.ship_speed=1.5
        #子弹设置
        self.bullet_speed=3.0
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=("white")
        self.bullets_allowed=10
        # self.bullets=[]
        #外星人设置
        self.alien_speed=1.0
        self.fleet_drop_speed=10
        #fleet_dircetion为1表示向右移动，为-1表示向左移动
        self.fleet_direction=1
