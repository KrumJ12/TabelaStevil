![alt text](https://github.com/KrumJ12/TabelaStevil/blob/master/Slike/menu.PNG "Menu")


Člana ekipe:


Marko Žugelj

Jernej Krum



Opis projekta:

Igra, v kateri imamo tabelo (n vrstic in stolpcev) števil,
cilj igre pa je, 
da iz zgornjega levega kota prispemo v spodnji desni kot 
z zahtevano vsoto števil, 
ki jih na poti poberemo. Premikanje je omejeno 
na tabelo, vsako polje lahko obiščemo enkrat.

![alt text](https://github.com/KrumJ12/TabelaStevil/blob/master/Slike/igra.PNG "Igra")

Tipke za premik:

-Puščica navzgor 

-Puščica navzdol

-Puščica desno

-Puščica levo

-Presledek (razveljavi potezo)



O implementaciji:



V Initu se registriramo na pritiske tipk, dodamo izbire v menu in naredimo začetni zaslon s sliko in gumbi. 


Ob pritisku na ZAČNI IGRO, se kliče metoda znova.
Uničimo prejšnji meni s sliko in pokažemo platno z aktivirano 
menijsko vrstico. Ker se ta metoda kliče tudi po vsaki odigrani 
igri, pobrišemo morebitno prejšnjo igro in ustvarimo
nov seznam odvisen od dimenzije, ponastavimo igralčeve koordinate, 
sezname že obiskanih kvadratkov in izbrišemo črte
ter pokličemo funkcijo, ki izračuna možno pot glede na nov seznam števil. 
Pravtako odštevalnik ponastavimo na začetno
vrednost, ki je odvisna od dimenzije. 
Števila iz seznama zapišemo po kvadratkih naše tabele ter označimo start in cilj.

Igralcu sproti sporočamo, koliko časa še ima, koliko točk ima trenutno nabranih in koliko jih mora imeti na koncu.



Metoda izracunajTocke na podlagi seznama števil izračuna neko pot od levega zgornjega kota (START), do desnega spodnjega 
kota (CILJ),
uporabniku pa javimo zahtevan seštevek točk. Na vsakem koraku pregledamo možne smeri in eno izberemo, obenem 
pa pazimo, da si ne zapremo 
poti do cilja (metoda obstajaPotDomov). Metoda deluje po principu zapolni iz slikarja. 



Druge metode:



- premikLevo, premikDesno, premikGor, premikDol (preverimo, če je premik sploh možen, spremenimo koordinate igralca 
in kličemo metodo posodobi)



- posodobi (Posodobi položaj igralca, nariše pot med starim in novim kvadratom (naša sled - črta), 
zapomnimo si črte in zasedene koordinate. 
Posodobi tekst nabranih točk (zaradi premika), če smo na koncu, se kliče metoda konec.)



- undo ( Razveljavi zadnjo potezo igralca, sproži pa se ob pritisku tipke SPACE. Če smo prišli na cilj, ne dovolimo vračanja, 
sicer pa pobrišemo vse, 
kar je nastalo ob zadnji potezi in premaknemo igralca korak nazaj.)



- odstevalnik (Odšteva čas do konca trenutne igre.)



- pokaziResitev (Pokaže rešitev, ki da zahtevan seštevek, vendar igralcu ne dovoli več igranja.)



- konec (Igralcu sporoči, če je uspešno prišel na cilj in mu ponudi novo igro.)



- nastaviTezavnost (Če igralec v menijski vrstici izbere kakšno drugo dimenzijo, se zažene nova igra v zahtevani velikosti.)



- nastaviStevila (Podobno kot prej, igralec izbira med celimi števili ali pa samo med pozitivnimi celimi števili.)



- koncnice (Za lepši prikaz vseh napisov med igro.)



- navodila (Info dialog, ki govori o navodilih za igro.)




Možne izboljšave:

- lepotni popravki

- možna rešitev bi bila natanko ena
- na začetku bi bilo nekaj kvadratkov onemogočenih, torej jih ne bi mogli obiskati

- razni bonusi, na primer lahko bi zapustili tabelo in storili določeno pot izven tabele

- način sfere, kjer bi lahko npr iz skrajne leve točke prišli v skrajno desno, iz skrajne gornje pa v spodnjo

- način za dva igralca, pravila premikanja kot kralja pri šahu, tekmovala pa bi, kdor bi zbral več točk oz matiral drugega (matiral seveda glede na zasedena polja)

- dosežki (preostali čas pri zmagi) bi se shranjevali in bi imeli lestvico top 10 rezultatov






















