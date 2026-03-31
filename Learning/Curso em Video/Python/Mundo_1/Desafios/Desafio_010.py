saldo = float(input('Quantos reais você tem? '))

dolar = saldo / 3.27

if saldo > dolar:
    print('Vamos ver quantos dolares você compra com {:.2f}, você consegue {:.2f} dolares'.format(saldo, dolar))
else:
    print('Você não consegue comprar nenhum dolar.')

