import math
print('===Périmètre et aire===')

def _perimetre_(a, b, c):
    return a + b + c
def _aireTri_(a, b, c):
    d = _perimetre_(a, b, c) / 2
    arg = d * (d-a) * (d-b) * (d-c)
    if arg < 0:
        return "Triangle impossible"
    
    return math.sqrt(arg)

def final(a, b, c):    
    return _perimetre_(a, b, c), _aireTri_(a, b, c)
    
#test
p, s = final(2, 5, 9)
print(f"Exemple : Pour un triangle avec les cotes 2 , 5 et 9 on a : \nPerimetre {p = }\nSurface {s = }")

#Demande à l'utilisateur
x = [float(input(f'Entrez la {i+1}è cote de votre triangle : ')) for i in range(3)]

p, s = final(*x)

print(f"Les calculs donnent:\nPerimetre {p = }\nSurface {s = }")


