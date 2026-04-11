def moy(note):
    return sum(note) / len(note)

moyenne = moy([13, 14, 15, 16, 17, 18, 19, 20, 20, 19, 18, 17, 16, 15, 14])
print(f"La moyenne de ces notes est {moyenne}")