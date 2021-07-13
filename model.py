import random
import math

SIRINA = 7
VISINA = 6
ZETON_1 = 1
ZETON_2 = 2

IGRALEC_1 = "IGRALEC 1"
IGRALEC_2 = "IGRALEC 2"
NAKLJUCNO = "NAKLJUČNA POTEZA"
IZBIRA_NAKLJUCNO = "N"
RACUNALNIK = "RAČUNALNIK"
IZBIRA_RACUNALNIK = "R"
DVA_IGRALCA = "Drugo"

NI_SE_KONEC = "Igraj naprej."
NEODLOCENO = "Izenačeno je."

DOLZINA_ZA_ZMAGO = 4

def nova_prazna_tabela(sirina, visina):
    sez = []
    for i in range(visina):
        sez.append([])
        for _ in range(sirina):
            sez[i].append(0)
    return sez

class Igra:
    def __init__(self, sirina, visina, kdo_je_na_vrsti, ime_1, ime_2):
        self.sirina = sirina
        self.visina = visina
        self.tabela = nova_prazna_tabela(sirina, visina)
        self.kdo_je_na_vrsti = kdo_je_na_vrsti
        self.kdo_prvi = kdo_je_na_vrsti
        self.ime_1 = ime_1
        self.ime_2 = ime_2
    
    def zamenjaj_prvega(self):
        if self.kdo_prvi == self.ime_1:
            self.kdo_prvi = self.ime_2
        else:
            self.kdo_prvi = self.ime_1

    def zamenjaj_potezo(self):
        if self.kdo_je_na_vrsti == self.ime_1:
            self.kdo_je_na_vrsti = self.ime_2
        else:
            self.kdo_je_na_vrsti = self.ime_1

    def igraj(self, poteza):
        n = self.visina - 1
        vrstica = self.tabela[n]
        pozicija = vrstica[poteza]
        while pozicija != 0:
            n -= 1
            vrstica = self.tabela[n]
            pozicija = vrstica[poteza]
        if self.kdo_je_na_vrsti == self.ime_1:
            self.tabela[n][poteza] = ZETON_1
        else:
            self.tabela[n][poteza] = ZETON_2
        self.zamenjaj_potezo()

    def nakljucna_poteza(self):
        return random.choice(self.mozni_stolpci())

    def mozni_stolpci(self):
        zgornja_vrstica = self.tabela[0]
        sez = []
        for i in range(self.sirina):
            if zgornja_vrstica[i] == 0:
                sez.append(i)
        return sez
    
    def polna_tabela(self):
        return len(self.mozni_stolpci()) == 0

    def izid(self):
        t = self.tabela
        s = self.sirina
        v = self.visina
        # najprej preverimo pogoje za zmago
        # vodoravno
        for i in range(v):
            for j in range(s - 3):
                if t[i][j] == t[i][j + 1] == t[i][j + 2] == t[i][j + 3]:
                    if t[i][j] == ZETON_1:
                        return self.ime_1
                    elif t[i][j] == ZETON_2:
                        return self.ime_2
        # navpično
        for i in range(v - 3):
            for j in range(s):
                if t[i][j] == t[i + 1][j] == t[i + 2][j] == t[i + 3][j]:
                    if t[i][j] == ZETON_1:
                        return self.ime_1
                    elif t[i][j] == ZETON_2:
                        return self.ime_2
        # diagonale s pozitivnim smernim koeficientom
        for i in range(3, v):
            for j in range(s - 3):
                if t[i][j] == t[i - 1][j + 1] == t[i - 2][j + 2] == t[i - 3][j + 3]:
                    if t[i][j] == ZETON_1:
                        return self.ime_1
                    elif t[i][j] == ZETON_2:
                        return self.ime_2
        # diagonale z negativnim smernim koeficientom
        for i in range(v - 3):
            for j in range(s - 3):
                if t[i][j] == t[i + 1][j + 1] == t[i + 2][j + 2] == t[i + 3][j + 3]:
                    if t[i][j] == ZETON_1:
                        return self.ime_1
                    elif t[i][j] == ZETON_2:
                        return self.ime_2
        if self.polna_tabela():
            return NEODLOCENO
        else:
            return NI_SE_KONEC

    def kopiraj(self):
        novo = nova_igra(self.sirina, self.visina, self.kdo_je_na_vrsti, self.ime_1, self.ime_2)
        return novo
    
    def otroci(self):
        otroci = []
        for i in range(self.sirina):
            if i in self.mozni_stolpci():
                otrok = self.kopiraj()
                otrok.igraj(i)
                otroci.append((i, otrok))
        return otroci

    def oceni_stanje(self, zeton=ZETON_2):
        nasprotnik = ZETON_1
        if zeton == ZETON_1:
            nasprotnik = ZETON_2
        ocena = 0
        t = self.tabela
        s = self.sirina
        v = self.visina
        # vodoravno
        for i in range(v):
            for j in range(s - 3):
                # prištejemo oceno za žetone računalnika
                if t[i][j] == t[i][j + 1] == zeton:
                    ocena += 10
                if t[i][j] == t[i][j + 1] == t[i][j + 2] == zeton:
                    ocena += 100
                if t[i][j] == t[i][j + 1] == t[i][j + 2] == t[i][j + 3] == zeton:
                    ocena += 10000
                # odštejemo oceno za žetone igralca
                if t[i][j] == t[i][j + 1] == nasprotnik:
                    ocena -= 10
                if t[i][j] == t[i][j + 1] == t[i][j + 2] == nasprotnik:
                    ocena -= 100
                if t[i][j] == t[i][j + 1] == t[i][j + 2] == t[i][j + 3] == nasprotnik:
                    ocena -= 10000
        # navpično
        for i in range(v - 3):
            for j in range(s):
                # prištejemo oceno za žetone računalnika
                if t[i][j] == t[i + 1][j] == zeton:
                    ocena += 10
                if t[i][j] == t[i + 1][j] == t[i + 2][j] == zeton:
                    ocena += 100
                if t[i][j] == t[i + 1][j] == t[i + 2][j] == t[i + 3][j] == zeton:
                    ocena += 10000
                # odštejemo oceno za žetone igralca
                if t[i][j] == t[i + 1][j] == nasprotnik:
                    ocena -= 10
                if t[i][j] == t[i + 1][j] == t[i + 2][j] == nasprotnik:
                    ocena -= 100
                if t[i][j] == t[i + 1][j] == t[i + 2][j] == t[i + 3][j] == nasprotnik:
                    ocena -= 10000
        # diagonale s pozitivnim smernim koeficientom
        for i in range(3, v):
            for j in range(s - 3):
                if t[i][j] == t[i - 1][j + 1] == zeton:
                    ocena += 10
                if t[i][j] == t[i - 1][j + 1] == t[i - 2][j + 2] == zeton:
                    ocena += 100
                if t[i][j] == t[i - 1][j + 1] == t[i - 2][j + 2] == t[i - 3][j + 3] == zeton:
                    ocena += 10000
                if t[i][j] == t[i - 1][j + 1] == nasprotnik:
                    ocena -= 10
                if t[i][j] == t[i - 1][j + 1] == t[i - 2][j + 2] == nasprotnik:
                    ocena -= 100
                if t[i][j] == t[i - 1][j + 1] == t[i - 2][j + 2] == t[i - 3][j + 3] == nasprotnik:
                    ocena -= 10000
        # diagonale z negativnim smernim koeficientom
        for i in range(v - 3):
            for j in range(s - 3):
                if t[i][j] == t[i + 1][j + 1] == zeton:
                    ocena += 10
                if t[i][j] == t[i + 1][j + 1] == t[i + 2][j + 2] == zeton:
                    ocena += 100
                if t[i][j] == t[i + 1][j + 1] == t[i + 2][j + 2] == t[i + 3][j + 3] == zeton:
                    ocena += 10000
                if t[i][j] == t[i + 1][j + 1] == nasprotnik:
                    ocena -= 10
                if t[i][j] == t[i + 1][j + 1] == t[i + 2][j + 2] == nasprotnik:
                    ocena -= 100
                if t[i][j] == t[i + 1][j + 1] == t[i + 2][j + 2] == t[i + 3][j + 3] == nasprotnik:
                    ocena -= 10000
        return ocena

    def minimax(self, globina, maximizingPlayer, alfa, beta):
        izid = self.izid()
        otroci = self.otroci()
        if globina == 0 or izid != NI_SE_KONEC:
            if izid != NI_SE_KONEC:
                if izid == self.ime_1:
                    return (None, -1000000)
                elif izid == self.ime2:
                    return (None, 1000000)
                else:
                    return (None, 0)
            else:
                return (None, self.oceni_stanje(ZETON_2))
        if maximizingPlayer:
            naj_stolpec = self.nakljucna_poteza()
            naj_vrednost = -math.inf
            for otrok in otroci:
                stolpec, igra_otrok = otrok
                nova_globina = globina - 1
                _, nova_vrednost = igra_otrok.minimax(nova_globina, False, alfa, beta)
                if nova_vrednost > naj_vrednost:
                    naj_vrednost = nova_vrednost
                    naj_stolpec = stolpec
                alfa = max(alfa, naj_vrednost)
                if alfa >= beta:
                    break
            return (naj_stolpec, naj_vrednost)
        else:
            naj_stolpec = self.nakljucna_poteza()
            naj_vrednost = math.inf
            for otrok in otroci:
                stolpec, igra_otrok = otrok
                nova_globina = globina - 1
                _, nova_vrednost = igra_otrok.minimax(nova_globina, True, alfa, beta)
                if nova_vrednost < naj_vrednost:
                    naj_vrednost = nova_vrednost
                    naj_stolpec = stolpec
                beta = min(beta, naj_vrednost)
                if alfa >= beta:
                    break
            return (naj_stolpec, naj_vrednost)

    def poteza_racunalnika(self):
        stolpec, _ = self.minimax(5, True, -math.inf, math.inf)
        return stolpec

def nova_igra(s, v, kdo_je_na_vrsti, ime_1, ime_2):
    return Igra(s, v, kdo_je_na_vrsti, ime_1, ime_2)
