# Ceci est un commentaire qui ne sera pas pris en compte lors de la compilation du programme en Python

# Afficher une chaîne de caractère 
# print('Salut, les amis de la Data !')

# mon_nom = "Rostaing"
# print(mon_nom)

# Afficher les caractères
# print("A")

# mon_caractere = "E"
# print(mon_caractere)

# mon_reel = 7.2
# print(mon_reel)

# a = 2
# b = 3

# # Faire la somme de deux entiers
# s = a + b

# print(s)

# x1 = int(input("Tape la valeur de x1: "))
# x2 = int(input("Tape la valeur de x2: "))

# somme = x1 // x2
# print(somme)


# if 2 > 5:
#     print("Vraie")
# else:
#     print("Faux")

# if 2 > 5:
#     print("Vraie")
# elif 2 > 5:
#     print("Faux")
# else:
#     print("Condition impossible")

# for i in range(1, 11, 2):
#     print("Bonjour!")

# i = 0
# while i < 5:
#     print("Bojour, les amis de la data !")
    
#     i = i + 1

# taille = 9
# pas = taille - 1
# pas = 9 - 1
# pas = 8
# t = [2, 5, 1, 0, 8, 7, 3, 6, 4]

# # print(t[8])
# for i in range(0, 9):
#     print(t[i])

# tab = [7, 20.5, "E", "Rostaing", True, False]
# # print(tab[4])

# j = 0
# while j < 6:
#     print(tab[j])

#     j = j  + 1
# def somme(x1, x2):
    
#     s = x1 + x2
#     print(s)
# # a = int(input("Tapez le premier entier: "))
# # b = int(input("Tapez le deuxième entier: "))
# resultat = somme(2, 5)
# print(resultat)

# def carre(nombre):

#     return nombre * nombre
# resultat = carre(2)
# print(resultat)

# valeur = "Rostaing AI"
# print(len(valeur))

# age = 12
# nom = "Rostaing"
# # text = "Mon nom est Rostaing, j'ai " + str(age)
# # print(text)

# text = f"Je m'appelle {nom}, j'ai {age} ans."
# print(text)

# Tuple

# t = (4, 5, 0, 2, 3)
# print(t[4])

# d = {"nom":"Rostaing", "age":10, "taille":1.80}
# print(d["age"])

# Set
# s = (("Rostaing", 10, 1.80))
# print(s)

# prenom = "rostaing"
# print(prenom.capitalize())

# try:
#     carre = 2 / 0
#     print(carre)
# except:
#     print("Erreur")
# else:
#     print("impossible")
# finally:
#     print("Fin programme")

# import math
# from math import cos, sin, pow, sqrt, tan, fabs

# racine_carree = sqrt(121)
# print(racine_carree)

# puissance = pow(4, 3)
# print(puissance)

# c = cos(0)
# print(c)

# s = sin(0)
# print(s)

# teta = 30
# t = sin(teta) / cos(teta)
# print(t)

# t = tan(teta)
# print(t)

# a = fabs(7)
# print(a)

# division =  lambda x: x / 2
# print(division(2))

# somme =  lambda x, y: x + y
# print(somme(2, 4))

# def nombre_pair(x):
#     if x % 2 == 0:
#         print(f"{x} est un nombre pair.")

#     else:
#         print(f"{x} est un nombre impair")
# nombre_pair(3)

# def maturite(age):
#     if age < 18:
#         print("Vous êtes mineur(e).")
#     else:
#         print("Vous êtes majeur(e).")

# a = int(input("Quel est votre âge: "))
# print(maturite(a))

# directeur = False
# if directeur:
#     print("Vous êtes directeur !")
# else:
#     print("Vous n'êtes pas directeur !")

# ET en python c'est and ou &
# temperature = 19
# if temperature >= 25:
#     print("chaud !")
# elif temperature >= 20 and temperature <= 24:
#     print("Normal")
# else:
#     print("Froid")

# di = {"nom":"Rostaing", "age":10, "taille":1.80, "fonction":"PDG"}
# for cle, valeur in di.items():
#     print(f"{cle} : {valeur}")

# tab = [100, 50, 65, 82, 23, 50, 65, 50]
# tab.sort()
# print(tab)
# tab.append(200)
# print(tab)
# print(tab.count(100))

# # tab.insert(4, 0)
# print(tab)
# tab.remove(82)
# print(tab)

# tab2 = tab.copy()
# print(tab2)

# tab.clear()
# print(tab)

# fruits = ["mangue", "orange", "banane"]
# voitures = ["BMW", "DavRos", "Volvo"]

# fruits.extend(voitures)
# print(fruits)

# fruits.reverse()
# print(fruits)

# for x in fruits:
#     print(x)

#     if x == "orange":
#         break

# for y in fruits:
#     if y == "orange":
#         continue
#     print(y)

# for x in fruits:
#     for y in voitures:
#         print(x, y)

# t = [2, 3, 7]
# l = [x*3 for x in t]
# print(l)

# nom  = "Rostaing"
# print(id(nom))
# print(hex(id(nom)))

# prenom = "rostaing"
# if prenom != "Rostaing":
#     print(f"Vous n'êtes pas {prenom}.")
# else:
#     print(f"Vous êtes {prenom}.")

# if prenom == "Rostaing":
#     print("Vraie")
# else:
#     print("Faux")

# if prenom is str("rostaing"):
#     print("Oui")
# else:
#     print("Non")

# if prenom is not str("rostaing"):
#     print("Oui")
# else:
#     print("Non")

# if prenom  not in str("rostaing"):
#     print("True")
# else:
#     print("False")

# age = 10
# nom = "Rostaing"
# c = "E"
# taille = 1.80
# is_ceo = True
# tab = [25, 78, 0, 4]
# tup = (45, 7, 8)
# d = {"nom":"Rostaing", "age":12}
# s = ((54, 0, 7))
# print(type(s))

# x = []
# if x is not None:
#     print("Pas vide")
# else:
#     print("Vide")

# k = [x for x in range(10) if x < 5]
# print(k)

# def dire_bonjour():
#     '''
#         Cette fonction dire_bonjour() permet de dire bonjour aux utilisateurs    
#     '''
#     print("Bojour, les amis de la data !")
# dire_bonjour()

# x = 10
# def age(y):
#     print(f"Bonjour, vous avez {y} ans")
# age(x)

# ou en python c'est or ou |
# Cas 1
# mon_prenom = "Rostaing"
# if mon_prenom == "Rostaing" or mon_prenom == "rostaing":
#     print("C'est moi !")
# else:
#     print("Ce n'est pas moi !")

# Cas 2
# mon_prenom = "Rostaing"
# if (mon_prenom == "Rostaing") | (mon_prenom == "rostaing"):
#     print("C'est moi !")
# else:
#     print("Ce n'est pas moi !")

# note = 10
# if note >= 10:
#     print("Validé !")
# else:
#     print("Pas validé !")

# a1, a2 = 10, 5: signiefie que a1 = 10 et a2 = 5
a1, a2 = 10.5, 5.5
difference = a1 - a2
print(difference)
