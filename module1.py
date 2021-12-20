import pygame
import random

class Asteroid(pygame.sprite.Sprite):
    def __init__(self,surf,group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf# графика
        x = random.randint(20,470)
        self.rect = self.image.get_rect() # положение и размер спрайта
        self.rect.x = random.randrange(100,499)
        self.rect.y = random.randrange(-100, -40)
        speed_aster = random.randint(1,10)# скорость одного астероида
        self.speedy = speed_aster
        speed_aster = random.randint(-3,3)# скорость одного астероида
        self.speedx = speed_aster 
        self.add(group)

    def update(self, *args):
        if args[0] == -100:
            self.kill()
        if self.rect.y < args[0]:
            self.rect.y += self.speedy
            self.rect.x += self.speedx

        else:
            self.rect.y = 0
            self.rect.x = 0
            self.kill()
