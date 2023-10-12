

import pygame
from pygame.locals import *

SIZE = WIDTH, HEIGHT = 640, 339
FPS = 60
pygame.mixer.pre_init(44100, 16, 2, 5012)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.mixer.music.load("megaWall.mp3")
bg_sur = pygame.image.load("bg8_2.png").convert_alpha()
is_pause = True  # 暂停与继续开关
is_play = False  # 音乐开关
while 1: #
    screen.blit(bg_sur, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RETURN: # 开始播放（一遍）
                pygame.mixer_music.play(1, 0.0)
                is_play = True
            if event.key == K_SPACE:   # 暂停播放
                if is_pause:
                    print("暂停播放")
                    pygame.mixer_music.pause()
                    is_pause = False
                else:
                    print("继续播放")
                    pygame.mixer_music.unpause()
                    is_pause = True
            if  event.mod in [KMOD_LCTRL, KMOD_RCTRL]:
                if event.key == K_s:     # 设置播放位置
                    pygame.mixer_music.rewind()
                    print("是否停止:", pygame.mixer_music.get_busy()," 毫秒")
                    pygame.mixer_music.set_pos(3)
                if event.key == K_g:     # 获取播放位置
                    play_time = pygame.mixer_music.get_pos()
                    print("已播放时长：", play_time, " 毫秒")

    if is_play:
        if pygame.mixer_music.get_busy():
            print("开始播放时间点:", pygame.time.get_ticks()," 毫秒")
            is_play = False
    else:
        if not pygame.mixer_music.get_busy():
            print("停止播放时间点:", pygame.time.get_ticks()," 毫秒")
            is_play = True
    pygame.display.update()
    clock.tick(FPS)


