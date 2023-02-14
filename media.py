def media(notas):
    """Calcula a média de uma sequência de notas de uma lista """
    return sum(notas) / len(notas)

def ler_notas(n):
    """Lê N notas que o usuario digitar e retorna uma lista de notas"""
    notas = []
    for i in range(n):
        nota =  float(input(str(i+1) + 'ª nota: '))
        notas.append(nota)
    return notas

num_alunos = int(input('Quantos alunos? '))
num_notas = int(input('Quantas notas? '))
for i in range(num_alunos):
    nome= input(str(i+1) + 'º do aluno(a): ')
    notas = ler_notas(num_notas)
    nota_final = media(notas)
    print('A nota de', nome, 'é', nota_final)