print('===Exercice1: Programme de calcul===')
def factoriel(n):
    if n == 0:
        return 1
    return n * factoriel(n-1)
    
def arrangement(n, p):
    return factoriel(n) / factoriel(n - p)
    # à complèter : nAp = fact(n) / (n-p)
def combinaison(n, p):
    return arrangement(n, p) / factoriel(p)
    pass# à complèter : nCp = ar(n,p) / fact(p) 
while True :
    choix = str(input("""Quelle opération voulez-vous faire?
            - ! pour factoriel
            - C pour combinaison
            - A pour arrangement
            \n """)).lower()
    match choix:
        case '!':
            
            n = float(input("Entrez le nombre: "))
            
            
            while n < 0 or n % 1 != 0:
                n = float(input("Entrez un nombre entier et positif: "))
            
            m = factoriel(n)
            print(f"{int(n)}! = {int(m) : ,} ")
            
            
        case 'a':
            while True :
                n = float(input("Entrez n : "))
                while n < 0 or n % 1 != 0:
                    n = float(input("Entrez un nombre entier et positif: "))
                p = float(input("Entrez le p (p < n) : "))
                while p < 0 or p % 1 != 0:
                    p = float(input("Entrez un nombre entier et positif: "))
                # à complèter
                if n < p :
                    print("n doit être supérieur à p")
                    continue
                r = arrangement(n, p)
            
                print(f"{int(n)}A{int(p)} = {int(r) : ,}")
                break
            

        case 'c':
            n = int(input("Entrez n : "))
            p = int(input("Entrez le p (p < n) : "))
            # à complèter
            result = combinaison(n, p)
            
            print(f"{n}C{p} = {int(result) : ,}")
        
        #case 'q':
            #break
        
        case _ :
            print("Entrez une opération correcte")
    continu = input('voulez-vous effectuer une autre opération?(O pour "oui" ou appuyer autre chose pour quitter) :').lower()
    reponse = ['oui','o']
    if continu in reponse :
        continue
    break