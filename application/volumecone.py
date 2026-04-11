print('===Calcul du volume du cône===')

def _volcone(r, h, pi = 3.14):
    return (pi * r**2 * h) / 3

r = float(input("Entrez le rayon du cône : "))
h = float(input("Entrez sa hauteur : "))
v = _volcone(r, h)
print(v)