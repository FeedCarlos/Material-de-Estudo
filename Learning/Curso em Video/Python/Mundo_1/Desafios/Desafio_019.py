# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random

alunos = random.choice(['Lucas', 'Lari', 'Pedro', 'Ana'])
#alunos = input['','','','']

print('O aluno escolhido foi {}'.format(alunos))