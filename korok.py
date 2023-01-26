def masodik():
    szamok = []
    index = 0
    print("II/A, B, C:\n\t",end="")
    while (index < 5):
        szam = int(input("\tKérek még {} számot![0, 120]".format(5-index)))
        szamok.append(szam)
        index += 1
    for i in range(len(szamok)-1):
        print(szamok[i],end=" : ")
    print(szamok[len(szamok)-1])
    return szamok

def elso_idos(lista):
    idosHely = 0
    index = 1
    while index < len(lista):
        if lista[index] > 70:
            idosHely = index
        index += 1
    idosHely = idosHely + 1
    return idosHely

def konzolra_ir(eredmeny):
    print("\tElső idős ember korának helye a listában: {}.".format(eredmeny))

def falj_ir(eredmeny):
    falj = open("oreg.txt", "w", encoding="utf-8")
    falj.write("\tElső idős ember korának helye a listában: {}.".format(eredmeny))