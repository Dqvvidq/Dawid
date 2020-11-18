

#wyswietl kazdy znak lancucha "camus"

a = "Camus"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

#program ktory pobiera od uzytkownika dwa lancuchy znakow do str

a = input("Co wczoraj napisałeś: ")
b = input("Do kogo wysłałes: ")

print("Wczoraj napisałem {} i wysłałem do {}".format(a, b))

#uzyj odpowiedniej metody aby zdanie zaczynalo sie od duzej litery

print("aldous Haxleu urodził się w 1894".capitalize())

#wywołaj metode która wzwroci łancuch znakow

m = ["Gdzie teraz?", "Kto teraz?", "Kiedy", "Teraz?"]
metoda = ", ".join(m)
print(metoda)

#liste przekształć w str

lista = ["Zwinny", "lis", "przeskoczył", "nad", "leniwym", "psem", "."]
jeden = " ".join(lista)
print(jeden)

#zastap litere s w $

b = "W czasie suszy szosa sucha"
b = b.replace("s","$")
print(b)

print("Hemingway".index("m"))

#zapisz w kodzie lancuch znakow

print('pobiegł "Szybko"')

# utoworz lancuch znakow uzywajac konkatenacji

print("trzy " * 3)

#zwroc wycinek obejmujacy

n = ("Długo na szturm i szaniec poglądał w milczeniu. Na koniec rzekł: 'Stracona'.")

print(n[:46])