# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo e mostre o comprimento da hipotenusa

# Importando o método hypot da biblioteca math
from math import hypot

c_o = float(input('Digite o comprimento do cateto oposto: '))
c_a = float(input('Digite o comprimento do cateto adjacente: '))

hip = hypot(c_o, c_a)

print('O valor do cateto oposto é {} do adjacente {}, então o comprimento da hipotenusa é {:.2f} cm'.format(c_o, c_a, hip))