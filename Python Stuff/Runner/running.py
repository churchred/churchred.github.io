
#
# a) Modifiser skriptet for 100 m-løpet slik at det bestemmer og 
#    skriver ut hvor lang tid som ble brukt på 100 m til nærmeste 100-del.
#
#
# b) Lag en st-graf for løpet i Python.
#
#
# c) Hvilken fart var det og hvor langt var det løpt etter halve tiden?
#
#-------------------------------------------------------------------------------------------------

from pylab import *
import os
import time

# Symboler til ramme som brukes på hovedskjermen
hor_line = '' #\u2500
vert_line = '\u2502'
bottom_left_corner = '\u2514'
upper_left_corner = '\u250C'
bottom_right_corner = '\u2518'
upper_right_corner = '\u2510'

# Farger
RED = '\33[31m'
LGREEN = '\33[92m'
GREEN = '\33[32m'
RESET = '\33[0m'

# Skjermstørrelser
WIDTH = 52
HEIGHT = 11
MENU_HEIGHT = 18
border_len = 30

# Bygger topp og bunn ramme, altså boksen på hovedmenyen
for i in range(0,border_len):
  hor_line += '\u2500'

class App():
  def __init__(self):

    # Setter størrelsen på app-vinduet
    cmd = 'mode ' + str(WIDTH) + ", " + str(MENU_HEIGHT)
    os.system(cmd)

    self.s = 0            # startposisjon , m
    self.v = 0            # startfart , m/s
    self.save_v = self.v  # Lagring av v
    self.t = 0            # starttid, s

    # Hvis vi skal stoppe etter x sekunder, eventuelt når
    self.stop_time = [0, False]

    self.s_lenght = 100         # Hvor lang er banen
    self.s_slutt = 100          # Hvor vi skal stoppe
    self.a = 6                  # Akselerasjon
    self.save_a = self.a        # Lagring av a
    self.dt = 0.001             # Hvor mye tid som går hvert tick
    self.air_resist = True      # Tar vi luft motstand med i beregningen?
    self.frame_delay = self.dt  # Hvor mye pause mellom hvert tick av appen (s)

    # Lister til graf
    self.s_verdier = [self.s]
    self.v_verdier = [self.v]
    self.t_verdier = [self.t]

  # Selve app loopen
  def run(self):
    while True:
      os.system('cls')
      self.__init__()
      self.get_input()

  # Får input fra bruker
  def get_input(self):
      
      os.system('cls')
        
      # Printer innhold
      print((upper_left_corner + hor_line + upper_right_corner).center(WIDTH))
      print((vert_line + "".center(border_len) + vert_line).center(WIDTH))
      print((vert_line + ("Max length (s): " + LGREEN + str(self.s_lenght) + RESET).center(border_len+len(LGREEN)+len(RESET)) + vert_line).center(WIDTH+len(LGREEN)+len(RESET)))
      print((vert_line + ("Start Velocity (v0): " + LGREEN + str(self.v) + RESET).center(border_len+len(LGREEN)+len(RESET)) + vert_line).center(WIDTH+len(LGREEN)+len(RESET)))
      print((vert_line + ("Acceleration (a): " + LGREEN + str(self.a) + RESET).center(border_len+len(LGREEN)+len(RESET)) + vert_line).center(WIDTH+len(LGREEN)+len(RESET)))
      print((vert_line + "".center(border_len) + vert_line).center(WIDTH))
      print((vert_line + ("Delta time (d): " + LGREEN + str(self.dt) + RESET).center(border_len+len(LGREEN)+len(RESET)) + vert_line).center(WIDTH+len(LGREEN)+len(RESET)))
      print((vert_line + ("Air resistance (air): " + LGREEN + str(self.air_resist) + RESET).center(border_len+len(LGREEN)+len(RESET)) + vert_line).center(WIDTH+len(LGREEN)+len(RESET)))
      print((vert_line + ("Frame delay (f): " + LGREEN + str(self.frame_delay) + RESET).center(border_len+len(LGREEN)+len(RESET)) + vert_line).center(WIDTH+len(LGREEN)+len(RESET)))
      print((vert_line + "".center(border_len) + vert_line).center(WIDTH))
      print((bottom_left_corner  + hor_line + bottom_right_corner).center(WIDTH))

      print("\n")
      print("(run, a=x, s=x, v0=x, d=x, f=x, air=t/f, reset)".center(WIDTH))
      print("\n")

      # Ber om bruker input om hva vi skal gjøre.
      inp = input("§ ".rjust(int(WIDTH/2) - int(border_len/2) + 2))
      inp = inp.split("=")

      try: 
        # Gjør om på akselerasjon
        if inp[0] == "a":
          self.a = float(inp[1])
          if self.a < 0:
            self.a = 0
          self.save_a = self.a

        # Gjør om på Start Velocity
        elif inp[0] == "v0":
          self.v = float(inp[1])
          if self.v < 0:
            self.v = 0
          self.save_v = self.v
        
        # Gjør om på banelengde
        elif inp[0] == "s":
          self.s_lenght = float(inp[1])
          if self.s_lenght <= 0:
            self.s_lenght = 1
          self.s_slutt = self.s_lenght

        # Gjør om på frame-delay
        elif inp[0] == "f":
          self.frame_delay = float(inp[1])
          if self.frame_delay < 0:
            self.frame_delay = 0

        # Gjør om på delta time
        elif inp[0] == "d":
          self.dt = float(inp[1])
          if self.dt < 0:
            self.dt = 0

        # Gjør om på air resist
        elif inp[0] == "air":
          if inp[1] == "true" or inp[1] == "True" or inp[1] == "t":
            self.air_resist = True
          if inp[1] == "false" or inp[1] == "False" or inp[1] == "f":
            self.air_resist = False

        # Starter simulasjonen
        elif inp[0] == "start" or inp[0] == "run" or inp[0] == "go" or inp[0] == "r":
          self.simulation()
        
        elif inp[0] == "reset":
          self.__init__()
        
        # Gjenta til bruker vil starte
        self.get_input()
          
      # Fanger opp error
      except ValueError:
        print("Error: Ikke et tall")
        time.sleep(1)

  def simulation(self):
    # Gjør om på skjerm størrelse
    cmd = 'mode ' + str(WIDTH) + ", " + str(HEIGHT)
    os.system(cmd)

    # Vi starter med 0% ferdig i løpet.
    curr_percent = 0 

    # Simulasjons loopen
    while self.s <= self.s_slutt:

      # Oppdaterer alle fysikk verdier
      if self.air_resist == True:
        self.v = self.v + self.acceleration() * self.dt # beregner ny fart med luftmotstand
      if self.air_resist == False:
        self.v = self.v + self.a * self.dt # beregner ny fart UTEN luftmotstand

      self.s =  self.s +  self.v *  self.dt             # beregner ny posisjon
      self.t =  self.t +  self.dt                       # øker tiden med dt 
      self.s_verdier.append(self.s)                     # Legger s inn i posisjonslisten
      self.v_verdier.append(self.v)                     # Legger v inn i fartslisten
      self.t_verdier.append(self.t)                     # Legger t inn i tidslisten
      time.sleep(self.frame_delay)                      # Kjører selve loopen bare en gang per 0.01 sekunder

      # Sjekker om vi har nådd stopppunkt hvis vi har det
      if self.stop_time[1] == True:
        if self.stop_time[0] <= self.t:
          self.stop_time = [0, False]
          break

      # Sjekker prosent, vi oppdaterer kun hver prosent
      # ellers hadde skjermen hakket veldig og tallene hadde bevegd seg fort.
      new_percent = int((self.s * 100) / self.s_lenght)
      if  new_percent > curr_percent:
        curr_percent = new_percent

        # Lager banen og personen som løper
        self.run = GREEN
        for i in range(0, 51):
          if i == int(curr_percent/2):
            self.run += RESET + RED + "V" + RESET
          else:
            self.run += "."

        # Printer all info hver prosent økning
        self.print_runner()

    # Printer en siste gang eller loopen for å få riktige verdier på tingene
    self.print_runner() 
    print("\n")

    # Tar imot input om hva vi skal videre
    inp = input("(t=x, s=x, run, graph=st/sv)  §: ")
    inp = inp.split("=")
    
    # Restart sim med et tidpunkt vi skal stoppe på
    if inp[0] == "t" and inp[1][0].isnumeric():
      self.gotoTime(float(inp[1]))

    # Restart sim med sted(m) vi skal stoppe på
    elif inp[0] == "s" and inp[1][0].isnumeric():
      self.gotoPlace(float(inp[1]))

    # Kjør sim igjen
    elif inp[0] == "start" or inp[0] == "run" or  inp[0] == "go":
      self.reset()
      self.simulation()

    # Tegner graf
    elif inp[0] == "graph" or inp[0] == "graf":
      
      if inp[1] == "sv":
        self.draw("Fart som funksjon av posisjon", "$s$/(m)", "$v$/(m/s)", self.s_verdier, self.v_verdier)
        
      if inp[1] == "st":
        self.draw("Posisjon som funksjon av tid", "$t$/(s)", "$s$/(m)", self.t_verdier, self.s_verdier)

      self.reset()

      # Setter størrelsen på app-vinduet
      cmd = 'mode ' + str(WIDTH) + ", " + str(MENU_HEIGHT)
      os.system(cmd)
      
    
    # Resetter variabler og sender deg tilbake
    else:
      self.reset()
      
      # Setter størrelsen på app-vinduet
      cmd = 'mode ' + str(WIDTH) + ", " + str(MENU_HEIGHT)
      os.system(cmd)


  # Printer alt mens personen løper
  def print_runner(self):
    os.system('cls')

    # Sjekker hvilken akselerasjon vi skal vise frem
    # basert på om vi har luftmotstand eller ikke
    if self.air_resist == True:
      temp_a = round(self.acceleration(), 3)
    if self.air_resist == False:
      temp_a = self.a
      
    print(" Acceleration: " + LGREEN + str(temp_a) + "  m/s\u00B2 " +  RESET + "\n" + 
      " Velocity: " + LGREEN + str(round(self.v, 3)) + "  m/s" + RESET + "\n\n" + self.run + "\n\n" + 
      "               s: " + LGREEN + str(round(self.s,2)) + "m" + RESET + " / " + str(float(self.s_lenght)) + "m" + 
      "\n\n               t: " + LGREEN + str(round(self.t, 2)) + "s" + RESET) 
    

  # Resetter variablene og starter simulasjonen på nytt, men nå har vi et sted å stoppe på.
  def gotoPlace(self, to_s):
    self.s_slutt = to_s
    self.reset()
    self.simulation()

  # Resetter variablene og starter simulasjonen på nytt, men nå har vi et tidspunkt å stoppe på.
  def gotoTime(self, to_t):
    self.reset()
    self.stop_time = [float(to_t), True]
    self.simulation()

  # Resetter alle variabler UTENOM lagrete variabler. 
  # Da kan vi starte på nytt uten å miste verdiene som vi la inn
  def reset(self):
    self.s = 0
    self.v = self.save_v
    self.t = 0
    self.s_verdier = [self.s]
    self.v_verdier = [self.v]
    self.t_verdier = [self.t]
    

  # Når farten(v) blir større blir akselerasjonen(a) mindre
  def acceleration(self): 
    current_acceleration = - 0.5 * self.v + self.a 
    return current_acceleration
  
  # Tegning av graf
  def draw(self, titl, xl, yl, list1, list2):
    plot(list1 , list2)  # lager grafen
    title(titl)          # tittel paa grafen
    xlabel(xl)           # x - akse - tittel
    ylabel(yl)           # y - akse - tittel
    grid()               # viser rutenett
    show()               # viser grafen




# Lager appen og kjører den
app = App()
app.run()
