n = int(input("n=? "))

if n < 0:
    print("La factorielle n'est pas definie pour les nombres négatifs.")
else:
    i = 1
    fact = 1

    while i <= n:
        fact = fact * i
        i = i + 1

    print("La factorielle de", n, "vaut", fact, ".")