#długi łańcuch znaków

"""
to jest
długi
łańcuch
znaków
"""

#łańcuchy znaków są iterowalne co ooznacza ze maja indeksy

moja = "Siema"
print(moja[0])
print(moja[1])
print(moja[2])
print(moja[3])
print(moja[4])

#pobieranie ujemnego indeksy z łańcucha znaków

print(moja[-1])

#łańcuchy znaków są niezmnienne
#konkatenacja czyli łączenie łańcuchów znaków

print("kot " + "w" + " butach")

#łańcuch znaków można pomnożyc

print("Puchatek " * 3)

#zmienianie liter na większe metoda

a = "uber".upper()
print(a)

#zmienianie liter na mniejsze metoda

b = a.lower()
print(b)

#zmienianie pierszej litery na większa metoda

print("ryczy rano los".capitalize())

#tworzenie nowych lancuchow znakow metoda format

print("Czesc {}".format("Zenon"))

m = input("Podaj imie: ")
print("Czesc {}".format(m))

#używanie większej liczby nawiasów klamrowych

author = "William Faulkner"
year_born = "1897"

print("Aktor {} urodził się w {}".format(author, year_born))

#tworzenie łańcucha znaków na podstawie danych wpisanych przez użytkownika

a = input("Wpisz imie: ")
b = input("Wpisz ulubiony sport: ")
c = input("Ile lat uprawiasz ten sport: ")

print("{} uprawia {} od {} lat".format(a, b, c))

#dzielenie łańcucha znakow metodą split

a = "Hej.Siema!".split(".")
print(a)

#dodawanie znaków pomiędzy str metoda

first_tree = "abc"
str = "+ ".join(first_tree)
print(str)

#laczenie listy w jeden ciag znakow

zakupy = ["Ziemniaki", "Maka", "Chelb", "Woda"]

m = " ".join(zakupy)
print(m)

# usuwanie odstepow metoda

s = "   lol        "
print(s)
s = s.strip()
print(s)

#zastepowanie znakow w str

equ = "Ostry wicher mrozi"
print(equ)
equ = equ.replace("r", "@")
print(equ)

#znajdowanie indeksu
try:
    print("Imperialny".index("r"))
except:
    print("Nie znaleziono znaku")

# sprawdzanie czy dany ciąg znaków występuje metoda in

print("kot" in "kot w butach")

if "czterej" in "czterej pancerni":
    print("Znajduje sie")
else:
    print("Nie znajduje sie")

print("kot" not in "kot w butach")

#umieszczanie "" wewnatrz łancucha znakow

print("odpowaida mu \"owszem.\"")

print('Witaj w swiecie "leszczu"')

#znak nowego wiersza

print("wiersz1\nwiersz2\nwiersz3")

#tworzenie wycinkow

fict = ["Clavel", "Camu", "Elo", "Uber", "legia"]
print(fict[0:3])

#tworzenie wycinku na str

ivan = "a zyc tak na skraju zguby trzeba samotnie"
#0 mozna pominac jako indeks tak samo jak ostatni indeks
print(ivan[26:])
print(ivan[:5])
print(ivan[0:10])
print(ivan[26:41])



