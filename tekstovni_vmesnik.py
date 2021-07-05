import model

def izpis_igre(igra):
    s = igra.sirina
    tekst = "\n" + (3 * s + 4) * "%" + "\n"
    for sez in igra.tabela:
        tekst += '   '
        for znak in sez:
            tekst += f'{znak}  '
        tekst.strip(' ')
        tekst += '\n'
    tekst += (3 * s + 4) * "%" + "\n"
    tekst += f"Na potezi je igralec {igra.kdo_je_na_vrsti}.\n"
    return tekst

def izpis_izida(igra):
    if igra.izid() == model.IGRALEC_1:
        return "Zmagal je igralec 1."
    elif igra.izid() == model.IGRALEC_2:
        return "Zmagal je igralec 2."
    elif igra.izid() == model.NEODLOCENO:
        return "Izenačeno je."

def zahtevaj_potezo(igra):
    niz = input(f"Vnesite število od 1 do {igra.sirina}:")
    if niz.isnumeric() and len(niz) > 0:
        st = int(niz)
        if st in range(1, igra.sirina + 1) and st not in igra.polni_stolpci():
            return st
    while True:
        niz = input(f"To pa ni možno. Izberite število od 1 do {igra.sirina}:")
        if niz.isnumeric() and len(niz) > 0:
            st = int(niz)
            if st in range(1, igra.sirina + 1) and st not in igra.polni_stolpci():
                return st

def nastavi_igro():
    s, v = 0, 0
    while True:
        s = input("Vnesite širino plošče. Širina naj bo vsaj 4. Ali pa pritisnite samo tipko Enter za standardno širino:")
        if len(s) == 0:
            s = model.SIRINA
            break
        elif s.isnumeric():
            s = int(s)
            if s >= 4:
                break
    while True:
        v = input("Vnesite višino plošče. Višina naj bo vsaj 4. Ali pa pritisnite samo tipko Enter za standardno višino:")
        if len(v) == 0:
            v = model.VISINA
            break
        elif v.isnumeric():
            v = int(v)
            if v >= 4:
                break
    return [s, v]

def pozeni_vmesnik():
    sez = nastavi_igro()
    igra = model.nova_igra(sez[0], sez[1])
    print(izpis_igre(igra))
    while True:
        poteza = zahtevaj_potezo(igra)
        igra.igraj(poteza)
        print(izpis_igre(igra))
        stanje = igra.izid()
        if stanje != model.NI_SE_KONEC:
            print(izpis_izida(igra))
            break

pozeni_vmesnik()