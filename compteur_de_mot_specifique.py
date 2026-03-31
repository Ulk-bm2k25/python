"""print("===Word encounter====")
text = input("Enter your sentence/text here :kk\n").lower()
word = input("Enter the word you want to know how many time repeated : ")
loword = word.lower()
t = 0
words = text.split()
for w in words:
    
    if w == loword:
        t += 1
print(f"'{word}' is repeated {t} times in the text")"""


""" We can simply use the function count()
t = text.count(loword)
"""



