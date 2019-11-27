# Kaip naudoti robotą filmavimo aikštelėje su Dragonframe

# Ko nedaryti

-- NIEKADA nedirbti šalia roboto, kai jis juda. Dragonframe nėra visai nuspėjamas, robotas gali staigiai grįžti į pradinę/bet kurią kitą trajektorijos padėtį. Visada, dirbdami prie roboto, nuspauskite _Move hold_ mygtuką kontrolerio pulte (žr. ). Mygtukas mirksi mėlynai, kada roboto judėjimas yra sustabdytas, ir šviečia nemirksėdamas, kada robotas gali vykdyti komandas.
-- Robotas korektiškai veikia tik 25% arba didesniu greičiu.
-- VISADA pasitikrinkite, ar roboto trajektorijos failas (vardo formatas: production_SCENE.csv atitinka Dragonframe projekto vardą. Kitu atveju robotas juda kito projekto trajektorija.
-- Nevaikščioti tarp kadrų, kol robotas juda. Tai kažkiek pratestuota ir matėme, kad robotas nešoka į naują trajektoriją, išskyrus tuos atvejus, kai naujas tikslas yra tarp esamos ir pirmosios jo pozicijos -- tada jis sustoja naujame taške. Taip jį galima sustabdyti anksčiau, tačiau tai nėra gerai išbandyta ir garantuojama.
-- Nepamiršti atspausti _Move Hold_ prieš paleidžiant judesio/fotografavimo/trynimo komandą iš Dragonframe. Tai kažkiek išbandyta, tačiau negarantuojama, kad robotas nepames pozicijos/nepraleis judesių.
-- Paleidus DF arba atsidarius naują take'ą, robotas gali grįžti į 1 poziciją. Turėkite tai omenyje, neišsigąskite ir niekada nelaikykite nieko ten, kur robotas gali pasiekti bet kuriame trajektorijos taške.
-- Kartais robotas po fotografavimo pravažiuoja sekančius nufotografuotus kadrus. Dar gerai neišsiaiškinta, kada ir kodėl.

# Darbo eiga

0. Įsitikinti
1. Pajungti Etherneto kabelį į kairę jungtį (berods, J204) ant kontrolerio ir į kompiuterio Etherneto jungtį.
2. Įjungti kontrolerį. ROS serveris turėtų pasileisti automatiškai, tai indikuoja oranžinis LED'as prie _Run_ mygtuko.
3. Kontroleriui pilnai startavus, perjungti robotą į _Local_ veikimo būseną (žr. ).
4. Paleisti Dragonframe. Įsitikinti, kad roboto veikimą užtikrinantis script'as yra susietas su Dragonframe (Dragonframe --> Preferences --> Advanced --> Enable action script)
5. Atsidaryti reikiamą projektą. Prieš tai įsitikinti, kad projekto Production ir Scene savybės atitinka trajektorijos failo vardą (žr. _Ko nedaryti_). 
6. Paleidus DF arba atsidarius naują take'ą, robotas gali grįžti į 1 poziciją. 



#Kaip diagnozuoti ir spręsti problemas, kai jos iškyla

1. Jei robotas nejuda: įsitikinti, kad jis yra _Local_ darbinėje būsenoje, kad įjungtos roboto ašys bei _Move Hold_ mygtukas (indikuojama LED'ais). Įsitikinti, kad aktyvi Staubli Ethernet jungtis (prie Mac'o _Network_ nustatymų). Įsitikinti, kad veikia ROS'o serveris (indikuojama oranžiniu LED'u prie _Run_ mygtuko. Įsitikinti, kad _dragonframe.sh_ script'as susietas su DF (žr. _Darbo eiga_ 4 punktas). Paklikinti kelis kartus tarp kadrų -- kartais robotas komandas gauna ne iš karto, startavus Dragonframe'ą. Jei niekas nepadeda, eiti į
2. Jei robotas pameta padėtį: įsitikinti, kad roboto greitis yra 25% arba daugiau. Gali padėti padidinti greitį ir pašokinėti tarp kadrų. Prieš tęsiant darbą, įsitikinti, kad robotas atvažiavo į reikiamą padėtį.
3. Kartais 1-2 atvejais gali padėti perjungti roboto darbinę padėtį į _Manual_ ir jį atvaryti iki nulinės padėties.
4. Kadras, į kurį turėjo nueiti robotas, ir 1 ašies koordinatės visada rašomos į log.txt failą (studijos Mac'e jis yra Staublio folderyje ant darbalaukio, t.y. /Users/primavera/Desktop/Staubli/log.txt). Jį galima realiu laiku stebėti terminale. Jeigu terminalas uždarytas, seka tokia: _Cmd+Space_, įrašyti _Terminal_, spausti _Enter_. Atsidarius terminalui, jame surinkti komandą _cd /Users/primavera/Desktop/Staubli_. Komanda _pwd_ galite įsitikinti, kad tikrai ten esate. Tada surinkti komandą _tail -f log.txt_.
5. Paties roboto pozicija yra rodoma pulte, einant į _Control panel_ --> _Controller status_ --> _Joint position_
6. Jeigu kažkas blogai ir vis dar neaišku, kodėl: pasižiūrėti, ką rodo pulto ekranas ir event log'as (_Menu_ mygtukas --> _Event log_ ar pan.)


