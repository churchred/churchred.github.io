import time
import pygame
import random
import os

pygame.init()
clock = pygame.time.Clock()

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


def random_nr():
        n = int(random.randrange(1, 1023, 2))
        return n

def menu():
        On = True
        nr = 1
        counter = ""
        one = 0
        two = 0
        three = 0
        four = 0

        while On is True:
                
                one = random_nr()
                two = random_nr()
                three = random_nr()
                four = random_nr()                
                
                file = open("RawData.txt", "a")
                file.write(str(nr) + ", " + str(one) + ", " + str(two) + ", " + str(three) + ", " + str(four))
                file.write("\n")
                file.close()
                
                #Interface
                os.system('CLS')
                print("Sending Data{}".format(counter))
                counter = counter + "."
                if counter == "....":
                        counter = ""

                nr += 1
                        

                clock.tick(5)
                
RawDataCheck()
menu()
quit()
