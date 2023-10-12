import os
import sys
import pygame
from pygame.locals import *

SIZE = WIDTH, HEIGHT = 640, 396
FPS = 60

pygame.init()
# 窗口居中
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("记录键盘按下字符")
clock = pygame.time.Clock()
# 开启重复产生键盘事件功能,(延迟，间隔)，单位为毫秒
pygame.key.set_repeat(200, 200)
name = ""
font = pygame.font.SysFont('arial', 80)
group = [KMOD_LSHIFT, KMOD_RSHIFT, KMOD_LSHIFT + \
         KMOD_CAPS, KMOD_RSHIFT + KMOD_CAPS]

while True:
    screen.fill((0, 164, 150))
    font_height = font.get_linesize()
    text = font.render(name[-17:], True, (255, 255, 255))
    height = HEIGHT/2 - font_height / 2
    screen.blit(text, (30, height, 500, font_height))

    evt = pygame.event.wait()
    if evt.type == QUIT:
        sys.exit()
    # 按键释放
    if evt.type == KEYUP:
        if evt.mod in group:
            pygame.key.set_repeat(200, 200)
    # 按键按下
    if evt.type == KEYDOWN:
        if evt.key in [K_ESCAPE, K_q]: # 退出
            pygame.quit()
            sys.exit()

        # 组合键若为 Shift 键，则加快回退的速度
        if evt.mod in group:
            if pygame.key.get_repeat() != (50, 50):
                pygame.key.set_repeat(50, 50)
        if evt.key == K_BACKSPACE:     # 回退键
            name = name[:-1]
        else:
            name += evt.unicode
        if evt.key == K_RETURN:        # 回车键, 清空
            name = ""

    pygame.display.update()
    clock.tick(FPS)
