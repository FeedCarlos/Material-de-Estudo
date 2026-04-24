# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('carro', 'moto', 'van', 'fulltech', 'turbo')
vogais = 'aeiou'
print('')
print('-'*50)
print('As Seguintes Palavras Contém as Veguintes Vogais')
print('-'*50)
for i in palavras:
    print(f'\n{i.upper()}: ', end='')
    for l in i:
        if l.lower() in vogais:
            print(f'{l } ', end='')