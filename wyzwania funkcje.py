#Funkcja pobiera liczbe i wzwraca ją do kwadratu
def f(x):
    """
    :param x: int
    :return: x do potęgi 2
    """
    return x ** 2

x = input("Podaj liczbę: ")
x = int(x)
print(f(x))

#Funkcja wyświetla łańcuch znaków

k = input("Napisz coś: ")

def l(k):
    """
    :param k: str
    :return: wyswietla lancuch znakow
    """
    print(k)
l(k)

#funkcja ktora ma 3 parametry wymagane i dwa opcjonalne
def j(x, y, z, n= 2, m = 3):
    """
    funkcja z 3 wymaganymi i 2 opcjonalnymi parametrami
    :param x: int
    :param y: int
    :param z: int
    :param n: int
    :param m: int
    :return: dodaje wszystkie liczby
    """
    return x + y + z + n + m
print(j(1, 2, 3))
print(j(1, 2, 3, 4))

#program z dwiema funkcjami ktore ze soba wspolgraja
x = input("Podaj liczbę: ")
x = int(x)

def jeden(x):
    """
    :param x: int
    :return: dzieli x przez 2
    """
    return x / 2

b = (int(jeden(x)))
print(b)

def mno(b):
    """
    :param b: int
    :return: mnozy b przez 4
    """
    return b * 4
print(int(mno(b)))

#funkcja ktora konwertuje lancuch znakow na liczbe typu float i obsluguje wyjatek
a = input("Podaj liczbę :")

def lan(a):
    """
    funkcja konwertuje str na float
    :param a: str
    :return: wzwarca float
    """
    try:
        a = float(a)
        print(a)
    except ValueError:
        print("Wpisz liczbę!")
lan(a)

#Dodawanie lancuchow dokumentujacych









