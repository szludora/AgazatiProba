def stadion():
    f = open("stadionok.txt", "r", encoding="utf-8")
    fejlec = f.readline()
    # print(fejlec)

    sorok = f.readlines()

    stadion = []
    varos = []
    csapatszam = []
    eloszor = []
    utoljara = []
    szeptemberi = 0
    v = ""

    i = 0
    while i < len(sorok):
        akt_sor = sorok[i].strip().split(";")
        stadion.append(akt_sor[0])
        varos.append(akt_sor[1])
        csapatszam.append(akt_sor[2])
        eloszor.append(akt_sor[3])
        utoljara.append(akt_sor[4])

        if varos[i] == "New York":
            v += str(stadion[i]) + " - " + str(csapatszam[i]) + "\n"

        elsomeccs = str(eloszor[i])
        if elsomeccs[6] == "9" and elsomeccs[5] == "0":
            szeptemberi += 1

        i += 1

    print(f"\nNew York-i stadionok, csapatszámaikkal:\n\n{v}")
    print(f"A csapatok darabszáma: {len(csapatszam)}\n")
    print(f"A szeptemberi kezdő mérkőzések száma: {szeptemberi} db.")
    f.close()
    print("\n_________________________________________________VÉGE_________________________________________________\n")

