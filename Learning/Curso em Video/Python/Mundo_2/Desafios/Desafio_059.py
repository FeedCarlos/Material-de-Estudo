'''
Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitado em cada caso.

'''
from time import sleep

n1 = 0
n2 = 0
opcao = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('-----------------------')
while opcao != 5:
    print('-----------------------')
    print('''Selecione uma opção:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair''')
    opcao = int(input('-> '))
    print('-----------------------')
    if opcao == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('O número {} é maior que o número {}'.format(n1, n2))
        elif n1 < n2:
            print('O número {} é maior que o número {}'.format(n2, n1))
        else:
            print('Nenhum dos valores é maior')
    elif opcao == 4:
       print('Reiniciando')
       sleep(1)
       n1 = int(input('Digite um número: '))
       n2 = int(input('Digite outro número: '))
    else:
        print('Saindo')
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        sleep(1)
        print('.')
print('FIM')