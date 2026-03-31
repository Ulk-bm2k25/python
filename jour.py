print('====Jours en semaines====')
n = int(input("Combien de jour? : "))
j = n % 7
jj = n // 7
s = '' 
if j > 1 : s ='s'
if j == 0:
    print(f"{n} jours font {jj} semaines")
else : print(f"{n} jours font {jj} semaines et {j} jour{s}")