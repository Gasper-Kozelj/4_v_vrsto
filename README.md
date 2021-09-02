# 4 v vrsto

## Avtor

* Gašper Koželj

## Opis

V tem projektu lahko igramo spletno različico priljubljene namizne igre **4 v vrsto**.

### Tekstovni vmesnik

Igro lahko igramo preko tekstovnega vmesnika. To naredimo tako, da odpremo datoteko `tekstovni_vmesnik.py`
in jo poženemo. Najprej nastavimo igro po navodilih (smernicah) nato pa lahko igramo. Stanje prikazuje tabela,
ki vsebuje števke 0, 1 in 2. 

### Spletni vmesnik

Za igranje s pomočjo spletnega vmesnika poženemo datoteko `4_v_vrsto.py` in sledimo spletnemu naslovu
lokalnega strežnika (ponavadi `http://127.0.0.1:8080/`). Sledimo gumbom in igramo.

### Načini igre

Igro lahko igrata dva igralca, ali pa en igralec proti računalniku, ki žetone meče naključno, ali pa proti računalniku, ki razmišlja.

#### Dva igralca

Igro lahko igrata dva igralca preko tekstovnega ali spletnega vmesnika.

#### Računalnik, ki meče naključno

Igralec lahko preko tekstovnega vmesnika igra proti računalniku, ki žetone meče naključno.

#### Računalnik, ki razmišlja

Igralec lahko preko tekstovnega vmesnika igra proti računalniku, ki razmišlja. Na žalost ne deluje tako, kot bi moral.
Narejen je s pomočjo metode [Minimax](https://en.wikipedia.org/wiki/Minimax).