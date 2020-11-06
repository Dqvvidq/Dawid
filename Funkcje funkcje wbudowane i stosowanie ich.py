#długość obiektu
a = len("Dawid")
print(a)

b = len("Python")
print(b)

#konwertowanie obiektu na str
print(type(200))

p = str(200)
print(type(p))

#konwertowanie na int
int("1")

#konwertowanie na float
print(100)
m = float(100)
print(m)

#pobieranie od urzytkownika danych za pomoca input
wiek = input("Ile masz lat:")
wiek_int = int(wiek)
if wiek_int < 18:
    print("Jestes młody")
else:
    print("Jesteś stary")

#funkcje mogą hermanizować logikę, którą chcemy wielokrotnie używać

def m(x):
    if x % 2 == 0:
        print("Liczba jest parzysta")
    else:
        print("Liczba nie jest parzysta")

m(1)
m(2)
m(3)
m(4)


#funkcje można wielokrotnie używać
n = input("Podaj liczbę:")
n = int(n)

if n % 2 == 0:
    print("liczba jest parzysta!")
else:
    print("Liczba nie jest parzysta")

if n < 50:
    print("Liczba jest mała")
elif n > 50:
    if n <= 70:
        print("Liczba jest w sam raz")
if n > 70:
    print("Liczba jest duza")

#kod można skrócić umieszczając go w funkcji

def u():
    n = input("Podaj liczbę")
    n = int(n)

    if n > 10:
        print("Liczba jest duża")
    else:
        print("Liczba jest mała")
    print(n * 2)
u()
u()
u()




