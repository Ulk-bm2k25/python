import string
print("===letters encounter===")
text = input("Entrez votre mot/texte :\n")
l = 0
for i in text : 
    if i in string.ascii_letters:
        l += 1
print(f"Ton texte comporte {l} lettres.")