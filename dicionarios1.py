#list, tuple, set e dict sao formas de representar um conjunto de dados em py
#dicionarios armazenan coleções mutáveis e desordenadas de quaisquer elementos, únicos ou não

dicionario_01 = {} # dicionário vazio
dicionario_02 = dict() # outro dicionário vazio

#ex:
populacao = {'Ceará': 9132078, 'Bahia': 14873064, 'Alagoas': 3337357}
print('O ceará possui {} habitantes.'.format(populacao['Ceará']))

#podemos indexar um valor armazenado em um dicionario utilizando nome do dicionario[chave] = val
#chaves em dicionario servem como indice
for chave, valor in populacao.items():
    if chave == 'Ceará' or 'Alagoas':
        artigo = 'O'
    else:
        artigo = 'A'
    print('{} {} possui {} habitantes.'.format(artigo ,chave, valor))

#basicamente iteramos uma lista. cada chave e cada valor correspondente das chaves se tornará uma variavel da lista "items"

#retornando uma lista com todas as chaves de um dicionario
print('Escolha entre os estados: ' + ', '.join(populacao.keys()))

#escolher chave de dicionario
estado = input('de qual estado voce quer saber a população? ')
pop = populacao.get(estado)
if pop == None:
    print('Infelizmente não temos esse estado:(')
    
else:
    print('{} possui {} habitantes'.format(estado, pop))

#lista ordenada alfabeticamente com as chaves de um dicionario
for estado in sorted(populacao):
    print('{} possui {} habitantes.'.format(estado, populacao[estado]))

#ordenando agora pelos valores da chave (menor pro maior)
for estado in sorted(populacao, key=lambda chave : populacao.get(chave)):
    print('{} possui {} habitantes.'.format(estado, populacao[estado]))
