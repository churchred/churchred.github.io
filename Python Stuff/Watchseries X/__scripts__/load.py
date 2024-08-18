import os
import csv
import sys



class LoadData():
  def __init__(self):
    self.Data_Names = [] # Where we store series info
    self.Data_Stats = [] # Where we store series save data
    self.Data_Favs = []  # Where we store bookmarked episodes

    # Every file present within main directory
    # that is NOT a series NEEDS to be here.
    self.Ignore_list = [
      "__cache__",
      "__pycache__",
      "__scripts__",
      "box_class.py",
      "button_class.py",
      "general.py",
      "load.py",
      "loadbar.py",
      "scrolling.py",
      "settings.py",
      "main.py",
      "main.exe",
      "main.pyw"
    ]


  # What happens when the app starts
  # We gather information about series/episodes
  def load(self):

    # Reads or makes all files needed
    self.first_time()

    # Removes items no longer present in the folder from save-file (Stats.txt, Names.txt)
    self.Update_Stats() 

    # Reads new save-data
    self.Data_Names = self.ReadNames()
    self.Data_Stats = self.ReadStats()
    self.Data_Favs = self.ReadFavs()

    return self.Data_Names, self.Data_Stats, self.Data_Favs

  # Look into this form of path finding, for exe files pyinstaller
  def resource_path(self, relative_path):
    try:
      base_path = sys._MEIPASS
    except:
      base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

  # Making sure every txt file is present and updates, 
  # and creating them if they're not
  def first_time(self):

    # Checks if "__cache__" folder exists and makes one if not
    try:
      os.makedirs("__cache__")
    except Exception as e:
      pass


    # Checks if "path.txt" exists, if not makes one. 
    # "Path.txt" contains the path to the current folder
    try:
      file = open(self.resource_path("__cache__/Path.txt"), "r") 
      file.close()
    except FileNotFoundError:

      dirname, junk = os.path.split(os.path.abspath(__file__)) # Makes path to current directory
      print(dirname)
      dirname2 = os.path.split(os.path.abspath(dirname))
      dirname2 = self.resource_path(dirname2[0])         # Gets true path to use in exe files (Alpha)
      file = open(self.resource_path("__cache__/Path.txt"), "w")             # Saves path to new file, "Path.txt"
      file.write(''.join(dirname2))
      file.close()  
      


    # Checks if Names.txt exists and makes on if it doesnt
    # "Names.txt" contains the name of every series and 
    # how many seasons and episodes it has
    try:
      path = self.ReadPath()		
      folder_names = os.listdir(path)         # Returns name of every file in curren directory
      file = open(self.resource_path("__cache__/Names.txt"), "w") # Opens, or creates, "Names.txt"
      
      # Checks each folder for how many seasons and episodes it has
      # Goes trough every file, except itself, __cache__ and empty folders.
      for i in folder_names: 

        
        if i not in self.Ignore_list and self.season_count(i) > 0:

          # Checks how may folders are inside each folder.
          # In other words, it returns the number of seasons
          seasons = self.season_count(i) 

          # This variable will store how many episode are within
          # each season folder. Example: "Fallout, number_seasons, 10, 9, 8"
          episodes_in_season = "" 
          
          # Checks inside each season folder within current series.
          for ii in range(1, int(seasons)+1):
            episodes_in_season = str(episodes_in_season) + str(self.episode_count(i, ii)) + ","
          
          # Removes the last "," in the string
          episodes_in_season = episodes_in_season[:-1]

          # Skriv inn antall sesonger og hvor mange episoder per sesong. 
          file.write(str(i) + "," + str(seasons) + "," + str(episodes_in_season))
          file.write('\n')
      file.close()

    except Exception as e:
      print("Error: ", e)



    # Checks if Stats.txt exists and makes one if it doesnt
    # "Stats.txt" contains where you are in each series 
    try:
      file = open(self.resource_path("__cache__/Stats.txt"), "r") 
      file.close()
      
    # If "Stats.txt" doesn't exist we make one
    except FileNotFoundError:     
      file = open(self.resource_path("__cache__/Stats.txt"), "w")
      path = self.ReadPath()
      folder_names = os.listdir(path)

      # Checks each folder for how many seasons and episodes it has
      # Goes trough every file, except itself, __cache__ and empty folders.
      for i in folder_names: 
        if i not in self.Ignore_list and self.season_count(i) > 0:
          file.write(str(i) + "," + "1" + "," + "1")
          file.write('\n')

      file.close()

    # Checks if Bookmarks.txt exists and makes one if it doesnt
    # "Bookmarks.txt" contains your bookmarked episodes
    try:
      file = open(self.resource_path("__cache__/Bookmarks.txt"), "r") 
      file.close()
    except FileNotFoundError:
      file = open(self.resource_path("__cache__/Bookmarks.txt"), "w")
      file.close()

  # A Function that takes a series name
  # and returns the number of seasons
  # (The number of folders within the series folder.)
  def season_count(self, name): 
    path = self.ReadPath()
    path = str(path + "\\" + name + "\\")
    seasons = (os.listdir(path))
    return(len(seasons))


  # A Function that takes a series' season numbers
  # and returns the number of episodes in that season
  # (The number of items within the season folder.)
  def episode_count(self, name, season): 
    path = self.ReadPath()
    path = str(path + "\\" + name + "\\" + "Season " + str(season) + "\\")
    episodes = len(os.listdir(path))
    return(episodes)


  # Reads "path.txt" and returns the directiory path
  def ReadPath(self): 
    file = open(self.resource_path("__cache__/Path.txt"), 'r')
    path_text = csv.reader(file)
    Array = []

    for i in path_text:
      Array.append(i)
    return_file = Array[0]

    file.close()
    return(''.join(return_file))


  # A Function that reads the "Stats.txt"
  # and returns the data within as a array
  def ReadStats(self): 
    file = open(self.resource_path("__cache__/Stats.txt"), 'r')
    text_temp = csv.reader(file)
    Array = []

    for i in text_temp:
      Array.append(i)
    file.close()
    return(Array)


  # A Function that reads the "Names.txt"
  # and returns the data within as a array
  def ReadNames(self): 
    file = open(self.resource_path("__cache__/Names.txt"), 'r')
    text_temp = csv.reader(file)
    Array = []

    for i in text_temp:
      Array.append(i)
    file.close()
    return(Array)


  # A Function that reads the "Bookmarks.txt"
  # and returns the data within as a array
  def ReadFavs(self):
    file = open(self.resource_path("__cache__/Bookmarks.txt"), 'r')
    text_temp = csv.reader(file)
    Array = []

    for i in text_temp:
      Array.append(i)
    file.close()
    return(Array)


  # "Names.txt" is remade each launch of the app.
  # This func takes the new data and compares it to the 
  # saved data and removes items that are no longer present.
  def Update_Stats(self): 
    file1 = open(self.resource_path("__cache__/Stats.txt"), "r")
    file2 = open(self.resource_path("__cache__/Names.txt"), "r")

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

    file = open(self.resource_path('__cache__/Stats.txt'), 'w')
    
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


  # For saving new data
  def save_bookmarks(self, List):
    
    # First we sort the list
    #List = sorted(List, key=lambda x: (x[0], x[1], x[2]))

    # Then save
    try:
      file = open(self.resource_path("__cache__/Bookmarks.txt"), "w")
      for i in range(len(List)):
        file.write(str(List[i][0]) + "," + str(List[i][1]) + "," + str(List[i][2]))
        file.write("\n")
      file.close()

    except Exception as e:
      print("Error while saving:\n", "    ", e)


  # Saves new location data to Stats.txt
  def save_stats(self, List):
    try:
      file = open(self.resource_path("__cache__/Stats.txt"), "w")
      for i in range(len(List)):
        file.write(str(List[i][0]) + "," + str(List[i][1]) + "," + str(List[i][2]))
        file.write("\n")
      file.close()

    except Exception as e:
      print("Error while saving:\n", "    ", e)

