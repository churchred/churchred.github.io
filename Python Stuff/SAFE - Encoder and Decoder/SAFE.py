import os
import time
import csv

def StartupCheck():
    try:
        file = open("List.txt", "r") 
        file.close()
    except FileNotFoundError:
        pass        
        file = open("List.txt", "w")   
        file.close()

def Show(OLD_Text):
    os.system('CLS')
    file = open("List.txt", 'r')
    text_temp = csv.reader(file)
    Text_Liste = []
    temp = ""
    for row in text_temp:
        Text_Liste = Text_Liste + [row]
    file.close()
    
    Text = str(Text_Liste)
    print(OLD_Text)
    time.sleep(1)
    os.system('CLS')
    print(Text)
    time.sleep(1)
    menu()

def menu():
    os.system('CLS')
    Text_Liste = []
    OLD_Text = ""
    temp = ""
    
    file = open("List.txt", 'r')
    text_temp = csv.reader(file)
    for i in text_temp:
        Text_Liste = Text_Liste + [i]
    file.close()
    Text = str(Text_Liste)
    
    print("Welcome to S.A.F.E          Warning: Cannot Encode large texts without problem, nor can it handle rows.")
    print("1. Encode")
    print("2. Decode")
    print("")
    print(Text)
    print("")
    Text_Liste = []
    OLD_Text = ""
    temp = ""
    choice = input("§ ")

    if choice == "1":
        
        file = open("List.txt", 'r')
        text_temp = csv.reader(file)
        for i in text_temp:
            Text_Liste = Text_Liste + [i]
        file.close()
        Text = str(Text_Liste)
        
        y = 0
        for i in Text:
            if y != 0 and y != 1 and y != 2 and y != len(Text) and y != len(Text)-1 and y != len(Text)-2 and y != len(Text)-3:
                x = ord(i)
                x = x+1
                x = chr(x)
                temp = temp + x
            y += 1
            
        OLD_Text = Text
        file = open("List.txt", "w")   
        file.write(str(temp))
        file.close()
        Show(OLD_Text)
            
            
    elif choice == "2":

        file = open("List.txt", 'r')
        text_temp = csv.reader(file)
        for i in text_temp:
            Text_Liste = Text_Liste + [i]
        file.close()
        Text = str(Text_Liste)
        
        y = 0
        for i in Text:
            if y != 0 and y != 1 and y != 2 and y != len(Text) and y != len(Text)-1 and y != len(Text)-2 and y != len(Text)-3:
                x = ord(i)
                x = x-1
                x = chr(x)
                temp = temp + x
            y += 1
        OLD_Text = Text
        file = open("List.txt", "w")   
        file.write(str(temp))
        file.close()
        Show(OLD_Text)
        
    else:
        print("Input Error")
        time.sleep(1)
        menu()


def Chat():
    print("Welcome to S.A.F.E          Warning: Cannot Encode large texts without problem, nor can it handle rows.")
    print("1. Encode")
    print("2. Decode")
    print("")
    print(Text)
    print("")
    Text_Liste = []
    OLD_Text = ""
    temp = ""
    choice = input("§ ")

    if choice == "1":
        
        file = open("List.txt", 'r')
        text_temp = csv.reader(file)
        for i in text_temp:
            Text_Liste = Text_Liste + [i]
        file.close()
        Text = str(Text_Liste)
        
        y = 0
        for i in Text:
            if y != 0 and y != 1 and y != 2 and y != len(Text) and y != len(Text)-1 and y != len(Text)-2 and y != len(Text)-3:
                x = ord(i)
                x = x+1
                x = chr(x)
                temp = temp + x
            y += 1

            
            
    elif choice == "2":
        y = 0
        for i in Text:
            if y != 0 and y != 1 and y != 2 and y != len(Text) and y != len(Text)-1 and y != len(Text)-2 and y != len(Text)-3:
                x = ord(i)
                x = x-1
                x = chr(x)
                temp = temp + x
            y += 1
        
    else:
        print("Input Error")
        time.sleep(1)
        menu()
    


StartupCheck()
menu()
quit()
