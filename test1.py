# # import sys
# # print(sys.argv)

# # print('ok')

# # print("Hello")

# # # Exercice 1 : Trouver la somme de 12 + 5
# # print('Somme: ', 12 + 5)

# # #Exercice 2 créer une variable first_name avec votre prenom. Afficher Prenom
# # first_name = 'Amélie'
# # print('Bonjour', first_name)
# # #ou 
# # print('Bonjour' + first_name)
# # #ou 
# # res = ' '.join(['Bonjour', first_name])

# #__________________________________________________________________________________________________________________________
# #Exercice 3 : 
# # prenom = input("Veuillez saisir votre prénom : ")


# # nom = input("Veuillez saisir votre nom : ")


# # annee_naissance = input("Veuillez saisir votre année de naissance (AAAA) : ")

# # age = 2024 - annee_naissance  


# # print(f"Bonjour {prenom} {nom}, vous avez {age} ans.")


# #__________________________________________________________________________________________________________________________

# #Exercice 4 :

# # nombre = float(input("Entrez un nombre : "))

# # double = nombre * 2

# # print(f"Le double de {nombre} est {double}.")



# #__________________________________________________________________________________________________________________________

# #Exercice 6
# # Réaliser un programme qui va demander à l’utilisateur de saisir son
# # poids, et sa taille en cm puis calculer l’IMC pour l’afficher.
# # Voici la formule de l’IMC 
# # IMC = Poids / Taille2

# # poids = float(sys.argv[1]) #float(input("Entrez votre poids en kg : "))
# # taille = float(sys.argv[2])#float(input("Entrez votre taille en cm : "))

# # taille = taille / 100

# # imc = poids / (taille ** 2)

# # print(f"Votre IMC est de {imc:.2f}.")

# #Correction Exercice 6
# import sys # Utilisation de la librairie "sys"

# #print(sys.argv)
# # Utilisation des paramètres de la ligne de commande à la place de input()
# # poids = float(sys.argv[1]) #float(input("Veuillez saisir votre poids en kg : "))
# # taille_cm = float(sys.argv[2]) # float(input("Veuillez saisir votre taille en cm : "))
# # taille_m = taille_cm / 100
# # imc = poids / (taille_m ** 2)
# # print(f"Votre IMC est : {imc:.2f}, poid:{poids}kg, taille: {taille_m}m")


# #__________________________________________________________________________________________________________________________

# #Exercice 7
# # Demandez à l’utilisateur de saisir son PRENOM, puis affichez le dans
# # une boite (caractères ┌ ┐└ ┘─│)
# # Mettez le en vert sur fond bleu (voir “console ANSI color“)


# # Demander à l'utilisateur de saisir son prénom
# prenom = input("Veuillez saisir votre prénom : ")

# # Calculer la largeur de la boîte en fonction de la longueur du prénom
# largeur = len(prenom)

# # Afficher le cadre adapté
# print("┌" + "─" * largeur + "┐")
# print(f"│\033[1;34;42m{prenom}\033[0m│")
# print("└" + "─" * largeur + "┘")

# #__________________________________________________________________________________________________________________________

# #  Exercice 8
# # Demandez une liste de mots (séparés par des espaces) puis affichez
# # cette liste en séparant les mots par des ‘/’

# # Demander une liste de mots à l'utilisateur
# mots = input("Veuillez entrer une liste de mots séparés par des espaces : ")

# # Transformer la chaîne en liste de mots
# liste_mots = mots.split()  # Découpe la chaîne en utilisant les espaces comme séparateurs

# # Rejoindre les mots avec '/'
# resultat = "/".join(liste_mots)

# # Afficher le résultat
# print("Liste avec des '/':", resultat)



# #__________________________________________________________________________________________________________________________

# #Exercice 9

# # Demander trois nombres à l'utilisateur
# nombre1 = float(input("Entrez le premier nombre : "))
# nombre2 = float(input("Entrez le deuxième nombre : "))
# nombre3 = float(input("Entrez le troisième nombre : "))

# # Calculer la moyenne
# moyenne = (nombre1 + nombre2 + nombre3) / 3

# # Afficher la moyenne
# print(f"La moyenne des trois nombres est : {moyenne:.2f}")

# #__________________________________________________________________________________________________________________________

# # Exercice 15
# # Demandez à l'utilisateur d'entrer un montant HT (hors taxes) et le
# # taux de TVA en pourcentage. Calculez et affichez le montant TTC
# # (toutes taxes comprises).

# montant_ht = float(input("Entrez le montant HT (hors taxes) : "))

# taux_tva_reduit = 5.5
# taux_tva_intermediaire = 10
# taux_tva = 20

# montant_ttc_reduit = montant_ht * (1 + taux_tva_reduit / 100)
# montant_ttc_intermediaire = montant_ht * (1 + taux_tva_intermediaire / 100)
# montant_ttc = montant_ht * (1 + taux_tva / 100)

# print(f"Le montant TTC avec une TVA réduite de {taux_tva_reduit}% est : {montant_ttc_reduit:.2f} €")
# print(f"Le montant TTC avec une TVA intermédiaire de {taux_tva_intermediaire}% est : {montant_ttc_intermediaire:.2f} €")
# print(f"Le montant TTC (toutes taxes comprises) est : {montant_ttc:.2f} €")

# #__________________________________________________________________________________________________________________________
# # Exercice 16
# # Demandez à l'utilisateur d'entrer un nombre puis:
# # un programme qui affiche le nombre de fois qu'il y a un chiffre 2 dedans

# #utiliser une regex avec ^2 pour supprimer tout sauf le 2

# #__________________________________________________________________________________________________________________________
# # Exercice 20
# # Écrivez un programme Python qui demande à l'utilisateur de saisir le rayon d'un cercle,
# # puis calcule et affiche l'aire du cercle et la longueur du périmètre
# import math
# r = float(input("Rayon : "))
# print(f"r={r:.2f}, Diamètre: {math.pi*2*r:.2f}, S={math.pi*r*r:.2f}")

# #__________________________________________________________________________________________________________________________
# # Exercice 21
# # Créez un programme qui vérifie si un mot de passe répond aux exigences suivantes :
# # Au moins 8 caractères de long.
# # Contient au moins une lettre majuscule et une lettre minuscule.
# # Contient au moins un chiffre.
# # Contient au moins un caractère spécial : !@#$%^&*()_+[]{}|:;"'<>,.?/

# import re

# # Fonction pour vérifier les exigences du mot de passe
# def verifier_mot_de_passe(mot_de_passe):
#     # Vérifier la longueur minimale
#     if len(mot_de_passe) < 8:
#         return "Le mot de passe doit contenir au moins 8 caractères."
    
#     # Vérifier la présence d'au moins une lettre majuscule
#     if not re.search(r"[A-Z]", mot_de_passe):
#         return "Le mot de passe doit contenir au moins une lettre majuscule."
    
#     # Vérifier la présence d'au moins une lettre minuscule
#     if not re.search(r"[a-z]", mot_de_passe):
#         return "Le mot de passe doit contenir au moins une lettre minuscule."
    
#     # Vérifier la présence d'au moins un chiffre
#     if not re.search(r"[0-9]", mot_de_passe):
#         return "Le mot de passe doit contenir au moins un chiffre."
    
#     # Vérifier la présence d'au moins un caractère spécial
#     if not re.search(r"[!@#$%^&*()_+\[\]{}|:;\"'<>,.?/]", mot_de_passe):
#         return "Le mot de passe doit contenir au moins un caractère spécial."
    
#     # Si toutes les conditions sont remplies
#     return "Le mot de passe est valide."

# # Demander à l'utilisateur de saisir un mot de passe
# mot_de_passe = input("Veuillez entrer un mot de passe : ")

# # Vérifier le mot de passe et afficher le résultat
# resultat = verifier_mot_de_passe(mot_de_passe)
# print(resultat)


# #__________________________________________________________________________________________________________________________

# #Exercice 22
# # users = ["bob", "alice", "bill", "karim"]
# # banned_users = ["elon"]
# # Je veux le message "All users are valid." si tous les users ne sont pas dans banned_users

# t = True
# users = ["bob", "alice", "bill", "karim"]
# banned_users = ["elon"]
# for user in users:
#     if user in banned_users:
#         print(f"{user} is a banned used !")
#         t = False
#         break
# if t: 
#     print("All users are valid.") 
    

#__________________________________________________________________________________________________________________________
#Exercice 23

# Écrivez un programme qui demande à l'utilisateur un nombre entier positif et calcule la somme de ses chiffres.
# Ex: 1234 → 10 car 1 + 2 + 3 + 4 = 10


# nombre = input("Entrez un nombre entier positif : ")

# if not nombre.isdigit():
#     print("Veuillez entrer un nombre entier positif.")
# else:
#     somme = sum(int(chiffre) for chiffre in nombre)
    
#     print(f"La somme des chiffres de {nombre} est : {somme}")
    
# OU 

# nombre = input("Entrez un nombre entier positif : ")

# somme = 0

# for chiffre in nombre:
#     somme += int(chiffre)

# print(f"La somme des chiffres de {nombre} est {somme}")
#__________________________________________________________________________________________________________________________

#Exercice 24
# # Écrivez un programme qui affiche tous les nombres pairs de 1 à 100 en utilisant une boucle.

# for nombre in range(2, 101, 2):
#     print(nombre)
    
#__________________________________________________________________________________________________________________________

# Exercice 25:
# Écrivez un programme qui demande à l'utilisateur de saisir une phrase,
# puis compte et affiche le nombre de voyelles (a, e, i, o, u) dans la
# phrase.

# phrase = input("Veuillez saisir une phrase: ")

# voyelles = "aeiouAEIOU"
# compteur = 0

# for lettre in phrase:
#     if lettre in voyelles:
#         compteur += 1

# print(f"Le nombre de voyelles dans la phrase est: {compteur}")

#__________________________________________________________________________________________________________________________
# Exercice :
# Écrivez un programme qui demande à l'utilisateur un nombre entier
# positif et calcule sa factorielle. La factorielle de n (notée n!) est
# le produit de tous les entiers de 1 à n. Par exemple, 5! = 5 × 4 × 3 × 2 x 1

# import sys
# '''
# Calcul de factorielle passé en parametre
# '''
# param = sys.argv[1]

# if param.isdigit():
#     N=int(param)
#     print('ok, N=', N)
#     acc=1
#     for i in range(1, N+1):
#         acc *= i
#     print(f'{N}! = {acc}')

# else:
#     print('Il faut un chiffre !')

#__________________________________________________________________________________________________________________________

# Exercice :
# Écrivez un programme qui génère les n premiers termes de la suite de
# Fibonacci. La suite de Fibonacci commence par 0 et 1, puis chaque
# terme suivant est la somme des deux termes précédents. Par exemple, si
# l'utilisateur entre n = 5, le programme doit afficher la suite : 0, 1, 1, 2, 3

# # Demander à l'utilisateur de saisir le nombre de termes de la suite de Fibonacci à afficher
# n = int(input("Entrez le nombre de termes de la suite de Fibonacci que vous voulez afficher : "))

# # Initialisation des deux premiers termes de la suite
# a, b = 0, 1

# # Si n est supérieur ou égal à 1, afficher le premier terme
# if n >= 1:
#     print(a, end=" ")

# # Si n est supérieur ou égal à 2, afficher le deuxième terme
# if n >= 2:
#     print(b, end=" ")

# # Utiliser une boucle pour générer les autres termes à partir du troisième
# for i in range(3, n + 1):
# #     c = a + b
# #     print(c, end=" ")
# #     a, b = b, c  # Mettre à jour a et b pour les termes suivants

# #__________________________________________________________________________________________________________________________
# # Écrivez un programme qui calcule le plus grand diviseur commun (PGCD) de deux nombres donnés par l'utilisateur en utilisant l'algorithme
# # d'Euclide. Pareil avec le PPCM !

# # a = int(input('veuillez saisir un nombre A: '))
# # b = int(input('veuillez saisir un nombre B: '))

# # a_ini = a
# # b_ini = b

# # while not (a == b):
# #     vmin=min(a, b)
# #     vmax=max(a, b)
# #     a=vmin # on garde la valeur la plus petite
# #     b=vmax-vmin # la différence

# # pgcd = a
# # ppcm = a_ini * b_ini / pgcd
# # print(f"A={a_ini}, B={b_ini} : PGCD={pgcd} PPCM={ppcm}")

# #__________________________________________________________________________________________________________________________

# # exercice:
# # Vérification de nombres premiers : Écrivez une fonction en Python qui vérifie si un nombre donné est premier ou non.
# import math 
# n = int(input('veuillez saisir un nombre : '))

# limit = int(math.sqrt(n))+1

# for D in range(2, limit):
#     r = n % D
#     print( D, 'reste', r)
#     if r == 0:
#         print(f"{D} divise {n}")
#         break
# else:
#     print(f"{n} est un nombre premier")

# # Avec optimisation :
# import math

# N = int(input('veuillez saisir un nombre : '))

# # on va tester que les diviseurs jusqu'à sqrt(N) (racine carré)
# limit = int(math.sqrt(N))+1

# # Est-ce que N divisible par 2 ?
# if N % 2 == 0:
#     print('N divisible par 2 !!!')
#     quit()

# # On teste que les nombres impair : 3, 5, 7, ......... -> sqrt(N)
# for D in range(3, limit, 2):
#     r = N % D
#     #print(D, 'reste', r)
#     if r == 0:
#         # D divise N !!!
#         print(f'{D} divise {N}, il est pas premier !')
#         break

# else:
#     print(f"{N} est premier !!!")

# #__________________________________________________________________________________________________________________________
# # Exercice 30
# Exercice : 
# Génération de nombres premiers : Écrivez une fonction qui génère tous
# les nombres premiers jusqu'à un nombre donné, en utilisant
# l'algorithme du crible d'Ératosthène.
# N = int(input('veuillez saisir un nombre : '))

# tbl = [True for i in range(N+1)]

# idx = 2

# while True:
#     crible = list(range(idx, N+1, idx))
#     #print(f"crible {idx} : {crible}")
#     for i in crible:
#         tbl[i] = False
#     #print(tbl)

#     # recherche du prochain index à True
#     i=idx+1
#     if i>=N: break
#     while tbl[i]==False:
#         if i>=N: quit()
#         i+=1
#     print(f'nbre: {i}')
#     idx = i

    #print('----------------------------------------')
    
    
#__________________________________________________________________________________________________________________________
# # Exercice 31

#Ecrire une fonction qui fait un tirage aléatoire d'étudiant.


import random


etudiants = [
    "BENOIST Amélie", "DE MATOS Anna", "DESSIS Bryan", "DIDE Florian",
    "DZELLAT KODIA Dassise", "JARRY Sullivan", "JORGE OLIVEIRA Théo",
    "KEBBI Ghilas", "MARQUENTIN DARDOUILLET Rémy", "OCAL Ozkan",
    "PARESCHI Thomas", "SCHNABEL Florian"
]

etudiant_tire = random.choice(etudiants)
