#utorz liste ulubionych muzykow
ulubieni_muzycy = ["Peja", "Tede", "Guzior", "Ramstein"]
print(ulubieni_muzycy)

#lista krotek miejsc które odwiedziłem

miejsca = [("Wrocław-13.43434:10.323123"),("Olesnica-12.12312:12.2313212")]

print(miejsca)

#słownik o sobie

ja = {"Wzrost": 174,
      "Waga": 68,
      "Ulubiony aktor": "John",
      "Ulubiona gra": "CS GO"}

print(ja["Wzrost"])
print(ja["Waga"])

x = input("Zapytaj mnie o coś: ")
if x in ja:
    ja = ja[x]
    print(ja)
else:
    print("Zapytaj o Wzrost, Wage,")

#słownik kojarzacy muzykow z ich utworami

muzyka = {"Peja": ["Slums atak", "Ludzie ulicy", "Szpan"],
          "Ramstein" : ["Sonne", "Ich will", "Rosen rot"],
          }
print(muzyka["Peja"])

