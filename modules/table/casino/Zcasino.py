# -*-coding:UTF8 -*
import random
import math
import os

money = 1000
continue_play = True

while continue_play:
    print("Votre porte-monnaie dispose de",money,"$")
    choice = input("Choisir un chiffre pour miser :")
    nb_choice = int(choice)
    choice = input("Choisir la mise sur ce chiffre :")
    dollar_choice = int(choice)
    money = money - dollar_choice
    if(nb_choice == 0):
        color_choice="red"
    elif(nb_choice%2 == 0):
        color_choice = "red"
    else:
        color_choice = "black"

    nb_pull = random.randrange(50)
    print("Le nombre tiré est le suivant :",nb_pull)
    if(nb_pull == 0):
        color_pull="red"
    elif(nb_pull%2 == 0):
        color_pull = "red"
    else:
        color_pull = "black"

    if(nb_pull == nb_choice):
        print("Vous gagnez :",math.ceil(dollar_choice*3),"$")
        money = money + (dollar_choice*3)
    elif(color_pull == color_choice):
        print("Vous gagnez :",math.ceil(dollar_choice*2),"$")
        money = money + (dollar_choice*2)
    else:
        print("Vous avez perdu !")
    if money <= 0:
        continue_play=False
os.system("pause")



