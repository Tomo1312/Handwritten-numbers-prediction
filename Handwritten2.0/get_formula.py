def get_formula(lista_brojeva):
    #indexi na kojima su operandi
    k = [i for i, n in enumerate(lista_brojeva) if n > 9]
    #potencija
    p = 1
    broj1 = 0
    broj2 = 0
    broj = 0
    operand = ""
    brojevi = []
    
    for i in range(k[0]):
        if lista_brojeva[k[0]-i-1] == 0:
            p = p * 10
        else:
            broj1 = broj1 + lista_brojeva[k[0]-i-1]*p
            p = p * 10

    brojevi.append(broj1)

    if len(k) > 1:
            for i in range(1,len(k)):
                print(i)
                p = 1
                broj = 0
                l = k[i] - 1
                for j in range(k[i] - k[i-1] - 1):
                    if lista_brojeva[l] == 0:
                        p = p * 10
                    else:
                        broj = broj + lista_brojeva[l]*p
                        p = p * 10
                    l = l-1
                brojevi.append(broj)

    p = 10**(len(lista_brojeva) - k[len(k)-1] - 2)
    
    for i in range(len(lista_brojeva)-k[len(k)-1]-1):
        if lista_brojeva[k[len(k)-1] + i + 1] == 0:
            p = p / 10
        else :
            broj2 = broj2 + lista_brojeva[k[len(k)-1] + i + 1] * p
            p = p / 10
    broj2 = int(broj2)

    brojevi.append(broj2)
    zbroj = brojevi[0]
    j = 0
    operandi = []
    
    for i in range(1, len(brojevi)):
        if lista_brojeva[k[j]] == 10:
            zbroj = zbroj + brojevi[i]
            operand = "+"
            operandi.append(operand)
            j = j + 1
        else:
            zbroj = zbroj - brojevi[i]
            operand = "-"
            operandi.append(operand)
            j = j + 1
    
    print (brojevi)
    print (operandi,"\n\n\n")
    print(broj1,end = ' ')
    
    j = 0
    for i in range(1,len(brojevi)):
        print(operandi[j], brojevi[i],end = ' ')
        j = j+1
    print("=", zbroj)
