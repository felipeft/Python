msg = "ola mundo!"
print(len(msg))

#dividindo a string em 2 partes
primeira_parte = msg[ : len(msg) // 2]
print(primeira_parte)

segunda_parte = msg[len(msg) // 2 :]
print(segunda_parte)

#convertendo para maiusculo
msg_maiuscula = msg.upper()
print(msg_maiuscula)

#convertendo para minusculo
msg_minuscula = msg_maiuscula.lower()
print(msg_minuscula)

#verificar existencia de digitos numericos na string
idade_str = input('digite sua idade: ')
if idade_str.isnumeric() == True:
    idade = int(idade_str)
    print('daqui a 10 anos voce vai ter ', idade+10, ' anos AHAHAHAH');
else:
    print('Invalido!')


texto = """João amava Teresa que amava Raimundo que amava Maria que amava Joaquim que amava Lili que não amava ninguém. """
#verificar ocorrencias de determiado caractere
quantos = texto.count("amava")
print(quantos)

#substituir as ocorrencias de determinada palavra por outra
quantos = texto.replace("amava", "gostava")
print(quantos)

#operador in para verificar a existencia de determinada palavra em uma string
if "Paulo" in texto:
    print("Paulo está na lista de pessoas")
else:
    print("Paulo nao esta na lista de pessoas :(")

#quebra de linha na string
poema = "João amava Teresa que amava Raimundo\nque amava Maria que amava Joaquim que amava Lili\nque não amava ninguém."
print(poema.replace("amava" , "colava de"))
#se usassemos \\ teriamos um simples '\' na string
#se ussasemos \t teriamos um grande espaçamento entre um caractere e outro

#uso do format
nome = input('digite o seu nome: ')
idade = input('digite a sua idade: ')
altura = input('digite a sua altura: ')
formato_msg = 'olá, {}!, sua idade é {} anos e sua altura é {}m. '
msg = formato_msg.format(nome, idade, altura)
print(msg)
#format enxerga {} e substitui pelos valores passados como parametro na funçao