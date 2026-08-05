# Crie um programa onde 4 jogadores joguem um dado e tenham resultado aleatório. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint

jogadores = dict()

for _ in range(4):
    nome = input('Nome: ')
    jogadores[nome] = randint(1, 10) 

print()
resultados = sorted(jogadores.items(), key=lambda jogador: jogador[1], reverse=True)
#print(resultados)
for posicao, jogador in enumerate(resultados, start=1):
    if jogador[1] > 1:
        print(f'{posicao}º Jogador {jogador[0]}, obteve {jogador[1]} Pontos!')
    else:
        print(f'{posicao}º Jogador {jogador[0]}, obteve {jogador[1]} Ponto!')