# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

lista = [int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite outro númeor: ')),
        int(input('Digite outro número: ')),
        int(input('Digite outro número: '))]
print('='*30)
print('Os números digitados foram: ',end='')
for c in lista:
    print(f'{c} ',end='')
print(f'\nO maior valor é {max(lista)} que está na posição {lista.index(max(lista))+1}')
print(f'O menor valor é {min(lista)} que está na posição {lista.index(min(lista))+1}')