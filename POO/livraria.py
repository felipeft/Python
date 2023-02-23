class Livro:
    titulo = ''
    copias_em_estoque = 0
    preco = 0.0

    #construtor
    def __init__(self, titulo = '', copias_em_estoque = 0, preco = 0.0):
        self.titulo = titulo
        self.copias_em_estoque = copias_em_estoque
        self.preco = preco

    def __str__(self):
        return 'Título:  {}; Estoque: {}; Preço: {}'.format(self.titulo, self.copias_em_estoque, self.preco)

    def vender(self, copias_vendidas):
        self.copias_em_estoque -= copias_vendidas
    #basicamente self serve para simbolizar o proprio objeto que chamou esse metodo

    def atualizar_preco(self, novo_preco):
        if novo_preco < 0.0:
            raise Exception('Preço Negativo!')
            self.preco = novo_preco

#criaçao de uma lista de livros
livros = [Livro('Joao caçador de tatu', 23, 20.0), Livro('introduçao a paiton', 50, 120.0), Livro('A revoluçao dos bixos', 115, 15.0)]

#modificando alguns objetos
livros[0].vender(5)

try:
    print('Tentando fazer atualização...')
    livros[0].atualizar_preco(-5.0)
    livros[1].atualizar_preco(200.0)
    print('Atualização concluida!')
except Exception as excp:
    print(excp)
    print('Fim da operação')

#adicionando um novo livro
livros.append(Livro('segredos da mente miseravel', 1, 1000.0))

#aprensentado a lista de livros disponiveis de maneira ordenada
print('Livros Disponiveis:')
#vai ordenar do preço mais baixo para mais alto
for livro in sorted(livros, key=lambda l : l.preco):
    print(livro)






