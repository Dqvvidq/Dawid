#petle for
name = "Ted"

for litera in name:
    print(litera)

#pętla for w liscie

list = ["banan", "chleb", "Vuda", "mleko"]

for lista in list:
    print(lista)

#petla for w krotce

kroteczka = ("Masło", True, False, 101)

for krotka in kroteczka:
    print(krotka)

#petla for w slowniku (wyswietla tylko klucze)

słownik = {"Audi": "A6",
           "Bmw": "e46",
           "Alfa Romeo": "156"}
for klucze in słownik:
    print(klucze)

#zwiększanie liter w liście

tv = ["Spadkobiercy", "Jaka to melodia", "Familiada"]

i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print (tv)

# inna składnia pętli for
for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)

# przenoszenie elementów dzięki pętli for

coms = ["programowanie", "znajomi", "hillout"]

all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)

# funkcja range

for i in range (1, 11):
    print(i)

#petla while

x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1

print("Szczęśliwego nowego roku!")

# instrukcja break
for i in range (0, 100):
    print(i)
    if i == 55:
        break

#program który będzie prosić użytkownika o wpisanie danych dopoki nacisnie q

qs = ["Jak masz na imie?: ", "Jaki jest twój ulubiony kolor?: ", "Jakie masz zadanie?: "]

n = 0
while True:
    print("Wpisz q aby zakończyć")
    a = input(qs[n])
    if a == "q":
        print("Zakończono program")
        break
    n = (n + 1) % 3

#instrukcja continue

for i in range (2, 6):
    if i == 3:
        continue
    print(i)

# instrukcja continue w petli while

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

# pętle zagnieżdżona

for i in range (1, 3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)
print(added)

# pętla for wewnatrz petli while

while input('t czy n?') !='n':
    for i in range (1, 6):
        print(i)