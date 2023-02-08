animais = [
    'gato',
    'ouriço',
    'pardal',
    'camaleão'
    ]
gastos = [10.15, 32.55, 23.49]
vazia = []

print(len(animais), len(gastos), len(vazia))

#packing em listas
aluguel = 450
energia = 80
agua = 70

contas = [aluguel, energia, agua]
despesas_totais = sum(contas)       #somente lista com valores numericos
print(despesas_totais)

gastos = [23.5, 45.6, 5.24, 2.36, 99.49]
#vamos alterar o terceiro elemento dessa lista (indice 2)
gastos[2] = 3.29    #gastos[-3]
del gastos[1]
gastos.insert(3, 100)
print(gastos, len(gastos))

#slicing (fatiamento)
numeros = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numeros[2:5], numeros[:5], numeros[3:8:2], numeros[3::2]) #x:y:z intercala

#concatenação
casas_pares = [198, 200, 202, 210, 212]
casas_pares = casas_pares[:3] + [204, 206, 208] + casas_pares[3:]
print(casas_pares)

#adicionar ao final
casas_pares.append(214)     #casas_pares += [214]
casas_pares.extend([216, 218])
print(casas_pares)

#ordenação 
compras = ['manteiga', 'aveia', 'sabao em pó', 'detergente', 'carvao', 'arroz']
item = 'farinha'
if not (item in compras):
    compras.append(item)

limite = 10
if compras.count(item) < limite:
    compras.append(item)
#print(compras)

posicao = compras.index('farinha')
compras[posicao] = 'farinha integral'
print(compras)

#no caso de haver outras ocorrencias de farinha na lista, pra substituir tudo devemos:
while 'farinha' in compras:
    posicao = compras.index('farinha')
    compras[posicao] = 'farinha integral'

print(compras)

notas = [7.3, 4.5, 6.7, 5.2, 8.4, 1.2, 9.4]
notas.sort()
print(notas)

teste = [3, 5, 7] * 2 + [2] * 3
print(teste)