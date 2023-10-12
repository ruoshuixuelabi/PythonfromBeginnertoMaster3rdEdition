


import pygame

pygame.init()
screen =  pygame.display.set_mode((640, 396))

obj = pygame.Rect(100, 100, 200, 200)

obj_01 = pygame.Rect(0, 100, 101, 100)   # 左
obj_02 = pygame.Rect(100, 0, 100, 101)   # 上
obj_03 = pygame.Rect(299, 100, 100, 100) # 右
obj_04 = pygame.Rect(100, 299, 100, 100) # 下
# 输出结果请看注释
print(obj.colliderect(obj_01)) # 左         
print(obj.colliderect(obj_02)) # 上         
print(obj.colliderect(obj_03)) # 右         
print(obj.colliderect(obj_04)) # 下         

if obj.left == obj_01.right: print("左 == 右")
else: print("左 != 右")
if obj.top == obj_02.bottom: print("上 == 下")
else: print("上 != 下")
if obj.right == obj_03.left: print("右 == 左")
else: print("右 != 左")
if obj.bottom == obj_04.top: print("下 == 上")
else: print("下 != 上")

print("obj.left =", obj.left, "obj_01.right =", obj_01.right)
print("obj.top =", obj.top, "obj_02.bottom =", obj_02.bottom)
print("obj.right =", obj.right, "obj_01.left =", obj_03.left)
print("obj.bottom =", obj.bottom, "obj_01.top =", obj_04.top)

print(obj.colliderect(obj_01.move(-1, 0)))  # 0
print(obj.colliderect(obj_02.move(0, -1)))  # 0
print(obj.colliderect(obj_03.move(1, 0)))   # 0
print(obj.colliderect(obj_04.move(0, 1)))   # 0

while 1:
    screen.fill((0, 163, 150))

    pygame.draw.rect(screen, pygame.Color("red"), obj, 1)
    pygame.draw.rect(screen, pygame.Color("green"), obj_01, 1)
    pygame.draw.rect(screen, pygame.Color("blue"), obj_02, 1)
    pygame.draw.rect(screen, pygame.Color("red"), obj_03, 1)
    pygame.draw.rect(screen, pygame.Color("white"), obj_04, 1)

    for event in pygame.event.get(pygame.QUIT):  # 事件索取
        if event:
            pygame.quit()
            exit()
    pygame.display.update()



