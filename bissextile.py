# -*-coding:UTF8 -*
import os

annee = input("Saisissez une année : ") # On attend que l'utilisateur saisisse l'année qu'il désire tester
try:
    annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre
    assert annee < 0
    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        print("L'année saisie est bissextile.")
    else:
        print("L'année saisie n'est pas bissextile.")
except ValueError:
    print("Vous n'avez pas saisi un nombre")
except AssertionError:
    print("L'année saisie est inférieure à 0")
os.system("pause")