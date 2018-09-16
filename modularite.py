#Création d'une fonction
def table_par_7():
    nb=7
    i=0
    while i<=10:
        print(nb*i)
        i+=1
#avec paramètre
def table(nb,max):
    i=0
    while i<=max:
        print(nb*i)
        i+=1

#avec paramètre dont max par defaut
def table_defaut(nb,max=10):
    ''' nb : le nombre pour afficher sa table
        max : le nombre d'occurence dans la table, en commençant par 0 (par defaut max = 10) '''
    i=0
    while i<=max:
        print(nb*i)
        i+=1

#avec une valeur retournée
def carre(nb):
    return nb*nb

#fonction lambda
f=lambda x: x*x

#fonction lambda a deux paramètres
l =lambda x,y:x*y

#import de module
import math
math.sqrt(18)

#changement du nom du module
import math as mathematique
mathematique.pi