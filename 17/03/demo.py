import os
import sys

# 导入pygame 及常量库
import pygame
from pygame.locals import *

SIZE = WIDTH, HEIGHT = 640, 396
FPS = 60

# 窗口居中
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()  # 初始化 设备
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("移动Surface")
clock = pygame.time.Clock()
# 加载图片
img_sur = pygame.image.load("sprite_02.png").convert_alpha()
img_rect = img_sur.get_rect() # 获取 Rect 对象
# 将此图 Rect 图像定位于 窗口中心
img_rect.center = screen.get_rect().center
new_img_rect = img_rect.copy() # 拷贝 Rect 对象





# 主体循环
while True:
    # 1. 清屏
    screen.fill((0, 163, 150))
    # 2. 绘制 图片 Surface
    screen.blit(img_sur, img_rect)
    # 绘制 原图 绘制区域边框
    pygame.draw.rect(screen, pygame.Color("black"), new_img_rect, 2)

    for event in pygame.event.get():  # 事件索取
        if event.type == QUIT: # 退出
            pygame.quit()
            sys.exit()
        # 键盘事件监听
        if event.type == KEYDOWN:
            if event.key == K_LEFT: # 左键
                img_sur.scroll(-64, 0)
                # 原地移动矩形对象
                new_img_rect.move_ip(-64, 0)
            if event.key == K_RIGHT: # 右键
                img_sur.scroll(64, 0)
                new_img_rect.move_ip(64, 0)
            if event.key == K_UP:   # 上键
                img_sur.scroll(0, -64)
                new_img_rect.move_ip(0, -64)
            if event.key == K_DOWN: # 下键
                img_sur.scroll(0, 64)
                new_img_rect.move_ip(0, 64)

    # 3.刷新
    pygame.display.update()
    clock.tick(FPS)


