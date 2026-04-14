# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('carro', 'moto', 'van', 'fulltech', 'turbo')

vogais = palavras.index('a', 'e', 'i')

print(f'{palavras[0]} as vogais são {vogais}')