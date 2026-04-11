print("Volume d'un parallélépipède")

def _volumepa(l, h, p):
    pass #Formule à chercher et à implémenter

largeur = float(input("La largeur? : "))
hauteur = float(input("La hauteur? : "))
profondeur = float(input("La profondeur : "))
if largeur < 0 or hauteur < 0 or profondeur < 0 : 
    print("Erreur!")
vol = _volumepa(largeur, hauteur, profondeur)

print(f"Volume = {vol : 4f}")
