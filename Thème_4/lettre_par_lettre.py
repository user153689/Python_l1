max_lettres = int(input("Nombre max de lettres ? "))
mot = ""
i = 0

while i < max_lettres:
    lettre = input("Lettre : ")
    if lettre == "stop":
        break
    mot += lettre
    i += 1

print(mot)