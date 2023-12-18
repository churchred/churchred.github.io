import os
import time
import csv
import pygame
from tkinter import *

pygame.init()
pygame.font.init()


#Varibaler
white = (255,255,255)
red = (255,0,0)
light_red = (255,102,102)
green = (0,255,0)
light_green = (102,255,102)
blue = (0,128,255)
light_blue = (51,153,255)
orange = (255,153,51)
light_orange = (255,178,102)
black = (0,0,0)
gray = (192,192,192)

HEIGHT = 700
WIDTH = 500

FPS = 30
SAFE_Online = True
CAPS = False

Text = ""
Array = []
temp = ""
MAX = 0
result = ""

X = WIDTH/2-150
Y = HEIGHT/2-75


Encode = False
Decode = False
Copy = False
Paste = False
Save = False
Load = False

#Lag skjerm
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('S.A.F.E')
clock = pygame.time.Clock()

def StartupCheck():
	try:
		file = open("List.txt", "r") 
		file.close()
	except FileNotFoundError:
		pass        
		file = open("List.txt", "w")   
		file.close()

def buttons():
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	myfont = pygame.font.SysFont("monospace", 25)
	myfont2 = pygame.font.SysFont("monospace", 15)
	Encode_text = myfont.render("Encode", 1, (black))
	Decode_text = myfont.render("Decode", 1, (black))
	
	Save_text = myfont2.render("Save", 1, (black))
	Load_text = myfont2.render("Load", 1, (black))
	Copy_text = myfont2.render("Copy", 1, (black))
	Paste_text = myfont2.render("Paste", 1, (black))
	
	
	pygame.draw.rect(gameDisplay, green, [X, 150, 100, 50]) #Encode
	pygame.draw.rect(gameDisplay, red, [X+200, 150, 100, 50]) #Decode
	
	pygame.draw.rect(gameDisplay, blue, [X+85, Y+355, 50, 50]) #Save
	pygame.draw.rect(gameDisplay, blue, [X+85+75, Y+355, 50, 50]) #Load
	
	pygame.draw.rect(gameDisplay, orange, [X+310, Y, 50, 50]) #Copy
	pygame.draw.rect(gameDisplay, orange, [X+310, Y+55, 50, 50]) #Paste

	pygame.draw.rect(gameDisplay, black, [WIDTH/2-5, Y-12, 10, 10]) #Clear
	
	if X+100 > mouse[0] > X-2 and 150+50 > mouse[1] > 150:
		pygame.draw.rect(gameDisplay, light_green, [X, 150, 100, 50]) #Encode
	if X+200+100 > mouse[0] > X+200-2 and 150+50 > mouse[1] > 150:
	   pygame.draw.rect(gameDisplay, light_red, [X+200, 150, 100, 50]) #Decode

	if X+85+50 > mouse[0] > X+85 and Y+355+50 > mouse[1] > Y+355:
	   pygame.draw.rect(gameDisplay, light_blue, [X+85, Y+355, 50, 50]) #Save
	if X+85+75+50 > mouse[0] > X+85+75 and Y+355+50 > mouse[1] > Y+355:
	   pygame.draw.rect(gameDisplay, light_blue, [X+85+75, Y+355, 50, 50]) #Load

	if X+310+50 > mouse[0] > X+310 and Y+50 > mouse[1] > Y:
	   pygame.draw.rect(gameDisplay, light_orange, [X+310, Y, 50, 50]) #Copy
	if X+310+50 > mouse[0] >X+310 and Y+55+50 > mouse[1] > Y+55:
	   pygame.draw.rect(gameDisplay, light_orange, [X+310, Y+55, 50, 50]) #Paste
	   
	   
	gameDisplay.blit(Encode_text, (X+5, 158+5))
	gameDisplay.blit(Decode_text, (X+200+5, 158+5))
	
	gameDisplay.blit(Save_text, (X+85+5, Y+355+10))
	gameDisplay.blit(Load_text, (X+85+75+5, Y+355+10))
	
	gameDisplay.blit(Copy_text, (X+310+5, Y+10))
	gameDisplay.blit(Paste_text, (X+310, Y+55+10))

	   
def heading():
	myfont = pygame.font.SysFont("monospace", 50)
	print_Text = myfont.render("S.A.F.E", 1, (black))
	gameDisplay.blit(print_Text, (WIDTH/2-115, 20))

def text_def(Text, Array):#              X  Y   W    H
	pygame.draw.rect(gameDisplay, gray, [X, Y, 300, 350])
	myfont = pygame.font.SysFont("monospace", 15)
	row = 0
	count = 0
	w = 0
	for i in range(len(Array)):
		print_Text = myfont.render(str(Array[i][1]), 1, (black))    
		gameDisplay.blit(print_Text, (X+10*w, Y+row))
		count += 1
		w += 1
		if count == 30:
			count = 0
			w = 0
			row += 15

	
while SAFE_Online == True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			SAFE_Online = False
		
		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
				CAPS = True
			if CAPS == False:
				if event.key == pygame.K_1:
				    Array.append([len(Array), "1"])
				    Text = Array
				if event.key == pygame.K_2:
				    Array.append([len(Array), "2"])
				    Text = Array
				if event.key == pygame.K_3:
				    Array.append([len(Array), "3"])
				    Text = Array
				if event.key == pygame.K_4:
				    Array.append([len(Array), "4"])
				    Text = Array
				if event.key == pygame.K_5:
				    Array.append([len(Array), "5"])
				    Text = Array
				if event.key == pygame.K_6:
				    Array.append([len(Array), "6"])
				    Text = Array
				if event.key == pygame.K_7:
				    Array.append([len(Array), "7"])
				    Text = Array
				if event.key == pygame.K_8:
				    Array.append([len(Array), "8"])
				    Text = Array
				if event.key == pygame.K_9:
				    Array.append([len(Array), "9"])
				    Text = Array
			if CAPS == False:
				if event.key == pygame.K_a:
					Array.append([len(Array), "a"])
					Text = Array
				if event.key == pygame.K_b:
					Array.append([len(Array), "b"])
					Text = Array
				if event.key == pygame.K_c:
					Array.append([len(Array), "c"])
					Text = Array
				if event.key == pygame.K_d:
					Array.append([len(Array), "d"])
					Text = Array
				if event.key == pygame.K_e:
					Array.append([len(Array), "e"])
					Text = Array
				if event.key == pygame.K_f:
					Array.append([len(Array), "f"])
					Text = Array
				if event.key == pygame.K_g:
					Array.append([len(Array), "g"])
					Text = Array
				if event.key == pygame.K_h:
					Array.append([len(Array), "h"])
					Text = Array
				if event.key == pygame.K_i:
					Array.append([len(Array), "i"])
					Text = Array
				if event.key == pygame.K_j:
					Array.append([len(Array), "j"])
					Text = Array
				if event.key == pygame.K_k:
					Array.append([len(Array), "k"])
					Text = Array
				if event.key == pygame.K_l:
					Array.append([len(Array), "l"])
					Text = Array
				if event.key == pygame.K_m:
					Array.append([len(Array), "m"])
					Text = Array
				if event.key == pygame.K_n:
					Array.append([len(Array), "n"])
					Text = Array
				if event.key == pygame.K_o:
					Array.append([len(Array), "o"])
					Text = Array
				if event.key == pygame.K_p:
					Array.append([len(Array), "p"])
					Text = Array
				if event.key == pygame.K_q:
					Array.append([len(Array), "q"])
					Text = Array
				if event.key == pygame.K_r:
					Array.append([len(Array), "r"])
					Text = Array
				if event.key == pygame.K_s:
					Array.append([len(Array), "s"])
					Text = Array
				if event.key == pygame.K_t:
					Array.append([len(Array), "t"])
					Text = Array
				if event.key == pygame.K_u:
					Array.append([len(Array), "u"])
					Text = Array
				if event.key == pygame.K_v:
					Array.append([len(Array), "v"])
					Text = Array
				if event.key == pygame.K_w:
					Array.append([len(Array), "w"])
					Text = Array
				if event.key == pygame.K_x:
					Array.append([len(Array), "x"])
					Text = Array
				if event.key == pygame.K_y:
					Array.append([len(Array), "y"])
					Text = Array
				if event.key == pygame.K_z:
					Array.append([len(Array), "z"])
					Text = Array
			if CAPS == True:
				if event.key == pygame.K_a:
					Array.append([len(Array), "A"])
					Text = Array
				if event.key == pygame.K_b:
					Array.append([len(Array), "B"])
					Text = Array
				if event.key == pygame.K_c:
					Array.append([len(Array), "C"])
					Text = Array
				if event.key == pygame.K_d:
					Array.append([len(Array), "D"])
					Text = Array
				if event.key == pygame.K_e:
					Array.append([len(Array), "E"])
					Text = Array
				if event.key == pygame.K_f:
					Array.append([len(Array), "F"])
					Text = Array
				if event.key == pygame.K_g:
					Array.append([len(Array), "G"])
					Text = Array
				if event.key == pygame.K_h:
					Array.append([len(Array), "H"])
					Text = Array
				if event.key == pygame.K_i:
					Array.append([len(Array), "I"])
					Text = Array
				if event.key == pygame.K_j:
					Array.append([len(Array), "J"])
					Text = Array
				if event.key == pygame.K_k:
					Array.append([len(Array), "K"])
					Text = Array
				if event.key == pygame.K_l:
					Array.append([len(Array), "L"])
					Text = Array
				if event.key == pygame.K_m:
					Array.append([len(Array), "M"])
					Text = Array
				if event.key == pygame.K_n:
					Array.append([len(Array), "N"])
					Text = Array
				if event.key == pygame.K_o:
					Array.append([len(Array), "O"])
					Text = Array
				if event.key == pygame.K_p:
					Array.append([len(Array), "P"])
					Text = Array
				if event.key == pygame.K_q:
					Array.append([len(Array), "Q"])
					Text = Array
				if event.key == pygame.K_r:
					Array.append([len(Array), "R"])
					Text = Array
				if event.key == pygame.K_s:
					Array.append([len(Array), "S"])
					Text = Array
				if event.key == pygame.K_t:
					Array.append([len(Array), "T"])
					Text = Array
				if event.key == pygame.K_u:
					Array.append([len(Array), "U"])
					Text = Array
				if event.key == pygame.K_v:
					Array.append([len(Array), "V"])
					Text = Array
				if event.key == pygame.K_w:
					Array.append([len(Array), "W"])
					Text = Array
				if event.key == pygame.K_x:
					Array.append([len(Array), "X"])
					Text = Array
				if event.key == pygame.K_y:
					Array.append([len(Array), "Y"])
					Text = Array
				if event.key == pygame.K_z:
					Array.append([len(Array), "Z"])
					Text = Array
		
			if event.key == pygame.K_BACKSPACE: #CAS
				try:
					nr = 0
					nr = len(Array)-1
					#print("Plass:", nr, " Symbol:", Array[nr])
					Array.remove(Array[nr])
					Text = Array
				except IndexError:
					print("Error")
					
			if event.key == pygame.K_SPACE:
				Array.append([len(Array), " "])
				Text = Array
			if event.key == pygame.K_COMMA:
				Array.append([len(Array), ","])
				Text = Array
			if event.key == pygame.K_PERIOD:
				if CAPS == True:
					Array.append([len(Array), ":"])
				if CAPS == False:
					Array.append([len(Array), "."])
				Text = Array
			if event.key == pygame.K_1 and CAPS == True:
				Array.append([len(Array), "!"])
				Text = Array
			if event.key == 45 and CAPS == True:
				Array.append([len(Array), "?"])
				Text = Array
			if event.key == pygame.K_8 and CAPS == True:
				Array.append([len(Array), "("])
				Text = Array
			if event.key == pygame.K_9 and CAPS == True:
				Array.append([len(Array), ")"])
				Text = Array
			if event.key == pygame.K_5 and CAPS == True:
				Array.append([len(Array), "%"])
				Text = Array
			if event.key == pygame.K_7 and CAPS == True:
				Array.append([len(Array), "/"])
				Text = Array

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
				CAPS = False


	#Sjekker om vi trykker på Encode/Decode
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if X+100 > mouse[0] > X-2 and 150+50 > mouse[1] > 150:#Encode
		if click[0] == 1:
			if Encode == False:
				if MAX <= 1:
					Array = []
					for i in range (len(Text)):
						x = ord(Text[i][1])
						x = x+1
						x = chr(x)
						Array.append([len(Array), x])
					Text = Array
					MAX += 1
					print(MAX)
				Encode = True
				
	if X+200+100 > mouse[0] > X+200-2 and 150+50 > mouse[1] > 150:#Decode
		if click[0] == 1:
			if Decode == False:
				if MAX >= (-1):
					Array = []
					for i in range (len(Text)):
						x = ord(Text[i][1])
						x = x-1
						x = chr(x)
						Array.append([len(Array), x])
					Text = Array
					MAX -= 1
					print(MAX)
				Decode = True
	
				
	if WIDTH/2-5+10 > mouse[0] > WIDTH/2-5 and Y-12+10 > mouse[1] > Y-12: #Clear Box
		if click[0] == 1:
			Array = []
			Text = Array
			MAX = 0

	if X+310+50 > mouse[0] > X+310 and Y+50 > mouse[1] > Y: #Copy
		if click[0] == 1:
			if Copy == False:
				
				print("Copy")
				r = Tk()
				r.withdraw()
				temp = ""
				r.clipboard_clear()
				for i in range (len(Array)):
					temp = temp+Array[i][1]
				r.clipboard_append(str(temp))
				r.destroy()
				Copy = True
				
				
	if X+310+50 > mouse[0] >X+310 and Y+55+50 > mouse[1] > Y+55: #Paste
		if click[0] == 1:
			if Paste == False:
				try:
					print("Paste")
					r=Tk()
					r.withdraw()
					temp = ""
					result = r.selection_get(selection="CLIPBOARD")
					r.destroy
					temp = str(result)
					for i in temp:
						Array.append([len(Array), i])
					Text = Array
					Paste = True
				except TclError:
					print("Value Error")

					
				
	if X+85+50 > mouse[0] > X+85 and Y+355+50 > mouse[1] > Y+355:#Save
		if click[0] == 1:
			if Save == False:
				StartupCheck()
				file = open("List.txt", "w")
				for i in range(len(Text)):
					file.write(str(Text[i][1]))
				file.close()
				Save = True
				
	if X+85+75+50 > mouse[0] > X+85+75 and Y+355+50 > mouse[1] > Y+355:#Load
		if click[0] == 1:
			if Load == False:
				StartupCheck()
				Array = []
				file = open("List.txt", 'r')
				text_temp = csv.reader(file)
				for i in text_temp:
					Array = Array + [i]
				file.close()
				Text = str(Array)
				Array = []
				y = 0
				for i in Text:
					if y != 0 and y != 1 and y != 2 and y != len(Text) and y != len(Text)-1 and y != len(Text)-2 and y != len(Text)-3:
						Array.append([y, i])
					y += 1
				for i in range (len(Array)):
					try:
						if Array[i][1] == "'" and Array[i+1][1] == "," and Array[i+2][1] == " " and Array[i+3][1] == "'":
							Array.remove(Array[i])
							Array.remove(Array[i+1])
							Array.remove(Array[i+1])

						Text = Array
					except IndexError:
						print("")

				Text = Array
				Load = True
	if len(Array) > 690:
		i = (len(Array)-690)
		for a in range (i):
			nr = 0
			nr = len(Array)-1
			Array.remove(Array[nr])
			Text = Array

	if click[0] == 0:
		Encode = False
		Decode = False
		Copy = False
		Paste = False
		Save = False
		Load = False

	
	#StartupCheck()
	gameDisplay.fill(white)
	text_def(Text, Array)
	heading()
	buttons()
	pygame.display.update()
	clock.tick(FPS)    




   
pygame.quit()
quit()
