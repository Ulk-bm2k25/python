print("===Word encounter====")
text = input("Enter your sentence/text here :\n").lower()
word = input("Enter the word you want to know how many time repeated : ")
loword = word.lower()
t = 0
words = text.split() #split() pour éclater les mots c'est à dire chaque groupe de caractère séparé par un espace sera écarté à part et mis dans une liste

for w in words:
    
    if w == loword:
        t += 1
print(f"'{word}' is repeated {t} times in the text")






