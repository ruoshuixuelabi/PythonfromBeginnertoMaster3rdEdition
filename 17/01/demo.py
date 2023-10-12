import random
import pygame
import sys

SIZE = WIDTH, HEIGHT = 640, 396
FPS = 60

pygame.init()
screen = pygame.display.set_mode(SIZE, 0, 32)
pygame.display.set_caption("Event")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)
font_height = font.get_linesize()	# 获取该文体单行的高度
event_list = []
line_num = SIZE[1]//font_height		# 屏幕可展示最大行数文字

running = True
# 主体循环
while running:
    # 等待获取一个事件并删除
    event = pygame.event.wait()
    event_list.append(str(event))
    # 保证 event_list 里面只保留可展示一个屏幕的文字
    event_text = event_list[-line_num:]

    if event.type == pygame.QUIT:
        sys.exit()

    screen.fill((54, 59, 64))

    y = SIZE[1]-font_height
    # 绘制事件文本
    for text in reversed(event_list):
        rgb = tuple((random.randint(0, 255) for i in range(3)))
        screen.blit( font.render(text, True, rgb), (0, y))
        y-=font_height

    pygame.display.update()
