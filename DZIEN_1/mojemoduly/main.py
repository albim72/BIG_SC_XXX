# import dane
# import dane as dn
from dane import nrfilii as nf
from dane import book as bk

from funkcje.funkcja_kol import czytaj_liste, czytaj_slownik
from  funkcje.informacja.message import msg


print(msg(34,"Kilka słów o kolekcjach! "))
#kopiowanie linii/bloku tekstu -> CTRL+D
print("to jest pierwszy program w PyCharm")
print("___ kolekcje z modułu: dane ___")
print(nf)
print(bk)

print("użycie funkcji do kolekcji..........")
czytaj_liste(nf)
czytaj_slownik(bk)
