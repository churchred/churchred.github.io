from pygame.locals import *
import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()

ost2_path = 'Sounds/ost2.mp3'
pygame.mixer.music.set_volume(VOLUME_MUSIC)


class Game:
    def __init__(self):
        self.HEIGHT = 500
        self.WIDTH = 800

        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        self.header = pygame.image.load('Bilder/head.png').convert_alpha()
        self.header = pygame.transform.scale(self.header, (int(self.WIDTH*0.3), int(self.HEIGHT*0.2)))
        self.start_bk1 = pygame.image.load('Bilder/start_screen_1.png').convert()
        self.start_bk2 = pygame.image.load('Bilder/start_screen_2.png').convert()
        self.start_bk_Array = [self.start_bk1, self.start_bk2]

        self.bk_x_1, self.bk_x_rel = 0, 0

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
