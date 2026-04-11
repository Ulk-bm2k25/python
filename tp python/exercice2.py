print("===Affichage de moyenne===")
liste_notes = []
for i in range(15):
    x = int(input(f"Entrez la {i+1}è note : "))
    liste_notes.append(x)
    

moy = sum(liste_notes) / 15


print(f"Cet élève a une moyenne de {moy : .3f} ")