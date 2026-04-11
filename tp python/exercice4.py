print("***SOMME DES N PREMIERS ENTIERS***")

#Récupération du n
n = int(input("Entrez un nombre entier :"))

#Condition de validité
if n < 0 or n % 1 != 0 :
    print("Erreur")

#code proprement dit
somme = 0
for i in range(n+1):
    somme += i

#Affichage du résultat
print (f"La somme des {n} premiers entiers est {somme}")