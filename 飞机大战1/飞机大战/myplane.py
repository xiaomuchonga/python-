import pygame

class MyPlane(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("D:/python/python项目实战/飞机大战1/飞机大战/images/me1.png").convert_alpha()
        self.image2 = pygame.image.load("D:/python/python项目实战/飞机大战1/飞机大战/images/me2.png").convert_alpha()
        self.destroy_image  = []
        self.active = True
        self.invincible = False
        self.destroy_image.extend([\
            pygame.image.load("D:/python/python项目实战/飞机大战1/飞机大战/images/me_destroy_1.png").convert_alpha(), \
            pygame.image.load("D:/python/python项目实战/飞机大战1/飞机大战/images/me_destroy_2.png").convert_alpha(), \
            pygame.image.load("D:/python/python项目实战/飞机大战1/飞机大战/images/me_destroy_3.png").convert_alpha(), \
            pygame.image.load("D:/python/python项目实战/飞机大战1/飞机大战/images/me_destroy_4.png").convert_alpha(), \
            ])
        self.rect = self.image1.get_rect()
        self.mask = pygame.mask.from_surface(self.image1)
        self.mask = pygame.mask.from_surface(self.image2)
        self.width , self.height = bg_size[0],bg_size[1]
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, \
            self.height - self.rect.height - 60
        self.speed = 10
    # 移动函数
    def moveUP(self):
        if self.rect.top > 0:
             self.rect.top -= self.speed
        else:
            self.rect.top = 0
    def moveDown(self):
        if self.rect.bottom < self.height-60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLeft(self):
        if self.rect.left>0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0
    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left+=self.speed
        else:
            self.rect.right = self.width
    def reset(self):
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, \
            self.height - self.rect.height - 60
        self.active = True
        self.invincible = True
