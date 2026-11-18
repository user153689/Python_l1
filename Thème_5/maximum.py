def maximum (x, y) :
    if x>=y :
        return  x
    else :
        return  y
if __name__=="__main__":
    x = float(input("x"))
    y = float(input("y"))
    print(maximum (x, y))