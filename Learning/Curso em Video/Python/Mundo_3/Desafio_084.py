# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.
cadastro = list()
pessoas = list()
peso = list()
leve = list()
cadastros = 0

while True:
    pessoas.append(str(input('Digite seu nome: ')))
    pessoas.append( int(input('Digite seu peso: ')))
    cadastro.append(pessoas[:])
    pessoas.clear()
    cadastros += 1
    pergunta = str(input('Gostaria de continuar? [S/N]: '))
    if pergunta in 'Nn':
        break
for c in cadastro:
    if c[1] >= 100:
        peso.append(c)
    else:
        leve.append(c)
print('-='*40)
if leve == 0:
    print('Não houve nenhuma pessoa pesada cadastrada.')
else:
    print(f'As pessoas cadastradas com mais peso foi {peso}')
if peso == 0:
    print('Não houve cadastro nenhuma pessoa com peso leve')
else:
    print(f'Com menos peso foram {leve}')
print(f'Foi cadastrado {cadastros} pessoas')
print(f'{cadastro}')

