from operator import truediv
import pygame

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480,700))

# 绘制背景图像
bg = pygame.image.load("D:/python/python项目实战/飞机大战1/images/background.png")
screen.blit(bg,(0,0))

# 绘制英雄的飞机
hero = pygame.image.load("D:\python\python项目实战\飞机大战1\images/me1.png")
screen.blit(hero,(189,574))
pygame.display.update()

clock = pygame.time.Clock()
# 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(189,574,102,126)
# 游戏循环
while True:
    # 指定代码更新频率
    clock.tick(60)

    # even_list = pygame.event.get()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            print("退出游戏...")

            # 卸载所有模块
            pygame.quit()
            # 直接终止正在执行的程序
            exit()

    # 修改飞机位置
    hero_rect.y -= 1

    # 判断是否超出边界
    if hero_rect.y <= -126:
        hero_rect.y = 700 
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)
    pygame.display.update()
    pass



pygame.quit()