#Obsługa wyjątków
a = input("Wpisz liczbę:")
b = input("Wpisz liczbę: ")
a = int(a)
b = int(b)
try:
    print(a/b)
except ZeroDivisionError:
    print("Drugą liczba nie moze byc 0")

#obsługa dwoch wyjątków
try:
    p = input("Pierwsza liczba: ")
    o = input("Druga liczba: ")
    p = int(p)
    o = int(o)
    print(p/o)
except(ZeroDivisionError, ValueError):
    print("Nieprawidłowe Dane")

#łancuchy dokumentujące!!
def add(x, y):
    """
    zwraca x + y
    :param x: int
    :param y: int
    :return: int suma x i y
    """
    return x + y

#uzywanie zmiennych tylko w tedy gdy to jest konieczne

x = 100
print(x)

print(100)

