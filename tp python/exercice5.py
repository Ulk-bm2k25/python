print("NOMBRE PREMIER OU NON")
#Récuération
n = int(input("Entrez le nombre (entier naturel) dont on veut connaître la parité : "))
#Validité
if n < 0 or n % 1 != 0:
    print("Erreur")
    exit()

#code
if n == 2 :
    print("2 est un nombre premier")
elif n == 0 or n == 1:
    print("Ce n'est pas un nombre premier")
elif n != 2:
    for i in range(2, n):
        if n % i == 0 : 
            print(f"{n} n'est pas un nombre premier")
            break
    else:
        print(f"{n} est un nombre premier")
        




     
