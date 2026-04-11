print("RESOLUTION D'EQUATION DU SECOND DEGRE")

def _discr(a, b, c):
    return b**2 - 4 * a * c 

a = float(input("Entrez le a : "))
b = float(input("Entrez le b : "))
c = float(input("Entrez le c : "))


delta = _discr(a, b, c)

if delta < 0:
    print("L'équation n'a pas de solution réelle")
elif delta == 0 :
    x0 = -b / (2 * a)
    print(f"L'équation admet une solution double {x0 = }")
else :
    x1 = (-b - delta ** .5) / (2 * a)
    x2 = (-b + delta ** .5) / (2 * a)
    
    print(f"Léquation admet deux solutions réelles : {x1 = : < 10} et {x2 = : > 10}")

