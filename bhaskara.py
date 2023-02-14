import math

def raizes2grau(a, b, c):
    Δ = b**2 - 4 * a * c
    if Δ < 0:
        print('o Δ eh negativo, logo nao ha raizes reais') 
        raizes = ()
        exit()
    else:
        x1 = (-b + math.sqrt(Δ)) / (2*a)
        x2 = (-b - math.sqrt(Δ)) / (2*a)
        if Δ == 0:
            raizes = (x1,)
        else:
            raizes = (x1, x2)

    return raizes

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
print('Equação: {}x² + {}x + {} = 0'.format(a, b, c))
print('Raizes reais:', raizes2grau(a, b, c))

