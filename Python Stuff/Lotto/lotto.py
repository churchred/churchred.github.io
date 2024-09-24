import random
import time
import sys
import os


lotto_nr_size = 8
lotto_min_value = 1
lotto_max_value = 10


# Lager en liste med alle mulige tall vi kan velge
lotto_matix = []
for i in range(lotto_min_value, lotto_max_value+1):
    lotto_matix.append(i)

global buffer
buffer = ""



# Lager en loadingbar og printer antall prosent. (Nåværende_verdi, max_mulig_verdi)
def loading(curr, max, start_time):

    bar_size = 20 # Størrelse på loading bar. Denne kan gjøres om på uten problemer. Baren er dynamisk.

    # Definerer farge jeg kan bruke i print. 
    green = "\033[32m"
    reset = "\033[39m"

    percent = round((curr*100)/max) # Regner ut prosenten av verdiene

    #Finner prosent verdi til loadingbaren sin størrelse basert på overall prosent.
    bar_max = bar_size
    bar_curr = round(bar_max*percent/100)

    bar = "|" # Legger til startveggen til baren
    
    # Fyller inn loading bar med fyll
    for i in range(0, bar_curr):
        bar += u"\u2588"

    # Fyller in den tomme biten av loading bar med mellomrom/tomrom
    for i in range(0, bar_max-bar_curr):
        bar += "."

    bar += "|" # Legger til sluttveggen til baren

    end_time = time.time() # Slutt tid
    elapsed_time = round((end_time - start_time), 2) # Hvor lang tid det tok
    
    if percent == 100:
        sys.stdout.write("\r" + green + bar + str(percent) + "%" + "  |  " + str(elapsed_time) + "s  |  " + str("{:,}".format(max)) + " rows " + reset)
        sys.stdout.flush()   
    else:
        sys.stdout.write("\r" + bar + str(percent) + "%" + "  |  " + str(elapsed_time) + "s  |  " + str("{:,}".format(curr)) + " rows ")
        sys.stdout.flush()


def lotto_array_maker():

    numbers_a = []
    matrix = lotto_matix.copy()

    # Lager lotto tall til same-person
    for i in range(0, lotto_nr_size):
        index = random.randrange(0, len(matrix)) # Lager et tall mellom 0 og lengden på Matrix. MAtrix inneholder alle mulige lotto tall.
        numbers_a.append(matrix[index])          # Legger til nytt tall i ny liste.
        matrix.remove(matrix[index])             # Fjerner det brukte tallet fra Matrix slik at vi kan få det igjen.

    numbers_a.sort()
    return numbers_a # Sorterer slik at ci kan lettere sammenlignes i IF-statements.



def Lotto(x):

    os.system('cls')
    
    # List of victories
    victory = [0, 0, 0]

    # Lager lotto tall til same-person
    same_guess = lotto_array_maker()

    st = time.time() # Sets start time
    print_stats(victory) # Loader stats slik at de er synlige mens loadingbaren er der. 
    loading(0, 100, st) # Lager baren. Greit å gjøre pga STORE loops, fordi 1% merket tar lang tid før skjer.
    
    
    
    for i in range(x):

        value = lotto_array_maker()

        different_guess = lotto_array_maker()
        
        percent = int((i*100)/x) # Regner ut prosenten av verdien
        old_percent = int(((i-1)*100)/x) # Regner ut prosenten av forrige verdi

        #Sjekker om prosent-ferdig er større en sist, if so then update loadingbar
        if percent > old_percent or i+1 == x:
              os.system('cls') # Clear terminal
              print_stats(victory)
              loading(i, x, st)
        
        # Har begge personene rett?
        if different_guess == value and same_guess == value:
            victory[2] += 1

        # Har Same-person rett?
        if same_guess == value:
            victory[0] += 1

        # Har Diff-person rett?
        if different_guess == value:
            victory[1] += 1


    os.system('cls') # Clear terminal
    global buffer # Update buffer (for å gjevne ut streken til høyre for "Both won:" i print_stats)
    buffer = ""

    print_stats(victory)
    loading(i, x, st)
    

def print_stats(v):
    print("Lotto Simulator: \n")
    print("Generating", "[" + "{:,}".format(nr) + "]", "lotto rows...")
    print("Each row has", lotto_nr_size, "numbers, between", lotto_min_value, "and", str(lotto_max_value) + ",", "no repeat numbers in a row")
    print("---------------------------------------------")
    print("Same value won:", v[0], "     |", round(((v[0]/nr)*100), 2), "%")
    print("Different value won:", v[1], "|", round(((v[1]/nr)*100), 2), "%")
    print("Both won:", v[2], buffer + "           |", round(((v[2]/nr)*100), 2), "%")
    print("---------------------------------------------")

    
nr = 10_000_000

Lotto(nr)


