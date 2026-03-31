# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = input(str('Digite seu nome: ')).lower()
busca = ('silva' in nome)

if busca == True:
    print('Seu nome tem Silva')
else:
    print('Seu nome não tem Silva')

# Outro tipo de identação para encontrar o silva no nome
"""busca = 'silva'


if nome.lower().find(busca) != -1:
    print('Você tem Silva no nome')
else:
    print('Você não tem Silva no nome')"""

