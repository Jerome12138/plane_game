__author__ = "Jerome Chang"

import pygame
from plane_sprites import *

pygame.init()  # 初始化pygame模块

# 初始化游戏窗口
pygame.display.set_caption('飞机大战')
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1. 加载图片
bg = pygame.image.load('./images/background.png')
# 2. 使用blit绘制图像
screen.blit(bg, (0, 0))
# 3. 更新游戏窗口
pygame.display.update()

# 创建英雄飞机
hero = pygame.image.load('./images/me1.png')
screen.blit(hero, (200, 500))
pygame.display.update()

# 创建游戏时钟对象
clock = pygame.time.Clock()

# 定义飞机的初始位置
hero_rect = pygame.Rect(200, 500, 102, 126)

# 创建敌机精灵
enemy = GameSprite('./images/enemy1.png')

# 创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy)

while True:
    # 设置游戏刷新帧率
    clock.tick(60)
    # 判断事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('退出游戏')
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            pass
    # 更新英雄位置
    hero_rect.y -= 1
    if hero_rect.bottom == 0:  # 如果飞出顶部，重新回到底部
        hero_rect.y = 700
    screen.blit(bg, (0, 0))  # 重新绘制背景，使图像不重影
    screen.blit(hero, hero_rect)
    # 刷新敌机精灵位置
    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.update()
