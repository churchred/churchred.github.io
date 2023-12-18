import pygame
import random
import math
import csv
import os
pygame.init()
pygame.font.init()

#Farger
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
RED_LIGHT = (255,100,100)
BLUE = (0,128,255)
GREEN = (0,255,0)
YELLOW = (255, 230, 0)
GRAY = (128,128,128)
GRAY_LIGHT = (160,160,160)

TITLE_WIDTH = 350
TITLE_HEIGHT = 500

HEIGHT = 500
WIDTH = 500

FPS = 200    


#Lage skjerm og FPS
SCREEN = pygame.display.set_mode((TITLE_WIDTH, TITLE_HEIGHT))
pygame.display.set_caption('Spaaaaace2')
clock = pygame.time.Clock()



LastTech = pygame.image.load('Bilder/LastTech.png')
bk = pygame.image.load('Bilder/background.png')
bk_title = pygame.image.load('Bilder/background_OLD.png')
option_page = pygame.image.load('Bilder/option.png')

#Load Bilder
ship = pygame.image.load('Bilder/skip.png')
ship_borken1 = pygame.image.load('Bilder/skip_skadd1.png')
ship_borken2 = pygame.image.load('Bilder/skip_skadd2.png')
ship_Array = [ship, ship_borken1, ship_borken2]

heart = pygame.image.load('Bilder/heart.png')
shot_anime = pygame.image.load('Bilder/skudd.png')
shot_anime2 = pygame.image.load('Bilder/skudd2.png')

LoadingBar = pygame.image.load('Bilder/LoadingBar.png')
rock_anime = pygame.image.load('Bilder/rock.png')
rock_anime2 = pygame.transform.scale(rock_anime, (425, 350))

Skill_1_icon = pygame.image.load('Bilder/Skill 1.png')
Skill_2_icon = pygame.image.load('Bilder/Skill 2.png')
Skill_3_icon = pygame.image.load('Bilder/Skill 3.png')
Skill_4_icon = pygame.image.load('Bilder/Skill 4.png')
Skill_5_icon = pygame.image.load('Bilder/Skill 5.png')

Skill_1_anime = pygame.image.load('Bilder/Skip_Skill 1.png')
Skill_2_anime = pygame.image.load('Bilder/Skip_Skill 2.png')
Skill_3_anime = pygame.image.load('Bilder/Skip_Skill 3.png')
Skill_4_anime = pygame.image.load('Bilder/Skip_Skill 4.png')

def file_check():  
        try:
                file = open("Bilder/Save.txt.", "r")
                file.close()

        except:
                file = open("Bilder/Save.txt.", "w")


def percent(delen, hele):
	return((delen*100)/hele)

def save():
	file_check()
	file = open("Bilder/Save.txt", "w")
	file.write("HP," + str(char.hp_MAX))
	file.write('\n')
	file.write("Speed," + str(char.speed))
	file.write('\n')
	file.write("Gold," + str(char.gold))
	file.write('\n')
	file.write("Damage," + str(char.dmg))
	file.write('\n')
	file.write("Shield_heal," + str(char.regen_speed))
	file.write('\n')
	file.write("Bullet_speed," + str(char.bullet_speed))
	file.write('\n')
	file.write("Bullets_per_second," + str(char.bullet_rate))
	file.write('\n')
	file.write("Starting_level," + str(char.starting_level))
	file.write('\n')
	file.write("ability_1," + str(char.ability_1))
	file.write('\n')
	file.write("ability_2," + str(char.ability_2))
	file.write('\n')
	file.write("ability_3," + str(char.ability_3))
	file.write('\n')
	file.write("ability_4," + str(char.ability_4))
	file.write('\n')
	file.write("ability_5," + str(char.ability_5))
	file.write('\n')
	
	file.write("ability_1_price," + str(shop_ability_1.price))
	file.write('\n')
	file.write("ability_2_price," + str(shop_ability_2.price))
	file.write('\n')
	file.write("ability_3_price," + str(shop_ability_3.price))
	file.write('\n')
	file.write("ability_4_price," + str(shop_ability_4.price))
	file.write('\n')
	file.write("ability_5_price," + str(shop_ability_5.price))
	file.write('\n')
	
	file.write("Start_Level_price," + str(shop_start_level.price))
	file.write('\n')
	file.write("Shots_per_Second_price," + str(shop_shot_inc.price))
	file.write('\n')
	file.write("Speed_price," + str(shop_speed_inc.price))
	file.write('\n')
	file.write("hp_price," + str(shop_hp_inc.price))
	file.write('\n')
	file.write("dmg_price," + str(shop_dmg_inc.price))
	file.close()
	
def load():
	try:
		file = open("Bilder/Save.txt", "r")
		file_Stats = csv.reader(file)

		Array = []

		for i in file_Stats:
			Array.append(i)
		file.close()

		#Char loading
		char.hp_MAX = int(Array[0][1])
		char.hp = char.hp_MAX
		char.speed = int(Array[1][1])
		char.gold = int(Array[2][1])
		char.dmg = int(Array[3][1])
		char.regen_speed = int(Array[4][1])
		char.bullet_speed = int(Array[5][1])
		char.bullet_rate = int(Array[6][1])
		char.starting_level = int(Array[7][1])
		char.ability_1 = eval(Array[8][1])
		char.ability_2 = eval(Array[9][1])
		char.ability_3 = eval(Array[10][1])
		char.ability_4 = eval(Array[11][1])
		char.ability_5 = eval(Array[12][1])

		#Price loading
		shop_ability_1.price = int(Array[13][1])
		shop_ability_2.price = int(Array[14][1])
		shop_ability_3.price = int(Array[15][1])
		shop_ability_4.price = int(Array[16][1])
		shop_ability_5.price = int(Array[17][1])

		shop_start_level.price = int(Array[18][1])
		shop_shot_inc.price = int(Array[19][1])
		shop_speed_inc.price = int(Array[20][1])
		shop_hp_inc.price = int(Array[21][1])
		shop_dmg_inc.price = int(Array[22][1])
		
		
	except FileNotFoundError:
		print("Error")

def exit_game():
	for i in Shots.shot_list:
		Shots.shot_list.remove(i)
	for i in Rocks.rock_list:
		Rocks.rock_list.remove(i)
		
	char.regen = char.regen_speed*FPS
	char.hurt = 0
	char.hp = char.hp_MAX
	char.x = 10
	char.y = HEIGHT-char.h

	SCREEN = pygame.display.set_mode((TITLE_WIDTH, TITLE_HEIGHT))

	lvl.__init__()
	
	Ability_1.duration = 0
	Ability_1.cooldown = 0
	Ability_1.cooldown_active = False
	Ability_1.skill_active = False

	Ability_2.duration = 0
	Ability_2.cooldown = 0
	Ability_2.cooldown_active = False
	Ability_2.skill_active = False

	Ability_3.duration = 0
	Ability_3.cooldown = 0
	Ability_3.cooldown_active = False
	Ability_3.skill_active = False

	Ability_4.duration = 0
	Ability_4.cooldown = 0
	Ability_4.cooldown_active = False
	Ability_4.skill_active = False

	Ability_5.duration = 0
	Ability_5.cooldown = 0
	Ability_5.cooldown_active = False
	Ability_5.skill_active = False

class Shots(pygame.sprite.Sprite):
	shot_list = pygame.sprite.Group()
	def __init__(self, x ,y):
		
		pygame.sprite.Sprite.__init__(self)
		Shots.shot_list.add(self)
		self.image = shot_anime
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.w = 25
		self.h = 25
		self.speed = round(HEIGHT/2)
		
	def move():
		for i in Shots.shot_list:
			i.rect.y -= i.speed  * lvl.elapsed
			if i.rect.y+i.h < 0:
				Shots.shot_list.remove(i)
		Shots.shot_list.draw(SCREEN)

class Rocks(pygame.sprite.Sprite):
	rock_list = pygame.sprite.Group()
	def __init__(self, x ,y):
		
		pygame.sprite.Sprite.__init__(self)
		Rocks.rock_list.add(self)
		self.image = rock_anime
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = -50
		self.w = 39
		self.h = 49
		self.speed = round(HEIGHT/3 + 50)

		self.damaged = False
		
		self.hp_MAX = lvl.rock_hp
		self.hp = self.hp_MAX 


	def create_new():
		R = Rocks((random.randrange(0,395)), 0-49)

	
	def move():
		Rocks.rock_list.draw(SCREEN)
		
		for i in Rocks.rock_list:
			i.rect.y += i.speed * lvl.elapsed#Beveger steinene nedover
			if i.rect.y > HEIGHT:
				lvl.rock_kill += 1
				Rocks.rock_list.remove(i) #Fjerner steinene hvis du er utenfor skjermen
				char.hp -= 1
				if char.hp == 0:
					game = False
					exit_game()

			if Ability_5.skill_active == True:
				Rocks.rock_list.remove(i)

			for ii in Shots.shot_list: #sjekker om skudda treffer steinen
				if ii.rect.x + ii.w > i.rect.x and ii.rect.x < i.rect.x + i.rect.w and ii.rect.y + ii.h > i.rect.y and ii.rect.y < i.rect.y + i.h:
					i.hp -= char.dmg
					Shots.shot_list.remove(ii)
					if i.hp <= 0:
						Rocks.rock_list.remove(i)
						lvl.rock_kill += 1
						char.gold += 1

				
			if i.hp < i.hp_MAX: #Sjekker om steinen er skadet
				i.damaged = True
				
			if i.damaged == True and i.hp > 0: #Lager hp bar til steinene
				pygame.draw.rect(SCREEN, GREEN, [i.rect.x+3, i.rect.y+3, (percent(i.hp, i.hp_MAX))/3, 5])	


	


class Player():
	def __init__(self):
		
		self.w = 39
		self.h = 49
		self.x = 10
		self.y = HEIGHT-self.h
		self.img = ship_Array[0]

		self.hp_MAX = 3 #Hvor mange liv har skipet
		self.hp = self.hp_MAX
		
		self.speed = 3*FPS  #Hvor raskt er skipet

		self.gold = 2500000
		self.dmg = 1
		
		self.move_left = False
		self.move_right = False

		self.hurt = 0
		self.regen_speed = 5 #Hvor fort skipet healer fra skade (Sekunder)

		self.bullet_speed = 10 #Hvor fort skudd beveger seg
		self.bullet_rate = 9 #Hvor mange skudd du kan skyte i sekundet

		self.starting_level = 1

		#Formler og Variabler som ikke skal røres
		self.shot = False
		self.shot_counter = 0
		self.regen = self.regen_speed*FPS

		self.ability_1 = False
		self.ability_2 = False
		self.ability_3 = False
		self.ability_4 = False
		self.ability_5 = False

	def draw(self):
		if Ability_1.skill_active == True:
			pygame.draw.rect(SCREEN, RED, [self.x+self.w/2, 0, 1, HEIGHT])
			SCREEN.blit(Skill_1_anime, (self.x, self.y-2))
			
		SCREEN.blit(ship_Array[self.hurt], (self.x, self. y))

		if Ability_2.skill_active == True:
			SCREEN.blit(Skill_2_anime, (self.x, self.y))

		if Ability_3.skill_active == True:
			SCREEN.blit(Skill_3_anime, (self.x, self.y))

		if Ability_4.skill_active == True:
			SCREEN.blit(Skill_4_anime, (self.x, self.y))

		#HP hjerter
		hp_y = 1
		hp_x = 0
		for i in range(0, self.hp):
			SCREEN.blit(heart, (445+(hp_x*10), 11*hp_y))
			hp_x += 1
			if hp_x == 4:
				hp_x = 0
				hp_y += 1

		#Shieldbar
		if self.hurt > 0:
			if Ability_3.skill_active == True:
				pygame.draw.rect(SCREEN, BLUE, [self.x, self.y+(self.h/1.2), percent(self.regen, 1*FPS)/2.5, 8])
				self.regen -= 1
				if self.regen == 0:
					self.regen = 0.5*FPS
					self.hurt -= 1
			else:
				self.regen -= 1
				pygame.draw.rect(SCREEN, BLUE, [self.x, self.y+(self.h/1.2), percent(self.regen, self.regen_speed*FPS)/2.5, 8])
				if self.regen == 0:
					self.regen = self.regen_speed*FPS
					self.hurt -= 1


		self.move()
		self.timers()
		self.dmg_ceck()
		
	def gun(self):
		if self.shot == False or Ability_4.skill_active == True:
			S = Shots(self.x+10, self.y)
			self.shot_counter = FPS/self.bullet_rate
			self.shot = True

	def dmg_ceck(self):
		for i in Rocks.rock_list:
			if self.x + self.w > i.rect.x and self.x < i.rect.x + i.rect.w and self.y + self.h > i.rect.y and self.y < i.rect.y + i.h:
				Rocks.rock_list.remove(i)
				lvl.rock_kill += 1
				self.hurt += 1
				if self.hurt > 2:
					lvl.game = False
					exit_game()

	def timers(self):
		if self.shot == True:
			self.shot_counter -= 1
			if self.shot_counter <= 0:
				self.shot = False

			

	def move(self):
		if self.move_left == True and self.x > 0:
			if Ability_2.skill_active == True:
				self.x -= self.speed*2
			else:
				self.x -= self.speed * lvl.elapsed
			
		if self.move_right == True and self.x < WIDTH-self.w-70:
			if Ability_2.skill_active == True:
				self.x += self.speed*2
			else:
				self.x += self.speed * lvl.elapsed


class Boss(pygame.sprite.Sprite):
	boss_list = pygame.sprite.Group()
	def __init__(self):
		
		pygame.sprite.Sprite.__init__(self)
		Boss.boss_list.add(self)

		self.image = rock_anime2
		self.rect = self.image.get_rect()
		self.w = 350
		self.h = 350
		self.rect.x = 0
		self.rect.y = -(self.h)
		self.hp_MAX = 300
		self.hp = self.hp_MAX

		self.shot = False
		self.bullet_rate = 8
		self.shot_counter = FPS/self.bullet_rate

	def draw():
		Boss.boss_list.draw(SCREEN)
		for i in Boss.boss_list:
			Boss.attack(i)
			
			
			if i.rect.y < (-(i.h/2)):
				i.rect.y += 1
				
			for ii in Shots.shot_list:
				if ii.rect.x + ii.w > i.rect.x and ii.rect.x < i.rect.x + i.rect.w and ii.rect.y + ii.h > i.rect.y and ii.rect.y < i.rect.y + i.h:
					i.hp -= char.dmg
					Shots.shot_list.remove(ii)

					if i.hp <= 0:
						Boss.boss_list.remove(i)
						lvl.boss = False
						
						for j in Rocks.rock_list:
							Rocks.rock_list.remove(j)
							
						lvl.switch_counter = lvl.switch_time*FPS

						lvl.timers()
							
					
			if i.hp != i.hp_MAX:
				pygame.draw.rect(SCREEN, GREEN, [i.rect.x+i.w/2, i.rect.y+i.h/1.5, (percent(i.hp, i.hp_MAX)), 5])
					
			
					
	def attack(self):
		if self.shot == False:
			S = Boss_shots((random.randrange(0,395)), 10)
			self.shot_counter = FPS/self.bullet_rate
			self.shot = True
			
		if self.shot == True:
			self.shot_counter -= 1
			if self.shot_counter <= 0:
				self.shot = False
		Boss_shots.move()

	
class Boss_shots(pygame.sprite.Sprite):
	shot_list = pygame.sprite.Group()
	def __init__(self, x ,y):
		
		pygame.sprite.Sprite.__init__(self)
		Boss_shots.shot_list.add(self)
		self.image = shot_anime2
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.w = 25
		self.h = 25
		self.speed = 4*FPS
		
	def move():
		for i in Boss_shots.shot_list:
			i.rect.y += i.speed  * lvl.elapsed
			if i.rect.y > HEIGHT:
				Boss_shots.shot_list.remove(i)
			if char.x + char.w > i.rect.x and char.x < i.rect.x + i.rect.w and char.y + char.h > i.rect.y and char.y < i.rect.y + i.h:
				char.hurt += 1
				Boss_shots.shot_list.remove(i)
				if char.hurt > 2:
					lvl.game = False
					exit_game()
				
		Boss_shots.shot_list.draw(SCREEN)
		#print(len(Boss_shots.shot_list))
		
class Level():
	def __init__(self):

		self.menu = True
		self.options = False
		self.game = False
		self.shop = False
		self.choice = 0

		elapsed = 0

		self.number_rocks_MAX = 10 #mange steiner til neste level
		self.number_rocks = self.number_rocks_MAX
		self.boss = False
		
		self.rocks_sec = 0.8 #Hvor mange steiner i sekundet
		self.rock_counter = 0

		self.level_gets_harder = 2
		self.level_gets_harder_count = 0
		
		self.rock_kill = 0

		self.level = 1
		
		self.rock_hp = 1
		self.rock_speed = 3


		self.switch_time = 3  #Sekunder mellom levler
		self.switch_counter = self.switch_time*FPS
		

	def run(self):
		self.timers()
		self.draw()

	def next_lvl(self):
		self.level += 1
		self.number_rocks_MAX += 3 #pluss 3 steiner per level

		self.level_gets_harder_count += 1
		if self.level_gets_harder_count == 2:
			self.level_gets_harder_count = 0
			self.rock_hp += 1
			self.rocks_sec += 0.2
		
		if self.level == 10:
			self.rock_hp += 1
			self.rock_speed += 1
			lvl.boss = True
			S = Boss()

		if lvl.boss == False:
			self.rock_kill = 0
			self.switch_counter = self.switch_time*FPS

			self.number_rocks = self.number_rocks_MAX

				

	def draw(self):
		c = math.floor(char.hp_MAX/5)
		text("LvL:", 15, BLACK, WIDTH-65, HEIGHT-35, False)
		text(str(self.level), 18, BLACK, WIDTH-28, HEIGHT-35, False)
		
		#print(str(self.rock_kill) + "/" + str(self.number_rocks_MAX))
		
		if self.rock_kill == self.number_rocks_MAX and lvl.boss == False:
			text("Going to next Level", 30, WHITE, WIDTH/2-200, HEIGHT/2-160, False)
		
		pygame.draw.rect(SCREEN, BLUE, [WIDTH-60, HEIGHT-16, ((percent(self.rock_kill, self.number_rocks_MAX))/2), 5])
		SCREEN.blit(LoadingBar, (WIDTH-60, HEIGHT-17))

	def timers(self):
		#Make rock
		#print(self.number_rocks, self.rock_counter)
		if self.number_rocks != 0:
			if self.rock_counter <= 0:
				Rocks.create_new()
				self.rock_counter = FPS/self.rocks_sec
				self.number_rocks -= 1
				#print(self.number_rocks)
			else:
				self.rock_counter -= 1
				
		if self.number_rocks == 0:
			if len(Rocks.rock_list) == 0:
				self.switch_counter -= 1
				if self.switch_counter == 0:
					self.next_lvl()
		


class button():
	def __init__(self, width, height, x, y, color, hover_color, click_color, text, text_size, text_color, text_center):
		self.w = width
		self.h = height
		self.x = x
		self.y = y

		self.col = color
		self.hov_col = hover_color
		self.text_col = text_color
		self.name = text
		self.text_size = text_size
		self.click_col = click_color
		self.center = text_center

		self.test_1 = False
		self.test_2 = False
		self.test_3 = False

		self.price = 25

	def draw(self):
		mouse = pygame.mouse.get_pos()
		pygame.draw.rect(SCREEN, self.col, (self.x, self.y+3, self.w, self.h))
		if self.x+self.w > mouse[0] > self.x and self.y+self.h> mouse[1] > self.y:
			pygame.draw.rect(SCREEN, self.hov_col, (self.x, self.y+3, self.w, self.h))
			if self.test_3 == True:
				pygame.draw.rect(SCREEN, self.click_col, (self.x, self.y+3, self.w, self.h))
			text(self.name, self.text_size, self.text_col, self.x+self.text_size/2, self.y, self.center)
			self.test_1 = True
			if self.click() == True:
				return(True)
		else:
			text(self.name, self.text_size, self.text_col, self.x+self.text_size/2, self.y, self.center)
			self.test_1 = False
			self.test_2 = False
			self.test_3 = False	

	def draw2(self):
		mouse = pygame.mouse.get_pos()
		pygame.draw.rect(SCREEN, self.col, (self.x, self.y+3, self.w, self.h))
		if self.x+self.w > mouse[0] > self.x and self.y+self.h> mouse[1] > self.y:
			pygame.draw.rect(SCREEN, self.hov_col, (self.x, self.y+3, self.w, self.h))
			if self.test_3 == True:
				pygame.draw.rect(SCREEN, self.click_col, (self.x, self.y+3, self.w, self.h))
			text(self.name + "(" + str(self.price) + "g" + ")", self.text_size, self.text_col, self.x+self.text_size/2, self.y+5, self.center)
			self.test_1 = True
			if self.click() == True:
				return(True)
		else:
			text(self.name + "(" + str(self.price) + "g" + ")", self.text_size, self.text_col, self.x+self.text_size/2, self.y+5, self.center)
			self.test_1 = False
			self.test_2 = False
			self.test_3 = False	

	def click(self):
		click = pygame.mouse.get_pressed()

		if click[0] == 0:
			self.test_2 = True

		if self.test_2 == True:
			if click[0] == 1:
				self.test_3 = True

		if self.test_3 == True:
			if click[0] == 0:
				self.test_1 = False
				self.test_2 = False
				self.test_3 = False
				return(True)

	
class Ability():
	def __init__(self, name, x, y, image, active_time, cooldown_time):
		self.name = name
		self.x = x
		self.y = y
		self.w = 50
		self.h = 50

		self.img = image
		
		self.skill = False
		
		self.skill_active = False
		self.duration_MAX = active_time*FPS #Varighet for skill i sekunder
		self.duration = 0
		
		self.cooldown_active = False
		self.cooldown_MAX = cooldown_time*FPS #Cooldown i sekunder
		self.cooldown = 0

	def draw(self):
		SCREEN.blit(self.img, (self.x, self.y))
		self.Active_bar()
		self.Cooldown_bar()
	
	def Active_bar(self):
		if self.skill_active == True and self.cooldown_active == False:
			self.duration += 1
			pygame.draw.rect(SCREEN, GREEN, [self.x, self.y+self.h, (50-(percent(self.duration, self.duration_MAX))/2), 5])
			if self.duration == self.duration_MAX:
				self.duration = 0
				self.skill_active = False
				self.cooldown_active = True
				

	def Cooldown_bar(self):
		if self.cooldown_active == True:
			self.cooldown += 1
			pygame.draw.rect(SCREEN, RED, [self.x, self.y+self.h, (50-(percent(self.cooldown, self.cooldown_MAX))/2), 5])
			if self.cooldown == self.cooldown_MAX:
				self.cooldown = 0
				self.cooldown_active = False
				self.skill_active == False
		

Ability_1 = Ability("Laser aim", WIDTH-60, HEIGHT-60*5-50, Skill_1_icon, 30, 20)     #Laser
Ability_2 = Ability("Speed boost", WIDTH-60, HEIGHT-60*4-50,  Skill_2_icon, 7, 25)  #Speed
Ability_3 = Ability("Shield boost", WIDTH-60, HEIGHT-60*3-50,  Skill_3_icon, 10, 35) #Shield
Ability_4 = Ability("Rapid Fire", WIDTH-60, HEIGHT-60*2-50,  Skill_4_icon, 10, 75)   #Rapid Fire
Ability_5 = Ability("Nuke", WIDTH-60, HEIGHT-60*1-50,  Skill_5_icon, 1, 100)         #Nuke

def text(text, size, color, x, y, center):
	myfont = pygame.font.SysFont("monospace", size)
	texty = myfont.render(text, 1, (color))
	text_rect  = texty.get_rect(center=(TITLE_WIDTH/2, TITLE_HEIGHT/2))
	if center == True:
		SCREEN.blit(texty, (text_rect[0], y))
	else:
		SCREEN.blit(texty, (x, y))


def PrintTitleScreen(choice):
	SCREEN.blit(LastTech, (TITLE_WIDTH/2-50,TITLE_HEIGHT*0.2))
	text("Made by Kristoffer Kirkerød", 15, WHITE, TITLE_WIDTH/2, TITLE_HEIGHT-25, True)
	pygame.draw.rect(SCREEN, GRAY, (TITLE_WIDTH/2-50, 250+3+(50*choice), 100, 25))
	text("START", 30, WHITE, 0, 250, True)
	text("SHOP", 30, WHITE, 0, 300, True)
	text("INFO", 30, WHITE, 0, 350, True)
	text("EXIT", 30, WHITE, 0, 400, True)


#Make the button for the start menu
button_1 = button(100, 25, TITLE_WIDTH/2-50, 250, BLACK, GRAY, GRAY_LIGHT, "START", 30, WHITE, True)
button_2 = button(100, 25, TITLE_WIDTH/2-50, 300, BLACK, GRAY, GRAY_LIGHT, "SHOP", 30, WHITE, True)
button_3 = button(100, 25, TITLE_WIDTH/2-50, 350, BLACK, GRAY, GRAY_LIGHT, "INFO", 30, WHITE, True)
button_4 = button(100, 25, TITLE_WIDTH/2-50, 400, BLACK, GRAY, GRAY_LIGHT, "EXIT", 30, WHITE, True)

save_button = button(50, 15, TITLE_WIDTH/2-60, 445, GRAY, RED_LIGHT, RED, "Save", 15, WHITE, False)
load_button = button(50, 15, TITLE_WIDTH/2+10, 445, GRAY, RED_LIGHT, RED, "Load", 15, WHITE, False)

#Make the shop buttons
shop_dmg_inc = button(135, 25, 10, 90, GRAY, RED_LIGHT, RED, "+1 dmg", 15, WHITE, False)
shop_hp_inc = button(135, 25, 10, 120, GRAY, RED_LIGHT, RED, "+1 hp", 15, WHITE, False)
shop_speed_inc = button(135, 25, 10, 150, GRAY, RED_LIGHT, RED, "+1 speed", 15, WHITE, False)
shop_shot_inc = button(135, 25, 10, 180, GRAY, RED_LIGHT, RED, "+1 shot", 15, WHITE, False)

shop_ability_5 = button(200, 23, 10, HEIGHT-45, GRAY, RED_LIGHT, RED, "Ability:[Nuke]", 15, WHITE, False)
shop_ability_4 = button(200, 23, 10, HEIGHT-45-(25*1), GRAY, RED_LIGHT, RED, "Ability:[Gun]", 15, WHITE, False)
shop_ability_3 = button(200, 23, 10, HEIGHT-45-(25*2), GRAY, RED_LIGHT, RED, "Ability:[Shield]", 15, WHITE, False)
shop_ability_2 = button(200, 23, 10, HEIGHT-45-(25*3), GRAY, RED_LIGHT, RED, "Ability:[Speed]", 15, WHITE, False)
shop_ability_1 = button(200, 23, 10, HEIGHT-45-(25*4), GRAY, RED_LIGHT, RED, "Ability:[Laser]", 15, WHITE, False)

shop_back = button(50, 15, WIDTH-55, 5, GRAY, RED_LIGHT, RED, "Back", 15, WHITE, False)

shop_start_level = button(248, 22, 10, HEIGHT-45-(25*6), GRAY, RED_LIGHT, RED, "Increase start Level", 15, WHITE, False)

shop_ability_1.price = 25
shop_ability_2.price = 40
shop_ability_3.price = 50
shop_ability_4.price = 60
shop_ability_5.price = 100

shop_shot_inc.price = 50
shop_speed_inc.price = 35

lvl = Level()
char = Player()


while lvl.menu:
	clicked = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN or event.key == pygame.K_s:
				if lvl.choice != 3:
					lvl.choice += 1
			if event.key == pygame.K_UP or event.key == pygame.K_w:
				if lvl.choice != 0:
					lvl.choice -= 1
			if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
				if lvl.choice == 0: #START
					lvl.game = True
					SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
				if lvl.choice == 1: #SHOP
					lvl.shop = True
					SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
				if lvl.choice == 2: #INFO
					lvl.options = True
					SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
				if lvl.choice == 3: #EXIT
					quit()
		
	SCREEN.blit(bk_title, (0, 0))
	
	if button_1.draw() == True:
		lvl.game = True
		for i in range(1, char.starting_level):
			lvl.next_lvl()
		SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
	if button_2.draw() == True:
		lvl.shop = True
		SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
	if button_3.draw() == True:
		lvl.options = True
		
		SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
	if button_4.draw() == True:
		quit()
	
	PrintTitleScreen(lvl.choice)
	
	if button_1.test_1 == True: #START
		lvl.choice = 0
	if button_2.test_1 == True: #SHOP
		lvl.choice = 1
	if button_3.test_1 == True: #INFO
		lvl.choice = 2
	if button_4.test_1 == True: #EXIT
		lvl.choice = 3


	if save_button.draw() == True:
		save()

	if load_button.draw() == True:
		load()

	pygame.display.update()
	clock.tick(FPS)


	while lvl.options:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				lvl.options = False
				SCREEN = pygame.display.set_mode((TITLE_WIDTH, TITLE_HEIGHT))
				
		click = pygame.mouse.get_pressed()
		if click[0] == 1:
			lvl.options = False
			SCREEN = pygame.display.set_mode((TITLE_WIDTH, TITLE_HEIGHT))
					
		SCREEN.blit(option_page, (0, 0))
		pygame.display.update()
		clock.tick(FPS)

	while lvl.shop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				lvl.shop = False
				SCREEN = pygame.display.set_mode((TITLE_WIDTH, TITLE_HEIGHT))
			
		SCREEN.fill(BLACK)
		SCREEN.blit(ship, (WIDTH-125, HEIGHT/4+15))
		text("Health:"+str(char.hp_MAX), 20, WHITE, WIDTH-125, HEIGHT/4+50+15, False)
		text("Damage:"+str(char.dmg), 20, WHITE, WIDTH-125, HEIGHT/4+70+15, False)
		text("Speed:"+str(char.speed), 20, WHITE, WIDTH-113, HEIGHT/4+90+15, False)
		text("Shots/sec:"+str(char.bullet_rate), 20, WHITE, WIDTH-160, HEIGHT/4+110+15, False)
		
		text("Starting Level:"+str(char.starting_level), 18, WHITE, WIDTH-200, HEIGHT/4+170+15, False)
		
		text("Gold:"+str(char.gold), 25, YELLOW, WIDTH-135-len(str(char.gold))*10, 25+25, False)

		if shop_back.draw() == True:
			lvl.shop = False
			SCREEN = pygame.display.set_mode((TITLE_WIDTH, TITLE_HEIGHT))

		#Increase damage
		if shop_dmg_inc.draw2() == True:
			if char.gold >= shop_dmg_inc.price:
				char.gold -= shop_dmg_inc.price
				char.dmg += 1
				shop_dmg_inc.price *= 2
				
		#Increase hp		
		if shop_hp_inc.draw2() == True:
			if char.hp_MAX != 12:
				if char.gold >= shop_hp_inc.price:
					char.gold -= shop_hp_inc.price
					char.hp_MAX += 1
					char.hp = char.hp_MAX
					shop_hp_inc.price *= 2
					
		#Increase speed
		if shop_speed_inc.draw2() == True:
			if char.speed < 6:
				if char.gold >= shop_speed_inc.price:
					char.gold -= shop_speed_inc.price
					char.speed += 1
					shop_speed_inc.price *= 2
					
		#increase shots per second		
		if shop_shot_inc.draw2() == True:
			if char.gold >= shop_shot_inc.price:
				char.gold -= shop_shot_inc.price
				char.bullet_rate += 1
				shop_shot_inc.price *= 5

					
		#Start Level
		if shop_start_level.draw2() == True:
			if char.gold >= shop_start_level.price:
				char.gold -= shop_start_level.price
				char.starting_level += 1
				shop_start_level.price *= 3      
					
		#Abilities!
		if shop_ability_1.draw2() == True:
			if char.ability_1 == False:
				if char.gold >= shop_ability_1.price:
					char.gold -= shop_ability_1.price
					char.ability_1 = True

		if shop_ability_2.draw2() == True:
			if char.ability_2 == False:
				if char.gold >= shop_ability_2.price:
					char.gold -= shop_ability_2.price
					char.ability_2 = True
				
		if shop_ability_3.draw2() == True:
			if char.ability_3 == False:
				if char.gold >= shop_ability_3.price:
					char.gold -= shop_ability_3.price
					char.ability_3 = True

		if shop_ability_4.draw2() == True:
			if char.ability_4 == False:
				if char.gold >= shop_ability_4.price:
					char.gold -= shop_ability_4.price
					char.ability_4 = True

		if shop_ability_5.draw2() == True:
			if char.ability_5 == False:
				if char.gold >= shop_ability_5.price:
					char.gold -= shop_ability_5.price
					char.ability_5 = True

		if char.ability_1 == True:
			pygame.draw.rect(SCREEN, RED_LIGHT, (shop_ability_1.x, shop_ability_1.y+3, shop_ability_1.w, shop_ability_1.h))
			SCREEN.blit(Skill_1_icon, (WIDTH-250, HEIGHT-150))

		if char.ability_2 == True:
			pygame.draw.rect(SCREEN, RED_LIGHT, (shop_ability_2.x, shop_ability_2.y+3, shop_ability_2.w, shop_ability_2.h))
			SCREEN.blit(Skill_2_icon, (WIDTH-175, HEIGHT-150))

		if char.ability_3 == True:
			pygame.draw.rect(SCREEN, RED_LIGHT, (shop_ability_3.x, shop_ability_3.y+3, shop_ability_3.w, shop_ability_3.h))
			SCREEN.blit(Skill_3_icon, (WIDTH-100, HEIGHT-150))

		if char.ability_4 == True:
			pygame.draw.rect(SCREEN, RED_LIGHT, (shop_ability_4.x, shop_ability_4.y+3, shop_ability_4.w, shop_ability_4.h))
			SCREEN.blit(Skill_4_icon, (WIDTH-250+37, HEIGHT-90))

		if char.ability_5 == True:
			pygame.draw.rect(SCREEN, RED_LIGHT, (shop_ability_5.x, shop_ability_5.y+3, shop_ability_5.w, shop_ability_5.h))
			SCREEN.blit(Skill_5_icon, (WIDTH-175+37, HEIGHT-90))


		text("SHOP!", 60, WHITE, 5, 5, False)
		pygame.display.update()
		clock.tick(FPS)   

	#Game begins here -------------------------------------------------------------------------
	while lvl.game:
		lvl.elapsed = clock.tick(FPS)/1000
		click = pygame.mouse.get_pressed()
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				quit()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					lvl.game = False
					exit_game()
					SCREEN = pygame.display.set_mode((TITLE_WIDTH, TITLE_HEIGHT))

				if event.key == pygame.K_UP or event.key == pygame.K_w:
					char.gun()
					
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					char.move_left = True
					char.move_right = False 
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					char.move_right = True
					char.move_left = False

				if event.key == pygame.K_1 or event.key == pygame.K_e:
					if char.ability_1 == True:
						if Ability_1.cooldown_active == False:
							Ability_1.skill_active = True
						
				if event.key == pygame.K_2 or event.key == pygame.K_SPACE:
					if char.ability_2 == True:
						if Ability_2.cooldown_active == False:
							Ability_2.skill_active = True
						
				if event.key == pygame.K_3 or event.key == pygame.K_LSHIFT:
					if char.ability_3 == True:
						if Ability_3.cooldown_active == False:
							char.regen = 0.5*FPS
							Ability_3.skill_active = True
						
				if event.key == pygame.K_4 or event.key == pygame.K_q:
					if char.ability_4 == True:
						if Ability_4.cooldown_active == False:
							Ability_4.skill_active = True
						
				if event.key == pygame.K_5 or event.key == pygame.K_LCTRL:
					if char.ability_5 == True:
						if Ability_5.cooldown_active == False:
							Ability_5.skill_active = True
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					char.move_left = False
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					char.move_right = False

		if click[0] == 1 or Ability_4.skill_active == True:
			if clicked == False or Ability_4.skill_active == True:
				char.gun()
				clicked = True
				
				
		if click[0] == 0:
			clicked = False
					

		SCREEN.blit(bk, (0, 0))

		
		
		if char.ability_1 == True:
			Ability_1.draw()
		if char.ability_2 == True:
			Ability_2.draw()
		if char.ability_3 == True:
			Ability_3.draw()
		if char.ability_4 == True:
			Ability_4.draw()
		if char.ability_5 == True:
			Ability_5.draw()
		
		char.draw()
		Shots.move()
		
		if lvl.boss == False:
			Rocks.move()
		if lvl.boss == True:
			Boss.draw()
			
		#print(lvl.elapsed)	
		lvl.run()
		pygame.display.update()

quit()
