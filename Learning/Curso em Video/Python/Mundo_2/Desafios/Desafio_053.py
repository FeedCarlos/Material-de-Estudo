# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#Ex: APOS A SOPA ler de trás para frente.

frase = str(input('Digite uma frase para verificarmos se é palíndromo: '))
for c in (frase, ):
    c = frase.strip()
    c = frase.replace(' ', '')
    invert = c[::-1]
    if c == invert:
        print(f"{frase} é um palíndromo!")
    else:
        print(f"{frase} NÃO é um palíndromo!")
print('Fim')