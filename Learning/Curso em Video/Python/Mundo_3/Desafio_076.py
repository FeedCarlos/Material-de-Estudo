# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular

products = ('arroz', 40,
            'feijão', 15,
            'açucar', 5)
print('-'*40)
print(f'{'Listagem de Preços':^40}')
print('-'*40)
for c in range(0, len(products)):
    if c % 2 == 0:
        print(f'{products[c]:.<30} ', end='')
    else:
        print(f'R${products[c]:>3.2f}')
print('-'*40)