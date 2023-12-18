import pygame
import random
import time
import webbrowser
pygame.init()

#Farger
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,128,255)
GREEN = (0,255,0)
GRAY = (128,128,128)
LIGHT_GRAY = (192,192,192)

#Load
bk = pygame.image.load('Background.png')
rc  = pygame.image.load('RocketCan.png')
pr  = pygame.image.load('Parachute.png')

#NB Variabler
WIDTH = 710
HEIGHT = 443
FPS = 20

#Tegner SCREEN
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Top Height')
clock = pygame.time.Clock()


class box():
    X = 100
    Y = 310

    bottom = 310
    
    curr_height = 0
    top_height = 0
    
    speed_u = 10
    speed_d = 1

    show_time_MAX = 1*FPS
    pause_MAX = 0.5*FPS
    
    show_time = show_time_MAX
    pause = pause_MAX

    
    curr_slide = 0
    MAX_slide = 0
    
    curr_col = GREEN
    Pause = False

    para = False
    move = False
    blink = False

    def Draw(self):
        if self.para == True:
            SCREEN.blit(pr, ((self.X-5), (self.Y-24)))
        if self.Y >= 310:
            self.para = False
        
        if self.move == True and self.Y >= 5:#Opp
            self.blink = False
            box.zero(self)
            self.Y -= self.speed_u
            self.curr_height += 10

        if self.move == False and self.Y < self.bottom:#Ned
            self.blink = False
            box.zero(self)
            self.Y += self.speed_d
            self.curr_height -= 1
            

        if self.curr_height > self.top_height:
            self.top_height = self.curr_height
            
        SCREEN.blit(rc, (self.X, self.Y))

    def blink_on(self):
        List = [0]
        
        #Fyller List
        for i in str(self.top_height):
            for j in range(0, int(i)):
                List.append(1)
            List.append(0)
        print(List)
        
        self.MAX_slide = (len(List))-1

        #Visning-tid
        if self.Pause == False:
            self.show_time -= 1
            if self.show_time == 0:
                self.Pause = True
                self.show_time = self.show_time_MAX
                if self.curr_slide <= self.MAX_slide:
                    self.curr_slide += 1
                    if self.curr_slide > self.MAX_slide:
                        self.curr_slide = 0
                
        #Pause-tid
        if self.Pause == True:
            self.pause -= 1
            if self.pause == 0:
                self.Pause = False
                self.pause = self.pause_MAX

        #Bytter farger
        if List[self.curr_slide] == 1:
            self.curr_col = BLUE
        if List[self.curr_slide] == 0:
            self.curr_col = RED
        if self.curr_slide == 0:
            self.curr_col = GREEN
            
        if self.Pause == False: #CAS
            #pygame.draw.rect(SCREEN, self.curr_col, [90, 350, 50, 50])
            pygame.draw.rect(SCREEN, self.curr_col, [self.X+8, self.Y-4, 10, 10])

    def zero(self):
        self.show_time_MAX = 1*FPS
        self.pause_MAX = 0.5*FPS

        self.show_time = self.show_time_MAX
        self.pause = self.pause_MAX

            
        self.curr_slide = 0
        self.MAX_slide = 0
            
        self.curr_col = GREEN
        self.Pause = False            
    
def text(x, y, size, color, text):
    myfont = pygame.font.SysFont("monospace", size)     
    dis_text = myfont.render(str(text), 1, (color))
    SCREEN.blit(dis_text, (x, y))
    
def simulation():
    game = True
    player = box()
    

    while game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_UP:
                    player.move = True
                    player.para = False
                if event.key == pygame.K_DOWN:
                    player.move = False
                    player.Y = player.bottom
                    player.curr_height = 0
                    
                if event.key == pygame.K_r:
                    player.top_height = 0
                    player.blink = False
                    box.zero(player)
                    
                if event.key == pygame.K_b:
                    if player.blink == False and player.Y == player.bottom:
                        player.blink = True
                    else:
                        player.blink = False
                        box.zero(player)
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.move = False
                    player.para = True


        SCREEN.blit(bk, (0, 0))
        
        if player.blink == True:
            box.blink_on(player)
        box.Draw(player)
        text(415, 20, 25, BLACK, "Top Height:{0}m".format(str(player.top_height)))
        text(415, 50, 25, BLACK, "Current Height:{0}m".format(str(player.curr_height)))
        pygame.display.update()
        clock.tick(FPS)


    
simulation()
pygame.quit()
quit()
