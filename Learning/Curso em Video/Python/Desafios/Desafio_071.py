# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunter ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$ 1.

from time import sleep

print('='*20)
print('  Caixa Eletrônico')
print('='*20)
sleep(1)

cinquenta = 0
vinte = 0
dez = 0
um = 0
valor = 0

while True:
    n = int(input('Qual é o valor que gostaria de sacar?\nR$: '))
    valor = n
    while True:
        if n >= 50:
            n -= 50
            cinquenta += 1
        elif n <= 50:
            break
    while True:    
        if n >= 20:
            n -= 20
            vinte += 1
        elif n <= 20:
            break
    while True:
        if n >= 10:
            n -= 10
            dez += 1
        elif n <= 10:
            break
    while True:
        if n >= 1:
            n -= 1
            um += 1
        elif n == 0:
            break
    break  
print(f'\nValor sacado {valor}\n{cinquenta} Cédulas de R$50\n{vinte} Cédulas de R$20\n{dez} Cédulas de R$10\n{um} Cédulas de R$1')
print('-'*20)
