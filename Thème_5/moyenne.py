def moyenne_ponderee (note1, note2, coeff1, coeff2) :
    coeff = coeff1+coeff2
    return (note1*coeff1 + note2*coeff2) / coeff
if __name__=="__main__":
    print("Debut du prog. principal")