# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# EX: Digite um número: 6.127 O número 6.127 tem a parte Inteira 6.

# Realizado a importação de floor da biblioteca math
# from math import floor
from math import trunc

# Criando uma variavel para pedir o número 
num = float(input('Digite qualuqer número real: '))

#n = floor(num)

print('O número digitado foi {} e o número inteiro seria {} '.format(num, trunc(num)))
