print('====Semaine en jour====')
n = int(input("Combien de semaines? : "))
j = n * 7 
m = j // 30
mm = j % 30

print(f"{n} semaines font {m} mois et {mm} jours")