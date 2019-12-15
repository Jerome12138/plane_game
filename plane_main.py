__author__ = "Jerome Chang"

import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")
        # 1. 创建游戏窗口
        pygame.display.set_caption("飞机大战")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2. 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 3. 创建精灵、精灵组
        self.__create_sprites()
        # 4. 设置定时器事件
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始...")
        while True:
            # 设置刷新帧率
            self.clock.tick(60)
            # 监听键盘事件
            self.__event_handler()
            # 检查碰撞
            self.__check_collide()
            # 更新精灵位置
            self.__update_sprites()
            # 更新屏幕显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            if event.type == CREATE_ENEMY_EVENT:
                self.enemy_group.add(Enemy())
            if event.type ==HERO_FIRE_EVENT:
                self.hero.fire()
        # 捕获按键方式二：可以按住方向键不放，就能够实现持续向某一个方向移动了，操作灵活性更好
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -4
        elif keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 4
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 1. 子弹摧毁敌机
        pygame.sprite.groupcollide(self.enemy_group,self.hero.bullets,True,True)
        # 2. 敌机摧毁英雄
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if len(enemies):
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        for group in [self.bg_group, self.enemy_group, self.hero_group,self.hero.bullets]:
            group.update()
            group.draw(self.screen)

    @staticmethod
    def __game_over():
        print('游戏结束')
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
