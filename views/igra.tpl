% import model
% rebase('base.tpl')

  <svg width="700" height="600">
    <rect rx="20" ry="20" width="700" height="600"
    style="fill:rgb(0,0,255);stroke-width:1;stroke:rgb(0,0,0)" />
% for poz in igra.pozicije_krogov():
%   if igra.tabela[poz[0]][poz[1]] == 0:
      <circle cx="{{poz[2]}}" cy="{{poz[3]}}" r="40" stroke="black" stroke-width="1" fill="white" />
%   elif igra.tabela[poz[0]][poz[1]] == 1:
      <circle cx="{{poz[2]}}" cy="{{poz[3]}}" r="40" stroke="black" stroke-width="1" fill="red" />
%   elif igra.tabela[poz[0]][poz[1]] == 2:
      <circle cx="{{poz[2]}}" cy="{{poz[3]}}" r="40" stroke="black" stroke-width="1" fill="yellow" />
%   else:
%     pass
  </svg>

% end
% end

% if stanje == igra.ime_1:

  <h1>Zmaga {{igra.ime_1}}</h1>
  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

% elif stanje == igra.ime_2:

  <h1>Zmaga {{igra.ime_2}}</h1>
  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

% elif stanje == model.NEODLOCENO:

  <h1>Izenačeno je</h1>
  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

% else:

  <h1>Na vrsti je {{igra.kdo_je_na_vrsti}}.</h1>
  <form action="/igra/" method="post">
    Vaša poteza: <input type="number" min="1" max="7" name="poteza" />
    <button type="submit">Potrdi</button>
  </form>

% end
