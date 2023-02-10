#vamos extrair informações de uma string utilizando dicionarios

mensagem = ('Estou amando este meu 1º curso de Python!')
ocorrencias = {}    #dic vazio 
for letra in mensagem:     #letras vai receber cada caractere de mensagem por vez
    ocorrencias[letra] = ocorrencias.get(letra, 0) + 1  #vai incrementando a medida que caracteres diferentes aparecem

print('A mensagem digitada possui {} caracteres. Sendo {} caracteres unicos.'.format(len(mensagem), len(ocorrencias)))
print('Cada um desses caracteres unicos ocorreu: ')
for letra in sorted(ocorrencias):
    print("\t'{}' ocorreu {} vezes.".format(letra, ocorrencias[letra]))

#o dicionario ocorrencias está assim:
#ocorrencias = {' ':7, '!':1, '1':1, 'E':1, 'P':1 ...}
#caractere é a chave
#vale lembrar que dicionarios guardam informações de maneira desordenada

#Nesse momento, pense em um cenário onde você quer fazer uma lista telefônica em forma de diretório: para cada letra do alfabeto, serão apresentados os dados dos contatos cujos nomes começam com essa letra. Estes dados são: nome, telefone e e-mail.
print('\n\nLista telefonica ( ͡° ͜ʖ ͡°)')

#usaremos um dicionario para cada contato e outro dicionario para todo a lista:
contatos = {}



ctt = {}
print('\n----Adição de contato----')
ctt['nome'] = input('Digite o nome do contato: ')
ctt['telefone'] = input('Digite o telefone do contato: ')
ctt['email'] = input('Digite o email do contato: ')

inicial = ctt['nome'][0].upper() #apenas para garantir que a inicial do nome está em maiusculo

#para o caso de nao haver contatos com essa inicial na lista
if inicial not in contatos:
    contatos[inicial] = []
    contatos[inicial].append(ctt)   #vai adicionar o contato na chave com a inicial certa

#front-end dessa lista
for inicial in sorted(contatos):
    print('---- Contatos com a letra {} ----'.format(inicial))
    for ctt in sorted(contatos[inicial] , key=lambda c: c['nome']):
        print('Nome: {}\t Telefone: {}\t Email: {}'.format(ctt['nome'], ctt['telefone'], ctt['email']))




                                                     




