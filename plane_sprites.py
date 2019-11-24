__author__ = "Jerome Chang"

import pygame

class GameSprite(pygame.sprite.Sprite):
    '''游戏精灵基类'''
    def __init__(self,image_name,speed = 1):
        # 调用父类的__init__方法
        super().__init__()
        # 定义精灵属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        '''更新位置'''
        self.rect.y +=self.speed