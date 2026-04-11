
import string
import random
import time
import sys


def generateur_mot_2_passe(longueur):
    lettres = string.ascii_letters #une constante venant de import string contenant l'alphabet
    chiffres = string.digits # lui contient les chiffres
    symboles = "!@#$%&"
    melange = lettres + chiffres
    
    s = input("voulez-vous des caractères spéciaux dans votre mot de passse? (O : oui et N : non ) : ").lower()
    reponse = ["oui", "o"]
    
    if s in reponse : melange = lettres + chiffres + symboles
    
    mot_de_passe = (random.choice(melange) for _ in range(longueur))
    return "".join(mot_de_passe) 
    
print("****Générateur de mot de passe****:")    
l = int(input("Indiquez la longueur de votre mdp à générer ( doit être supérieur ou égal à 8) : "))

while l < 8:
    l = int(input("longueur doit être supérieure ou égale à 8 : "))


