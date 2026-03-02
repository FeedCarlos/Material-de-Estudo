# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci. EX: 0 - 1 - 1 - 2 - 3 - 5 - 8

print('-'*25)
print('Sequência de Fibonacci')
print('-'*25)

n = int(input('Qual termo gostaria de ver na sequência de Fibonacci:  '))
termo1 = 0
termo2 = 1
termo3 = 1
count = 3
print('{} → {} → '.format(termo1, termo2), end='')
while count <= n:
    termo3 = termo1 + termo2
    print('{} → '.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    count += 1
print('FIM')
print('-'*40)