def f(x):
    return x * 2

a = f(2)
print(a)

if a == 10:
    print("a jest równe 10")
elif a == 9:
    print("a jest równe 9")
elif a == 4:
    print("a jest równe 4")
else:
    print("nie wiem")

#definicja bez parametru
def h():
    return 1 + 1
m = h()
print(m)

#funkcja która zawiera trzy parametry
def f(x, y, z):
    return x + y + z
wynik = f(1, 2, 3)
print(wynik)