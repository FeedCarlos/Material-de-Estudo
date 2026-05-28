# Crie um programa que o usuário possa digitar sete valores numérico e cadastre-os em uma lista única que mantenha separados os valores pareas e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''
temp = []
par = []
impar = []

count = 1

while True:
    temp.append(int(input(f'Digite o {count}º valor: ')))
    if temp[0] %2 == 0:
        par.append(temp[:])
    else:
        impar.append(temp[:])
    count += 1
    temp.clear()
    per = str(input('Gostaria de continuar? [S/N]: '))
    if per in 'Nn':
        break
print('-='*30)
print(f"Os varoles pares foram: {sorted(par)} ")
print()
print(f"Os valores ímpares foram {sorted(impar)}")
'''

num = [[], []]
valor = 0
count = 1

for c in range(0,7):
    valor = int(input(f'Digite o {count}º valor: '))
    if valor %2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
    count += 1
print('-='* 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')


'''
print('Os números pares digitados foram: ',end='')
for p in num:
    if p %2 == 0:
        print(f'{p} ', end='')
print()
print('Os números ímpares digitados foram: ', end='')
for i in num:
    if i %2 == 1:
        print(f'{i} ', end='')
'''