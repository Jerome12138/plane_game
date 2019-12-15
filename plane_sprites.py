__author__ = "Jerome Chang"

import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    '''游戏精灵基类'''

    def __init__(self, image_name, speed=1):
        # 调用父类的__init__方法
        super().__init__()
        # 定义精灵属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        '''更新位置'''
        self.rect.y += self.speed


class Background(GameSprite):
    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self, *args):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    def __init__(self):
        # 设置敌机的随机初始速度
        super().__init__("./images/enemy1.png", random.randint(1, 3))
        # 设置敌机的随机初始位置
        self.rect.bottom = 0
        self.rect.x = random.randint(20, SCREEN_RECT.width - self.rect.width - 20)
        # 判断已有敌机位置，避开已有敌机

    def update(self, *args):
        super().update()
        # 判断敌机是否飞出屏幕，飞出则从敌机组删除
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
            print('游戏退出')
            pygame.quit()
            exit()

    def __del__(self):
        print('%s敌机被销毁' % self.rect)


class Hero(GameSprite):
    def __init__(self):
        super().__init__('./images/me1.png', 0)
        self.rect.bottom = SCREEN_RECT.height - 120
        self.rect.centerx = SCREEN_RECT.centerx
        self.bullets = pygame.sprite.Group()

    def update(self, *args):
        # 飞机水平移动
        self.rect.x += self.speed
        # 边界限制
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # 创建子弹精灵
        bullet = Bullet()
        # 设置子弹初始位置
        bullet.rect.bottom = self.rect.y - 20
        bullet.rect.centerx = self.rect.centerx
        # 将子弹添加到子弹精灵组
        self.bullets.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super().__init__('./images/bullet1.png', -2)

    def update(self, *args):
        super().update()
        if self.rect.y <= 0:
            self.kill()
