print("TABLE DE MULTIPLICATION")
n = int(input("Quel nombre souhaitez-vous avoir la table de multiplication? : "))
print(f'La table de multiplication de {n} est :\n')
for i in range(13):
    print(f"{n} x {i} = {n*i} ")
