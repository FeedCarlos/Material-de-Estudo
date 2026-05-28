# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.
'''cadastro = list()
pessoas = list()
peso = list()
leve = list()
cadastros = 0

while True:
    pessoas.append(str(input('Digite seu nome: ')))
    pessoas.append(int(input('Digite seu peso: ')))
    cadastro.append(pessoas[:])
    pessoas.clear()
    cadastros += 1
    pergunta = str(input('Gostaria de continuar? [S/N]: '))
    if pergunta in 'Nn':
        break
for c in cadastro:
    peso.append(c[1])
    leve.append(c[1])

print('-='*40)
if leve[0] == False:
    print('Não houve nenhuma pessoa pesada cadastrada.')
else:
    print(f'As pessoas cadastradas com mais peso foi {peso}')
if peso[0] == "":
    print('Não houve cadastro nenhuma pessoa com peso leve')
else:
    print(f'Com menos peso foram {leve}')
print(f'Foi cadastrado {cadastros} pessoas')
print(f'{cadastro}')
'''
temp = []
princ = []

maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()

    resp = str(input("Quer continuar? [S/N] "))
    if resp in 'Nn':
        break

print('-='*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f"O maior peso foi {maior}Kg de ",end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi {menor}Kg de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print()