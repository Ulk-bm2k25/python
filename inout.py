print("=== Cheking if in====")
texte = input("Entrez votre mot/phrase/texte ici :\n").lower()
mot = input("Entrez le caractère/mot à vérifier : ")
m = mot.lower()
if m in texte : 
    print(f"Oui, {mot} est dans le texte")
else : print(f"Non, '{mot}' n'est pas dans le texte")