import time
import os
import csv
import pygame

pygame.init()
pygame.font.init()

Ikke_open_video = True

def StartupCheck():
	#Sjekker om __cache__ Folder finnes:
	try:
		os.makedirs("__cache__")
	except:
		pass
	
	#Sjekker om Path finnes
	try:
		file = open("__cache__/Path.txt", "r") 
		file.close()
	except FileNotFoundError:
		dirname, filename = os.path.split(os.path.abspath(__file__))
		file = open("__cache__/Path.txt", "w")
		file.write(str(dirname))
		file.close()  
 

	#Oppdaterer Names
	try:
		path = ReadPath()
		folder_names = (os.listdir(path[0]))

		file = open("__cache__/Names.txt", "w")
		for i in folder_names: #Finnes navn, antall seasons, og antall episoder for hver season
			if i != (os.path.basename(__file__)) and i != '__cache__' and season_count(i) > 0:
				s = season_count(i)
				e = ""
				for ii in range(1, int(s)+1):
					e = str(e) + str(episode_count(i, str(ii))) + ","
				file.write(str(i) + "," + str(s) + "," + str(e))
				file.write('\n')
		file.close()
	except Exception as e:
		print("Update Names: ", e)
		
	#Sjekker om Stats finnes
	try:
		file = open("__cache__/Stats.txt", "r") 
		file.close()
		Oppdate_Stats() #Har det kommet noen nye serier som skal legger til? Eller er noen borte?
		
	except FileNotFoundError:       
		file = open("__cache__/Stats.txt", "w")
		
		path = ReadPath()
		folder_names = (os.listdir(path[0]))
		
		for i in folder_names: #Finnes navn, antall seasons, og antall episoder for hver season
			if i != (os.path.basename(__file__)) and i != '__cache__':
				file.write(str(i) + "," + "1" + "," + "1")
				file.write('\n')

		file.close()

	#Sjekker om Bookmarks finnes
	try:
		file = open("__cache__/Bookmarks.txt", "r") 
		file.close()
		Oppdate_Bookmarks()
	except FileNotFoundError:
		file = open("__cache__/Bookmarks.txt", "w")
		file.close()


	Oppdate_Stats()
	Oppdate_Bookmarks()

def Oppdate_Stats(): #Sjekker om det finnes noen nye serier
	file1 = open("__cache__/Stats.txt", "r")
	file2 = open("__cache__/Names.txt", "r")

	file_Stats = csv.reader(file1)
	file_Names = csv.reader(file2)
	
	Array_Stats_old = []
	Array_Stats_new = []
	Array_Names = []
	
	for i in file_Stats:
		Array_Stats_old.append(i)
	for i in file_Names:
		Array_Names.append(i)

	file1.close()
	file2.close()

	file = open('__cache__/Stats.txt', 'w')
	
	for i in Array_Names:
		Array_Stats_new.append([i[0], "1", "1"])


	#Sjekker om det finnes like serier i gamle Stats og nye Stats.
	for i in range(0, len(Array_Stats_new)):
		for ii in range(0, len(Array_Stats_old)):
			if Array_Stats_new[i][0] == Array_Stats_old[ii][0]:
				Array_Stats_new[i] = Array_Stats_old[ii]


	for i in Array_Stats_new:
		file.write(i[0] + "," + i[1] + "," + i[2])
		file.write('\n')
	file.close()
	
def Oppdate_Bookmarks():
	Array_Stats = ReadStats()
	Array_Bookmarks = ReadBookmarks()
	Matching = []

	for i in range(0, len(Array_Stats)):
		for ii in range(0, len(Array_Bookmarks)):
			if Array_Stats[i][0] == Array_Bookmarks[ii][0]:
				Matching.append(Array_Bookmarks[ii])

	file = open("__cache__/Bookmarks.txt", "w")
	for i in range(0, len(Matching)):
		file.write(str(Matching[i][0]) + "," + str(Matching[i][1]) + "," + str(Matching[i][2]))
		file.write("\n")
	file.close()

def season_count(name): #Sender tilbake antall sesonger i en serie
	path = ReadPath()
	path = str(path[0] + "\\" + name + "\\")
	seasons = (os.listdir(path))
	return(len(seasons))


def episode_count(name, season): #Sender tilbake antall episoder i en seres sin sesong
	path = ReadPath()
	path = str(path[0] + "\\" + name + "\\" + "Season " + season + "\\")
	episodes = str(os.listdir(path))
	return(len(os.listdir(path)))


		
def ReadPath(): #Leser og sender tilbake navn på Path
	file = open("__cache__/Path.txt", 'r')
	path_text = csv.reader(file)
	Array = []

	#Legger text fra fil inn i lesbar liste
	for i in path_text:
		Array.append(i)
	return_file = Array[0]

	file.close()
	return(return_file)

def ReadStats(): #Sender tilbake en Array med alle "Stats"
	file = open("__cache__/Stats.txt", 'r')
	text_temp = csv.reader(file)
	Array = []

	for i in text_temp:
		Array.append(i)
	file.close()
	return(Array)

def ReadBookmarks(): #Sender tilbake en Array med alle "Stats"
	file = open("__cache__/Bookmarks.txt", 'r')
	text_temp = csv.reader(file)
	Array = []

	for i in text_temp:
		Array.append(i)
	file.close()
	return(Array)

def ReadNames_Episode(name, season): #Finnes det flere ep i sesong? Sjekker "Names" isetdet for å telle mappene.
	file = open("__cache__/Names.txt", 'r')
	text_temp = csv.reader(file)
	Array = []

	for i in text_temp:
		Array.append(i)
	file.close()
	return(int(Array[int(name)][int(season)+1]))

def ReadNames_Season(name): #Finnes det sesonger i en serie? Sjekker "Names" isetdet for å telle mappene.
	file = open("__cache__/Names.txt", 'r')
	text_temp = csv.reader(file)
	Array = []

	for i in text_temp:
		Array.append(i)
	file.close()
	return(int(Array[int(name)][1]))        
		
def text(text, size, color, x, y):
	myfont = pygame.font.SysFont("monospace", size)
	texty = myfont.render(text, 1, (color))
	SCREEN.blit(texty, (x, y))



class Back_button():
	def __init__(self, WIDTH2):
		self.x = WIDTH2-42
		self.y = 5
		self.w = 38
		self.h = 13

	def draw(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		color = button_col
		if self.x+self.w > mouse[0] > self.x and self.y+self.h> mouse[1] > self.y:
			color = hover_col
		pygame.draw.rect(SCREEN, color, [self.x, self.y, self.w, self.h])
		text("Back", 15, text_col, self.x+1, 3)
		
	def click(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
	
		if self.x+self.w > mouse[0] > self.x and self.y+self.h> mouse[1] > self.y:
			if click[0] == 1:
				return(True)

class Favorite_button():
	def __init__(self, WIDTH2, HIEGHT2):
		self.w = 74
		self.h = 13
		self.x = WIDTH2/2 - self.w/2 - 10
		self.y = HEIGHT2-self.h-5
		self.name = "Bookmark"


	def draw(self, nr, cc):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		color = button_col
		if self.x+self.w > mouse[0] > self.x and self.y+self.h> mouse[1] > self.y:
			color = hover_col
		pygame.draw.rect(SCREEN, color, [self.x, self.y, self.w, self.h])
		
		if cc == 1:
			fav_Array = ReadBookmarks()
			Array = ReadStats()
			for i in range(0, len(fav_Array)):
				if fav_Array[i][0] == Array[nr][0] and  fav_Array[i][1] == Array[nr][1] and  fav_Array[i][2] == Array[nr][2]:
					pygame.draw.rect(SCREEN, fav_true_col, [self.x, self.y, self.w, self.h])
					text("ed", 15, text_col, self.x+1+10*7, self.y-2)


		
		text(self.name, 15, text_col, self.x+1, self.y-2)
		
	def click(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
	
		if self.x+self.w > mouse[0] > self.x and self.y+self.h> mouse[1] > self.y:
			if click[0] == 1:
				return(True)
	def bookmark(self, fav_Array, Array, nr):
		count = 1
		file = open("__cache__/Bookmarks.txt", "w")
		for i in range(0, len(fav_Array)):
			file.write(str(fav_Array[i][0]) + "," + str(fav_Array[i][1]) + "," + str(fav_Array[i][2]))
			file.write("\n")
			if str(fav_Array[i][0]) == str(Array[nr][0]) and  str(fav_Array[i][1]) == str(Array[nr][1]) and  str(fav_Array[i][2]) == str(Array[nr][2]):
				count -= 1
			count += 1


		if count != len(fav_Array):
			file.write(str(Array[nr][0]) + "," + str(Array[nr][1]) + "," + str(Array[nr][2]))
			file.write("\n")
		
		file.close()

		Array_pre = ReadBookmarks()
		
		for i in range (0, len(Array_pre)):
			Array_pre[i][1] = int(Array_pre[i][1])
			Array_pre[i][2] = int(Array_pre[i][2])
			

		Array_aft = sorted(Array_pre)

		for i in range (0, len(Array_aft)):
			Array_aft[i][1] = str(Array_aft[i][1])
			Array_aft[i][2] = str(Array_aft[i][2])
			
		
		file = open("__cache__/Bookmarks.txt", "w")
		for i in range(0, len(Array_aft)):
			file.write(str(Array_aft[i][0]) + "," + str(Array_aft[i][1]) + "," + str(Array_aft[i][2]))
			file.write("\n")
		file.close()


class Next_button():
	def __init__(self, WIDTH2, HEIGHT2):
		self.w = 75
		self.h = 75
		self.x = WIDTH2-self.w-20
		self.y = (HEIGHT2/2)-(self.w/2)+20

	def draw(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		color = button_col
		if self.x+self.w > mouse[0] > self.x and self.y+self.h> mouse[1] > self.y:
			color = hover_col
		pygame.draw.rect(SCREEN, color, [self.x, self.y, self.w, self.h])
		text("Next", 30, text_col, self.x+1, self.y+20)
	
	def click(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
	
		if self.x+self.w > mouse[0] > self.x and self.y+self.h> mouse[1] > self.y:
			if click[0] == 1:
				return(True)
	def next_ep(self, nr):
		Array = ReadStats()
		if Array[nr][2] == str(ReadNames_Episode(nr, (Array[nr][1]))):#Finnes det flere ep i sesong?
			if Array[nr][1] != str(ReadNames_Season(nr)): #Finnes det flere sesonger i serie?
				Array[nr][1] = str(int(Array[nr][1])+1)
				Array[nr][2] = "1"
			else:
				pass
		else:
			Array[nr][2] = str(int(Array[nr][2])+1)
			
		file = open("__cache__/Stats.txt", "w")
		for i in range(len(Array)):
			file.write(str(Array[i][0]) + "," + str(Array[i][1]) + "," + str(Array[i][2]))
			file.write("\n")
		file.close()


class Prev_button():
	def __init__(self, WIDTH2, HEIGHT2):
		self.w = 75
		self.h = 75
		self.x = 20
		self.y = (HEIGHT2/2)-(self.w/2)+20

	def draw(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		color = button_col
		if self.x+self.w > mouse[0] > self.x and self.y+self.h> mouse[1] > self.y:
			color = hover_col
		pygame.draw.rect(SCREEN, color, [self.x, self.y, self.w, self.h])
		text("Prev", 30, text_col, self.x, self.y+20)
	
	def click(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
	
		if self.x+self.w > mouse[0] > self.x and self.y+self.h> mouse[1] > self.y:
			if click[0] == 1:
				return(True)
	def prev_ep(self, nr):
		Array = ReadStats()
		if Array[nr][2] == "1":
			if Array[nr][1] != "1":
				Array[nr][1] = str(int(Array[nr][1])-1)
				Array[nr][2] = str(ReadNames_Episode(nr, Array[nr][1]))
			else:
				pass	
		else:
			Array[nr][2] = str(int(Array[nr][2])-1)

		file = open("__cache__/Stats.txt", "w")       
		for i in range(len(Array)):
			file.write(str(Array[i][0]) + "," + str(Array[i][1]) + "," + str(Array[i][2]))
			file.write("\n")
		file.close()

class choose_button():
	def __init__(self, WIDTH2, HEIGHT2):
		self.w = 49
		self.h = 15
		self.x = WIDTH2-53
		self.y = 25
		

	def draw(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		color = button_col
		if self.x+self.w > mouse[0] > self.x and self.y+self.h> mouse[1] > self.y:
			color = hover_col
		pygame.draw.rect(SCREEN, color, [self.x, self.y, self.w, self.h])
		text("Change ep", 13, text_col, self.x, self.y+1)
		
	def click(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
	
		if self.x+self.w > mouse[0] > self.x and self.y+self.h> mouse[1] > self.y:
			if click[0] == 1:
				return(True)
	def switch_ep(self):
		pass

#-----------------------------------------------------------------------------------------------------

if Ikke_open_video == False:
	StartupCheck()

#Farger
WHITE = (255,255,255)
BLACK = (0,0,0)

GRAY = (128,128,128)
GRAY_LIGHT = (192,192,192)

RED = (255, 0, 0)
RED_LIGHT = (255,100,100)

YELLOW = (255,255,0)

BLUE = (0,128,255)
BLUE_LIGHT = (135,206,235)

GREEN = (0,255,0)
GREEN_LIGHT = (0, 204, 102)

BROWN_LIGHT = (250,240,230)


#Interface colors: CAS
bk_col = BLACK        #Bakgrunns farge
text_col = GREEN           #Text farge
button_col = BLACK         #Knapp farge
hover_col = GRAY      #Bytter til denne farger når du har musa på den
current_ep = YELLOW        #Fargen som viser hvilken ep du er på i episode change
fav_true_col = bk_col      #Fargen på knappen hvis episoden er bookmarket

HEIGHT2 = 150
WIDTH2 = 450

HEIGHT = 350
WIDTH = 550

FPS = 30     

app = True
watch = False
choose = False
fav = False

Array = ReadStats()

slider_y = 0
slider_speed = 25

clicked = False

text_inp = []

back_b = Back_button(WIDTH2)
back_b2 = Back_button(WIDTH)

fav_b = Favorite_button(WIDTH2, HEIGHT2)
fav_b2 = Favorite_button(WIDTH, HEIGHT)
fav_b2.x = WIDTH-fav_b2.w-15
fav_b2.y = 5
fav_b2.w += 9
fav_b2.name = "Bookmarks"

next_b = Next_button(WIDTH2, HEIGHT2)
prev_b = Prev_button(WIDTH2, HEIGHT2)
choose_b = choose_button(WIDTH2, HEIGHT2)

#Lage skjerm og FPS
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Watch - A Kriss Software')
clock = pygame.time.Clock()

def fav_check(nr):
	Array = ReadStats()
	Fav_Array = ReadBookmarks()
	ret = 0
	for i in range(0, len(Array)):
		if Fav_Array[nr][0] == Array[i][0]:
			Array[i][1] = Fav_Array[nr][1]
			Array[i][2] = Fav_Array[nr][2]
			ret = i
	
	file = open("__cache__/Stats.txt", "w")       
	for i in range(len(Array)):
		file.write(str(Array[i][0]) + "," + str(Array[i][1]) + "," + str(Array[i][2]))
		file.write("\n")
	file.close()
	return(ret)

def rect_check(x, y, w, h):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	if x+w > mouse[0] > x and y+h> mouse[1] > y:
		if click[0] == 1:
			return(True)        

def hover_check(x, y, w, h):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	if x+w > mouse[0] > x and y+h> mouse[1] > y:
		return(True)
		
def press_check(Array, slider_y, xx):
	x = 10
	y = 55+slider_y
	size = 18
	highest = 0

	if xx > 0:
		x = xx
	
	for i in range (0, len(Array)):
		if highest < len(Array[i][0]):
			highest = len(Array[i][0])
			bar = (x+12*highest+7*size+120)

	for i in range (0, len(Array)):
		if xx == 0:
			if rect_check(x, y, bar, size) == True:
				Arr = [True, i]
				return(Arr)
		if xx > 0:
			if rect_check(x, y, size, size) == True:
				Arr = [True, i]
				return(Arr)
		y += (size+8)
			
def slett_fav(nr):

	fav_Array = ReadBookmarks()

	fav_Array.remove(fav_Array[nr])
	file = open("__cache__/Bookmarks.txt", "w")
	for i in range(len(fav_Array)):
		file.write(str(fav_Array[i][0]) + "," + str(fav_Array[i][1]) + "," + str(fav_Array[i][2]))
		file.write("\n")
	file.close()
	
def UI_Main(Array, slider_y, fav, clicked):
	x = 10
	y = 55+slider_y
	size = 18
	highest = 0
	color = button_col

	

	
	for i in range (0, len(Array)):
		if highest < len(Array[i][0]):
			highest = len(Array[i][0])
			bar = (x+12*highest+7*size+120)
		
	for i in range (0, len(Array)):
		pygame.draw.rect(SCREEN, button_col, [x, y, bar, size])
		if fav == 1:
			xx = x+bar+2
			pygame.draw.rect(SCREEN, button_col, [xx, y, size, size])

			if hover_check(x+bar+2, y, 18, size) == True:
				pygame.draw.rect(SCREEN, hover_col, [xx, y, size, size])

			pygame.draw.line(SCREEN, RED, (xx, y), (xx+size-1, y+size-1), 1)
			pygame.draw.line(SCREEN, RED, (xx, y+size-1), (xx+size-1, y), 1)

			p_c = press_check(Array, slider_y, xx)
			try:
				if clicked == False:
					if p_c[0] == True:
						slett_fav(p_c[1])
						break
			except:
				pass
				
		if hover_check(x, y, bar, size) == True:
			pygame.draw.rect(SCREEN, hover_col, [x, y, bar, size])
			
		text(str(Array[i][0]), size, text_col, x, y)
		text("Season:[{}]".format(str(Array[i][1])), size, text_col, x+12*highest, y)
		text("Episode:[{}]".format(str(Array[i][2])), size, text_col, (x+12*highest)+7*size, y)
		y += (size+8)

def UI_Watch(nr, Array):
	text(Array[nr][0], 30, text_col, 10, 5)
	text("Season:{}".format(Array[nr][1]), 30, text_col, 130, 55)
	text("Episode:{}".format(Array[nr][2]), 30, text_col, 130, 85)
	back_b.draw()
	prev_b.draw()
	next_b.draw()
	choose_b.draw()
	fav_b.draw(nr, 1)

def UI_change(Array, nr, WIDTH, HEIGHT, slider_y, clicked):
	back_b2.draw()
	xx = 0
	yy = 0
	tab = 0
	fav_Array = ReadBookmarks()
	text(str(Array[nr][0]), 30, text_col, WIDTH/2-len(Array[nr][0])*4.5, HEIGHT/2)
	for i in range (0, (ReadNames_Season(nr))):
		
		text("Season{}".format(i+1), 30, text_col, 10, 10*tab+15+22*yy+50*i+slider_y)
		
		for ii in range(0, (ReadNames_Episode(nr, i+1))):
			y = 10*tab+15+22*yy+50*i+slider_y+30
			x = 25+35*xx
			mouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			
			pygame.draw.rect(SCREEN, button_col, [x, y, 20, 20])
			#print(str(Array[nr]))

			for iii in range(0, len(fav_Array)):
				if str(fav_Array[iii][0]) == str(Array[nr][0]):
					if str(fav_Array[iii][1]) == str(i+1):
						if str(fav_Array[iii][2]) == str(ii+1):
							pygame.draw.rect(SCREEN, WHITE, [x, y, 20, 20])
                
			if str(Array[nr][1]) == str(i+1) and str(Array[nr][2]) == str(ii+1):
				pygame.draw.rect(SCREEN, current_ep, [x, y, 20, 20])


			
			if x+20 > mouse[0] > x and y+20> mouse[1] > y:
				pygame.draw.rect(SCREEN, hover_col, [x, y, 20, 20])
				if clicked == False:
					if click[0] == 1:
						Array[nr][1] = i+1
						Array[nr][2] = ii+1
						file = open("__cache__/Stats.txt", "w")       
						for i in range(len(Array)):
							file.write(str(Array[i][0]) + "," + str(Array[i][1]) + "," + str(Array[i][2]))
							file.write("\n")
						file.close()
						return(True)
					
				
			text(str(ii+1), 12, text_col, x+4, y+3)
			
			xx += 1
			if xx == 5:
				xx = 0
				yy += 1
		xx = 0
		tab += 1
		
def start_episode(c):
	Array = ReadStats()
	path = ReadPath()
	if Ikke_open_video == False:
		openfile = str(path[0] + "\\" + Array[c][0] + "\\Season " + Array[c][1] + "\\Episode " + Array[c][2] + ".m4v")
		try:
			os.startfile(openfile)
			pass
		except:
			try:
				openfile = str(path[0]) + "\\" + Array[c][0] + "\\Season " + Array[c][1] + "\\Episode " + Array[c][2] + ".mp4"
				os.startfile(openfile)
			except Exception as e:
				print(e)
				pass


while app:
	click = pygame.mouse.get_pressed()
	if click[0] == 0:
		clicked = False
	if click[0] == 1:
		clicked = True
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			app = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 4 and slider_y < 0:
				slider_y += slider_speed
			if event.button == 5:
				slider_y -= slider_speed
	try:
		check = press_check(Array, slider_y, 0)
		if check[0] == True:
			if clicked == False:
				nr = check[1]
				start_episode(nr)
				watch = True
				SCREEN = pygame.display.set_mode((WIDTH2, HEIGHT2))
	except Exception as e:
		pass


	if fav_b2.click() == True:
		if clicked == False:
			clicked = True
			Fav_Array = ReadBookmarks()
			fav = True
		
	SCREEN.fill(bk_col)
	text("Series:", 30, text_col, 10, 10+slider_y)
	UI_Main(Array, slider_y, 0, clicked)
	fav_b2.draw(0, 0)
	pygame.display.update()
	clock.tick(FPS)
	
	while fav:
		click = pygame.mouse.get_pressed()
		if click[0] == 0:
			clicked = False
		if click[0] == 1:
			clicked = True
			Fav_Array = ReadBookmarks()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				app = False
				fav = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4 and slider_y < 0:
					slider_y += slider_speed
				if event.button == 5:
					slider_y -= slider_speed
		try:
			check = press_check(Fav_Array, slider_y, 0)
			if check[0] == True:
				if clicked == False:
					nr = check[1]
					nr = fav_check(nr)
					start_episode(nr)
					watch = True
					fav = False
					Array = ReadStats()
					SCREEN = pygame.display.set_mode((WIDTH2, HEIGHT2))
					
		except Exception as e:
			pass

		if back_b2.click() == True:
			if clicked == False:
				clicked = True
				fav = False
				Array = ReadStats()
				slider_y = 0
			
		SCREEN.fill(bk_col)
		text("Bookmarked Episodes:", 30, text_col, 10, 10+slider_y)
		UI_Main(Fav_Array, slider_y, 1, clicked)
		back_b2.draw()
		pygame.display.update()
		clock.tick(FPS)
	
		
	while watch:
		click = pygame.mouse.get_pressed()
		if click[0] == 0:
			clicked = False
		if click[0] == 1:
			clicked = True
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				app = False
				watch = False
				
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					watch = False
					Array = ReadStats()
					slider_y = 0
					SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

					
		if fav_b.click() == True:
			if clicked == False:
				clicked = True
				Fav_Array = ReadBookmarks()
				fav_b.bookmark(Fav_Array, Array, nr)
				
				
		if back_b.click() == True:
			if clicked == False:
				watch = False
				Array = ReadStats()
				slider_y = 0
				SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

		if next_b.click() == True:
			if clicked == False:
				clicked = True
				next_b.next_ep(nr)
				Array = ReadStats()
				start_episode(nr)

		if prev_b.click() == True:
			if clicked == False:
				clicked = True
				prev_b.prev_ep(nr)
				Array = ReadStats()
				start_episode(nr)

		if choose_b.click() == True:
			if clicked == False:
				clicked = True
				choose = True
				SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
				
			
		SCREEN.fill(bk_col)
		UI_Watch(nr, Array)
		pygame.display.update()
		clock.tick(FPS)

		while choose:
			click = pygame.mouse.get_pressed()
			if click[0] == 0:
				clicked = False
			if click[0] == 1:
				clicked = True
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					app = False
					watch = False
					choose = False
					
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 4 and slider_y < 0:
						slider_y += slider_speed
					if event.button == 5:
						slider_y -= slider_speed	
					
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						choose = False
						Array = ReadStats()
						slider_y = 0
						SCREEN = pygame.display.set_mode((WIDTH2, HEIGHT2))
						

			SCREEN.fill(bk_col)

			if back_b2.click() == True:
				if clicked == False:
					clicked = True
					choose = False
					Array = ReadStats()
					slider_y = 0
					SCREEN = pygame.display.set_mode((WIDTH2, HEIGHT2))
			
			if UI_change(Array, nr, WIDTH, HEIGHT, slider_y, clicked) == True:
				if clicked == False:
					clicked = True
					choose = False
					Array = ReadStats()
					start_episode(nr)
					slider_y = 0
					SCREEN = pygame.display.set_mode((WIDTH2, HEIGHT2))
				
			pygame.display.update()
			clock.tick(FPS)

pygame.quit()
