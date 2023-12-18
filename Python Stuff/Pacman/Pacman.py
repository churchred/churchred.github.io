import pygame
import random
import time
pygame.init()
pygame.font.init()

#Farger
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
gray = (128,128,128)

dis_width = 500     #500/25 = 20
dis_height = 525      


#Lage skjerm og FPS
gameDisplay = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Pacman')
clock = pygame.time.Clock()


img_1 = pygame.image.load('Bilder/Pacman_1.png')
img_2 = pygame.image.load('Bilder/Pacman_2.png')
#img_3 = pygame.image.load('Bilder/Pacman_3.png') Ikke laget ennå
img = img_2
pcmn = img

pcmn2 = pygame.image.load('Bilder/Pacman_2.png')
ball = pygame.image.load('Bilder/ball.png')
ghostRed = pygame.image.load('Bilder/ghostRed.png')
ghostPink = pygame.image.load('Bilder/ghostPink.png')
ghostGreen = pygame.image.load('Bilder/ghostGreen.png')
exit_icon = pygame.image.load('Bilder/exit.png')
start_icon = pygame.image.load('Bilder/start.png')
LastTech = pygame.image.load('Bilder/LastTech.png')
kris_icon = pygame.image.load('Bilder/kriss.png')

pygame.mixer.music.load('Bilder/pcmn_ost.mp3')
effect = pygame.mixer.Sound('Bilder/pcmn_eat2.wav')
effect.set_volume(.2)


#Gameloopen
menu = True
gameOver = True
choice = 0
Level = 1
FPS = 10
music = False
#                                 #  #
Map = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
       1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1,
       1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1,
       1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1,
       1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
       1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1,
       1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1,
       1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1,
       1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, #
       1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1,
       1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1,
       1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1,
       1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1,
       1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
       1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1,
       1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1,
       1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1,
       1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]



class Ball(pygame.sprite.Sprite):
	ballsprites = pygame.sprite.Group()
	def __init__(self, x ,y):
		
		pygame.sprite.Sprite.__init__(self)
		Ball.ballsprites.add(self)
		
		self.image = pygame.image.load('Bilder/ball.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = 25
		self.height = 25

def text():
	myfont = pygame.font.SysFont("monospace", 18)
	Level_Text = myfont.render(str(Level), 1, (white))
	Level_Text2 = myfont.render("Level:", 1, (white))
	gameDisplay.blit(Level_Text, (75, 505))
	gameDisplay.blit(Level_Text2, (3, 505))

def bk_bilde():
	xx = 1
	gameDisplay.blit(pcmn2, (125, 25))
	for i in range(0, 10):
		gameDisplay.blit(ball, (150+(i*25), 25))

	
while menu:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			menu = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				if music == True:
					music = False
				else:
					music = True
			if event.key == pygame.K_DOWN:
				if choice != 1:
					choice += 1
			if event.key == pygame.K_UP:
				if choice != 0:
					choice -= 1
			if event.key == pygame.K_RETURN:
				if choice == 0:
					if music == True:
						pygame.mixer.music.play(0)
						pygame.mixer.music.set_volume(0.2)
					gameOver = False
				if choice == 1:
					menu = False
	#Variabler
	move_right = True
	move_left = False
	move_up = False
	move_down = False

	next_move = 1
	# 1 = Right
	# 2 = Left
	# 3 = Up
	# 4 = Down

	speed = (25/2)
	make_balls = False
	ball_count = 0
	
	pcmn_X = 25
	pcmn_Y = 25
	rute_x = 0
	rute_y = 0
	pcmn_ret = 1
	lose = False
	framecounter_MAX = 2  #SPRITE COUNTER
	framecounter = framecounter_MAX 
	spritecounter = 1
	
	#Ghost RED Var
	ghostRed_move = 3
	ghostRed_x = 450
	ghostRed_y = 475
	ghostRed_Array = []

	#Ghost PINK Var
	ghostPink_move = 3
	ghostPink_x = 25
	ghostPink_y = 475
	ghostPink_Array = []

	#Ghost GREEN Var
	ghostGreen_move = 2
	ghostGreen_x = 150
	ghostGreen_y = 375
	ghostGreen_Array = []

					
	gameDisplay.fill(black)
	gameDisplay.blit(LastTech, (200,100))
	gameDisplay.blit(kris_icon, (300,500))
	pygame.draw.rect(gameDisplay, gray, [175, 250+(choice*100), 150, 50])
	gameDisplay.blit(start_icon, (175, 250))
	gameDisplay.blit(exit_icon, (175, 350))
	bk_bilde()
	text()
	pygame.display.update()
	clock.tick(FPS)
	
	while not gameOver:
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				menu = False
				gameOver = True
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					gameOver = True

				if event.key == pygame.K_1:
					if music == True:
						music = False
					else:
						music = True
					
				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					next_move = 1
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					next_move = 2
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					next_move = 3
				if event.key == pygame.K_DOWN or event.key == pygame.K_s:
					next_move = 4
					
#Testing av Rotasjon i bilder.. NOT WORKING
##if move_right == True:
##move_left = False
##move_up = False
##move_down = False
##pcmn2 = pygame.transform.rotate(pcmn2,-90)
				

		gameDisplay.fill(black)		
		for row in Map:
			if row == 1:
				pygame.draw.rect(gameDisplay, blue, [rute_x, rute_y, 25, 25])
				if (pcmn_X+25)  == rute_x and pcmn_Y == rute_y: #RIGHT CHECK BLUE
					if move_right == True:
						move_right = False
				if pcmn_X  == (rute_x+25) and pcmn_Y == rute_y: #LEFT CHECK BLUE
					if move_left == True:
						move_left = False
				if pcmn_X  == rute_x and pcmn_Y == (rute_y+25): #UP CHECK BLUE
					if move_up == True:
						move_up = False
				if pcmn_X  == rute_x and (pcmn_Y+25) == rute_y: #DOWN CHECK BLUE
					if move_down == True:
						move_down = False
						
			if row == 0:
				if make_balls == False:
					K = Ball(rute_x, rute_y)
					ball_count += 1
					
				if (pcmn_X+25)  == rute_x and pcmn_Y == rute_y: #RIGHT CHECK BLACK
					if next_move == 1:
						move_right = True
						move_left = False
						move_up = False
						move_down = False
						pcmn_ret = 1
						next_move = 0
				if pcmn_X  == (rute_x+25) and pcmn_Y == rute_y: #LEFT CHECK BLACK
					if next_move == 2:
						move_right = False
						move_left = True
						move_up = False
						move_down = False
						pcmn_ret = 2
						next_move = 0
				if pcmn_X  == rute_x and pcmn_Y == (rute_y+25): #UP CHECK BLACK
					if next_move == 3:
						move_right = False
						move_left = False
						move_up = True
						move_down = False
						pcmn_ret = 3
						next_move = 0
				if pcmn_X  == rute_x and (pcmn_Y+25) == rute_y: #DOWN CHECK BLACK
					if next_move == 4:
						move_right = False
						move_left = False
						move_up = False
						move_down = True
						pcmn_ret = 4
						next_move = 0

						
				#Sjekker mulige veier for GhostRed
				if ghostRed_x+25 == rute_x and ghostRed_y == rute_y or ghostRed_x+speed == rute_x and ghostRed_y == rute_y:
					if ghostRed_move != "2":
						ghostRed_Array.append("1")
				if ghostRed_x == rute_x+25 and ghostRed_y == rute_y or ghostRed_x == rute_x+speed and ghostRed_y == rute_y:
					if ghostRed_move != "1":
						ghostRed_Array.append("2")
				if ghostRed_x == rute_x and ghostRed_y == rute_y+25 or ghostRed_x == rute_x and ghostRed_y == rute_y+speed:
					if ghostRed_move != "4":
						ghostRed_Array.append("3")
				if ghostRed_x == rute_x and ghostRed_y+25 == rute_y or ghostRed_x == rute_x and ghostRed_y+speed == rute_y:
					if ghostRed_move != "3":
						ghostRed_Array.append("4")

				#Sjekker mulige veier for ghostPink
				if ghostPink_x+25 == rute_x and ghostPink_y == rute_y or ghostPink_x+speed == rute_x and ghostPink_y == rute_y:
					if ghostPink_move != "2":
						ghostPink_Array.append("1")
				if ghostPink_x == rute_x+25 and ghostPink_y == rute_y or ghostPink_x == rute_x+speed and ghostPink_y == rute_y:
					if ghostPink_move != "1":
						ghostPink_Array.append("2")
				if ghostPink_x == rute_x and ghostPink_y == rute_y+25 or ghostPink_x == rute_x and ghostPink_y == rute_y+speed:
					if ghostPink_move != "4":
						ghostPink_Array.append("3")
				if ghostPink_x == rute_x and ghostPink_y+25 == rute_y or ghostPink_x == rute_x and ghostPink_y+speed == rute_y:
					if ghostPink_move != "3":
						ghostPink_Array.append("4")

				#Sjekker mulige veier for ghostGreen
				if ghostGreen_x+25 == rute_x and ghostGreen_y == rute_y or ghostGreen_x+speed == rute_x and ghostGreen_y == rute_y:
					if ghostGreen_move != "2":
						ghostGreen_Array.append("1")
				if ghostGreen_x == rute_x+25 and ghostGreen_y == rute_y or ghostGreen_x == rute_x+speed and ghostGreen_y == rute_y:
					if ghostGreen_move != "1":
						ghostGreen_Array.append("2")
				if ghostGreen_x == rute_x and ghostGreen_y == rute_y+25 or ghostGreen_x == rute_x and ghostGreen_y == rute_y+speed:
					if ghostGreen_move != "4":
						ghostGreen_Array.append("3")
				if ghostGreen_x == rute_x and ghostGreen_y+25 == rute_y or ghostGreen_x == rute_x and ghostGreen_y+speed == rute_y:
					if ghostGreen_move != "3":
						ghostGreen_Array.append("4")

						
			rute_x += 25
			if rute_x == dis_width:
				rute_x = 0
				rute_y += 25

		rute_x = 0
		rute_y = 0
		make_balls = True
		
				
		#print("U:", block_up, " D:", block_down, " R:", block_right, " L:", block_left)
		#print(Ball.ballsprites)
		#print(pcmn_X, pcmn_Y)
		#print(ghostRed_Array)
		#print(ball_count)
		#print(spritecounter)
		#print("PCMN(", pcmn_X, ",", pcmn_Y, ")", "Green(", ghostGreen_x, ",", ghostGreen_y, ")", "Red(", ghostRed_x, ",", ghostRed_y, ")", "Pink(", ghostPink_x, ",", ghostPink_y, ")")
		print("Array:", Ball.ballsprites, " Var:", ball_count)

		
		#"Beveger" sprite
		framecounter -= 1
		if framecounter == 0:
			if spritecounter > 2:
				spritecounter = 1
			if spritecounter == 1:
				img = img_1
				pcmn = img
			if spritecounter == 2:
				img = img_2
				pcmn = img
			spritecounter += 1
			framecounter = framecounter_MAX
		
		#Beveger Pacman                        
		if move_left == True:
			pcmn_X -= speed
		if move_right == True:
			pcmn_X += speed 
		if move_up == True:
			pcmn_Y -= speed
		if move_down == True:
			pcmn_Y += speed
		if pcmn_X+-25 >= dis_width:
			pcmn_X = 0
		if pcmn_X+25 <= 0:
			pcmn_X = dis_width-25

		if pcmn_ret == 1: #Right
			pcmn = img
		if pcmn_ret == 2: #Left
			pcmn = pygame.transform.rotate(img, 180)
		if pcmn_ret == 3: #Up
			pcmn = pygame.transform.rotate(img, 90)
		if pcmn_ret == 4: #Down
			pcmn = pygame.transform.rotate(img, -90)


		#Beveger RED Ghost
		nr_len = (len(ghostRed_Array))
		nr_ran = (random.randrange(0,nr_len))
		nr_final = ghostRed_Array[(nr_ran)]
		ghostRed_move = str(nr_final)
		
		if ghostRed_move == "1": #Right
			ghostRed_x += speed
			if ghostRed_x+25 >= dis_width:
			     ghostRed_x = 0   
		if ghostRed_move == "2": #Left
			ghostRed_x -= speed
			if ghostRed_x <= 0:
				ghostRed_x = dis_width-25
		if ghostRed_move == "3": #Up
			ghostRed_y -= speed
		if ghostRed_move == "4": #Down
			ghostRed_y += speed
			
		ghostRed_Array = []

		#Beveger PINK Ghost
		nr_len = (len(ghostPink_Array))
		nr_ran = (random.randrange(0,nr_len))
		nr_final = ghostPink_Array[(nr_ran)]
		ghostPink_move = str(nr_final)
		
		if ghostPink_move == "1": #Right
			ghostPink_x += speed
			if ghostPink_x+25 >= dis_width:
			     ghostPink_x = 0   
		if ghostPink_move == "2": #Left
			ghostPink_x -= speed
			if ghostPink_x <= 0:
				ghostPink_x = dis_width-25
		if ghostPink_move == "3": #Up
			ghostPink_y -= speed
		if ghostPink_move == "4": #Down
			ghostPink_y += speed
			
		ghostPink_Array = []

		#Beveger GREEN Ghost
		nr_len = (len(ghostGreen_Array))
		nr_ran = (random.randrange(0,nr_len))
		nr_final = ghostGreen_Array[(nr_ran)]
		ghostGreen_move = str(nr_final)
		
		if ghostGreen_move == "1": #Right
			ghostGreen_x += speed
			if ghostGreen_x+25 >= dis_width:
			     ghostGreen_x = 0   
		if ghostGreen_move == "2": #Left
			ghostGreen_x -= speed
			if ghostGreen_x <= 0:
				ghostGreen_x = dis_width-25
		if ghostGreen_move == "3": #Up
			ghostGreen_y -= speed
		if ghostGreen_move == "4": #Down
			ghostGreen_y += speed
			
		ghostGreen_Array = []
		
		if pcmn_X < ghostRed_x+25 and pcmn_X+25 > ghostRed_x and pcmn_Y < ghostRed_y+25 and pcmn_Y+25 > ghostRed_y:
			lose = True
			print("RED")
		if pcmn_X < ghostPink_x+25 and pcmn_X+25 > ghostPink_x and pcmn_Y < ghostPink_y+25 and pcmn_Y+25 > ghostPink_y:
			lose = True
			print("PINK")
		if pcmn_X < ghostGreen_x+25 and pcmn_X+25 > ghostGreen_x and pcmn_Y < ghostGreen_y+25 and pcmn_Y+25 > ghostGreen_y:
			lose = True
			print("GREEN")
		if lose == True:
			Level = 1
			for i in Ball.ballsprites:
				Ball.ballsprites.remove(i)
			lose = False
			gameOver = True
			#print("Game Over")
			
		#Sjekker om Pacman spiser Baller
		for i in Ball.ballsprites:
			if i.rect.x == pcmn_X and i.rect.y == pcmn_Y:
				if music == True:
					effect.play()
				Ball.ballsprites.remove(i)
				ball_count -= 1
				if ball_count == 0:
					Level += 1
					gameOver = True
		
				
		Ball.ballsprites.draw(gameDisplay)
		gameDisplay.blit(pcmn, (pcmn_X,pcmn_Y))
		gameDisplay.blit(ghostRed, (ghostRed_x, ghostRed_y))
		gameDisplay.blit(ghostPink, (ghostPink_x, ghostPink_y))
		gameDisplay.blit(ghostGreen, (ghostGreen_x, ghostGreen_y))
		pygame.display.update()
		clock.tick(FPS)


pygame.quit()
quit()
