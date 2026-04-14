# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. - Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que está na tupla.

from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('-='*30)
print('Os Valores Sortiados Foram: ', end='')
for c in n:
    print(f'{c}, ', end='')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')
'''
maior = n1 
menor = n1 

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n4 > maior:
    maior = n4
if n5 > maior:
    maior = n5

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
if n4 < menor:
    menor = n4
if n5 < menor:
    menor = n5

num = (n1, n2, n3, n4, n5)
print('-'*30)
print(' Os Cinco Números Gerados Foi ')
print(f' {num[0]},  {num[1]},  {num[2]},  {num[3]},  {num[4]}')
print(f'O maior número gerado foi {maior}')
print(f'O menor número gerado foi {menor}')
print('-'*30)
'''