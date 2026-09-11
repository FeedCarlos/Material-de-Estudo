# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra "Fim", o programa se encerrará. OBS: use cores

print('~'*25)
print("SISTEMA DE AJUDA PyHelp")
print("~"*25)

def ajuda(msg):
    help(msg)

pergunta = ''
while True:
    pergunta = input("Função ou Biblioteca: ")
    if pergunta.upper() == "FIM":
        break
    else:
        ajuda(pergunta)

