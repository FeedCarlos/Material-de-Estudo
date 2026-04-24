# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.
lista = list()

while True:
    while True:
        try:
            n = int(input('Digite um número: '))
            lista.append(n)
            break
        except ValueError:
            print('Valor inválido digite um valor válido!')
    p = str(input('Gostaria de continuar? [S/N]: '))
    if p in 'Nn':
        break
print('-='*30)
print(f'A quanitade de números digitados foi {len(lista)}')
lista.reverse()
print(f'Os valores digitados foram {lista}')
if 5 in lista:
    print(f'O valor 5 está na lista, na posição {lista.index(5)+1}')
else:
    print('O valor 5 não está na lista')