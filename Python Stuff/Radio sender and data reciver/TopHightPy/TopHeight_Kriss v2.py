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


#Load
bk = pygame.image.load('Background.png')
rc  = pygame.image.load('RocketCan.png')
pr  = pygame.image.load('Parachute.png')
fire_img = pygame.image.load('fire.png')
#fire_img = pygame.transform.rotate(img, 180)

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

    bottom = 310 #Bakken hvor rakketen står
    counter_up = 5
    
    curr_height = 0
    top_height = 0
    
    speed_u = 10 #Speed up
    speed_d = 1  #Falling speed (down)

    show_time_MAX = 1*FPS
    pause_MAX = 0.5*FPS
    
    show_time = show_time_MAX #Hvor lenge lysa skal være PÅ
    pause = pause_MAX #Hvor lenge mellomrommet mellom lysa er

    
    curr_slide = 0
    MAX_slide = 0
    
    falling_MAX = 10 #Hvor høyt den flyr etter å ha stoppa
    falling = falling_MAX
    
    curr_col = GREEN
    Pause = False

    para = False
    move = False
    fall = False
    blink = False
    done = True
    fire = False

    def Draw(self):
        if self.para == True:
            SCREEN.blit(pr, ((self.X-5), (self.Y-24)))#FALLSKJERM
        if self.move == True:
            SCREEN.blit(fire_img, ((self.X), (self.Y+26)))#ILD

        #Hvis rakket er nær bakken    
        if self.Y >= self.bottom:
            self.para = False
            self.done = False
            self.fall = False
            
        #Beveger rakket OPP
        if self.move == True:
            self.blink = False
            box.zero(self)
            self.Y -= self.speed_u
            self.curr_height += 10

        #Fly litt etter stopp    
        if self.fall == False and self.done == False and self.move == False and self.Y < self.bottom:
            self.Y -= self.falling
            self.falling -= 1
            self.curr_height += self.falling
            if self.falling == 0:
                self.falling = self.falling_MAX
                self.fall = True
                self.done = True
                self.para = True
                self.curr_height = self.curr_height+10
                
        #Beveger rakket NED
        if self.move == False and self.Y < self.bottom and self.fall == True:
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
            
        if self.Pause == False: #Lysa
            #pygame.draw.rect(SCREEN, self.curr_col, [90, 350, 50, 50]) #STORT LYS
            pygame.draw.rect(SCREEN, self.curr_col, [self.X+8, self.Y-4, 10, 10])

    def zero(self):
        #RESETTER BLINKING
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
    bk_y = 0
    txt_y = 20
    move_up = False
    move_down = False
    cam_h = 0
    cam_speed = 15

    x= 125
    y = 199
    z = 242
    
    
    LIGHT_BLUE = (125, 199, 242) #Matcher bk perfect! FARGE

    while game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_UP:
                    player.move = True
                    player.para = False
                    
                    
                if event.key == pygame.K_DOWN:
                    #Resetter skjermflytting
                    bk_y = 0
                    player.Y += player.counter_up
                    player.bottom = 310
                    player.counter_up = 0
                    cam_h = 0
                    x= 125
                    y = 199
                    z = 242
                    
                    #Resetting rakket
                    player.move = False
                    player.Y = player.bottom
                    player.curr_height = 0
                    
                if event.key == pygame.K_r:
                    #Resetter top height
                    player.top_height = 0
                    player.blink = False
                    box.zero(player)


                #Moving the screen
                if event.key == pygame.K_w:
                    move_up = True
                if event.key == pygame.K_s:
                    move_down = True
                    
                if event.key == pygame.K_b:
                    #Starter Blinking
                    if player.blink == False and player.Y == player.bottom:
                        player.blink = True
                    else:
                        player.blink = False
                        box.zero(player)
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.done = False
                    player.move = False
                    player.fall = False
                if event.key == pygame.K_w:
                    move_up = False
                if event.key == pygame.K_s:
                    move_down = False

        #Beveger kamera opp
        if move_up == True:
            bk_y += cam_speed
            player.Y += cam_speed
            player.bottom += cam_speed
            player.counter_up -= cam_speed
            cam_h += cam_speed

            if cam_h > 1999 and x != 0:
                x -= 1
                y -= 1
                z -= 1
                
        #Beveger Kamera ned  
        if move_down == True:
            if player.bottom != 310:
                bk_y -= cam_speed
                player.Y -= cam_speed
                player.bottom -= cam_speed
                player.counter_up += cam_speed
                cam_h -= cam_speed
                
            if cam_h > 2000 and z != 243:
                x += 1
                y += 1
                z += 1
                    
        col = (x, y, z)
        SCREEN.fill(col)
        SCREEN.blit(bk, (0, bk_y))

        if player.blink == True:
            box.blink_on(player)
            
        #print("Bunn_Y:[{0}]".format(player.bottom), "Player_Y:[{0}]".format(player.Y),
        #      "Current Height:[{0}]".format(player.curr_height),"bk_y:[{0}]".format(cam_h) ,"Camera Height:[{0}]".format(cam_h))    

        box.Draw(player)
        text(490, 20, 25, BLACK, "Top:{0}m".format(str(player.top_height)))
        text(490, 45, 25, BLACK, "Current:{0}m".format(str(player.curr_height)))
        text(WIDTH-40, HEIGHT-15, 12, BLACK, cam_h)
        pygame.display.update()
        clock.tick(FPS)


    
simulation()
pygame.quit()
quit()
