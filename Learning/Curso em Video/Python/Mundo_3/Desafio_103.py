# Faça um programa que tenha um função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente. 

def ficha(nome="<desconhecido>", gols=0):
    print(f"O jogador {nome} fez {gols} gols na partida.")


nome = input("Nome do jogador: ")
if nome == "":
    nome = "<desconhecido>"
else:
    nome = nome
    try:
        gols = input("Quantos gols: ")
        if gols == "":
            gols = 0
        else:
            gols = int(gols)
    except ValueError:
        gols = 0
        
ficha(nome, gols)