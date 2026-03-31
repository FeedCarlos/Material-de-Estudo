# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('-'*40)
print('Vamos ver os 10 primeiros termos')
print('-'*40)

termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termos = termo1
ini = 1

while ini <= 10:
    print("{}, ".format(termos),  end='')
    termos += razao 
    ini += 1
print('FIM') 
