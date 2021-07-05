SIRINA = 7
VISINA = 6

IGRALEC_1 = 1
IGRALEC_2 = 2
NI_SE_KONEC = "D"
NEODLOCENO = "N"

def nova_prazna_tabela(sirina, visina):
    sez = []
    for i in range(visina):
        sez.append([])
        for _ in range(sirina):
            sez[i].append(0)
    return sez

class Igra:
    def __init__(self, sirina, visina, kdo_je_na_vrsti):
        self.sirina = sirina
        self.visina = visina
        self.tabela = nova_prazna_tabela(sirina, visina)
        self.kdo_je_na_vrsti = kdo_je_na_vrsti
        self.kdo_prvi = kdo_je_na_vrsti
    
    def zamenjaj_prvega(self):
        if self.kdo_prvi == IGRALEC_1:
            self.kdo_prvi = IGRALEC_2
        else:
            self.kdo_prvi = IGRALEC_1

    def zamenjaj_potezo(self):
        if self.kdo_je_na_vrsti == IGRALEC_1:
            self.kdo_je_na_vrsti = IGRALEC_2
        else:
            self.kdo_je_na_vrsti = IGRALEC_1
    
    def igraj(self, poteza):
        poteza -= 1
        n = self.visina - 1
        while self.tabela[n][poteza] != 0:
            n -= 1
        self.tabela[n][poteza] = self.kdo_je_na_vrsti
        self.zamenjaj_potezo()
    
    def poln_stolpec(self, poteza):
        return self.tabela[0][poteza - 1] != 0

    def polni_stolpci(self):
        sez = []
        for i in range(self.sirina):
            if self.tabela[0][i] != 0:
                sez.append(i + 1)
        return sez
    
    def polna_tabela(self):
        return len(self.polni_stolpci()) == self.sirina

    def izid(self):
        t = self.tabela
        s = self.sirina
        v = self.visina
        # najprej preverimo pogoje za zmago
        # vodoravno
        for i in range(v):
            for j in range(s - 3):
                if t[i][j] == t[i][j + 1] == t[i][j + 2] == t[i][j + 3]:
                    if t[i][j] == IGRALEC_1:
                        return IGRALEC_1
                    elif t[i][j] == IGRALEC_2:
                        return IGRALEC_2
        # navpično
        for i in range(v - 3):
            for j in range(s):
                if t[i][j] == t[i + 1][j] == t[i + 2][j] == t[i + 3][j]:
                    if t[i][j] == IGRALEC_1:
                        return IGRALEC_1
                    elif t[i][j] == IGRALEC_2:
                        return IGRALEC_2
        # diagonale s pozitivnim smernim koeficientom
        for i in range(3, v):
            for j in range(s - 3):
                if t[i][j] == t[i - 1][j + 1] == t[i - 2][j + 2] == t[i - 3][j + 3]:
                    if t[i][j] == IGRALEC_1:
                        return IGRALEC_1
                    elif t[i][j] == IGRALEC_2:
                        return IGRALEC_2
        # diagonale z negativnim smernim koeficientom
        for i in range(v - 3):
            for j in range(s - 3):
                if t[i][j] == t[i + 1][j + 1] == t[i + 2][j + 2] == t[i + 3][j + 3]:
                    if t[i][j] == IGRALEC_1:
                        return IGRALEC_1
                    elif t[i][j] == IGRALEC_2:
                        return IGRALEC_2
        if self.polna_tabela():
            return NEODLOCENO
        else:
            return NI_SE_KONEC

def nova_igra(s=SIRINA, v=VISINA, kdo_je_na_vrsti=IGRALEC_1):
    return Igra(s, v, kdo_je_na_vrsti)