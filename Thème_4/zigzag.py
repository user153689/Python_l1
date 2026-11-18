debut = int(input("Numero de début : "))
fin = int(input("Numero de fin : "))
n = int(input("Nombre de z : "))

i = debut

while i <= fin:
    if i % 2 == 0:
        print(i, "z" * n + "zigzag")
    else:
        print("z" * n + "zigzag", i)

    i = i + 1