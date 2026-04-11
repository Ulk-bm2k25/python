print("""°°°MAXimum ou MINimum°°°\n Cela prend en compte une série de nombres entiers entrés
      par l'utilisateur et leui demande s'il souhaiterait avoir le maximum, le minimum ou les deux \n""")
            #FROM SCRATCH
#maximum
'''def maximum(*args):
    list_max = [args]
    list_max.sort()
    return list_max[-1]

#minimum
def minimum(*args):
    list_min = [args]
    list_min.sort()
    return list_min[0]'''# ON peut s'en passer

#test 
Max = max(2, 4, 3, 8)
mini = min(14, 12, 85, 2, 5, 8)
print(f"Par exemple maximum(2, 4, 3, 8) est {Max = }, et minimum(14, 12, 85, 2, 5, 8) est {mini = }")

n = int(input("Combien de nombres contient votre série : "))

x = [int(input(f"Entrez le nombre {i+1} : ")) for i in range(n)]


Max = max(*x)
mini = min(*x)

choice = input("Que voulez-vous avoir? (M : pour le maximum et m :pour le maximum; O pour les deux): ")

match choice:
    case 'M':
        print(f"Le maximum est {Max = }.")
    case 'm':
        print(f"Le minimum est {mini = }")
    case 'O':
        print(f" {Max = } \n {mini = } ")
    case _ : 
        print("Opération incorrecte!")

#print(y)
#print(x)

#print





