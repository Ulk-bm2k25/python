print("===Word encounter====")
texte = input("Entrez votre mot/phrase/texte ici :\n")
t = 0
for i in texte:
    if i == ' ':
        t += 1
t += 1
if texte == "":
    print(f"Ton ne comporte aucun mot 🩻.")
if t == 2 :
    print(f"Ton texte comporte un seul mot.")
if t > 2:
    print(f"Ton texte comporte {t} mots")
