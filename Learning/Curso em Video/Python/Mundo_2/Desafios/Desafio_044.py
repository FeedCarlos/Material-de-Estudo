# Elabore um programa que calcule o valor de ser pago por um produto, considerando o seu preço normal e condição de pagamento: - à vista dinheiro/cheque: 10% de desconto - à vista no cartão: 5% de desconto - em até 2x no cartão: preço normal - 3x ou mais no cartão: 20% de juros.

product = float(input('Qual é o valor do produto? R$'))
print('')
print('[1] À vista dinheiro ou cheque\n[2] À vista no cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão')
pay = int(input('Qual será o método de pagamento? '))
if pay == 4:
    parcelas = int(input('Em quantas parcelas?'))

print('')

juros = (product*20) / 100

if pay == 1:
    print('O valor do produto à vista no dinheiro fica R${:.2f}!'.format(product - (product*10)/100))
elif pay == 2:
    print('O valor do produto à vista no cartão fica R${:.2f}!'.format(product - (product*5)/100))
elif pay == 3:
    print('O valor do produto em até 2x no cartão fica R${:.2f}'.format(product))
elif pay == 4:
    print('O valor do produto em 3x ou mais no cartão fica R${:.2f}'.format(product+juros * parcelas))
else:
    print('Erro! Tente novamente')



