# Import a library
import pygame
import os
# Initialize the game engien
pygame.init()

# Define colors http://www.colorpicker.com/ 
WHITE	= (255,255,255)
BLACK	= (  0,  0,  0)
RED	= (255,  0,  0)
GREEN	= (0,  255,  0)
BLUE	= (0,    0,255)

#Load
Background = pygame.image.load('Background.png')
RocketCan  = pygame.image.load('RocketCan.png')
Parachute  = pygame.image.load('Parachute.png')

font = pygame.font.Font("C:/Windows/Fonts/SCHLBKB.TTF", 25)

# Set the width an Height of the screen
screen = pygame.display.set_mode((710, 443))

pygame.display.set_caption("TopHeight")

# Veriebls
done = False
movment_Up = False
Blink = False
Reset = False

FPS = 20

Top_Height = 0
Current_Height = 0

RocketCan_Y = 310
Old_RC_Y = RocketCan_Y
Parachute_Y = RocketCan_Y - 24

RocketCan_speed_up = 10
RocketCan_speed_down = 1

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def Blink_def(Top_Height, Blink, RocketCan_Y):
	if Blink == True:
		pygame.draw.rect(screen, GREEN, [100,RocketCan_Y,10,10])
		print("Blink")
	else:
		pass

#---------- Main Program Loop ----------
while done == False:
	# ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
	for event in pygame.event.get(): 									#User did something (Key stroak/moving mouse etc.)
		if event.type == pygame.QUIT:
			done = True
			
		if event.type == pygame.KEYDOWN:								#What happens if pressing a key:
			if event.key == pygame.K_UP or event.key == pygame.K_w: 	#Key Up/w
				movment_Up = True
			if event.key == pygame.K_b:									#Key b
				Blink = True
			if event.key == pygame.K_r:									#Key r
				Reset = True
		
		if event.type == pygame.KEYUP: 									#What happens if releasing a key
			if event.key == pygame.K_UP or event.key == pygame.K_w:  	#Key Up/w
				movment_Up = False
			if event.key == pygame.K_b: 								#Key b
				Blink = False
			if event.key == pygame.K_r: 								#Key r 									
				Reset = False
	
	#ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
	
	#ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
	if movment_Up == True: 												#Moveing up, buy pressing up/w
		if RocketCan_Y > 0:
			RocketCan_Y -= RocketCan_speed_up
			Parachute_Y = -100
			
	if movment_Up == False: 											#Moveing down, without pressing key
		if RocketCan_Y < 310:
			RocketCan_Y += RocketCan_speed_down
			Parachute_Y = RocketCan_Y - 24
		if RocketCan_Y >= 310:
			Parachute_Y = -100
	
	if RocketCan_Y < Old_RC_Y: 											#Traking of Top Height
		Old_RC_Y = RocketCan_Y
		Top_Height = 310-Old_RC_Y
	Current_Height = 310-RocketCan_Y
	
	if Reset == True: 													#Reset Top Height
		Top_Height = Current_Height
		Old_RC_Y = RocketCan_Y
	
	#ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
	
	
	#ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
	screen.blit(Background, (0,0))
	
	T_Height = font.render("Top Height:         "+str(Top_Height), True, BLACK)
	C_Height = font.render("Current Height: "+str(Current_Height), True, BLACK)
	screen.blit(T_Height, [400,100])
	screen.blit(C_Height, [400,150])
	
	Blink_def(Top_Height, Blink,RocketCan_Y)
	screen.blit(RocketCan, (105,RocketCan_Y))
	screen.blit(Parachute, (100,Parachute_Y))
	#ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
	
	pygame.display.flip()
	
	clock.tick(FPS)
	
pygame.quit()






