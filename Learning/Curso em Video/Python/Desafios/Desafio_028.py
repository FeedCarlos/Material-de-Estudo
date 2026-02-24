# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random 
from time import sleep

num_random = random.randint(0, 5)
print('-=-'*20)
print('Estou pensando em um número entre 0 e 5.. Tente adivinhar!')
print('-=-'*20)
num = int(input('Adivinhe um número entre 1 e 5: '))
print('\nPROCESSANDO...\n')
sleep(3)
if num == num_random:
    print('VOCÊ VENCEU!\nO número sortido foi {}'.format(num_random))
else:
    print('EU VENCI!\nO número sortido era {}'.format(num_random))


