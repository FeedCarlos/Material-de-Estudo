# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A - Qual é o total gasto na compra.
# B - Quantos produtos custam mais de R$ 1000.
# C - Qual é o nome do produto mais barato.

print('='*30)
print('   Controle de Gastos')
print('='*30)

low_price = 0
expensive = 0
name_expen = ''
total = 0

while True:
    name_produto = str(input('Qual o nome do produto? '))
    valor_produto = float(input('Digite o valor do produto: R$ '))
    if low_price == 0:
        low_price = valor_produto
        exepensive = valor_produto
        name_expen = name_produto
    if valor_produto < low_price:
        low_price = valor_produto
        name_expen = name_produto
    if valor_produto > 1000:
        expensive += 1
    total = total + valor_produto
    cont = str(input('Gostaria de adicionar mais [S/N]? '))
    while cont not in 'SsNn':
        cont = str(input('Digite uma opção válida [S/N]: '))
    if cont not in ('Nn'):
        print('Vamos lá')
        print('-'*30)
    else:
        break
print('='*40)
print(f'O valor total da compra deu {total:.2f}\nTeve {expensive} produtos acima de R$ 1.000\nO produto mais barato foi {name_expen}')
print('='*40)