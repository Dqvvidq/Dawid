#metoda upper

print("Witaj")
print("Witaj".upper())

#metoda replace

print("Witaj".replace("j", "m"))

#tworzenie listy

fruit = ["mango", "banan", "gruszka"]
print(fruit)

#metoda append czyli dodawanie nowego elementu na koncu listy

fruit.append("pomelo")
fruit.append("figa")
print(fruit)

#w liscie mozna zapisywac dane dowolnego typu

fruit.append(100)
fruit.append(True)
fruit.append(20.0)

print(fruit)

#listy mają indeksy od 0 do ...

print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[3])

#listy są elementami modyfikowalnymi
colors = ["fioletowy", "czerwony", "niebieski", "zołty"]
print(colors)
colors[2] = "biały"
print(colors)

#usuwanie elementu z listy

farba = ["żółta","niebieska", "zielona"]
print(farba)
item = farba.pop()
print(item)
print(farba)

#listy mozna połaczyc dzieki operatorom dodawania

k = farba + colors
print(k)

# za pomocą in można sprawidzic czy element znajduje sie w liscie

colors1 = ["czarny", "biały", "pomaranczowy"]
print("czarny" in colors1)

# żeby sprawdzić czy nie ma elementu na liście trzeba napisac przed in not (not in)

print("różowy" not in colors1)
print("czarny" not in colors1)

# liczba elementów listy

print(len(colors))
print(len(colors1))

# praktyczne wykorzystanie listy

lista_zakupow = ["masło", "chleb", "jajka", "kisiel", "mąka"]

zgadnij = input("Zgadnij element z listy: ")
if zgadnij in lista_zakupow:
    print("Zgadłeś!!")
else:
    print("nie zgadłes!")











