import bottle
import model

SKRIVNOST = 'KajTeBriga'
DATOTEKA_S_STANJEM = 'stanje.json'

stiri_v_vrsto = model.StiriVVrsto(DATOTEKA_S_STANJEM)

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.post('/nova_igra/')
def nova_igra():
    id_igre = stiri_v_vrsto.nova_igra()
    bottle.response.set_cookie('idigre', id_igre, secret=SKRIVNOST, path='/')
    bottle.redirect("/igra/")

@bottle.get('/igra/')
def pokazi_igro():
    id_igre = bottle.request.get_cookie('idigre', secret=SKRIVNOST)
    igra, stanje, kdo_je_na_vrsti = stiri_v_vrsto.igre[id_igre]
    return bottle.template('igra.tpl', igra=igra, id_igre=id_igre, stanje=stanje, kdo_je_na_vrsti=kdo_je_na_vrsti)

@bottle.post('/igra/')
def igraj():
    id_igre = bottle.request.get_cookie('idigre', secret=SKRIVNOST)
    poteza = bottle.request.forms.getunicode('poteza')
    poteza = int(poteza) - 1
    stiri_v_vrsto.igraj(id_igre, poteza)
    bottle.redirect('/igra/')

@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')

bottle.run(reloader=True, debug=True)