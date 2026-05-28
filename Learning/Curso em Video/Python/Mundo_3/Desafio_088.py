# Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint

mega = []
print('''------------------------------
      JOGA NA MEGA SENA
------------------------------''')

quant_jogos = int(input('Quantos jogos gostaria que eu sorteie? '))

for i in range(quant_jogos):
    num_sorted = set()
    mega.sort()

    while len(num_sorted) < 6:
        num_sorted.add(randint(1,60))
    mega.append(list(num_sorted))
print()
print(f'-=-=-= SORTEANDO {quant_jogos} JOGOS =-=-=-')
for j in range(len(mega)):
    print(f'Jogo {j+1}: {mega[j]}')
print('-=-=-=-=-= < BOA SORTE > =-=-=-=-=-=-')

    