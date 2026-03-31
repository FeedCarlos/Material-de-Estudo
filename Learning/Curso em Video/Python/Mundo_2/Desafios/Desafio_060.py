# Faça um programa que leia um número qualquer e mostre o seu fatorial. EX 5! = 5x4x3x2x1 = 120
'''n = 0
n = int(input('Digite um número para ver o fatorial: '))
fatorial = 0
while n != 0:
    if n != 0:
        calculo = n * n
        fatorial = calculo
        n -= 1
        
    print(n)
print('FIM {}'.format(fatorial))'''

'''from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'. format(n, f))'''

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end= '')
    f *= c
    c -= 1
print('{}'.format(f))