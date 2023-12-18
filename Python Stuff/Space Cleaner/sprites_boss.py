import pygame
from pygame.locals import *
from settings import *

pygame.init()


class Boss_1(pygame.sprite.Sprite):
    def __init__(self, w, h):
        pygame.sprite.Sprite.__init__(self)

        self.scale_x, self.scale_y = 0, 0
        self.size = [0.15, 0.12]
        self.w, self.h = (round(w*size[0])), (round(h*size[1]))

        self.name = "Boss"
        self.hp_MAX = 100
        self.hp = self.hp_MAX

        self.image_org = pygame.image.load('Bilder/boss1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image_org, (self.w, self.h))
        self.rect = self.image.get_rect()

        self.rect.x = w+self.w
        self.rect.y = 0

        self.stuff_array = pygame.sprite.Group()  # Liste med ting man kan plukke opp (Eks: HP)

    def update(self, dt, w, h):
        self.stuff_array.update()
        self.stuff_array.draw()

    def resize(self, w_old, h_old, w_new, h_new, hp):
        self.scale_x = (self.pos.x * 100) / w_old
        self.scale_y = (self.pos.y * 100) / h_old

        self.pos.x = (self.scale_x * w_new) / 100
        self.pos.y = (self.scale_y * h_new) / 100

        self.w, self.h = (round(w_new * size[0])), (round(h_new * size[1]))
        self.image = pygame.transform.scale(self.image_org, (self.w, self.h))

        self.speed = w_new / self.speed_nr





        self.rect.x = (self.scale_x * w_new) / 100
        self.rect.y = (self.scale_y * h_new) / 100

        self.w, self.h = round(w_new * 0.3), round(h_new * 0.2)
        self.image = pygame.transform.scale(self.image_org, (self.w, self.h))

        self.speed = round(w_new / self.speed_nr)

