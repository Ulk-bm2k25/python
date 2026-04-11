scores = {"Alice": 85, "Bob": 92, "Chloé": 78}
admis = {nom : note for nom, note in scores.items() if note >= 80}

print(admis) 
#x = dict(input())