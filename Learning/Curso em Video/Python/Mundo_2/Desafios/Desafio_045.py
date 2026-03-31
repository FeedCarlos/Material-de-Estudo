# Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

print('''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    Vamos jogar Jokenpô     
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=''')

player = str(input('Escolha entre..\nPedra\nPapel\nTesoura\n-> '))

print('=-='*15)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('=-='*15)

pc = random.choice(['Pedra', 'Papel', 'Tesoura'])

if pc == 'Pedra':
    if player == 'Pedra':
        print('Nós dois escolhemos pedra! Deu empate.')
    elif player == 'Papel':
        print('Papel ganha de pedra! Você ganhou!')
    elif player == 'Tesoura':
        print('Tesoura perde para pedra! Eu ganhei!')
elif pc == 'Papel':
    if player == 'Papel':
        print('Nós dois escolhemos papel! Deu empate.')
    if player == 'Pedra':
        print('Papel é melhor que pedra! Eu ganhei!')
    if player == 'Tesoura':
        print('Tesoura é melhor que papel! Você ganhou!')
elif pc == 'Tesoura':
    if player == 'Tesoura':
        print('Nós dois escolhemos tesoura! Deu empate.')
    if player == 'Pedra':
        print('Pedra é melhor que tesoura! Você ganhou!')
    if player == 'Papel':
        print('Tesoura é melhor que papel! Eu ganhei!')
else:
    print('Essa opção não é válida!')

'''
if player == 'Pedra' and pc == 'Papel' or player == 'Tesoura' and pc == 'Pedra' or player == 'Papel' and pc == 'Tesoura':
    print('\033[1;31m {} é melhor que {}! Eu Ganhei!\033[m'.format(pc, player))
elif player == 'Papel' and pc == 'Pedra' or player == 'Pedra' and pc == 'Tesoura' or player == 'Tesoura' and pc == 'Papel':
    print('\033[1;32m{} é melhor que {}! Você ganhou!\033[m'.format(player, pc))
print('=-='*15)'''
