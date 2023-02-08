saldo = 500
idade_usuario = 25
cheque_especial = 500
valor_saque = 700

if saldo < valor_saque:
    if idade_usuario >= 25 and saldo + cheque_especial >= valor_saque:
        saldo -= valor_saque
        print('saque no valor de R$%0.2f' % valor_saque, ' foi feito')
        print('Cheque especial: R$%0.2f' % saldo)
    
    else:
        print('saque nao efetuado!')
        print('saldo insuficiente')
else:
    saldo -= valor_saque
    print('saque no valor de ', valor_saque, ' foi feito')
    print('saldo: R$%0.2f' % saldo)
