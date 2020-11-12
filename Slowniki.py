#tworzenie słownika
my_dict = {}
print(my_dict)

#przykładowa krotka
fruits = {"Agerest":
          "Zielony",
          "Jablko":
          "Czerwone",
          "Sliwka":
          "Fioletowa"}

print(fruits)

#dodawanie do słownika pary klucz:wartość
fruits["Arbus"]="Green"

print(fruits)

# pobieranie wartości ze słownika
print(fruits["Jablko"])

# kolejny przykład
facts = {}
print(facts)

facts["programowanie"] = "Zabawa"
facts["Ckz"] = "Szkoła"
facts["ZsTiE"] = "Technikum"

print(facts)

#sprawdzanie w słowniku czy jest w nim konkretny klucz
print("programowanie" in facts)

# sprawdzanie czy klucza nie ma w słowniku
print("Ckz" not in facts)
print("szkoła" not in facts)

#pary (klucz:wartosc) mozna usowac ze słownika
books = {"Harry":
         "Potfel",
         "Johny":
         "Kontrawolta",
         "Twoj":
         "Stary"}
print(books)
del books["Harry"]
print(books)

#program z wykorzystaniem słownika

rhymes = {"1": "Witaj",
          "2": "Swiecie",
          "3": "Python",
          "4": "Java"}

n = input("Wpisz liczbe od 1-4: ")

if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Od 1-4!!")

