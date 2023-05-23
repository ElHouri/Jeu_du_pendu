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
 Les lettres sont en miniscule.
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

# Afficher les lettres devinees ou pas
def afficher_mot_actuel(mot_aleatoire, lettres_trouvees):
    mot_affiche=""
    # vérifie si la lettre est présente dans la liste 
    for lettre in mot_aleatoire:
        if lettre in lettres_trouvees:
                mot_affiche += lettre + " "
        else:
                mot_affiche += "_ "
    return mot_affiche.strip()


def jouer_au_pendu() :
    # chosis un mot dans le fichier text
    mot_aleatoire = choisir_mot(liste_mots)
    # nombre de tentatives
    tentatives=6
    # liste des lettres trouvées
    lettres_trouvees=[]

    # debut de la boucle limitee par le nombre de tentative
    while tentatives > 0 :
        # demande a l utilisateur d entrer une lettre
        lettre=input("Entre une lettre miniscule :")
        # Cas d'erreur
        assert lettre.isalpha(),"Erreur : Veuillez entrer uniquement des lettres alphabétiques."
        assert lettre.islower(),"Erreur : Veuillez entrer uniquement des lettres miniscules."
        
        # Si la lettre a deja ete trouvee
        if lettre in lettres_trouvees:
            print(f'Vous avez déjà deviné la lettre {lettre} ! Essayer une autre !')
        # Si la lettre est dans le mot cherche
        elif lettre in mot_aleatoire:
            print(f'Bravo vous avez deviné une bonne lettre ! ')
            lettres_trouvees.append(lettre)
            mot_actuel=afficher_mot_actuel(mot_aleatoire, lettres_trouvees)
            print(mot_actuel)
            # Si toutes les lettres on étaient déterminées
            if "_" not in mot_actuel:
                print(f'Félicitation,  vous avez deviné le mot au complet : {mot_aleatoire}! Gagné')
                return
        # la lettre n est pas dans le mot
        else: 
            tentatives-=1
            print(f"La lettre {lettre} n'est pas dans le mot ! Il vous reste {tentatives} tentatives")
    print(f"C'est perdu ! Le mot était {mot_aleatoire}")        
jouer_au_pendu()