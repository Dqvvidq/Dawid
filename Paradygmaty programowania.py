#styl programowania proceduralnego. Zmienne są przechowywane w stanie globalnym, a operacje na
#nich są wykonywane w funkcjach

x = 2
y = 4
z = 8
xyz = x + y + z
print(xyz)

rock = []
country = []

def collectet_songs():
    song = "Wpisz tytuł piosenki"
    ask = "Naciśnij r lub c albo q, by wyjść"

    while True:
        genere = input(ask)
        if genere == "q":
            break

        if genere == "r":
            rk = input(song)
            rock.append(rk)

        elif genere ==("c"):
            cy = input(song)
            country.append(cy)
        else:
            print("Nieprawidłowe polecenie")
    print(rock)
    print(country)

collectet_songs()

#funkcja w której mogą wystąpić efekty uboczne ze wzgledu na stan globalny
a = 0
def increment():
    global a
    a += 1

#funkcja w której nie wystąpią efekty uboczne ze względu na wyeliminowaie stanu globalnego
def _increment ():
    return a + 1

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Utworzono!")
or1 = Orange(280, "Ciemnopomaranczowy")

print(or1.weight)
print(or1.color)

or2 = Orange(240, "ciemnozolty")
or3 = Orange(400, "jasny")

print(or2)

