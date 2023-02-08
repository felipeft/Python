frutas = {"maçã", "banana", "churrasco", "maçã"}
print(frutas)

#tuplas = (); listas = []; conjuntos = {}

#lista de cidades
respostas = ['Manaus', 'Brasília', 'Fortaleza', 'Manaus', 'Rio de Janeiro', 'Brasília', 'Fortaleza', 'Natal', 'Sobral', 'Fortaleza', 'Cuiabá', 'Sobral', 'Aracoiaba', 'Natal', 'Belo Horizonte', 'Fortaleza', 'Sobral', 'Petrolina']
#"convertendo" lista para conjunto
cidades = set(respostas)
#removerá duplicatas
print(cidades)

nome = 'Ana Maria Freitas'
letras = set(nome)
print(letras)

#op entre conjuntos
mult_2 = {0, 2, 4, 6, 8, 10, 12}
mult_3 = {0, 3, 6, 9, 12}

print(mult_2 | mult_3) #uniao
print(mult_2 & mult_3) #intersecção
print(mult_2 - mult_3) #diferença 1
print(mult_3 - mult_2) #diferença 2

#entrada e saida de novos dados
modelos = {'clio', 'gol', 'palio'}
modelos.add('fox')  #para adicionar apenas um elemento
print(modelos)
modelos.update({'duster', 'tcross'})    #para adicionar varios elementos
print(modelos)

modelos.discard('gol')
print(modelos)
#existe a opçao remove mas gera um erro caso o elemento nao esteja de fato no conjunto