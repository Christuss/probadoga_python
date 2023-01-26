import Gombak_1


def harmadik():
    fajl = open("gombak.txt", 'r', encoding="utf-8")
    sorok = fajl.readlines()
    index = 0
    while index < len(sorok):
        sor = Gombak_1.Gomba(sorok[index])
        print(sorok[index])
        index += 1
    return sorok

def gombak_szama(lista):
        print("III/A, B:\n\tA gombák száma: {}.".format(len(lista)))
