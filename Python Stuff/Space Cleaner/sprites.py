import pygame
from pygame.locals import *
from settings import *

vec = pygame.math.Vector2

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, w, h):
        pygame.sprite.Sprite.__init__(self)

        self.scale_x, self.scale_y = 0, 0
        self.w, self.h = (round(w*0.15)), (round(h*0.12))

        self.name = "Ship"
        self.hp_MAX = 100
        self.hp = self.hp_MAX

        self.image_org = pygame.image.load('Bilder/ship2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image_org, (self.w, self.h))
        self.rect = self.image.get_rect()

        self.pos = vec(10, h/2-self.w/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.speed_nr = 20
        self.speed = w/self.speed_nr

        self.friction = -0.065  # Hvor lang tid det tar før skipet stopper etter du slipper knappen

        self.shots_seconds = 0.5*FPS  # Hvor ofte man kan skyte i antall sekunder
        self.shots_count = 0

    def get_keys(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.acc.x = self.speed * dt
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.acc.x = -self.speed * dt
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.acc.y = -self.speed * dt
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.acc.y = self.speed * dt
        if self.acc.x != 0 and self.acc.y != 0:
            self.acc.x *= 0.7071  # Kvadratroten av 2; Slik at den ikke er raksere diagonalt
            self.acc.y *= 0.7071

    def get_click(self):
        if self.shots_count <= 0:
            self.shots_count = self.shots_seconds
            return True

    def update(self, dt, w, h):
        self.acc = vec(0, 0)

        self.get_keys(dt)

        # Regner ut bevelsen
        self.acc += self.vel * self.friction
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Sjekker om den går utenfor skjermen
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.y < 0:
            self.pos.y = 0
        if self.pos.x+self.w > w:
            self.pos.x = w-self.w
        if self.pos.y+self.h > h:
            self.pos.y = h-self.h

        # Oppdateter posisjonen
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

        # Hvor ofte du kan skyte; Se også def get_click!
        if self.shots_count != 0:
            self.shots_count -= 1

    def resize(self, w_old, h_old, w_new, h_new, hp):
        self.scale_x = (self.pos.x * 100) / w_old
        self.scale_y = (self.pos.y * 100) / h_old

        self.pos.x = (self.scale_x * w_new) / 100
        self.pos.y = (self.scale_y * h_new) / 100

        self.w, self.h = (round(w_new * 0.15)), (round(h_new * 0.12))
        self.image = pygame.transform.scale(self.image_org, ((round(w_new*0.15)), (round(h_new*0.12))))

        self.speed = w_new / self.speed_nr

    def get_precent(self):
        return (self.hp * 100) / self.hp_MAX


# Skudd!
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, col):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Bullet"
        self.scale_x, self.scale_y = 0, 0
        self.w, self.h = w*0.015, h*0.005

        self.speed_nr = 1
        self.speed = w / self.speed_nr

        self.image = pygame.Surface((self.w, self.h))
        self.color = col
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self, dt, w, h, screen, p_y):
        if self.color == RED:
            self.rect.x += self.speed * dt
            if self.rect.x > w:
                self.kill()
        else:
            if (self.speed * dt) < 1:
                self.rect.x -= 1
            if (self.speed * dt) > 1:
                self.rect.x -= round(self.speed * dt)
            if self.rect.right <= 0:
                self.kill()

    def resize(self, w_old, h_old, w_new, h_new):
        self.scale_x = (self.rect.x * 100) / w_old
        self.scale_y = (self.rect.y * 100) / h_old

        self.rect.x = (self.scale_x * w_new) / 100
        self.rect.y = (self.scale_y * h_new) / 100

        self.w, self.h = w_new * 0.015, h_new * 0.005
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(RED)

        self.speed = w_new / self.speed_nr


# SØPPELKASSER
class Trash(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h,img):
        pygame.sprite.Sprite.__init__(self)

        self.name = "Trash"
        self.scale_x, self.scale_y = 0, 0
        self.w, self.h = round(w*0.1), round(h*0.1)

        self.speed_nr = 5 # Hvor mange sekunder tar det å reise over skjermen?
        self.speed = w / self.speed_nr

        self.image_org = img
        self.image = pygame.transform.scale(self.image_org, (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self, dt, w, h, screen, p_x):
        if (self.speed*dt) < 1:
            print("1")
            self.rect.x -= 1
        if (self.speed*dt) > 1:
            self.rect.x -= round(self.speed * dt)
        if self.rect.right <= 0:
            self.kill()

    def resize(self, w_old, h_old, w_new, h_new):
        self.scale_x = (self.rect.x * 100) / w_old
        self.scale_y = (self.rect.y * 100) / h_old

        self.rect.x = (self.scale_x * w_new) / 100
        self.rect.y = (self.scale_y * h_new) / 100

        self.w, self.h = round(w_new * 0.1), round(h_new * 0.1)
        self.image = pygame.transform.scale(self.image_org, (self.w, self.h))

        self.speed = w_new / self.speed_nr


# MENU
class HealtBar(pygame.sprite.Sprite):
    def __init__(self, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.name = "HP_BAR"
        self.scale_x, self.scale_y = 0, 0
        self.w, self.h = w*0.3, h*0.03
        self.w_MAX = round(w*0.3)

        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 10, 10

    def update(self, dt, w, h):
        pass

    def change_hp(self, hp, hp_MAX, w, h):
        self.w = (self.w_MAX * (hp/100))
        if self.w <= 0:
            self.w = 1
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(GREEN)

    def resize(self, w_old, h_old, w_new, h_new, hp):
        self.scale_x = (self.rect.x * 100) / w_old
        self.scale_y = (self.rect.y * 100) / h_old

        self.rect.x = (self.scale_x * w_new) / 100
        self.rect.y = (self.scale_y * h_new) / 100

        self.h = h_new*0.03
        self.w_MAX = round(w_new * 0.3)
        self.w = (self.w_MAX * (hp / 100))
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(GREEN)


# Healing Item
class HP(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h,img):
        pygame.sprite.Sprite.__init__(self)

        self.name = "HP_UP"
        self.scale_x, self.scale_y = 0, 0
        self.w, self.h = round(w*0.02), round(h*0.02)

        self.speed_nr = 5  # Hvor mange sekunder tar det å reise over skjermen?
        self.speed = w / self.speed_nr

        self.image_org = img
        self.image = pygame.transform.scale(self.image_org, (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self, dt, w, h):
        if (self.speed*dt) < 1:
            self.rect.x -= 1
        if (self.speed*dt) > 1:
            self.rect.x -= round(self.speed * dt)
        if self.rect.right <= 0:
            self.kill()

    def resize(self, w_old, h_old, w_new, h_new):
        self.scale_x = (self.rect.x * 100) / w_old
        self.scale_y = (self.rect.y * 100) / h_old

        self.rect.x = (self.scale_x * w_new) / 100
        self.rect.y = (self.scale_y * h_new) / 100

        self.w, self.h = round(w_new*0.02), round(h_new*0.02)
        self.image = pygame.transform.scale(self.image_org, (self.w, self.h))

        self.speed = w_new / self.speed_nr


# Astroider
class Rocks(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, img):
        pygame.sprite.Sprite.__init__(self)

        self.name = "Rock"
        self.scale_x, self.scale_y = 0, 0
        self.w, self.h = round(w * 0.3), round(h * 0.2)

        self.speed_nr = 1  # Hvor mange sekunder tar det å reise over skjermen?
        self.speed = w / self.speed_nr

        self.image_org = img
        self.image = pygame.transform.scale(self.image_org, (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

        self.warning = True
        self.warning_count = 0.1*FPS
        self.warning_spawn_count = 2*FPS

    def update(self, dt, w, h, screen, p_y):
        if not self.warning:
            self.rect.x -= self.speed * dt
            if self.rect.x <= -self.w:
                self.kill()
        else:
            self.warning_count -= 1
            if self.warning_count <= 0:
                pygame.draw.rect(screen, RED, (w*0.98, self.rect.y, w*0.01, self.h))
                self.warning_count = 0.1 * FPS
            self.warning_spawn_count -= 1
            if self.warning_spawn_count <= 0:
                self.warning = False

    def resize(self, w_old, h_old, w_new, h_new):
        self.scale_x = (self.rect.x * 100) / w_old
        self.scale_y = (self.rect.y * 100) / h_old

        self.rect.x = (self.scale_x * w_new) / 100
        self.rect.y = (self.scale_y * h_new) / 100

        self.w, self.h = round(w_new * 0.3), round(h_new * 0.2)
        self.image = pygame.transform.scale(self.image_org, (self.w, self.h))

        self.speed = round(w_new / self.speed_nr)


# UFO
class UFO(pygame.sprite.Sprite):
    def __init__(self, w, h, img):
        pygame.sprite.Sprite.__init__(self)

        self.name = "UFO"
        self.scale_x, self.scale_y = 0, 0
        self.w, self.h = round(w*0.15), round(h*0.15)

        self.hp_MAX = 10
        self.hp = self.hp_MAX

        self.dmg = 10

        self.speed_nr = 4  # Hvor mange sekunder tar det å reise over skjermen?
        self.speed = h / self.speed_nr

        self.shots_seconds = 1*FPS  # Hvor ofte man kan skyte i antall sekunder
        self.shots_count = 0

        self.image_org = img
        self.image = pygame.transform.scale(self.image_org, (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = w-round(w*0.16), 0-round(h*0.16)

    def update(self, dt, w, h, screen, p_y):
        if self.rect.y < p_y:
            self.rect.y += round(self.speed * dt)
        if self.rect.y > p_y:
            self.rect.y -= round(self.speed * dt)

        if self.hp != self.hp_MAX:
            pygame.draw.rect(screen, GREEN, (self.rect.x+self.w/4, self.rect.y, (self.hp*self.w)*0.06, self.h*0.05))

    def get_click(self):
        if self.shots_count <= 0:
            self.shots_count = self.shots_seconds
            return True
        self.shots_count -= 1

    def resize(self, w_old, h_old, w_new, h_new):
        self.scale_x = (self.rect.x * 100) / w_old
        self.scale_y = (self.rect.y * 100) / h_old

        self.rect.x = (self.scale_x * w_new) / 100
        self.rect.y = (self.scale_y * h_new) / 100

        self.w, self.h = round(w_new * 0.15), round(h_new * 0.15)
        self.image = pygame.transform.scale(self.image_org, (self.w, self.h))

        self.speed = round(h_new / self.speed_nr)