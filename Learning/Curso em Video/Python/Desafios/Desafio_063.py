# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci. EX: 0 - 1 - 1 - 2 - 3 - 5 - 8

print('-'*25)
print('Sequência de Fibonacci')
print('-'*25)

n = int(input('Digite um número para vermos a sequência: '))
count = 0
n2 = n - 1
n3 = n - 2
while count < 10:
    print('1-{}'.format(n))
    print('2-{}'.format(n2))
    print('3-{}'.format(n3))
    count += 1
    n += 1
    n2 += 1
    n3 += 1
    if n2 >= 0 and n3 >= 0:
        n = (n2 + n3)
print('FIM')