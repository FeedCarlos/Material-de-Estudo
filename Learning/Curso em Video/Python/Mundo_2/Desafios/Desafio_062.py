# Melhore o DESAFIO 061, perguntando para o ususário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

print('''
--------------------------
Vamos verificar os termos
--------------------------''')
primeiro_t = int(input('Digite o primeiro TERMO: '))
razao = int(input('Digite a razão: '))
primeiro = primeiro_t
ini = 1
termos = 0
mais = 10

while mais != 0:
    termos = termos + mais
    while ini <= termos:
        print('{} → '.format(primeiro), end='')
        primeiro += razao
        ini += 1
    print('Pausa')
    mais = int(input('Quantos termos vocÊ quer mostrar a mais? '))
print('Encerrando.caraio')
