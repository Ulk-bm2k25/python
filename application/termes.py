print("termes de multiplication de 7")

li = [x * 7 for x in range(1, 20) ]
for x in li:
    if x % 3 == 0:
        print(f"{x}*", end=' ')
    else : print(x, end=" ")
    
