# Crie um programa que leia o ano de nascimento de sete pessoas. No final, monstre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    nascimento = int(input(f'{c}º qual é sua data de nascimento: '))
    if ano - nascimento >= 18:
        maior += 1
    else:
        menor += 1
print(f'Temos aqui {maior} de maior e {menor} de menor')