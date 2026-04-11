print("""===Fonction maximum====\n Cela prend en compte une série de 3 nombres 
      et renvoie le plus grand """)
def maximun(n1, n2, n3):
    list_max = [n1, n2, n3]
    list_max.sort()
    return list_max[-1]
    #à complèter par l'algorithme qui détermine le maximum des trois

#test 
max = maximun(2, 5, 4)

print(f"Par exemple maximum(2, 5, 4) est {max = }.\n")
x = {}
#Demande à l'utilisateur
for i in range(3):
    x[i] = int(input(f"Entrez le nombre {i + 1}: "))

max = maximun(x[0], x[1], x[2])

print(f"Le maximum est {max = }", flush= True)


