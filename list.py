# -*-coding:UTF8 -*
# Tuto python pour les listes

#### Création ####
ma_liste = list() # création d'une liste vide
ma_liste = [] # méthode de création bis pour une liste
ma_liste = [0,1,2,3,4,5]# instantiation d'une liste non vide
ma_liste = [1,2.5,"une liste",[]]# avec objets de types différentrs

#### Sélection ####
ma_liste[0] # accède au premier élément de la liste
ma_liste[2] # le troisième élément
ma_liste[1] = "change" # 'remplacement du second élément

#### Ajouts ####
ma_liste.append(56)# Ajoute un élément supplémentaire à la fin de la liste
ma_liste.insert(1,"insertion") # insertion de la chaine de caractères en deuxième place de la liste
ma_liste2 = ["ext","ension"]
ma_liste.extend(ma_liste2) # concatenation de la liste 1 avec la liste 2 en fin de la ligne 1
ma_liste + ma_liste2# 2nd méthode de concaténation
ma_liste +=ma_liste2# 3rd méthode de concaténation

### Suppresion ###
del ma_liste[0]#Supprime le 1er élément de la liste (param = index dans la liste)
del ma_liste#Supprime la liste
ma_liste.remove(56)#Supprime les éléments égaux à 52 dans la liste !!!! Ne retire que la première occurence !!!!!


### Parcours de liste ####
ma_liste = ['a','b','c','d','e','f','g','h']
i=0
while i < len(ma_liste):
    print(ma_liste[i])
    i+= 1

#méthode plus performante

for elt in ma_liste:
    print(elt)

#Autre méthode plus performante
for i, elt in enumerate(ma_liste):
    print("A l'indice {} se trouve {}.".format(i,elt))

