
import pygame
from pygame.locals import *

SIZE = WIDTH, HEIGHT = 640, 339
FPS = 60
pygame.mixer.pre_init(44100, 16, 2, 5012)
pygame.init()
pygame.mixer.music.load("preview.ogg")
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
bg_sur = pygame.image.load("bg8_1.png").convert_alpha()
is_pause = True  # 暂停与继续开关

while 1:
    screen.blit(bg_sur, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RETURN:  # 开始无限播放
                pygame.mixer_music.play(-1, 0.0)
                print("开始播放 1 次")
            if event.key == K_SPACE:   # 暂停播放
                if is_pause:
                    pygame.mixer_music.pause()
                    is_pause = False
                    print("暂停播放")
                else:
                    pygame.mixer_music.unpause()
                    is_pause = True
                    print("继续播放")
            if event.mod in [KMOD_LCTRL, KMOD_RCTRL]:
                if event.key == K_w:       # 播放 10 次
                    pygame.mixer_music.play(9, 0.0)
                    print("开始播放 10 次")
                if event.key == K_z:       # 停止播放
                    pygame.mixer_music.stop()
                    print("停止播放")
                if event.key == K_o:       # 淡出播放
                    pygame.mixer_music.fadeout(3000)
                    print("淡出停止播放")
    pygame.event.clear()
    pygame.display.update()
    clock.tick(FPS)


