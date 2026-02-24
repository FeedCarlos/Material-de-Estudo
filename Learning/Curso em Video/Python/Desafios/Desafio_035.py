# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se ela podem ou não formar um triângulo.

a = float(input('Digite o valor do lado a: '))
b = float(input('Digite o valor do lado b: '))
c = float(input('Digite o valor do lado c: '))

cond1 = a + b > c
cond2 = a + c > b
cond3 = b + c > a

if cond1 == True and cond2 == True and cond3 == True:
    print('Os seguintes comprimentos A = {}, B = {} e C = {} formam um triângulo'.format(a, b, c))
else:
    print('Os seguintes comprimentos não formam um triângulo')
