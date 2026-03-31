# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

alunos = (['Pedro', 'Lari', 'Carlos', 'Gi'])

sort = shuffle(alunos)

print('Entre os gurpos dos seguintes lideres {} a sequência de apresentação ficou {}'.format(alunos, sort))

