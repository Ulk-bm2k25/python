import string
print("===letters printer==")
text = str(input("Enter your sentence/text : ")).lower()
l = 0
set_letters = []
letters = string.ascii_letters

for i in letters :
    if i in text:
        l += 1
        set_letters.append(i)
if len(set_letters) == 26:
    print(f"Your text contains all the letters of alphabet")

elif len(set_letters) < 26:
    print(f"Your text used {l} letters of alphabet which are : {" ".join(set_letters)}.")

