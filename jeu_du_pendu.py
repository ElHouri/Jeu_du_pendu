###Jeu du Pendu###

#Auteur : Eline Houri 
#Cours : MGA802
#Date : 23/05/23

#Bibliothèques utilisées
import random

#Titre
titre="Jeu du Pendu"
print('{:*^50}'.format(titre))   

#Message d'introduction 
introduction=''' Le jeu du pendu est un jeu de devinettes où vous devez trouver un mot en proposant des lettres.
 Vous avez un nombre limité de tentatives pour deviner le mot.
 Dans notre cas, vous avez 6 tentatives. 
 Chaque lettre correcte révèle sa position dans le mot, tandis que chaque lettre incorrecte vous rapproche de la défaite. 
 L'objectif est de deviner le mot avant d'être pendu.
 Veuillez noter que les mots selectionés ne contiennent pas d'accents ou de caractères spéciaux.
 '''
print(introduction)

#Instruction
titre_instruction="INSTRUCTION"
print('{:*^50}'.format(titre_instruction)) 

#Lecture du fichier texte contenant les mots
with open("mots_pendu.txt", 'r') as f:
# Lire le contenu du fichier et Transformer une chaine de caractères en une liste
    liste_mots= f.read().split()

# Fonction pour choisir un mot au hasard dans le fichier texte
def choisir_mot(liste_mots):
    return random.choice(liste_mots)


def afficher_mot_actuel(mot_aleatoire, lettres_trouvees):
    mot_affiche=""
    for lettre in mot_aleatoire:
        if lettre in lettres_trouvees:
                mot_affiche += lettre + " "
        else:
                mot_affiche += "_ "
    return mot_affiche.strip()


def jouer_au_pendu() :
    mot_aleatoire = choisir_mot(liste_mots)
    tentatives=6
    lettres_trouvees=[]

    while tentatives > 0 :
        lettre=input("Entre une lettre miniscule :")
        if lettre.isalpha():
            if lettre.islower():
                if lettre in mot_aleatoire:
                    print(f'Bravo vous avez deviné une bonne lettre ! ')
                    lettres_trouvees.append(lettre)
                    mot_actuel=afficher_mot_actuel(mot_aleatoire, lettres_trouvees)
                    print(mot_actuel)
                    if "_" not in mot_actuel:
                        print(f'Félicitation,  vous avez deviné le mot au complet : {mot_aleatoire}! Gagné')
                        return
                elif lettre in lettres_trouvees:
                    print(f'Vous avez déjà deviné la lettre {lettre} ! Essayer une autre !')
                else: 
                    tentatives-=1
                    print(f"La lettre {lettre} n'est pas dans le mot ! Il vous reste {tentatives} tentatives")
            else:   
                 print("Erreur : Veuillez entrer uniquement des lettres miniscules.")
        else :
             print("Erreur : Veuillez entrer uniquement des lettres alphabétiques.")   
    print(f"C'est perdu ! Le mot était {mot_aleatoire}")        
jouer_au_pendu()