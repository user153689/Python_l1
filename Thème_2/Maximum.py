print ("Maximum de trois entiers")
un = int(input("1er entier= "))
deux = int(input("2eme entier= "))
trois = int(input("3eme entier= "))

if un>=deux and un>=trois :
    print ("Le maximum est :", un)
elif deux>=un and deux>=trois : 
    print("Le maximum est :", deux)
elif trois>=un and trois>=deux : 
    print("Le maximum est :", trois)