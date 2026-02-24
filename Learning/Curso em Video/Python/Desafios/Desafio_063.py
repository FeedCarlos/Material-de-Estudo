# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci. EX: 0 - 1 - 1 - 2 - 3 - 5 - 8

print('-'*25)
print('Sequência de Fibonacci')
print('-'*25)

n = int(input('Digite um número para vermos a sequência: '))
ini = n
ini = 1
f_1 = ini - 1
f_2 = ini - 2
calc = f_1 + f_2
count = 0
final = 7
while count != final:
    print('{}'.format(ini))
    if ini == 1:
        ini += 1
    else: 
        ini = calc
print('FIM')