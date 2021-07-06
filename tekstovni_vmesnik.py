import model

PONOVNA_IGRA = "P"
IZHOD = "I"

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
    if igra.izid() == model.NI_SE_KONEC:
        tekst += f"Na potezi je {igra.kdo_je_na_vrsti}.\n"
    return tekst

def izpis_izida(igra):
    if igra.izid() == igra.ime_1:
        return f"Zmaga {igra.ime_1}."
    elif igra.izid() == igra.ime_2:
        return f"Zmaga {igra.ime_2}."
    elif igra.izid() == model.NEODLOCENO:
        return model.NEODLOCENO

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

def pridobi_imeni():
    ime_1 = input(f"Vnesite ime prvega igralca (privzeto ime je {model.IGRALEC_1}):")
    if ime_1 == "":
        ime_1 = model.IGRALEC_1
    ime_2 = input(f"Vnesite ime drugega igralca (privzeto ime je {model.IGRALEC_2}):")
    if ime_2 == "":
        ime_2 = model.IGRALEC_2
    return [ime_1, ime_2]

def ponudi_moznosti():
    tekst = f"""Ali želita igrati ponovno?\n
    {PONOVNA_IGRA}: Ponovna igra.
    {IZHOD}: Izhod.
    """
    return tekst

def zahtevaj_moznost():
    return input("Vnesite možnost:")

def izberi_ponovitev(kdo_prvi, imeni):
    print(ponudi_moznosti())
    izbira = zahtevaj_moznost().strip().upper()
    if izbira == PONOVNA_IGRA:
        sez = nastavi_igro()
        igra = model.nova_igra(sez[0], sez[1], kdo_prvi, imeni[0], imeni[1])
        return igra
    else:
        return IZHOD

def pozeni_vmesnik():
    imeni = pridobi_imeni()
    sez = nastavi_igro()
    igra = model.nova_igra(sez[0], sez[1], imeni[0], imeni[0], imeni[1])
    print(izpis_igre(igra))
    while True:
        poteza = zahtevaj_potezo(igra)
        igra.igraj(poteza)
        print(izpis_igre(igra))
        stanje = igra.izid()
        if stanje != model.NI_SE_KONEC:
            print(izpis_izida(igra))
            igra.zamenjaj_prvega()
            kdo_prvi = igra.kdo_prvi
            igra = izberi_ponovitev(kdo_prvi, imeni)
            if igra == IZHOD:
                break
            print(izpis_igre(igra))

pozeni_vmesnik()