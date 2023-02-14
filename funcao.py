def f(x):
    valor = 5 * x ** 2
    return valor

#variaveis globais
pi = 3.141592
def circunferencia(raio):
    return 2 * pi * raio

#passagem de parametros
def zero_esq(x, n):
    xs = str(x)
    return '0' * (n - len(xs)) + xs #caso o numero seja por exemplo = 2 ent fica 02
    #perceba que: '0' * 0 é a mesma coisa que uma string vazia 

def formatar_data(dia, mes, ano, extenso=False):
    if extenso:
        meses= ['janeiro', 'fevereiro', 'março,', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
        return (zero_esq(dia, 2) + ' de '  + meses[mes-1] + ' de ' + zero_esq(ano, 4))
    else:
        return(zero_esq(dia, 2) + '/' + zero_esq(mes, 2) + '/' + zero_esq(ano, 4))

#main
print('f(x) = 5*x^2')
for i in range(1, 4):
    res = f(i)
    print('f ({}) = {}'.format(i, res))

print(circunferencia(10))

data = formatar_data(7, 12, 2023)
data2 = formatar_data(1, 8, 198, True)
print(data + '\n' + data2)



