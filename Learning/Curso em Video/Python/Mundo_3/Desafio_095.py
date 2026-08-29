# Aprimore o Desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

'''
Informações que o usuário terá que inserir:
nome - jogos - gols de cada partida

Informações que o programa terá que calcular:
total de gols

Estrutura do dicionário:
- nome - gols - total
'''
jogadores = []

while True:
    jogador = {}
    jogador['gols'] = []
    while True:
        try:
            jogador['nome'] = str(input("Nome do jogador: "))
            break
        except ValueError:
            print("ERRO: Digite seu nome")
    jogador['partidas'] = int(input("Jogador jogou quantos jogos: "))
    if jogador['partidas'] == 0:
            gols = 0
            jogador['gols'].append(gols)
    for jogo in range(jogador['partidas']):
        gols = int(input(f"Quantos gols foi feito no {jogo+1}º jogo? "))
        jogador['gols'].append(gols)
    jogador['total_gols'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    pergunta = input("Gostaria de continuar [S|N]? ").upper()[0]
    if pergunta in 'Nn':
        break
print()
print('='*50)
print(f"Cod  Nome"," "*10, "Gols", " "*5, "Total")
print('-'*50)
for posicao, cadastrado in enumerate(jogadores):
    print(f"{posicao:<3} {cadastrado['nome']:<13}  {str(cadastrado['gols']):<10} {cadastrado['total_gols']:>5}")
print('-'*50)
print()
while True:
    dados = int(input("De qual jogador você gostaria de ver os dados? "))
    print(f"Segue levantamento do jogador {jogadores[dados]['nome']}")
    print()
    if jogador['partidas'] > 0:
        for partida, gol  in enumerate(jogadores[dados]['gols']):
            print(f"Na {partida+1}ª partida fez {gol}")
        print('-'*50)
    else:
        print(f"O jogador não fez nehum gol no compeonato")
    print()
    sair = input('Gostaria de continuar [SIM | NÃO]? ').upper()[0]
    print()
    if sair in 'N':
        break
# print(jogador)
#print(jogadores)