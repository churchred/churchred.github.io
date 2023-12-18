from pygame.locals import *
import pygame
import csv
import random
from settings import *  # En annen .py fil jeg har
from sprites import *  # En annen .py fil jeg har
from sprites_boss import *  # En annen .py fil jeg har


pygame.init()
pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024)
pygame.font.init()

#Load sounds
laser_sound = pygame.mixer.Sound('Sounds/laser.wav')
heal_sound = pygame.mixer.Sound('Sounds/heal.wav')
alarm_sound = pygame.mixer.Sound('Sounds/alarm.wav')
dmg_sound = pygame.mixer.Sound('Sounds/dmg.wav')


laser_sound.set_volume(VOLUME_EFFECT)
heal_sound.set_volume(VOLUME_EFFECT)
alarm_sound.set_volume(VOLUME_EFFECT)
dmg_sound.set_volume(VOLUME_EFFECT)

ost1_path = 'Sounds/ost.mp3'
ost2_path = 'Sounds/ost2.mp3'
pygame.mixer.music.set_volume(VOLUME_MUSIC)


class Game:
    def __init__(self):
        self.HEIGHT = 500
        self.WIDTH = 800

        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.bk = pygame.image.load('Bilder/bk2.png').convert()

        self.header = pygame.image.load('Bilder/head.png').convert_alpha()
        self.header = pygame.transform.scale(self.header, (int(self.WIDTH*0.3), int(self.HEIGHT*0.2)))
        self.start_bk1 = pygame.image.load('Bilder/start_screen_1.png').convert()
        self.start_bk2 = pygame.image.load('Bilder/start_screen_2.png').convert()
        self.start_bk_Array = [self.start_bk1, self.start_bk2]

        self.hp_img = pygame.image.load('Bilder/heart.png').convert_alpha()
        self.rock_img = pygame.image.load('Bilder/astroid.png').convert_alpha()
        self.trash_img = pygame.image.load('Bilder/trash.png').convert_alpha()
        self.ufo_img = pygame.image.load('Bilder/ufo.png').convert_alpha()

        self.dt = 0  # Hvor mange millisekunder mellom hver frame

        self.running = True      # Running everything
        self.playing = True      # Running the game
        self.pause = False       # Pause
        self.start = True        # Running startscreen
        self.gameover = False    # Running losescreen
        self.settings = False    # Running settings
        self.high_score = False  # Running high scores

        self.bk_x_1, self.bk_x_rel = 0, 0

    def new(self):  # Starts new game
        self.player_array = pygame.sprite.Group()  # Array med player
        self.all_bullets_array = pygame.sprite.Group()  # Liste med skudd
        self.all_enemies_array = pygame.sprite.Group()  # Liste med enemies og andre ting man kan skyte
        self.all_good_array = pygame.sprite.Group()  # Liste med ting man kan plukke opp (Eks: HP)

        self.player = Player(self.WIDTH, self.HEIGHT)
        self.hp_bar = HealtBar(self.WIDTH, self.HEIGHT)
        self.player_array.add(self.player)
        self.player_array.add(self.hp_bar)

        self.choice = 0  # Valg på start menuen, hvilken har du markert?

        # SPILLVARIABLER for selve spillet
        self.meters = 0
        self.m_count = 0 # Slik at self.meters ikke er for rask.
        self.points = 0

        # Trash variabler
        self.trash_per_second = 2*FPS  # Hvor mye trash som kommer per sekund
        self.trash_count = 0

        # Rock variabler
        self.rock_count = 0
        self.rock_per_sec = 10

        # UFO variabler
        self.ufo = False
        self.ufo_per_second = 20  # Hvor ofte ufoer kommer etter hverandre
        self.ufo_count = 0

        # BOSSER
        self.boss = False

        self.run()

    def start_screen(self):  # Inro screen
        self.start = True
        nr = 0
        count = 0

        col_1 = WHITE
        col_2 = WHITE
        col_3 = WHITE
        col_4 = WHITE

        self.choice = 0
        pygame.mixer.music.load(ost2_path)
        pygame.mixer.music.play(-1)
        while self.start:
            self.events()

            if self.choice == 0:
                col_1 = RED
                col_2 = WHITE
                col_3 = WHITE
                col_4 = WHITE
            if self.choice == 1:
                col_1 = WHITE
                col_2 = RED
                col_3 = WHITE
                col_4 = WHITE
            if self.choice == 2:
                col_1 = WHITE
                col_2 = WHITE
                col_3 = RED
                col_4 = WHITE
            if self.choice == 3:
                col_1 = WHITE
                col_2 = WHITE
                col_3 = WHITE
                col_4 = RED

            self.SCREEN.blit(pygame.transform.scale(self.start_bk_Array[nr], (self.WIDTH, self.HEIGHT)), (0, 0))

            x = self.WIDTH / 2 - int(self.WIDTH*0.5) / 2
            self.SCREEN.blit(pygame.transform.scale(self.header, (int(self.WIDTH*0.5), int(self.HEIGHT*0.4))), (x, self.HEIGHT*0.02))

            self.text("START", int(self.WIDTH * 0.05), col_1, 0, self.HEIGHT / 2.2, True)
            self.text("HIGH SCORES", int(self.WIDTH * 0.05), col_2, 0, self.HEIGHT / 1.85, True)
            self.text("SETTINGS", int(self.WIDTH * 0.05), col_3, 0, self.HEIGHT / 1.6, True)
            self.text("EXIT", int(self.WIDTH * 0.05), col_4, 0, self.HEIGHT / 1.4, True)

            count += 1
            if count == FPS*0.5:
                count = 0
                nr += 1
                if nr > len(self.start_bk_Array)-1:
                    nr = 0
            self.clock.tick(FPS)
            pygame.display.update()

    def lose_screen(self):
        while self.gameover:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.gameover = False

                if event.type == VIDEORESIZE:
                    print("VIDEO CHANGED")

                    for i in self.player_array:
                        i.resize(self.WIDTH, self.HEIGHT, event.w, event.h)
                    for i in self.all_bullets_array: # Resizer alle sprites i denne arrayen
                        i.resize(self.WIDTH, self.HEIGHT, event.w, event.h)
                    for i in self.all_enemies_array:
                        i.resize(self.WIDTH, self.HEIGHT, event.w, event.h)
                    for i in self.all_good_array:
                        i.resize(self.WIDTH, self.HEIGHT, event.w, event.h)

                    self.WIDTH, self.HEIGHT = event.w, event.h  # Gjør om WIDTH og HEIGHT til ny verdier
                    self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
                    self.all_bullets_array.update(self.dt, self.WIDTH, self.HEIGHT)

            self.draw()
            self.text("GAMEOVER!", int(self.WIDTH*0.09), WHITE, 10, self.HEIGHT/2, True)
            self.text("Press SPACE to continiue!", int(self.WIDTH * 0.03), WHITE, 10, self.HEIGHT / 1.5, True)

            pygame.display.update()
            self.clock.tick(FPS)

    def pause_screen(self):
        if self.pause:
            self.text("Paused", round(self.WIDTH*0.07), WHITE, 0, 0, False)
            pygame.display.update()

    def high_score_screen(self):
        self.high_score = False

    def settings_screen(self):
        self.settings = False

    def run(self):  # Gameloop
        self.playing = True
        g.start_screen()
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000  # For timebased movement
            if not self.pause:
                self.update()
            self.events()
            self.draw()
            self.pause_screen()
            self.lose_screen()

    def update(self):  # Gameloop - Update
        self.move_bk()
        self.player_array.update(self.dt, self.WIDTH, self.HEIGHT)
        self.all_bullets_array.update(self.dt, self.WIDTH, self.HEIGHT, self.SCREEN, self.player.rect.y)
        self.all_enemies_array.update(self.dt, self.WIDTH, self.HEIGHT, self.SCREEN, self.player.rect.y)
        self.all_good_array.update(self.dt, self.WIDTH, self.HEIGHT)
        self.collision_check()
        self.boss_setup()
        if not self.boss:
            self.counter_mobs()

        pygame.display.update()

    def boss_setup(self):
        if self.boss:
            pass

    def collision_check(self):
        for i in self.all_bullets_array:
            for ii in self.all_enemies_array:
                if ii.rect.x + ii.w > i.rect.x and ii.rect.x < i.rect.x + i.rect.w and ii.rect.y + ii.h > i.rect.y and ii.rect.y < i.rect.y + i.h:
                    if i.name == "Bullet" and ii.name == "Trash":
                        get_hearth = random.randrange(0, HEART_SPAWN_RATE, 1)
                        if get_hearth == 1:
                            h = HP(ii.rect.x, ii.rect.y, self.WIDTH, self.HEIGHT, self.hp_img)
                            self.all_good_array.add(h)
                        self.points += 5
                        ii.kill()
                        i.kill()
                    if i.name == "Bullet" and ii.name == "UFO":
                        ii.hp -= 1
                        i.kill()
                        if ii.hp <= 0:
                            ii.kill()
                            self.ufo = False

        for i in self.player_array:
            for ii in self.all_enemies_array:
                if ii.rect.x + ii.w > i.rect.x and ii.rect.x < i.rect.x + i.rect.w and ii.rect.y + ii.h > i.rect.y and ii.rect.y < i.rect.y + i.h:
                    if ii.name == "Trash" and i.name == "Ship":  # COLL mellom skip og trash
                        self.damage_taken(5)
                        if self.points != 0:
                            self.points -= 5
                        ii.kill()

                    if ii.name == "Rock" and i.name == "Ship":
                        self.damage_taken(20)
                        ii.kill()

                    if ii.name == "Bullet" and i.name == "Ship":
                        self.damage_taken(5)
                        ii.kill()

            for ii in self.all_good_array:
                if ii.rect.x + ii.w > i.rect.x and ii.rect.x < i.rect.x + i.rect.w and ii.rect.y + ii.h > i.rect.y and ii.rect.y < i.rect.y + i.h:
                    if ii.name == "HP_UP" and i.name == "Ship":  # COLL mellom skip og hp
                        pygame.mixer.Sound.play(heal_sound)
                        i.hp += 10
                        if i.hp > i.hp_MAX:
                            i.hp = i.hp_MAX
                        self.hp_bar.change_hp(i.hp, i.hp_MAX, self.WIDTH, self.HEIGHT)
                        ii.kill()

    def damage_taken(self, dmg):
        pygame.mixer.Sound.play(dmg_sound)
        self.player.hp -= dmg
        if self.player.hp <= 0:
            self.playing = False
            self.gameover = True
        self.hp_bar.change_hp(self.player.hp, self.player.hp_MAX, self.WIDTH, self.HEIGHT)

    def counter_mobs(self):
        if self.m_count <= 0:
            self.meters += 1
            self.m_count = 0.1*FPS
            if self.meters == 100:
                self.rock_per_sec -= 1
            if self.meters == 200:
                self.rock_per_sec -= 1
            if self.meters == 300:
                self.rock_per_sec -= 1
            if self.meters == 400:
                self.rock_per_sec -= 1
            if self.meters == 500:
                self.rock_per_sec -= 1
            if self.meters == 600:
                self.rock_per_sec -= 1
            if self.meters == 700:
                self.rock_per_sec -= 1
            if self.meters == 800:
                self.rock_per_sec = 0
            if self.meters == 1000:
                for i in self.all_enemies_array:
                    i.kill()
                self.boss = True
        self.m_count -= 1

        # Trash
        if self.trash_count <= 0:
            self.trash_count = self.trash_per_second
            y = random.randrange(0, round(self.HEIGHT*0.9))
            self.t = Trash(self.WIDTH, y, self.WIDTH, self.HEIGHT, self.trash_img)
            self.all_enemies_array.add(self.t)
        self.trash_count -= 1

        # Rock
        if self.rock_count >= self.rock_per_sec*FPS:
            pygame.mixer.Sound.play(alarm_sound)
            r = Rocks(self.WIDTH, self.player.rect.y, self.WIDTH, self.HEIGHT, self.rock_img)
            self.all_enemies_array.add(r)
            self.rock_count = 0
        self.rock_count += 1

        # UFO
        if not self.ufo:
            if self.ufo_count >= self.ufo_per_second*FPS:
                u = UFO(self.WIDTH, self.HEIGHT, self.ufo_img)
                self.all_enemies_array.add(u)
                self.ufo = True
                self.ufo_count = 0
            self.ufo_count += 1

        if self.ufo:
            for i in self.all_enemies_array:
                if i.name == "UFO":
                    if i.get_click():
                        s = Bullet(i.rect.x, i.rect.y+i.h/2, self.WIDTH, self.HEIGHT, PURPLE)
                        self.all_enemies_array.add(s)

    def events(self):  # Gameloop - Events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    pygame.mixer.music.stop()

                if self.start:
                    if event.key == pygame.K_RETURN:
                        if self.choice == 0:
                            self.start = False
                            pygame.mixer.music.load(ost1_path)
                            pygame.mixer.music.play(-1)

                        if self.choice == 1:
                            self.high_score = True

                        if self.choice == 2:
                            self.settings = True

                        if self.choice == 3:
                            pygame.display.quit()
                            pygame.quit()
                            quit()

                    if event.key == pygame.K_DOWN:
                        if self.choice != 3:
                            self.choice += 1
                    if event.key == pygame.K_UP:
                        if self.choice != 0:
                            self.choice -= 1

                if not self.start:
                    if event.key == pygame.K_p:
                        if self.pause:
                            self.pause = False
                            pygame.mixer.music.unpause()
                        else:
                            self.pause = True
                            pygame.mixer.music.pause()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.start:
                    if not self.pause:
                        if self.player.get_click():
                            pygame.mixer.Sound.play(laser_sound)
                            self.s = Bullet(self.player.rect.x+self.player.w*0.8, self.player.rect.y+self.player.h*0.7, self.WIDTH, self.HEIGHT, RED)
                            self.all_bullets_array.add(self.s)

            if event.type == VIDEORESIZE:
                print("VIDEO CHANGED")

                for i in self.player_array:
                    i.resize(self.WIDTH, self.HEIGHT, event.w, event.h, self.player.hp)
                for i in self.all_bullets_array: # Resizer alle sprites i denne arrayen
                    i.resize(self.WIDTH, self.HEIGHT, event.w, event.h)
                for i in self.all_enemies_array:
                    i.resize(self.WIDTH, self.HEIGHT, event.w, event.h)
                for i in self.all_good_array:
                    i.resize(self.WIDTH, self.HEIGHT, event.w, event.h)

                self.WIDTH, self.HEIGHT = event.w, event.h  # Gjør om WIDTH og HEIGHT til ny verdier
                self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
                self.all_bullets_array.update(self.dt, self.WIDTH, self.HEIGHT)

    def draw(self):
        self.SCREEN.blit(pygame.transform.scale(self.bk, (self.WIDTH, self.HEIGHT)), (self.bk_x_rel - self.WIDTH, 0))
        if self.bk_x_rel < self.WIDTH:
            self.SCREEN.blit(pygame.transform.scale(self.bk, (self.WIDTH, self.HEIGHT)), (self.bk_x_rel, 0))

        self.player_array.draw(self.SCREEN)
        self.all_bullets_array.draw(self.SCREEN)
        self.all_enemies_array.draw(self.SCREEN)
        self.all_good_array.draw(self.SCREEN)

        self.text(str(self.meters)+"m", int(self.WIDTH * 0.03), WHITE, self.WIDTH*0.9, 0, False)
        self.text("|" + str(self.points)+"P", int(self.WIDTH * 0.03), WHITE, self.hp_bar.rect.x+self.hp_bar.w_MAX, 0, False)

    def move_bk(self):
        self.bk_x_rel = self.bk_x_1 % self.WIDTH
        self.bk_x_1 -= (self.WIDTH / 5) * self.dt

    def text(self, txt, size, color, x, y, center):
        myfont = pygame.font.SysFont("monospace", size)
        texty = myfont.render(txt, 1, color)
        text_rect = texty.get_rect(center=(self.WIDTH / 2, self.HEIGHT / 2))
        if center:
            x = self.WIDTH / 2 - texty.get_rect().width / 2
            self.SCREEN.blit(texty, (x, y))
        if not center:
            self.SCREEN.blit(texty, (x, y))


g = Game()


while g.running:
    print("NEW GAME")
    g.new()



pygame.display.quit()
pygame.quit()
quit()
