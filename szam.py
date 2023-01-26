import random


def elso():
    szam = random.randint(1, 50)
    print("I/A:\n\tA generált szám: {}".format(szam))
    print("I/B:\n\t", end="")
    if (szam % 3 == 0 and szam % 5 == 0):
        print("A szám öttel és hárommal is osztható!")
    elif (szam % 5 == 0):
        print("A szám öttel osztható!")
    elif (szam % 3 == 0):
        print("A szám hárommal  osztható!")
    else:
        print("")


