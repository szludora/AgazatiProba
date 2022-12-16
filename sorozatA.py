import random


def sorozatA(db):

    """Írass ki a konzolra 13 páratlan számból álló véletlen számsorozatot [40,150]
    zárt intervallumon. A generált értékeket tárold lista adatszerkezetben. (3p)"""
    szamok = []
    szamsor = ""

    while len(szamok) < db:
        szam = int(random.random()*111)+40
        if szam % 2 != 0:
            szamok.append(szam)
            szamsor += str(szam) + "*   "

    print(f"{szamsor}\n")

    return ketjegyuek(szamok)


def ketjegyuek(lista):
    i = 0
    ketjegyu = 0

    while i < len(lista):
        szam = lista[i]
        if szam < 100 and szam > 9:
            ketjegyu += 1
        i += 1

    eredmeny = f"kétjegyűek száma: {ketjegyu}\n"
    print(eredmeny)

    f = open("ketjegyu.txt", "a")
    f.write(eredmeny)
    f.close()
    print("\n_________________________________________________VÉGE_________________________________________________\n")
