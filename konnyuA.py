def beker():
    szamok = []
    legkisebb_negyzet = 9999

    i = 0

    while len(szamok) < 3:
        szam = int(input(f"Adja meg a(z) {i+1}. negatív egész számot: "))
        while szam >= 0:
            szam = int(input(f"Adja meg újra a(z) {i+1}. negatív egész számot: "))
        szamok.append(szam)

        if szamok[i]**2 < legkisebb_negyzet:
            legkisebb_negyzet = szamok[i]**2
            hely = i+1

        i += 1
    print(f"\nA legkisebb négyzetű szám: {szamok[hely-1]}, megadási sorrendje: {hely}")
    print("\n_________________________________________________VÉGE_________________________________________________\n")
