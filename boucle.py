#tuto pour les boucles avec Python
#boucle whiel
nb=7
i=0
while i<=10:
    print(nb*i)
    i+=1

# boucle for
string = "Chaîne de caractère"
for lettre in string:
    print(lettre)
#autre exemple
for lettre in string:
    if lettre in "AEYUIOaeyuio":
        print(lettre)
    else:
        print("*")

