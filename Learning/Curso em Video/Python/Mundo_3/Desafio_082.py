# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = list()
par = list()
impar = list()

while True: 
    while True:
        try:
            n = int(input('Digite um número: '))
            lista.append(n)
            break
        except ValueError:
            print('Digite um valor válido!')
    per = str(input('Gostaria de continuar? [S/N]: '))
    if per in 'Nn':
        break
for c in range(len(lista)):
        if lista[c] % 2 == 0:
             par.append(lista[c])
        else:
             impar.append(lista[c])
print('-='*30)
print(f'Os números digitados foi {lista}')
print('-'*60)
if len(par) > 0:
     print(f'Os números pares são {par}')
else:
     print('Não teve números pares!')
print('-'*60)
if len(impar) > 0:
     print(f'Os números impar digitados foi {impar}')
else:
     print('Não teve número impar!')
print('-'*60)