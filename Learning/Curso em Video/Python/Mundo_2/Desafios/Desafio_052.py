# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
count = 0

for c in range(n, n+1):
    if c < 2:
        print("O {} NÃO é primo".format(c))
    elif c == 2:
        print(" {} é unico par primo".foramt(c))
    elif c %2 == 0:
        print("O {} NÃO é primo".format(c))
    else:
        print('O {} é primo'.format(c))
print('FIM')


'''
n = int(input(': '))

divi = n // n == True
divi2 = n // 1 == n
divi3 = n // 2 == n
'''