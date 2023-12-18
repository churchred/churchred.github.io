import csv
import time
import pygame
import os
from collections import deque

pygame.init()

def RawDataCheck():
    #Sjekker om Rawdata finnes
    try:
        file = open("RawData.txt", "r") 
        file.close()
    except FileNotFoundError:
        pass        
        print("Error: No File 'RawData' found.")
        time.sleep(2)
        print("Creating file..")
        time.sleep(1)
        file = open("RawData.txt", "w") 
        file.close()
        print("Done!")
        time.sleep(2)
        os.system('CLS')
        
def CalculatedCheck():
    #Sjekker om Rawdata finnes
    try:
        file = open("Calculated.txt", "r") 
        file.close()
    except FileNotFoundError:
        pass        
        print("Error: No File 'Calculated.txt' found.")
        time.sleep(2)
        print("Creating file..")
        time.sleep(1)
        file = open("Calculated.txt", "w") 
        file.close()
        print("Done!")
        time.sleep(2)
        os.system('CLS')


def main():
    
    run = True
    FPS = 30
    clock = pygame.time.Clock()

    prev_ID = 0
    curr_ID = 0
    
    pause = False
    counter = 0

    while run == True:
        try:
            #Lager variabler
            Liste_OLD = []
            Liste_OLD_Print = []
            Liste_NEW = []
            antall = 4  #Antall per rad (ikke inkludert ID)

            #Åpner fila og finner siste rad
            file = open("RawData.txt", 'r')
            lastrow = deque(csv.reader(file), 1)[0]

            
            #Overfører siste rad data til Liste
            for i in lastrow:
                Liste_OLD = Liste_OLD + [i]
            file.close()

            #Sjekker ID
            curr_ID = int(Liste_OLD[0])

            #Gjør om til int slik at det ser bedre ut når jeg Printer senere
            Liste_OLD_Print = (Liste_OLD[:])
            Liste_OLD_Print = list(map(int, Liste_OLD_Print))
            Liste_OLD_Print.remove(Liste_OLD_Print[0])

            #Gjør om lista ved å plusse på med 1 og dytter det inn i ny liste
            
            Liste_OLD[1] = round(((0.095 + (5.0*(int(Liste_OLD[1]))/1023)/5)/0.009)*10, 2)
                
            Liste_OLD[2] = round(((5.0*(int(Liste_OLD[2]))/1023)/0.01)-273.15, 2)
                
            Liste_OLD[3] = round(1.33*(3.3*(int(Liste_OLD[3]))/1023) - 1.26, 2)
                
            Liste_OLD[4] = round(1.33*(3.3*(int(Liste_OLD[4]))/1023) - 1.26, 2)

            Liste_OLD.remove(Liste_OLD[0])
            Liste_NEW.append(Liste_OLD)
            

            #Lager ny fil som inneholder nye verdier
            if curr_ID != prev_ID:
                temp = ""
                new_file = open("Calculated.txt", "a")
                temp = str(curr_ID)
                temp = temp + ", "
                for i in range (0, antall):
                     temp = temp + str(Liste_NEW[0][i])
                     if i != (antall-1):
                        temp = temp + ", "
                new_file.write(str(temp))
                new_file.write("\n")
                new_file.close()
                pause = False
                counter = 0

                #Printer verdier
                print('ID:{}'.format(curr_ID), str(Liste_OLD_Print).ljust(22), Liste_NEW[0])
                #print('ID:{0}, {1} {2}'.format(curr_ID, Liste_OLD_Print, Liste_NEW[0]))
                
            else:
                counter += 1
                if counter >= (2*FPS):
                    if pause == False:
                        print("No new data..")
                        counter = 0
                        pause = True
                
            prev_ID = curr_ID
            clock.tick(FPS)
           
        #except Exception as e:
            #print("Error:", e)
        except:
            pass
            


RawDataCheck()
CalculatedCheck()
main()
quit()
