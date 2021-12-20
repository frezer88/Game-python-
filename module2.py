import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y,surf):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf# графика
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()
