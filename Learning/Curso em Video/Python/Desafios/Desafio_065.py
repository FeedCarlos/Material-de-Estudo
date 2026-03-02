# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = int(input('Digite alguns valores para descobrirmos a média entre eles:'))
maior = 0
menor = 0
count = 0
total = 0
media = 0
prox = ''
while prox == 'N':
    prox = str(input('Quer continuar? [S/N]'))
    if prox != 'N':
        num = int(input('Digite outro:'))
        soma = num + total
        total = soma 
        maior = num
        menor = num 
        if num > maior:
            maior = num
        else:
            menor = num
    count += 1
    media = total / count
print('Total: {}, Média {}, Maior {}, Menor {}'.format(total, media, maior, menor))
