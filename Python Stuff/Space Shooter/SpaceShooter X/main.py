from pygame.locals import *
import pygame
from settings import *  # Gathers info and variables from settings.py
import csv

pygame.init()
pygame.font.init()


class App:

    def __init__(self):
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH

        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.running = True
        self.series_list_key = True
        self.series_watch = False
        self.bookmarks = False
        self.episode_change = False

        self.run()

    def run(self):
        while self.running:
            self.series_list()
            self.series_watch()
            self.bookmarks()
            self.episode_change()

    def series_list(self):
        while self.series_list_key:
            self.events()
            self.update()
            self.SCREEN.fill(bk_color)

    def series_watch(self):
        pass

    def bookmarks(self):
        pass

    def episode_change(self):
        pass

    def update(self):
        pygame.display.update()
        self.clock.tick(FPS)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                quit()

    def startup(self):
        pass


a = App()

while a.running:
    print("STARTING")
    a.new()

pygame.display.quit()
pygame.quit()
quit()