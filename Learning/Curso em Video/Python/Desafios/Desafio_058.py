# Melhore o jogo do Desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from time import sleep
from random import randint

n_random = randint(1,10)
print('''----------ADIVINHE!----------''')
sleep(1)
print('Estou pensando em um número, entre 0 e 10')
sleep(1)
print('Tente ADIVINHAR!')
sleep(1)
print('-------------------------------')
count = 0
num = 0
while num != n_random:
    num = int(input('Digite um número: '))
    if num > 10:
        print('É até 5.. né')
    if num != n_random:
        count += 1
print('ACERTOU!! O meu número era {}'.format(n_random))
print('Foram {} tentativas'.format(count))
