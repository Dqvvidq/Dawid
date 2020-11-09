#parametry wymagalne i opcjonalne
def f(x=2):
    return x ** x
print(f())
print(f(4))

def g(x, y=10):
    return x + y
print(g(2))
r = g(4, 7)
print(r)

# zmienne globalne
x = 1
y = 2
z = 3

def f():
    print(x)
    print(y)
    print(z)

f()

# zmienne lokalne

def g():
    m = 4
    n = 5
    b = 6
#print(m)
#print(n)
#print(b)

x = 100
def j():
    global x
    x += 1
    print(x)
j()