import sys
import pygame
from settings import Settings # type: ignore 从settings.py中导入Settings类
from ship import Ship # type: ignore
from bullet import Bullet # type: ignore

class AlienInvasion:
    #管理游戏资源和行为的类
    def __init__(self):
        #初始化游戏并创建游戏资源
        pygame.init() #初始化背景
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        #self.screen=pygame.display.set_mode((1200,800))#创建一个显示窗口，尺寸：宽1200像素、高800像素
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        
        pygame.display.set_caption("Alien Invasion")

        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        #设置背景色
        #self.bg_color=(230,230,230)
    
    def run_game(self):
        #开始游戏主循环
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            #侦听键盘和鼠标事件
            #for event in pygame.event.get():
                #if event.type==pygame.QUIT:
                    #sys.exit()
            
            #每次循环是都会重绘屏幕
            #self.screen.fill(self.settings.bg_color)
            #self.ship.blitme()
            #self.screen.fill(self.bg_color)
            #让最近绘制的屏幕可见
            #pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        #响应按键和鼠标事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
                # if event.key==pygame.K_RIGHT:
                #     self.ship.moving_right=True
                # elif event.key==pygame.K_LEFT:
                #     self.ship.moving_left=True
                # elif event.key==pygame.K_UP:
                #     self.ship.moving_up=True
                # elif event.key==pygame.K_DOWN:
                #     self.ship.moving_down=True
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)
                # if event.key==pygame.K_RIGHT:
                #     self.ship.moving_right=False
                # elif event.key==pygame.K_LEFT:
                #     self.ship.moving_left=False
                # elif event.key==pygame.K_UP:
                #     self.ship.moving_up=False
                # elif event.key==pygame.K_DOWN:
                #     self.ship.moving_down=False
                    #向右移动飞船
                    #self.ship.rect.x+=1
        
    def _check_keydown_events(self,event):
        #响应按下
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=True
        elif event.key==pygame.K_UP:
            self.ship.moving_up=True
        elif event.key==pygame.K_DOWN:
            self.ship.moving_down=True
        #按q键退出,必须是英文的q按键
        elif event.key==pygame.K_ESCAPE:
            sys.exit()
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self,event):
        #响应不按
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=False
        elif event.key==pygame.K_UP:
            self.ship.moving_up=False
        elif event.key==pygame.K_DOWN:
            self.ship.moving_down=False
    
    def _fire_bullet(self):
        #创建一颗子弹，并将其加入编组bullets
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet =Bullet(self)
            self.bullets.add(new_bullet)
    
                
    def _update_screen(self):
        #更新屏幕上的图像，并切换到新屏幕
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()                  
        self.ship.blitme()

        pygame.display.flip()
    
    def _update_bullets(self):
        #更新子弹的位置并删除已经消失的子弹
        #更新子弹的位置
        self.bullets.update()

        #删除已经消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)
        

if __name__=='__main__':
    #创建游戏实例并运行游戏
    ai=AlienInvasion()
    ai.run_game()

