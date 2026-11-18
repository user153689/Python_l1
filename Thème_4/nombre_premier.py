n=int(input("Nombre : "))
est_premier= True
if n<2 :
    est_premier= False
i=2
while i*i<=n :
    if n% i == 0:
        est_premier= False
        break
    i+=1
if est_premier :
    print(n, "est premier.")
else :
    print(n, "n'est pas premier.")
