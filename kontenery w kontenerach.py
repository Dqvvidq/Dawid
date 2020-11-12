#kontener w kontenerach
lista = []
print(lista)

rap = ["Rychu Peja", "Kenea West", "Szakira"]
czolgi = ["Is", "KV", "GC"]
jedzenie = ["Chelb", "Makaron", "Mrozonki"]

lista.append(rap)
lista.append(czolgi)
lista.append(jedzenie)

print(lista)
print(lista[2])

#kiedy wprowadzimy zmiany w liście rap zmiany zostana zapisane w "lista"
czolgi.append("Rudy")
print(lista)

#krotki w listach
lokacja = []

la = [34.0522, 188.2437]
chicago = [41.8781, 87.6298]

lokacja.append(la)
lokacja.append(chicago)

print(lokacja)

#listy w krotkach
pl = ["WkS", "Legia", "Arka"]
de = ["Borussia", "Bayern", "Koln"]

liga = (pl, de)
print(liga)
print(liga[0])

#słownik w liscie i tupli
liczby = {"1", "2", "3", "4", "5"}
lista_liczby = [liczby]
tuple_liczby = (liczby,)

print(lista_liczby)
print(tuple_liczby)

#listy, tuple, słowniki jako wartości w słowniku

ny = {"lokalizacja":
        (40.7128, 74.0059),
      "celebryci":
        ["W.Alen", "J.rock", "K.Bacon"],
      "fakty":
          {"stan": "NY",
           "Kraj": "Ameryka"}
}
