import math

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

Δ = b**2 - 4 * a * c

if Δ < 0:
    print('o Δ eh negativo, logo nao ha raizes reais') 
    exit()

x1 = (-b + math.sqrt(Δ)) / (2*a)
x2 = (-b - math.sqrt(Δ)) / (2*a)

print(x1, x2)
