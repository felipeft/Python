class pessoa:
    #esses atributos sao variaveis encapsuladas dentro da classe
    nome = ''
    titulo = ''
    genero = ''
    nascimento = ''

class filme:
    nro_copias = 0
    titulo = ''
    genero = ''
    lançamento = ''

class tarefa:
    titulo = ''
    duracao = 0
    dificudade = 0
    
mae = pessoa()
pai =  pessoa()
usuario = pessoa()

f = filme()

#usuario.nome = input('Nome completo: ')
#mae.nome = input("Nome completo da mae: ")
#pai.nome = input("nome completo do pai: ")

#print('O nome do usuario do serviço é: ' + usuario.nome)

#podemos criar uma lista para atribuir elementos a classes
t = tarefa()
tarefas = [tarefa(), tarefa(), tarefa()]
tarefas[0].titulo = 'Lavar'
tarefas[0].duracao = 0.5
tarefas[0].dificudade = 0
tarefas[1].titulo = 'cozinhar'
tarefas[1].duracao = 1.0
tarefas[1].dificudade = 2
tarefas[2].titulo = 'treinar'
tarefas[2].duracao = 1.5
tarefas[2].dificudade = 1

#agora vamos ordenar essa lista
sorted(tarefas, key=lambda: t.titulo)
tarefas.sort(key=lambda : t.titulo)
