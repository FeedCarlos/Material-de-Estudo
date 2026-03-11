# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
from time import sleep
print('-='*40)
print('Digite alguns valores para descobrirmos o total e a média entre eles')
print('-='*40)
sleep(1)
print('VAMOS COMEÇAR!')
sleep(1)
print('-='*35)

maior = menor = count = media = total = 0
prox = 'S'
while prox != 'N':
    num = int(input('Digite: '))
    soma = num + total
    total = soma  
    if count == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    prox = str(input('Gostaria de continuar? [S/N]\n→ ')).upper()
    if prox == 'N':
        prox = 'N'
    count += 1
media = total / count
print('-='*40)
print('O total foi {}\nA média {:.2f}\nO maior valor {}\nO menor valor {}'.format(total, media, maior, menor))
print('-='*40)
