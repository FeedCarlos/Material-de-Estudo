# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. - Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que está na tupla.

from random import randint

c = 0
maior = 0
menor = 0

n1 = randint(0, 100)
n2 = randint(0, 100)
n3 = randint(0, 100)
n4 = randint(0, 100)
n5 = randint(0, 100)

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
