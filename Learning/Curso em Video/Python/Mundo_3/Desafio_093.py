# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# Informações que o usuário terá que digitar:
# - Nome do jogador
# - Quantas partidas ele jogou
# - Quantos gols foi feito 

# Quais informações o programa vai calcular:
# Total de gols feito no campeonato

# Estrutura do dicionário
# - nome
# - partidas
# - gols por partida
# - total de gols

jogadores = {}

jogadores["nome"] = input("Digite seu nome: ")
jogadores["partidas"] = int(input("Quantas partidas você jogou: "))

jogadores["gols"] = []
for partida in range(1, jogadores["partidas"]+1 ):
    gols = int(input(f"Quantos gols foram feitos na {partida}º partida? "))
    jogadores["gols"].append(gols)

jogadores["total_gols"] = sum(jogadores["gols"])

print()
print("-="*30)
print(f'''
O jogador {jogadores["nome"]}
Jogou {jogadores["partidas"]} partidas nesse campeonato.
Fez um total de {jogadores["total_gols"]} gols.
''')
