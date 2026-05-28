# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formação correta.

    # _____________
    # |___|___|___|
    # |___|___|___|
    # |___|___|___|
'''
matriz = []
count = 1

for linha in range(3):
    nova_linha = []
    for coluna in range(3):
        num = int(input(f'Digite o {count}º número: '))
        nova_linha.append(num)
        count += 1
    matriz.append(nova_linha)
print('-='*20)
for linha in matriz:
    print(linha)
'''

matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='* 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()