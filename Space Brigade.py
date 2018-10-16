




                                    # # # # # # # # # # # # # # # # # # # # #
                                    #                                       #
                                    #   Name of Project:    Space Brigade   #
                                    #   Name of Auther:     Edward Hayden   #
                                    #   Start Date:         12/10/18        #
                                    #   End Date:           N/A             #
                                    #                                       #
                                    # # # # # # # # # # # # # # # # # # # # #






#   Modules:

import tkinter
import time
from os import system
import random
from random import randint

#   Variables:

Missed = False

Sheild = 100
Hp = 100
Credits = 100

EnemySheild = 0
EnemyHp = 0

Return = ""

BG_Colour = "#cee0e0"
FG_Colour = "#25468c"

AccentColour = "#7fd3f9"

Height = "800"
Width = "800"

Font = ("Monaco", "70")

FontSmall = ("Monaco", "40")


#   Battle Mechanic:

def BattleStart(EnemySheild1, EnemyHp1, Return1):

    global EnemySheild
    global EnemyHp
    global Sheild
    global Hp

    EnemySheild = EnemySheild1
    EnemyHp = EnemyHp1
    Return = Return1

    print("Battle Started:")
    print("    EnemySheild: "+str(EnemySheild))
    print("    EnemyHp: "+str(EnemyHp))

    MainText.configure(text = "Enemy aproaching sir, their sheild is at "+str(EnemySheild)+"%.")

    Button1.configure(text = "-Fire Phasers-", command = FirePhasers)
    Button2.configure(text = "-Fire Missiles-", command = Nothing)
    Button3.configure(text = "-Repair-", command = Nothing)

    
def FirePhasers():
    global Missed
    global EnemySheild
    global EnemyHp
    global Sheild
    global Hp
    print("Fired Phasers.")

    Hit = randint(1,10)

    if Hit == 9:
        print("Phasers Missed.")
        Missed = True
            
    else:
        print("Phaser Hit.")

        Missed = False
        Dmg = randint(8, 15)
        print("Phasers did "+str(Dmg)+" Damage.")
        if EnemySheild > 0:
            EnemySheild = EnemySheild - Dmg
        else:
            EnemyHp = EnemyHp - Dmg

    BattleMain()

def BattleMain():
    global EnemySheild
    global EnemyHp
    global Sheild
    global Hp

    print("Battle Main.")

    if Missed == True:
        MainText.configure(text = "We missed sir!")


    else:
        if EnemyHp > 0:
                
            if EnemySheild > 0:
                MainText.configure(text = "Postive hit sir, their sheild is at "+str(EnemySheild)+"%.")
            else:
                 MainText.configure(text = "Postive hit sir, their hull strength is at "+str(EnemyHp)+"%.")

            Button1.configure(text = "-------->", command = EnemyTurn)
            Button2.configure(text = "         ", command = Nothing)
            Button3.configure(text = "         ", command = Nothing)
        
                
        else:
            Credits = Credits + 20
                
            MainText.configure(text = "Enemy destroyed sir! [+20 Credits]")

            Button1.configure(text = "-------->", command = BattleEnd)
            Button2.configure(text = "         ", command = Nothing)
            Button3.configure(text = "         ", command = Nothing)

                      
    
def EnemyTurn():
    global Missed
    global EnemySheild
    global EnemyHp
    global Sheild
    global Hp

    print("Enemy Turn.")

        
    Hit = randint(1,7)

    if Hit == 6:
        print("Enemy Missed.")
        Missed = True
            
    else:
        print("Enemy Hit.")

        Missed = False
        Dmg = randint(8, 15)
        print("Enemy did "+str(Dmg)+" Damage.")
        if Sheild > 0:
            Sheild = Sheild - Dmg
        else:
            Hp = Hp - Dmg

    DamageReport()

def DamageReport():
    global Missed
    global EnemySheild
    global EnemyHp
    global Sheild
    global Hp

    print("Damage report.")

    if Missed == True:
        MainText.configure(text = "They missed sir!")


    else:
        if Hp > 0:
                
            if Sheild > 0:
                MainText.configure(text = "We're hit sir, our sheild is at "+str(Sheild)+"%.")
            else:
                MainText.configure(text = "We're hit sir, hull strength is at "+str(Hp)+"%.")

            Button1.configure(text = "-------->", command = Battle)
            Button2.configure(text = "         ", command = Nothing)
            Button3.configure(text = "         ", command = Nothing)
        
                
        else:                
            MainText.configure(text = "--==GAME OVER==--")

            Button1.configure(text = "-------->", command = Quit)
            Button2.configure(text = "         ", command = Nothing)
            Button3.configure(text = "         ", command = Nothing)


def Battle():
    global EnemySheild
    global EnemyHp
    global Sheild
    global Hp

    MainText.configure(text = "What do we do Captain?")

    Button1.configure(text = "-Fire Phasers-", command = FirePhasers)
    Button2.configure(text = "-Fire Missiles-", command = Nothing)
    Button3.configure(text = "-Repair-", command = Nothing)




def BattleEnd():
    global Return
    (Return)()


    
    






#   Miscellaneous:

def Nothing():
    print ("Nothing selected.")


def MinusHealth():
    global Hp
    global EnemyDmg
    global Sheild
    print ("Damage Taken.")
    
    if Sheild <= 0:
        if Hp <= 0:
            print("Game Over")
            MainMenu()
        else:
            Hp = Hp - EnemyDmg
            HealthBar.configure(text = "Sheilds: ["+str(Sheild)+"]    Health: ["+str(Hp)+"]")

    else:                               
        Sheild = Sheild - EnemyDmg
        HealthBar.configure(text = "Sheilds: ["+str(Sheild)+"]    Health: ["+str(Hp)+"]")
    

#   Story:


#       Menu:

def MainMenu():
    global Sheild
    global Hp
    global BG_Colour
    global FG_Colour
    global Font
    global FontSmall
    print ("Menu selected.")


    ExitButton = tkinter.Button(root, text = "[!Quit!]", bg = BG_Colour, fg = FG_Colour, font = FontSmall, command = Quit)


    HealthBar = tkinter.Label(root, text = "Sheilds: ["+str(Sheild)+"]    Health: ["+str(Hp)+"]", bg = AccentColour, fg = FG_Colour, font = FontSmall)


    InventoryButton = tkinter.Button(root, text = "[Item's]", bg = BG_Colour, fg = FG_Colour, font = FontSmall, command = Nothing)


    Spacer = tkinter.Label(root, text = "", bg = BG_Colour, fg = FG_Colour, font = Font)
    Spacer.grid(row = 1, column = 1)

    
    MainText = tkinter.Label(root, text = "--==Space Brigade==--", bg = BG_Colour, fg = FG_Colour, font = Font)

    Underline.configure(text = "--------------------", bg = BG_Colour, fg = FG_Colour, font = Font)

    Button1.configure(text = "Play", bg = BG_Colour, fg = FG_Colour, font = Font, command = Tutorial_1)
    Button2.configure(text = "Settings", bg = BG_Colour, fg = FG_Colour, font = Font, command = Settings)
    Button3.configure(text = "Quit", bg = BG_Colour, fg = FG_Colour, font = Font, command = Quit)

    Underline2.configure(text = "--------------------", bg = BG_Colour, fg = FG_Colour, font = Font)


#       Settings:

def Settings():
    print ("Settings selected.")

    MainText.configure(text = "--==Settings==--")

    Button1.configure(text = "UI Theme", command = Nothing)
    Button2.configure(text = "        ", command = MinusHealth)
    Button3.configure(text = "Back", command = MainMenu)


#       UI Theme:

def UI_Theme():
    print ("UI Theme was selected.")

    MainText.configure(text = "--==UI Theme==--")

    Button1.configure(text = "Coming Soon", command = Nothing)
    Button2.configure(text = "Coming Soon", command = Nothing)
    Button3.configure(text = "Back", command = MainMenu)


#       Quit:

def Quit():
    print ("Quit selected.")

    root.destroy()
    exit()


#   Tutorial:

def Tutorial_1():
    print ("Tutorial selected.")

    MainText.configure(text = "Welcome Captain, to basic training.", font = FontSmall)

    Button1.configure(text = "-------->", command = Tutorial_2)
    Button2.configure(text = "         ", command = Nothing)
    Button3.configure(text = "         ", command = Nothing)


def Tutorial_2():
    print ("Tutorial selected.")

    MainText.configure(text = "Now you've graduated from centrel command,")

    Button1.configure(text = "-------->", command = Tutorial_3)
    Button2.configure(text = "         ", command = Nothing)
    Button3.configure(text = "         ", command = Nothing)

def Tutorial_3():
    print ("Tutorial selected.")

    MainText.configure(text = "We need to make sure you know what your doing.")

    Button1.configure(text = "-------->", command = Tutorial_4)
    Button2.configure(text = "         ", command = Nothing)
    Button3.configure(text = "         ", command = Nothing)

def Tutorial_4():
    print ("Tutorial selected.")

    MainText.configure(text = "We've setup a training vessel, destroy it.")

    Button1.configure(text = "-Begin Battle-", command = BattleStart(100, 100, Tutorial_4))
    Button2.configure(text = "         ", command = Nothing)
    Button3.configure(text = "         ", command = Nothing)


#   Main Window:

root = tkinter.Tk()
root.configure(bg = BG_Colour)
root.geometry(Height+"x"+Width)
root.title("Space Brigade")


ExitButton = tkinter.Button(root, text = "[!Quit!]", bg = BG_Colour, fg = FG_Colour, font = FontSmall, command = Quit)
ExitButton.grid(row = 0, column = 0)


HealthBar = tkinter.Label(root, text = "Sheilds: ["+str(Sheild)+"]    Health: ["+str(Hp)+"]", bg = AccentColour, fg = FG_Colour, font = FontSmall)
HealthBar.grid(row = 0, column = 1)


InventoryButton = tkinter.Button(root, text = "[Item's]", bg = BG_Colour, fg = FG_Colour, font = FontSmall, command = Nothing)
InventoryButton.grid(row = 0, column = 2)


Spacer = tkinter.Label(root, text = "", bg = BG_Colour, fg = FG_Colour, font = Font)
Spacer.grid(row = 1, column = 1)


MainText = tkinter.Label(root, text = "--==Space Brigade==--", bg = BG_Colour, fg = FG_Colour, font = Font)
MainText.grid(row = 2, column = 0, columnspan = 3)


Underline = tkinter.Label(root, text = "--------------------", bg = BG_Colour, fg = FG_Colour, font = Font)
Underline.grid(row = 3, column = 1)


Button1 = tkinter.Button(root, text = "Play", bg = BG_Colour, fg = FG_Colour, font = Font, command = Tutorial_1)
Button1.grid(row = 4, column = 1)

Button2 = tkinter.Button(root, text = "Settings", bg = BG_Colour, fg = FG_Colour, font = Font, command = Settings)
Button2.grid(row = 5, column = 1)

Button3 = tkinter.Button(root, text = "Quit", bg = BG_Colour, fg = FG_Colour, font = Font, command = Quit)
Button3.grid(row = 6, column = 1)


Underline2 = tkinter.Label(root, text = "--------------------", bg = BG_Colour, fg = FG_Colour, font = Font)
Underline2.grid(row = 7, column = 1)



root.mainloop()

MainMenu()
