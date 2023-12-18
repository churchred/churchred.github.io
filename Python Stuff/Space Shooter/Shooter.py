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


#Load Bilder
ship = pygame.image.load('Bilder/skip.png')
ship_borken1 = pygame.image.load('Bilder/skip_skadd1.png')
ship_borken2 = pygame.image.load('Bilder/skip_skadd2.png')
bk = pygame.image.load('Bilder/background.png')
bk_title = pygame.image.load('Bilder/background_OLD.png')
heart = pygame.image.load('Bilder/heart.png')
LoadingBar = pygame.image.load('Bilder/LoadingBar.png')
Skill_1_icon = pygame.image.load('Bilder/Skill 1.png')
Skill_2_icon = pygame.image.load('Bilder/Skill 2.png')
Skill_3_icon = pygame.image.load('Bilder/Skill 3.png')
Skill_4_icon = pygame.image.load('Bilder/Skill 4.png')
Skill_5_icon = pygame.image.load('Bilder/Skill 5.png')
Skill_1_anime = pygame.image.load('Bilder/Skip_Skill 1.png')
Skill_2_anime = pygame.image.load('Bilder/Skip_Skill 2.png')
Skill_3_anime = pygame.image.load('Bilder/Skip_Skill 3.png')
Skill_4_anime = pygame.image.load('Bilder/Skip_Skill 4.png')
start_icon = pygame.image.load('Bilder/start.png')
exit_icon = pygame.image.load('Bilder/exit.png')
LT_Icon = pygame.image.load('Bilder/LastTech.png')
kris_icon = pygame.image.load('Bilder/kriss.png')
option_page = pygame.image.load('Bilder/option.png')
info_icon = pygame.image.load('Bilder/info.png')


#Lage skjerm og FPS
gameDisplay = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Spaaace')
clock = pygame.time.Clock()

#Gameover funk
def gameover():
	print("Gameover")
	time.sleep(1)

#Classen som lager skudda
class Shot(pygame.sprite.Sprite):
	shotsprites = pygame.sprite.Group()
	def __init__(self,x ,y):
		
		pygame.sprite.Sprite.__init__(self)
		Shot.shotsprites.add(self)
		
		self.image = pygame.image.load('Bilder/skudd.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = 20
		self.height = 20

#Classen som lager steinene
class Rock(pygame.sprite.Sprite):
	rocksprites = pygame.sprite.Group()
	def __init__(self,x ,y):
		
		pygame.sprite.Sprite.__init__(self)
		Rock.rocksprites.add(self)
		
		self.image = pygame.image.load('Bilder/rock.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = (y-49)
		self.width = 20
		self.height = 20

		
def text(LvL, XP):
	myfont = pygame.font.SysFont("monospace", 18)
	myfont2 = pygame.font.SysFont("monospace", 25)
	
	Level_Text = myfont.render("Level", 1, (black))
	LvL_Text = myfont2.render(str(LvL), 1, (black))
	
	gameDisplay.blit(Level_Text, (438, 450))
	if LvL >= 10:
		gameDisplay.blit(LvL_Text, (451, 470))
	else:
		gameDisplay.blit(LvL_Text, (458, 470))
	
	#print("Level:", LvL, " XP:", XP, "/", MAX_XP)

def UI(Liv,Ship_DMG, Ship_X, XP, LvL, sjold_prosent):
	Hp = int(Liv)
	nr = 0
	hp_y = 15
	
	for i in range(0, Hp):
		if nr == 5:
			nr = 0
			hp_y += 15
	
		gameDisplay.blit(heart, (440+(nr*10), hp_y))
		nr += 1
		
	gameDisplay.blit(LoadingBar, (440, hp_y+15))   #Mulig XP bar istedet i fremtiden?
	pygame.draw.rect(gameDisplay, blue, [440, hp_y+15, (XP_prosent/2), 8])        
		
	if Ship_DMG == True:
		pygame.draw.rect(gameDisplay, blue, [Ship_X-5, 495, (sjold_prosent/2), 8]) #Shield Bar vises på skipet

def Ability_UI(LvL, SkillBar_1, SkillBar_2, SkillBar_3, SkillBar_4, SkillBar_5, Skill_1_Cooldown, Skill_2_Cooldown, Skill_3_Cooldown, Skill_4_Cooldown, Skill_5_Cooldown, CD_1, CD_2, CD_3, CD_4, CD_5):
	if SkillBar_1 == True:
	     gameDisplay.blit(Skill_1_icon, (440, 100))
	if SkillBar_2 == True:
	     gameDisplay.blit(Skill_2_icon, (440, 160))
	if SkillBar_3 == True:
	     gameDisplay.blit(Skill_3_icon, (440, 220))
	if SkillBar_4 == True:
	     gameDisplay.blit(Skill_4_icon, (440, 280))
	if SkillBar_5 == True:
		gameDisplay.blit(Skill_5_icon, (440, 340))

	if Skill_1_Cooldown == True:
		pygame.draw.rect(gameDisplay, red, [440, 150, 50-(CD_1/2), 8])
	if Skill_2_Cooldown == True:
		pygame.draw.rect(gameDisplay, red, [440, 210, 50-(CD_2/2), 8])
	if Skill_3_Cooldown == True:
		pygame.draw.rect(gameDisplay, red, [440, 270, 50-(CD_3/2), 8])
	if Skill_4_Cooldown == True:
		pygame.draw.rect(gameDisplay, red, [440, 330, 50-(CD_4/2), 8])
	if Skill_5_Cooldown == True:
		pygame.draw.rect(gameDisplay, red, [440, 390, 50-(CD_5/2), 8])
	
def Ship_def(Ship_X, Ship_Skade, Skill_1, Skill_2, Skill_3, Skill_4, Dur_1, Dur_2, Dur_3, Dur_4, Dur_5):
	if Skill_1 == True:
		gameDisplay.blit(Skill_1_anime, (Ship_X, 445))
		pygame.draw.rect(gameDisplay, red, [Ship_X+19, 0, 1, 480])
		pygame.draw.rect(gameDisplay, green, [440, 150, 50-(Dur_1/2), 8])

	if Ship_Skade == 0:
		gameDisplay.blit(ship, (Ship_X, 445))
	if Ship_Skade == 1:
		gameDisplay.blit(ship_borken1, (Ship_X, 445))
	if Ship_Skade == 2:
		gameDisplay.blit(ship_borken2, (Ship_X, 445))
	
	if Skill_2 == True:
		gameDisplay.blit(Skill_2_anime, (Ship_X, 445))
		pygame.draw.rect(gameDisplay, green, [440, 210, 50-(Dur_2/2), 8])
	if Skill_3 == True:
		gameDisplay.blit(Skill_3_anime, (Ship_X, 445))
		pygame.draw.rect(gameDisplay, green, [440, 270, 50-(Dur_3/2), 8])
	if Skill_4 == True:
		gameDisplay.blit(Skill_4_anime, (Ship_X, 445))
		pygame.draw.rect(gameDisplay, green, [440, 330, 50-(Dur_4/2), 8])



#Gameloopen
menu = True
option = True
gameOver = True
choice = 0

while menu:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			menu = False
			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				if choice != 2:
					choice += 1
			if event.key == pygame.K_UP:
				if choice != 0:
					choice -= 1
					
			if event.key == pygame.K_RETURN:
				if choice == 0:
					gameOver = False
				if choice == 2:
					menu = False
				if choice == 1:
					option = False



	#Variabler_ True/False  -------------------------------------------------------
	movment_left = False
	movment_right = False
	Ship_DMG = False
	rapid_fire = False
	Skill_1 = False
	Skill_2 = False
	Skill_3 = False
	Skill_4 = False
	Skill_5 = False
	SkillBar_1 = False
	SkillBar_2 = False
	SkillBar_3 = False
	SkillBar_4 = False
	SkillBar_5 = False
	Skill_1_Cooldown = False
	Skill_2_Cooldown = False
	Skill_3_Cooldown = False
	Skill_4_Cooldown = False
	Skill_5_Cooldown = False
		
	#Variabler: Location
	Ship_X = 200
	X = 240
	Y = 450
	Ship_Skade = 0

	#Variabler: CHANGEABLE
	FPS = 60
	LvL = 0            #Hvilket Level spille starter på
	LvL_ROCK = 0       #IKKE I BRUK ENNÅ
	spawn_speed = 1    #Hvor mange steiner spawner i sekundet
	MAX_Liv = 3        #HP
	RATE_skudd = 3     #Skudd du kan skyte i sekundet
	ship_speed = 5     #Hvor mange pixler skipet beveger seg
	ship_healing = 9   #Hvor mange skunder det tar før skipet fixer seg selv
	rock_speed = 3     #Hvor mange pixler steinen beveger seg
	bullet_speed = 10  #Hvor mange pixler skudda beveger seg
	MAX_XP = 10        #XP som trengs for neste Level
	MAX_XP_INC = 1     #Hvor mye MER XP som trengs for neste lvl

	#Varigheten for Skills, in seconds.
	Skill_1_dur_MAX = 15    #Laser Aim
	Skill_2_dur_MAX = 10    #Speed
	Skill_3_dur_MAX = 10    #Healing speed
	Skill_4_dur_MAX = 10    #Rapid fire
	Skill_5_dur_MAX = 1     #Nuke

	#Skill Cooldowns, in seconds
	Skill_1_cd_MAX = 20    #Laser Aim
	Skill_2_cd_MAX = 25    #Speed
	Skill_3_cd_MAX = 30    #Healing speed
	Skill_4_cd_MAX = 40    #Rapid fire
	Skill_5_cd_MAX = 60    #Nuke

	#Variabler: Set
	Spawn_nr = 0
	skudd = 0
	MAX_skudd = FPS/RATE_skudd
	MAX_rock = FPS/spawn_speed
	Ship_Heal = ship_healing*FPS
	ship_heal2 = Ship_Heal
	Ship_Heal_Skill = FPS/2
	ship_heal2_skill = Ship_Heal_Skill
	XP = 0
	Liv = MAX_Liv
	sjold_prosent = 0
	XP_prosent = 0
	frame_counter = 0
	click = 0
	
	Skill_1_dur = 0
	Skill_2_dur = 0
	Skill_3_dur = 0
	Skill_4_dur = 0
	Skill_5_dur = 0
	
	Skill_1_cd = 0
	Skill_2_cd = 0
	Skill_3_cd = 0
	Skill_4_cd = 0
	Skill_5_cd = 0
	
	CD_1 = 0
	CD_2 = 0
	CD_3 = 0
	CD_4 = 0
	CD_5 = 0
	
	Dur_1 = 0
	Dur_2 = 0
	Dur_3 = 0
	Dur_4 = 0
	Dur_5 = 0


	
	#--------------------------------------------------------------------------



	gameDisplay.blit(bk_title, (0,0))
	gameDisplay.blit(LT_Icon, (200,100))
	gameDisplay.blit(kris_icon, (300,477))
	pygame.draw.rect(gameDisplay, gray, [175, 250+(choice*50), 150, 50])
	
	gameDisplay.blit(start_icon, (175, 250))
	gameDisplay.blit(info_icon, (175, 300))
	gameDisplay.blit(exit_icon, (175, 350))
	
	pygame.display.update()
	clock.tick(FPS)
	while not option:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				option = True
				menu = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:             
					option = True
				
		gameDisplay.blit(option_page, (0,0))
		pygame.display.update()
		clock.tick(FPS)

	while not gameOver:
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				menu = False
				gameOver = True
				
			if event.type == pygame.KEYDOWN:#DOWN-----
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					if Skill_4 == False:
						if skudd == 0:
							K = Shot((Ship_X+10), 480)
							skudd = MAX_skudd
					else:
						rapid_fire = True

				if event.key == pygame.K_ESCAPE:
					for A in Rock.rocksprites: #Rock(39x49)  #Skudd(20x20)   #Ship(39x49)
						Rock.rocksprites.remove(A)
					for A in Shot.shotsprites: #Rock(39x49)  #Skudd(20x20)   #Ship(39x49)
						Shot.shotsprites.remove(A)
					gameOver = True
					
				if event.key == pygame.K_DOWN: 
					S = Rock((random.randrange(0,395)), 0)

				#-------------------------------------	
				if event.key == pygame.K_1 or event.key == pygame.K_e:
					if SkillBar_1 == True:
						if Skill_1_Cooldown == False:
							Skill_1 = True
				if event.key == pygame.K_2 or event.key == pygame.K_SPACE:
					if SkillBar_2 == True:
						if Skill_2_Cooldown == False:
							Skill_2 = True
				if event.key == pygame.K_3 or event.key == pygame.K_LSHIFT:
					if SkillBar_3 == True:
						if Skill_3_Cooldown == False:
							Skill_3 = True
				if event.key == pygame.K_4 or event.key == pygame.K_q:
					if SkillBar_4 == True:
						if Skill_4_Cooldown == False:
							Skill_4 = True
				if event.key == pygame.K_5 or event.key == pygame.K_LCTRL or event.key == pygame.K_s:
					if SkillBar_5 == True:
						if Skill_5_Cooldown == False:
							Skill_5 = True
				#-------------------------------------
						
				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					movment_right = True
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					movment_left = True

					
			if event.type == pygame.KEYUP:#UP------
				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					movment_right = False
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					movment_left = False
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					rapid_fire = False


		#Beveger Steinene og sjekker om de treffer skipet             
		for i in Rock.rocksprites: #Rock(39x49)  #Skudd(20x20)   #Ship(39x49)
			i.rect.y += (rock_speed + LvL/20)
			if i.rect.y >= 500:
				Rock.rocksprites.remove(i)
				Liv -= 1
			if (i.rect.y+49) > Y:     
				if Ship_X > i.rect.x and Ship_X < (i.rect.x + 39) or (Ship_X + 39) > i.rect.x and (Ship_X + 39) < (i.rect.x+39):
					Rock.rocksprites.remove(i)
					if Ship_Skade == 2:
						for A in Rock.rocksprites: #Rock(39x49)  #Skudd(20x20)   #Ship(39x49)
							Rock.rocksprites.remove(A)
						gameOver = True
					if Ship_Skade < 2:
						Ship_Skade += 1
						Ship_DMG = True
						XP -= 3
						if XP < 0:
							XP = 0
						
					
					
		#Beveger skudda og sjekker om de treffer steinene          
		for C in Shot.shotsprites:
			C.rect.y -= bullet_speed
			if C.rect.y <= -20:
				Shot.shotsprites.remove(C)
			for i in Rock.rocksprites:
				if (i.rect.y+49) > C.rect.y and i.rect.y < C.rect.y:
					if C.rect.x > i.rect.x and C.rect.x < (i.rect.x + 39) or (C.rect.x + 20) > i.rect.x and (C.rect.x + 20) < (i.rect.x + 39):
							 Rock.rocksprites.remove(i)
							 Shot.shotsprites.remove(C)
							 
							 XP += 1
							 if XP == MAX_XP:
								 LvL += 1	 
								 if LvL >= 1: #Hvilken LvL du får ablity på
									 SkillBar_1 = True
								 if LvL >= 2:
									 SkillBar_2 = True
								 if LvL >= 2:
									 SkillBar_3 = True
								 if LvL >= 2:
									 SkillBar_4 = True
								 if LvL >= 2:
									 SkillBar_5 = True
								 if Liv != 20:
									 Liv += 1
##								 if LvL == 5 or LvL == 10 or LvL == 15:
##									 MAX_rock -= 10
								 MAX_rock -= 1
								 XP = 0
								 MAX_XP += MAX_XP_INC
								 


							 

		#Beveger Skipet                        
		if movment_left == True:
			if Ship_X > 0:
				if Skill_2 == True:
				       Ship_X -= 10 
				else:
					Ship_X -= ship_speed
		if movment_right == True:
			if Ship_X < 390:
				if Skill_2 == True:
				       Ship_X += 10 
				else:
					Ship_X += ship_speed

		#Spawner Steiner
		if Spawn_nr >= MAX_rock:
			S = Rock((random.randrange(0,395)), 0)
			Spawn_nr = 0
		Spawn_nr += 1
		
		#Ordner skudd var        
		if skudd != 0:
			skudd -= 1
			
		#Ordner liv var          
		if Liv < 1:
			for A in Rock.rocksprites: #Rock(39x49)  #Skudd(20x20)   #Ship(39x49)
				Rock.rocksprites.remove(A)
			for A in Shot.shotsprites: #Rock(39x49)  #Skudd(20x20)   #Ship(39x49)
				Shot.shotsprites.remove(A)
				
			gameOver = True
			
		#Ordner healing var
		if Ship_DMG == True:
			if Skill_3 == True:
				ship_heal2_skill -= 1
				if ship_heal2_skill < 0:
					Ship_Skade -= 1
					ship_heal2_skill = Ship_Heal_Skill
					if Ship_Skade == 0:
						Ship_DMG = False      
			if Skill_3 == False:
				ship_heal2 -= 1
				if ship_heal2 < 0:
					Ship_Skade -= 1
					ship_heal2 = Ship_Heal
					if Ship_Skade == 0:
						Ship_DMG = False

		#Test for Mouse
		click = pygame.mouse.get_pressed()
		if click[0] == 1:
			if Skill_4 == False:
				if skudd == 0:
					K = Shot((Ship_X+10), 480)
					skudd = MAX_skudd
			else:
				rapid_fire = True                        
			
		
		#Rapid shooting
		if Skill_4 == True:
			if rapid_fire == True:
				if skudd == 0:
					K = Shot((Ship_X+10), 480)
					skudd = 10
		#Nuke
		if Skill_5 == True:
			for A in Rock.rocksprites: #Rock(39x49)  #Skudd(20x20)   #Ship(39x49)
				Rock.rocksprites.remove(A)
				XP += 1
				if XP == MAX_XP:
					LvL += 1	 
					if LvL == 5 or LvL == 10 or LvL == 15:
						 MAX_rock -= 10			 
					XP = 0
					MAX_XP += MAX_XP_INC
			
		
		#Prosent Utregning til barer
		if Skill_3 == True:
			sjold_prosent = ((100*ship_heal2_skill)/Ship_Heal_Skill)
			XP_prosent = ((100*XP)/MAX_XP)
		if Skill_3 == False:
			sjold_prosent = ((100*ship_heal2)/Ship_Heal)
			XP_prosent = ((100*XP)/MAX_XP)

		
		#Frame_counter sin telling, og holder telling på Skills tid
		frame_counter += 1
		if frame_counter == FPS:
			frame_counter = 0
			if Skill_1 == True:
				Skill_1_dur += 1
				Dur_1 = ((Skill_1_dur)*100)/Skill_1_dur_MAX
				if Skill_1_dur == Skill_1_dur_MAX:
					Skill_1_dur = 0
					Skill_1_Cooldown = True
					Skill_1 = False
			if Skill_2 == True:
				Skill_2_dur += 1
				Dur_2 = ((Skill_2_dur)*100)/Skill_2_dur_MAX
				if Skill_2_dur == Skill_2_dur_MAX:
					Skill_2_dur = 0
					Skill_2_Cooldown = True
					Skill_2 = False
			if Skill_3 == True:
				Skill_3_dur += 1
				Dur_3 = ((Skill_3_dur)*100)/Skill_3_dur_MAX
				if Skill_3_dur == Skill_3_dur_MAX:
					Skill_3_dur = 0
					Skill_3_Cooldown = True
					Skill_3 = False
			if Skill_4 == True:
				Skill_4_dur += 1
				Dur_4 = ((Skill_4_dur)*100)/Skill_4_dur_MAX
				if Skill_4_dur == Skill_4_dur_MAX:
					Skill_4_dur = 0
					Skill_4_Cooldown = True
					Skill_4 = False
			if Skill_5 == True:
				Skill_5_dur += 1
				Dur_5 = ((Skill_5_dur)*100)/Skill_5_dur_MAX
				if Skill_5_dur == Skill_5_dur_MAX:
					Skill_5_dur = 0
					Skill_5_Cooldown = True
					Skill_5 = False
					
			if Skill_1_Cooldown == True:
				Skill_1_cd += 1
				CD_1 = ((Skill_1_cd)*100)/Skill_1_cd_MAX
				if Skill_1_cd == Skill_1_cd_MAX:
					Skill_1_cd = 0
					Skill_1_Cooldown = False
			if Skill_2_Cooldown == True:
				Skill_2_cd += 1
				CD_2 = ((Skill_2_cd)*100)/Skill_2_cd_MAX
				if Skill_2_cd == Skill_2_cd_MAX:
					Skill_2_cd = 0
					Skill_2_Cooldown = False                               
			if Skill_3_Cooldown == True:
				Skill_3_cd += 1
				CD_3 = ((Skill_3_cd)*100)/Skill_3_cd_MAX
				if Skill_3_cd == Skill_3_cd_MAX:
					Skill_3_cd = 0
					Skill_3_Cooldown = False
			if Skill_4_Cooldown == True:
				Skill_4_cd += 1
				CD_4 = ((Skill_4_cd)*100)/Skill_4_cd_MAX
				if Skill_4_cd == Skill_4_cd_MAX:
					Skill_4_cd = 0
					Skill_4_Cooldown = False
			if Skill_5_Cooldown == True:
				Skill_5_cd += 1
				CD_5 = ((Skill_5_cd)*100)/Skill_5_cd_MAX
				if Skill_5_cd == Skill_5_cd_MAX:
					Skill_5_cd = 0
					Skill_5_Cooldown = False

					
		gameDisplay.blit(bk, (0,0))
		Shot.shotsprites.draw(gameDisplay)
		Ship_def(Ship_X, Ship_Skade, Skill_1, Skill_2, Skill_3, Skill_4, Dur_1, Dur_2, Dur_3, Dur_4, Dur_5)
		Rock.rocksprites.draw(gameDisplay)
		UI(Liv,Ship_DMG, Ship_X, XP, LvL, sjold_prosent) #HP og XP og Sjold
		Ability_UI(LvL, SkillBar_1, SkillBar_2, SkillBar_3, SkillBar_4, SkillBar_5, Skill_1_Cooldown, Skill_2_Cooldown, Skill_3_Cooldown, Skill_4_Cooldown, Skill_5_Cooldown, CD_1, CD_2, CD_3, CD_4, CD_5) #Ability stuff
		text(LvL, XP)
		pygame.display.update()
		clock.tick(FPS)


pygame.quit()
quit()
